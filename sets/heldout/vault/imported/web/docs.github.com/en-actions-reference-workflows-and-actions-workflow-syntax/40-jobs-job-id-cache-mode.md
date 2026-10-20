---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#40-jobs-job-id-cache-mode.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-40-jobs-job-id-cache-mode
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.cache-mode`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#40-jobs-job-id-cache-mode
source_hash: ea55af81fcbcd8e7a432c990f98c9047e5eac3f372decb95f7de4f7dde6e5484
---
Use `jobs.<job_id>.cache-mode` to set the level of GitHub Actions cache access for a single job. A value set here overrides any workflow-level [`cache-mode`](#cache-mode) for this job only.

The accepted values are `read`, `write`, `write-only`, and `none`, with the same meanings as the top-level key. If neither the job nor the workflow sets `cache-mode`, a trigger-based default applies. For more information about each value, see [`cache-mode`](#cache-mode) and [Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching#defaults).

Warning

Explicitly declaring `cache-mode: write` or `cache-mode: write-only` on low-trust triggers can bypass the secure default read-only cache restriction and reintroduce cache-poisoning risk. For guidance and mitigations, see [Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching#bypassing-the-default-untrusted-trigger-cache-restriction).

You can also set `cache-mode` on a job that calls a reusable workflow to limit the cache access granted to the called workflow. For more information, see [Reusing workflow configurations](https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#supported-keywords-for-jobs-that-call-a-reusable-workflow) and [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows#controlling-cache-access-in-reusable-workflows).

### Example of `jobs.<job_id>.cache-mode`

```
jobs:
  build:
    runs-on: ubuntu-latest
    cache-mode: write
  test:
    runs-on: ubuntu-latest
    cache-mode: read
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
