---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#45-jobs-job-id-steps.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-45-jobs-job-id-steps
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.steps`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#45-jobs-job-id-steps
source_hash: 95673431ed3520a0b9f88820100b2645e3e3971f36eef7b463912d98600ee597
---
A job contains a sequence of tasks called `steps`. Steps can run commands, run setup tasks, or run an action in your repository, a public repository, or an action published in a Docker registry. Not all steps run actions, but all actions run as a step. Each step runs in its own process in the runner environment and has access to the workspace and filesystem. Because steps run in their own process, changes to environment variables are not preserved between steps. GitHub provides built-in steps to set up and complete a job.

GitHub only displays the first 1,000 checks, however, you can run an unlimited number of steps as long as you are within the workflow usage limits. For more information, see [Billing and usage](https://docs.github.com/en/actions/concepts/billing-and-usage) for GitHub-hosted runners and [Actions limits](https://docs.github.com/en/actions/reference/limits) for self-hosted runner usage limits.

### Example of `jobs.<job_id>.steps`

```
name: Greeting from Mona

on: push

jobs:
  my-job:
    name: My Job
    runs-on: ubuntu-latest
    steps:
      - name: Print a greeting
        env:
          MY_VAR: Hi there! My name is
          FIRST_NAME: Mona
          MIDDLE_NAME: The
          LAST_NAME: Octocat
        run: |
          echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```

## [`jobs.<job_id>.steps[*].id`](#jobsjob_idstepsid)

A unique identifier for the step. You can use the `id` to reference the step in contexts. For more information, see [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
