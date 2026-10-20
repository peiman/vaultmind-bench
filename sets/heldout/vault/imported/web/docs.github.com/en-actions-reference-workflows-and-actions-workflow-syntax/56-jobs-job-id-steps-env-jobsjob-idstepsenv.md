---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#56-jobs-job-id-steps-env-jobsjob-idstepsenv.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-56-jobs-job-id-steps-env-jobsjob-idstepsenv
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].env`](#jobsjob_idstepsenv)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#56-jobs-job-id-steps-env-jobsjob-idstepsenv
source_hash: a30fc7a8064506d7abb89138d12c016dbe68b9d4b37e14ad59166f27fd7eeec1
---
Sets variables for steps to use in the runner environment. You can also set variables for the entire workflow or a job. For more information, see [`env`](#env) and [`jobs.<job_id>.env`](#jobsjob_idenv).

When more than one environment variable is defined with the same name, GitHub uses the most specific variable. For example, an environment variable defined in a step will override job and workflow environment variables with the same name, while the step executes. An environment variable defined for a job will override a workflow variable with the same name, while the job executes.

Public actions may specify expected variables in the README file. If you are setting a secret or sensitive value, such as a password or token, you must set secrets using the `secrets` context. For more information, see [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts).

### [Example of `jobs.<job_id>.steps[*].env`](#example-of-jobsjob_idstepsenv)

```
steps:
  - name: My first action
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      FIRST_NAME: Mona
      LAST_NAME: Octocat
```

## [`jobs.<job_id>.steps[*].continue-on-error`](#jobsjob_idstepscontinue-on-error)

Prevents a job from failing when a step fails. Set to `true` to allow a job to pass when this step fails.

## [`jobs.<job_id>.steps[*].timeout-minutes`](#jobsjob_idstepstimeout-minutes)

The maximum number of minutes to run the step before killing the process. Maximum: 360 for both GitHub-hosted and self-hosted runners.

Fractional values are not supported. `timeout-minutes` must be a positive integer.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
