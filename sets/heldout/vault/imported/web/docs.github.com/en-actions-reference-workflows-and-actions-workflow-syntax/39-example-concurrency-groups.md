---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#39-example-concurrency-groups.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-39-example-concurrency-groups
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.concurrency` › Example: Concurrency groups'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#39-example-concurrency-groups
source_hash: fe448502c79e96fbb9d5246dedac1dbb513a26e8e584d98c77d17b4f540ce0f6
---
Concurrency groups provide a way to manage and limit the execution of workflow runs or jobs that share the same concurrency key.

The `concurrency` key is used to group workflows or jobs together into a concurrency group. When you define a `concurrency` key, GitHub Actions ensures that only one workflow or job with that key runs at any given time. If a new workflow run or job starts with the same `concurrency` key, GitHub Actions will cancel any workflow or job already running with that key. The `concurrency` key can be a hard-coded string, or it can be a dynamic expression that includes context variables.

It is possible to define concurrency conditions in your workflow so that the workflow or job is part of a concurrency group.

This means that when a workflow run or job starts, GitHub will cancel any workflow runs or jobs that are already in progress in the same concurrency group. This is useful in scenarios where you want to prevent parallel runs for a certain set of a workflows or jobs, such as the ones used for deployments to a staging environment, in order to prevent actions that could cause conflicts or consume more resources than necessary.

In this example, `job-1` is part of a concurrency group named `staging_environment`. This means that if a new run of `job-1` is triggered, any runs of the same job in the `staging_environment` concurrency group that are already in progress will be cancelled.

```
jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: staging_environment
      cancel-in-progress: true
```

Alternatively, using a dynamic expression such as `concurrency: ci-${{ github.ref }}` in your workflow means that the workflow or job would be part of a concurrency group named `ci-` followed by the reference of the branch or tag that triggered the workflow. In this example, if a new commit is pushed to the main branch while a previous run is still in progress, the previous run will be cancelled and the new one will start:

```
on:
  push:
    branches:
      - main

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true
```

### Example: Queueing multiple pending runs

By default, only one job or workflow run can be `pending` in a concurrency group at a time. To allow multiple runs to queue instead of being canceled, set `queue: max`. With `queue: max`, up to 100 jobs or workflow runs can wait in the concurrency group; once the queue is full, any additional runs are canceled.

For example, the following workflow queues deployments to the `production` environment, processing them one at a time in order based on when each run started waiting on the concurrency group:

```
on:
  push:
    branches:
      - main

concurrency:
  group: production-deploy
  queue: max
```

Note that `queue: max` cannot be combined with `cancel-in-progress: true`, because the two options describe conflicting behaviors for handling in-progress runs.

### Example: Using concurrency to cancel any in-progress job or run

To use concurrency to cancel any in-progress job or run in GitHub Actions, you can use the `concurrency` key with the `cancel-in-progress` option set to `true`:

```
concurrency:
  group: ${{ github.ref }}
  cancel-in-progress: true
```

Note that in this example, without defining a particular concurrency group, GitHub Actions will cancel *any* in-progress run of the job or workflow.

### Example: Using a fallback value

If you build the group name with a property that is only defined for specific events, you can use a fallback value. For example, `github.head_ref` is only defined on `pull_request` events. If your workflow responds to other events in addition to `pull_request` events, you will need to provide a fallback to avoid a syntax error. The following concurrency group cancels in-progress jobs or runs on `pull_request` events only; if `github.head_ref` is undefined, the concurrency group will fallback to the run ID, which is guaranteed to be both unique and defined for the run.

```
concurrency:
  group: ${{ github.head_ref || github.run_id }}
  cancel-in-progress: true
```

### Example: Only cancel in-progress jobs or runs for the current workflow

If you have multiple workflows in the same repository, concurrency group names must be unique across workflows to avoid canceling in-progress jobs or runs from other workflows. Otherwise, any previously in-progress or pending job will be canceled, regardless of the workflow.

To only cancel in-progress runs of the same workflow, you can use the `github.workflow` property to build the concurrency group:

```
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### Example: Only cancel in-progress jobs on specific branches

If you would like to cancel in-progress jobs on certain branches but not on others, you can use conditional expressions with `cancel-in-progress`. For example, you can do this if you would like to cancel in-progress jobs on development branches but not on release branches.

To only cancel in-progress runs of the same workflow when not running on a release branch, you can set `cancel-in-progress` to an expression similar to the following:

```
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: ${{ !contains(github.ref, 'release/')}}
```

In this example, multiple pushes to a `release/1.2.3` branch would not cancel in-progress runs. Pushes to another branch, such as `main`, would cancel in-progress runs.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
