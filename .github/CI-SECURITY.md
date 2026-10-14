# Personal CI and Security Policy

This fork uses a **minimal, read-only CI** for individual AI Engineering
roadmaps. It does not publish a curriculum website or build/download books.
All five workflows inherited from upstream were removed from this fork by
the CI migration PR. The original versions remain available in upstream Git
history if they are needed later.

## Jobs

| Job | What is verified | What is not verified |
|---|---|---|
| Tracked file policy | Known sensitive paths, local files and large/binary personal-roadmap artifacts | The actual content of ordinary files |
| Gitleaks | Recognizable credential/token patterns in Git changes | Every possible secret and all historical exposures |
| Personal Markdown lint | Markdown conventions in `my-roadmaps/` and this document | Existing upstream 500+ lesson documents |
| GitHub Actions lint | Workflow YAML and GitHub Actions expression syntax | Whether externally maintained actions or tools are intrinsically safe |

No jobs use self-hosted runners, Docker administration, SSH credentials,
cloud keys, deployment secrets, `contents: write` permissions or auto-commit.
The only token supplied to Gitleaks is GitHub's built-in **read-only**
`GITHUB_TOKEN` for repository/PR context.

## Repository file guard

`scripts/check_personal_file_policy.py` uses `git ls-files` to inspect all
tracked files, not just the PR diff. It blocks common private-key names,
environment files, local credentials, DB/state artifacts, generated caches and
logs. Safe sample environment templates are allowed, but their **contents**
must still pass secret scanning.

Three existing upstream manual-capture logs are narrowly exempted through
the `manuals/*/capture/out/*.log` pattern. This is compatibility with
documented upstream fixtures, **not** permission to add sensitive logs.
Personal-roadmap directories also reject binary archives, symlinks and files
larger than 2 MiB. Place large runtime outputs in a separate, access-controlled
artifact store rather than this public repository.

## Workflow and merge rules

- PRs run all four checks; merging remains a human decision.
- For required checks, configure GitHub branch protection/rulesets manually
  after the jobs have run and their exact names appear in GitHub.
- Merging this PR changes the **files in the repository**; review GitHub
  Settings > Actions > General separately for the default workflow-token
  permission (recommended: read-only).
- GitHub-hosted runners and external actions still execute third-party code.
  Existing checkout, markdownlint, Gitleaks and actionlint versions are pinned.
- When bringing upstream changes into the fork, review workflow changes
  explicitly. Do not blindly restore upstream `.github/workflows/` files
  during merges or syncs.

## Remaining limitations

Gitleaks signatures are heuristic and may miss secrets. If Gitleaks reports
a true secret, rotate/revoke it immediately; merely removing it from a later
commit is insufficient. Scanning a pre-existing fork history can also surface
historical examples: inspect each report, and do not add broad ignore rules
or hardcode exemptions to force a green check.

The CI intentionally does not execute every educational project, test all
runtime dependencies, install models or deploy workloads. Add narrowly scoped
unit/contract/evaluation tests only when personal projects require them.
