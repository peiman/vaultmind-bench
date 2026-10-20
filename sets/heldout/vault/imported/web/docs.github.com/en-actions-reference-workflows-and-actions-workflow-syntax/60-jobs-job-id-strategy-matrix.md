---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#60-jobs-job-id-strategy-matrix.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-60-jobs-job-id-strategy-matrix
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.strategy.matrix`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#60-jobs-job-id-strategy-matrix
source_hash: d073862d6622592753d4990a2cfb7cfb468f38885d25316cf42a8c1e64b806a2
---
Use `jobs.<job_id>.strategy.matrix` to define a matrix of different job configurations. For more information, see [Running variations of jobs in a workflow](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations).

A matrix will generate a maximum of 256 jobs per workflow run. This limit applies to both GitHub-hosted and self-hosted runners.

The variables that you define become properties in the `matrix` context, and you can reference the property in other areas of your workflow file. In this example, you can use `matrix.version` and `matrix.os` to access the current value of `version` and `os` that the job is using. For more information, see [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

Note

The variable names are case insensitive. For example, `OS` and `os` will be treated as the same variable.

By default, GitHub will maximize the number of jobs run in parallel depending on runner availability. The order of the variables in the matrix determines the order in which the jobs are created. The first variable you define will be the first job that is created in your workflow run.

### Using a single-dimension matrix

The following workflow defines the variable `version` with the values `[10, 12, 14]`. The workflow will run three jobs, one for each value in the variable. Each job will access the `version` value through the `matrix.version` context and pass the value as `node-version` to the `actions/setup-node` action.

```
jobs:
  example_matrix:
    strategy:
      matrix:
        version: [10, 12, 14]
    steps:
      - uses: actions/setup-node@v7
        with:
          node-version: ${{ matrix.version }}
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
