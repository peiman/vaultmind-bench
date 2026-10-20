---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#21-how-permissions-are-calculated-for-a-workflow-job.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-21-how-permissions-are-calculated-for-a-workflow-job
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `permissions` › How permissions are calculated for a workflow job
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#21-how-permissions-are-calculated-for-a-workflow-job
source_hash: 6ae845e35113be15ee3a26df7d4d7eba50c1d148a875335e29b0259f4af8193a
---
The permissions for the `GITHUB_TOKEN` are initially set to the default setting for the enterprise, organization, or repository. If the default is set to the restricted permissions at any of these levels then this will apply to the relevant repositories. For example, if you choose the restricted default at the organization level then all repositories in that organization will use the restricted permissions as the default. The permissions are then adjusted based on any configuration within the workflow file, first at the workflow level and then at the job level. Finally, if the workflow was triggered by a pull request event other than `pull_request_target` from a forked repository, and the **Send write tokens to workflows from pull requests** setting is not selected, the permissions are adjusted to change any write permissions to read only.

### Setting the `GITHUB_TOKEN` permissions for all jobs in a workflow

You can specify `permissions` at the top level of a workflow, so that the setting applies to all jobs in the workflow.

#### Example: Setting the `GITHUB_TOKEN` permissions for an entire workflow

This example shows permissions being set for the `GITHUB_TOKEN` that will apply to all jobs in the workflow. All permissions are granted read access.

```
name: "My workflow"

on: [ push ]

permissions: read-all

jobs:
  ...
```

### Using the `permissions` key for forked repositories

You can use the `permissions` key to add and remove `read` permissions for forked repositories, but typically you can't grant `write` access. The exception to this behavior is where an admin user has selected the **Send write tokens to workflows from pull requests** option in the GitHub Actions settings. For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#enabling-workflows-for-forks-of-private-repositories).

### Permissions for workflow runs triggered by Dependabot

Workflow runs triggered by Dependabot pull requests run as if they are from a forked repository, and therefore use a read-only `GITHUB_TOKEN`. These workflow runs cannot access any secrets. For information about strategies to keep these workflows secure, see [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use).

## `env`

A `map` of variables that are available to the steps of all jobs in the workflow. You can also set variables that are only available to the steps of a single job or to a single step. For more information, see [`jobs.<job_id>.env`](#jobsjob_idenv) and [`jobs.<job_id>.steps[*].env`](#jobsjob_idstepsenv).

Variables in the `env` map cannot be defined in terms of other variables in the map.

When more than one environment variable is defined with the same name, GitHub uses the most specific variable. For example, an environment variable defined in a step will override job and workflow environment variables with the same name, while the step executes. An environment variable defined for a job will override a workflow variable with the same name, while the job executes.

### Example of `env`

```
env:
  SERVER: production
```

## `defaults`

Use `defaults` to create a `map` of default settings that will apply to all jobs in the workflow. You can also set default settings that are only available to a job. For more information, see [`jobs.<job_id>.defaults`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_iddefaults).

When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.

## `defaults.run`

You can use `defaults.run` to provide default `shell` and `working-directory` options for all [`run`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstepsrun) steps in a workflow. You can also set default settings for `run` that are only available to a job. For more information, see [`jobs.<job_id>.defaults.run`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_iddefaultsrun). You cannot use contexts or expressions in this keyword.

When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.

### Example: Set the default shell and working directory

```
defaults:
  run:
    shell: bash
    working-directory: ./scripts
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
