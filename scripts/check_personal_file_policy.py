#!/usr/bin/env python3
"""Fail if tracked files have sensitive names, generated paths or unsafe artifacts.

Operate on Git's index rather than only changed files so a later PR does not
silently retain dangerous previously committed artifacts.
"""
from __future__ import annotations

import fnmatch
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BLOCKED_COMPONENTS = frozenset({
    ".ssh", ".aws", ".kube", ".terraform", ".venv", "venv", "env",
    "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache",
    ".ruff_cache", ".idea", ".vscode", ".next", ".git",
})
BLOCKED_NAMES = frozenset({
    ".env", ".netrc", ".npmrc", ".pypirc", ".ds_store", "thumbs.db",
    "id_rsa", "id_dsa", "id_ecdsa", "id_ed25519",
    "credentials.json", "service-account.json", "service_account.json",
    "google-credentials.json", "terraform.tfstate",
})
ENV_EXAMPLES = frozenset({
    ".env.example", ".env.sample", ".env.template", ".env.dist",
})
BLOCKED_SUFFIXES = (
    ".pem", ".key", ".p12", ".pfx", ".p8", ".jks", ".keystore",
    ".kdbx", ".tfstate", ".tfstate.backup", ".sqlite", ".sqlite3",
    ".db", ".pyc", ".pyo", ".swp", ".swo", ".bak", ".tmp", ".log",
    ".safetensors", ".ckpt", ".pt", ".pth",
)
PERSONAL_BINARY_SUFFIXES = (
    ".zip", ".7z", ".rar", ".tar", ".tar.gz", ".tgz", ".pdf", ".exe",
    ".dll", ".dmg", ".iso", ".bin", ".onnx",
)
MAX_PERSONAL_BYTES = 2 * 1024 * 1024

# Existing, non-secret logs are part of the upstream manual's reproducible
# lesson captures. New personal roadmap logs are NEVER exempt.
def legacy_capture_log(path: str) -> bool:
    return fnmatch.fnmatchcase(path, "manuals/*/capture/out/*.log")


# Upstream educational sandbox test fixture (not a real virtualenv).
# Do not add generic exceptions for other paths named "env".
def legacy_environment_fixture(path: str) -> bool:
    return path == "manuals/docker-sandboxes-101/capture/fixtures/env/sbxenv.yaml"


def reject_reason(path: str, size: int = 0, symlink: bool = False) -> str | None:
    normalized = path.replace("\\", "/")
    elements = [part.casefold() for part in normalized.split("/")]
    name = elements[-1]
    if any(element in BLOCKED_COMPONENTS for element in elements[:-1]) and not legacy_environment_fixture(normalized):
        return "generated, credential or local configuration directory"
    if name in BLOCKED_NAMES:
        return "sensitive or local-only filename"
    if name.startswith(".env.") and name not in ENV_EXAMPLES:
        return "environment-specific secrets filename"
    if name.endswith(BLOCKED_SUFFIXES):
        if name.endswith(".log") and legacy_capture_log(normalized):
            return None
        return "secret-bearing, generated or local-data extension"
    if name.endswith(".tfstate.") or ".tfstate." in name:
        return "Terraform state or state backup"
    if normalized.startswith("my-roadmaps/"):
        if symlink:
            return "symlinks are not allowed in personal roadmap artifacts"
        if name.endswith(PERSONAL_BINARY_SUFFIXES):
            return "binary/archive artifacts belong outside the learning roadmap"
        if size > MAX_PERSONAL_BYTES:
            return "personal roadmap file exceeds 2 MiB"
    return None


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--cached"],
        cwd=ROOT, check=True, stdout=subprocess.PIPE,
    )
    return [os.fsdecode(chunk) for chunk in result.stdout.split(b"\0") if chunk]


def main() -> int:
    errors: list[tuple[str, str]] = []
    files = tracked_files()
    for rel in files:
        file_path = ROOT / rel
        try:
            info = file_path.lstat()
        except FileNotFoundError:
            errors.append((rel, "tracked file missing from checkout"))
            continue
        reason = reject_reason(rel, info.st_size, file_path.is_symlink())
        if reason:
            errors.append((rel, reason))
    if errors:
        for path, reason in errors:
            print(f"BLOCKED: {path} — {reason}", file=sys.stderr)
        print(f"{len(errors)} forbidden tracked path(s)", file=sys.stderr)
        return 1
    print(f"PASS: {len(files)} tracked paths reviewed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
