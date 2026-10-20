---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#43-jobs-job-id-defaults-run.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-43-jobs-job-id-defaults-run
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.defaults.run`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#43-jobs-job-id-defaults-run
source_hash: 8b7954550267c2cb3b4b336d17909abbeb876c89c5cbaedf62dcd0b785fc5ba3
---
Use `jobs.<job_id>.defaults.run` to provide default `shell` and `working-directory` to all `run` steps in the job.

You can provide default `shell` and `working-directory` options for all [`run`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idstepsrun) steps in a job. You can also set default settings for `run` for the entire workflow. For more information, see [`defaults.run`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrun).

These can be overridden at the `jobs.<job_id>.defaults.run` and `jobs.<job_id>.steps[*].run` levels.

When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
