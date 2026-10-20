---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#32-jobs-job-id-runs-on.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-32-jobs-job-id-runs-on
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.runs-on`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#32-jobs-job-id-runs-on
source_hash: dc54440eb147ee15ad0d8b70cf0c7355abaa3bfca0bdfc278010712c7d886c7e
---
Use `jobs.<job_id>.runs-on` to define the type of machine to run the job on.

- The destination machine can be either a [GitHub-hosted runner](#choosing-github-hosted-runners), [larger runner](#choosing-runners-in-a-group), or a [self-hosted runner](#choosing-self-hosted-runners).
- You can target runners based on the labels assigned to them, or their group membership, or a combination of these.
- You can provide `runs-on` as:
  
  - A single string
  - A single variable containing a string
  - An array of strings, variables containing strings, or a combination of both
  - A `key: value` pair using the `group` or `labels` keys
- If you specify an array of strings or variables, your workflow will execute on any runner that matches all of the specified `runs-on` values. For example, here the job will only run on a self-hosted runner that has the labels `linux`, `x64`, and `gpu`:
  
  ```
  runs-on: [self-hosted, linux, x64, gpu]
  ```
  
  For more information, see [Choosing self-hosted runners](#choosing-self-hosted-runners).
- You can mix strings and variables in an array. For example:
  
  ```
  on:
    workflow_dispatch:
      inputs:
        chosen-os:
          required: true
          type: choice
          options:
          - Ubuntu
          - macOS
  
  jobs:
    test:
      runs-on: [self-hosted, "${{ inputs.chosen-os }}"]
      steps:
      - run: echo Hello world!
  ```
- If you would like to run your workflow on multiple machines, use [`jobs.<job_id>.strategy`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstrategy).

Note

Quotation marks are not required around simple strings like `self-hosted`, but they are required for expressions like `"${{ inputs.chosen-os }}"`.

### Choosing GitHub-hosted runners

If you use a GitHub-hosted runner, each job runs in a fresh instance of a runner image specified by `runs-on`.

The value for runs-on, when you are using a GitHub-hosted runner, is a workflow label or the name of a runner group. The labels for the standard GitHub-hosted runners are shown in the following tables.

For more information, see [GitHub-hosted runners](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
