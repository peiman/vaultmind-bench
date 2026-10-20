---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#20-defining-access-for-the-github-token-scopes.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-20-defining-access-for-the-github-token-scopes
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `permissions` › Defining access for the `GITHUB_TOKEN` scopes
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#20-defining-access-for-the-github-token-scopes
source_hash: 9d2304d332fdbcb7777d6d9676445eb158d58416dae809114bb7894ba36993fd
---
You can define the access that the `GITHUB_TOKEN` will permit by specifying `read`, `write`, or `none` as the value of the available permissions within the `permissions` key.

```
permissions:
  actions: read|write|none
  artifact-metadata: read|write|none
  attestations: read|write|none
  checks: read|write|none
  code-quality: read|write|none
  contents: read|write|none
  copilot-requests: write|none
  deployments: read|write|none
  id-token: write|none
  issues: read|write|none
  discussions: read|write|none
  packages: read|write|none
  pages: read|write|none
  pull-requests: read|write|none

  security-events: read|write|none
  statuses: read|write|none
  vulnerability-alerts: read|none
```

If you specify the access for any of these permissions, all of those that are not specified are set to `none`.

You can use the following syntax to define one of `read-all` or `write-all` access for all of the available permissions:

```
permissions: read-all
```

```
permissions: write-all
```

You can use the following syntax to disable permissions for all of the available permissions:

```
permissions: {}
```

#### Changing the permissions in a forked repository

You can use the `permissions` key to add and remove read permissions for forked repositories, but typically you can't grant write access. The exception to this behavior is where an admin user has selected the **Send write tokens to workflows from pull requests** option in the GitHub Actions settings. For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#enabling-workflows-for-forks-of-private-repositories).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
