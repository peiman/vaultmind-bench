---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#23-concurrency.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-23-concurrency
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `concurrency`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#23-concurrency
source_hash: bf603cd8aba2b3daa35f9475885322d7d2ed5b3ea5dbb6e8447af15bd0e4f3b5
---
Use `concurrency` to ensure that only a single job or workflow using the same concurrency group will run at a time. A concurrency group can be any string or expression. The expression can only use [`github`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context), [`inputs`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#inputs-context) and [`vars`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#vars-context) contexts. For more information about expressions, see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions).

You can also specify `concurrency` at the job level. For more information, see [`jobs.<job_id>.concurrency`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idconcurrency).

This means that there can be at most one running job or workflow in a concurrency group at any time. When a concurrent job or workflow is queued, if another job or workflow using the same concurrency group in the repository is in progress, the queued job or workflow will be `pending`. By default, any existing `pending` job or workflow in the same concurrency group will be canceled and the new queued job or workflow will take its place.

To also cancel any currently running job or workflow in the same concurrency group, specify `cancel-in-progress: true`. To conditionally cancel currently running jobs or workflows in the same concurrency group, you can specify `cancel-in-progress` as an expression with any of the allowed expression contexts.

To allow more than one `pending` job or workflow run to wait in the same concurrency group, use the optional `queue` property. The `queue` property accepts the following values:

- `single` (default): At most one job or workflow run can be `pending` in the concurrency group. When a new job or workflow run is queued, any existing `pending` job or workflow run in the same group is canceled and replaced.
- `max`: Up to 100 jobs or workflow runs can be `pending` in the concurrency group. When the queue is full, any additional jobs or workflow runs are canceled.

The combination of `queue: max` and `cancel-in-progress: true` is not allowed and will result in a workflow validation error.

Note

- The concurrency group name is case insensitive. For example, `prod` and `Prod` will be treated as the same concurrency group.
- Jobs or workflow runs in the same concurrency group are processed in first-in-first-out (FIFO) order according to the time each one started waiting on the concurrency group, not the time each workflow was dispatched. Since the actual start time of a job or run may vary, ordering is not guaranteed.

### Example: Using concurrency and the default behavior

The default behavior of GitHub Actions is to allow multiple jobs or workflow runs to run concurrently. The `concurrency` keyword allows you to control the concurrency of workflow runs.

For example, you can use the `concurrency` keyword immediately after where trigger conditions are defined to limit the concurrency of entire workflow runs for a specific branch:

```
on:
  push:
    branches:
      - main

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

You can also limit the concurrency of jobs within a workflow by using the `concurrency` keyword at the job level:

```
on:
  push:
    branches:
      - main

jobs:
  job-1:
    runs-on: ubuntu-latest
    concurrency:
      group: example-group
      cancel-in-progress: true
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
