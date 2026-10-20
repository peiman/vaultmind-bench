---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#53-jobs-job-id-steps-working-directory-jobsjob-idstep.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-53-jobs-job-id-steps-working-directory-jobsjob-idstep
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].working-directory`](#jobsjob_idstepsworking-directory)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#53-jobs-job-id-steps-working-directory-jobsjob-idstep
source_hash: 2934a8dcec6e5af8c29683df97ebbf601c1d796dcc30f2c2b9324abd00e0fc60
---
Using the `working-directory` keyword, you can specify the working directory of where to run the command.

```
- name: Clean temp directory
  run: rm -rf *
  working-directory: ./temp
```

Alternatively, you can specify a default working directory for all `run` steps in a job, or for all `run` steps in the entire workflow. For more information, see [`defaults.run.working-directory`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrunworking-directory) and [`jobs.<job_id>.defaults.run.working-directory`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_iddefaultsrunworking-directory).

You can also use a `run` step to run a script. For more information, see [Adding scripts to your workflow](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/add-scripts).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
