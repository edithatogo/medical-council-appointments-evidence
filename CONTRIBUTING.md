# Contributing to medical-council-appointments-evidence

This repository contains a bounded documentary evidence record of Medical Council appointments. Contributions should correct source identities, improve provenance or clarify supported claims while preserving the published record's limits.

## Before you start

Read [README.md](README.md), [RIGHTS.md](RIGHTS.md), [NOTICE](NOTICE) and the relevant catalogue and claim-source entries. Check open issues and pull requests. Distinguish official source documents, extracted derivatives, researcher annotations and proposed safeguards. A chronology or missing record does not by itself establish causation or unlawfulness.

For bugs, provide the affected version or commit, environment, minimal reproduction, expected result and observed result. For a substantial proposal, describe the use case and compatibility impact before expanding implementation scope. Use existing issue templates when offered.

## Development and validation

The README specifies a local Python 3.15.1 environment and the archive verification command:

```sh
.venv/bin/python scripts/verify.py
```

This verifies archive file hashes, not source accuracy or publication rights. For changed evidence, inspect the actual source and identify the precise proposition and passage affected. Preserve original URLs, retained-version hashes, dates, extraction boundaries and redistribution qualifications.

Treat [checksums.json](checksums.json) and [provenance.json](provenance.json) as evidence records. Do not silently regenerate them merely to clear a mismatch; explain any source or payload change alongside its updated checksum. Preserve immutable release history and identify the commit being discussed.

For model or diagram changes, check that labels and arrows retain their documented non-executable and non-causal meaning. Keep legislative status, interpretation and recommendations separate. Do not introduce private correspondence, unpublished manuscripts or unrelated private repository history into this public collection.

## Pull requests

Create a focused branch from the current `main` branch and submit a pull request to this repository. Link the relevant issue or existing project task, explain the resulting behaviour, and update affected examples and documentation. Keep unrelated changes in separate pull requests.

Report executed commands, outcomes and the commit they validate. Identify unavailable checks and remaining limitations explicitly. Follow the repository's existing review and automated-check requirements; retain required gates and current ownership. Address findings and verify the final head before integration. Repository changes do not themselves authorise a release or external operational action.

## Security, rights and conduct

Follow the [security policy](https://github.com/edithatogo/.github/blob/main/SECURITY.md). Use private vulnerability reporting if available; otherwise request a private contact without publishing vulnerability details. Keep credentials, personal information and restricted source material out of issues, fixtures, logs and artifacts.

Read the [existing licence](LICENSE-CODE) and preserve attribution and third-party terms. Follow the [code of conduct](https://github.com/edithatogo/.github/blob/main/CODE_OF_CONDUCT.md) and keep technical discussions respectful.

## Basis for this guide

This guide follows [GitHub's contribution-guideline guidance](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors) and the contribution-process and testing principles in [OpenSSF Best Practices](https://www.bestpractices.dev/en/criteria). It does not assert certification.
