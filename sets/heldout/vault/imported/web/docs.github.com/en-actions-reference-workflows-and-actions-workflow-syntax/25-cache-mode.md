---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#25-cache-mode.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-25-cache-mode
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `cache-mode`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#25-cache-mode
source_hash: 9615471cddf40af701ad77c27c9eded39d51eef910f4d02ebe9944f78462f71c
---
Use `cache-mode` to control the level of GitHub Actions cache access that jobs in the workflow are granted. Setting `cache-mode` at the top level applies to every job in the workflow, unless a job overrides it with [`jobs.<job_id>.cache-mode`](#jobsjob_idcache-mode).

Access is enforced with scoped cache tokens, so a job cannot restore or save caches beyond the mode it is granted. `cache-mode` accepts the following values.

ValueRestore cachesSave caches`read`YesNo`write`YesYes`write-only`NoYes`none`NoNo

If you omit `cache-mode`, a `read` or `write` default is used based on the trigger type. For trigger-dependent effective defaults, see [Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching#defaults).

Warning

Explicitly declaring `cache-mode: write` or `cache-mode: write-only` on low-trust triggers can bypass the secure default read-only cache restriction and reintroduce cache-poisoning risk. For guidance and mitigations, see [Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching#bypassing-the-default-untrusted-trigger-cache-restriction).

When a cache operation is not permitted by the effective mode, the cache step logs an informational message and continues. The job and workflow do not fail. A skipped restore is treated as a cache miss; a skipped save is simply not performed. For more information, see [Dependency caching reference](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching#controlling-cache-access-with-cache-mode).

### Example of `cache-mode`

```
cache-mode: read

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/cache@v4
        with:
          path: ~/.npm
          key: npm-${{ hashFiles('**/package-lock.json') }}
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
