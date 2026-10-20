---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#47-example-using-secrets.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-47-example-using-secrets
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].if`](#jobsjob_idstepsif) › Example: Using secrets'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#47-example-using-secrets
source_hash: c9ce943bc66d3f627d96bce5f00fc8bf976132823ebcaa61af88a49453e5f9fa
---
Secrets cannot be directly referenced in `if:` conditionals. Instead, consider setting secrets as job-level environment variables, then referencing the environment variables to conditionally run steps in the job.

If a secret has not been set, the return value of an expression referencing the secret (such as `${{ secrets.SuperSecret }}` in the example) will be an empty string.

```
name: Run a step if a secret has been set
on: push
jobs:
  my-jobname:
    runs-on: ubuntu-latest
    env:
      super_secret: ${{ secrets.SuperSecret }}
    steps:
      - if: ${{ env.super_secret != '' }}
        run: echo 'This step will only run if the secret has a value set.'
      - if: ${{ env.super_secret == '' }}
        run: echo 'This step will only run if the secret does not have a value set.'
```

For more information, see [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability) and [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).

## [`jobs.<job_id>.steps[*].name`](#jobsjob_idstepsname)

A name for your step to display on GitHub.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
