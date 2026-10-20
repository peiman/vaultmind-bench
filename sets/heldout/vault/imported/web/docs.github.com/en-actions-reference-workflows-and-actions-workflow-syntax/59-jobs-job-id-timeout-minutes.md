---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#59-jobs-job-id-timeout-minutes.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-59-jobs-job-id-timeout-minutes
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.timeout-minutes`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#59-jobs-job-id-timeout-minutes
source_hash: 4fc66c5b4dfa61008a4dcb990ac5e126b6852316bf8e959ab2d187b2d658a70c
---
The maximum number of minutes to let a job run before GitHub automatically cancels it. Default: 360

If the timeout exceeds the job execution time limit for the runner, the job will be canceled when the execution time limit is met instead. For more information about job execution time limits, see [Billing and usage](https://docs.github.com/en/actions/concepts/billing-and-usage#usage-limits-and-policy) for GitHub-hosted runners and [Actions limits](https://docs.github.com/en/actions/reference/limits) for self-hosted runner usage limits.

Note

The `GITHUB_TOKEN` expires when a job finishes or after a maximum of 24 hours. For self-hosted runners, the token may be the limiting factor if the job timeout is greater than 24 hours. For more information on the `GITHUB_TOKEN`, see [Use GITHUB\_TOKEN for authentication in workflows](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token).

## `jobs.<job_id>.strategy`

Use `jobs.<job_id>.strategy` to use a matrix strategy for your jobs. A matrix strategy lets you use variables in a single job definition to automatically create multiple job runs that are based on the combinations of the variables. For example, you can use a matrix strategy to test your code in multiple versions of a language or on multiple operating systems. For more information, see [Running variations of jobs in a workflow](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/run-job-variations).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
