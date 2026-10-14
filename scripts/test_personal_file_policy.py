"""Unit tests for the path-based repository artifact policy."""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_personal_file_policy import reject_reason


class FilePolicyTests(unittest.TestCase):
    def assert_blocked(self, path, **kwargs):
        self.assertIsNotNone(reject_reason(path, **kwargs), path)

    def assert_allowed(self, path, **kwargs):
        self.assertIsNone(reject_reason(path, **kwargs), path)

    def test_secrets(self):
        for path in [
            ".env", ".env.production", ".env.local",
            "demo/id_ed25519", "demo/private.key", "cert/server.pem",
            "auth/credentials.json", "account/service-account.json",
            "secrets/.aws/credentials", "terraform/terraform.tfstate",
            "db/customer.sqlite", "app/customer.db",
        ]:
            with self.subTest(path=path):
                self.assert_blocked(path)

    def test_generated_artifacts(self):
        for path in [
            "demo/node_modules/file.js", "src/__pycache__/model.pyc",
            ".venv/pyvenv.cfg", "notes/run.log",
            "my-roadmaps/enterprise-ai-delivery/out.zip",
            "my-roadmaps/enterprise-ai-delivery/model.onnx",
        ]:
            with self.subTest(path=path):
                self.assert_blocked(path)

    def test_explicit_exemptions(self):
        self.assert_allowed(".env.example")
        self.assert_allowed("my-roadmaps/enterprise-ai-delivery/README.md")
        self.assert_allowed("manuals/docker-sandboxes-101/capture/out/23-serve-api.log")
        self.assert_blocked("my-roadmaps/demo/records.log")
        self.assert_blocked("my-roadmaps/demo/docs.md", symlink=True)
        self.assert_blocked("my-roadmaps/demo/data.csv", size=2 * 1024 * 1024 + 1)

    def test_paths_are_case_insensitive_for_sensitive_names(self):
        self.assert_blocked("MyRoadmaps/ENV/.ENV")
        self.assert_blocked("MY-ROADMAPS/demo/SECRET.P12")


if __name__ == "__main__":
    unittest.main()
