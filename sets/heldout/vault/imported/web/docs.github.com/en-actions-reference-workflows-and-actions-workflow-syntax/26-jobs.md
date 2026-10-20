---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#26-jobs.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-26-jobs
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#26-jobs
source_hash: a1f2060a061feac492ef5e560e22b0686c4b056e6f3f14732cb36852d50927ea
---
A workflow run is made up of one or more `jobs`, which run in parallel by default. To run jobs sequentially, you can define dependencies on other jobs using the `jobs.<job_id>.needs` keyword.

Each job runs in a runner environment specified by `runs-on`.

You can run an unlimited number of jobs as long as you are within the workflow usage limits. For more information, see [Billing and usage](https://docs.github.com/en/actions/concepts/billing-and-usage) for GitHub-hosted runners and [Actions limits](https://docs.github.com/en/actions/reference/limits) for self-hosted runner usage limits.

If you need to find the unique identifier of a job running in a workflow run, you can use the GitHub API. For more information, see [REST API endpoints for GitHub Actions](https://docs.github.com/en/rest/actions#workflow-jobs).

## `jobs.<job_id>`

Use `jobs.<job_id>` to give your job a unique identifier. The key `job_id` is a string and its value is a map of the job's configuration data. You must replace `<job_id>` with a string that is unique to the `jobs` object. The `<job_id>` must start with a letter or `_` and contain only alphanumeric characters, `-`, or `_`.

### Example: Creating jobs

In this example, two jobs have been created, and their `job_id` values are `my_first_job` and `my_second_job`.

```
jobs:
  my_first_job:
    name: My first job
  my_second_job:
    name: My second job
```

## `jobs.<job_id>.name`

Use `jobs.<job_id>.name` to set a name for the job, which is displayed in the GitHub UI.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
