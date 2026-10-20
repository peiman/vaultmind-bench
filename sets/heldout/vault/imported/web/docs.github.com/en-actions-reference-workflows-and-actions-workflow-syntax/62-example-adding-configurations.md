---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#62-example-adding-configurations.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-62-example-adding-configurations
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.strategy.matrix.include` › Example: Adding configurations'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#62-example-adding-configurations
source_hash: c03c7d4dc705bc304619269c3fe7b0d468f8fa6ce2ae04f6f4280695d504fa58
---
For example, this matrix will run 10 jobs, one for each combination of `os` and `version` in the matrix, plus a job for the `os` value of `windows-latest` and `version` value of `17`.

```
jobs:
  example_matrix:
    strategy:
      matrix:
        os: [macos-latest, windows-latest, ubuntu-latest]
        version: [12, 14, 16]
        include:
          - os: windows-latest
            version: 17
```

If you don't specify any matrix variables, all configurations under `include` will run. For example, the following workflow would run two jobs, one for each `include` entry. This lets you take advantage of the matrix strategy without having a fully populated matrix.

```
jobs:
  includes_only:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        include:
          - site: "production"
            datacenter: "site-a"
          - site: "staging"
            datacenter: "site-b"
```

## `jobs.<job_id>.strategy.matrix.exclude`

An excluded configuration only has to be a partial match for it to be excluded.

All `include` combinations are processed after `exclude`. This allows you to use `include` to add back combinations that were previously excluded.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
