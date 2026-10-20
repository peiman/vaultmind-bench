---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#27-jobs-job-id-permissions.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-27-jobs-job-id-permissions
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.permissions` (1/3)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#27-jobs-job-id-permissions
source_hash: f9c758cf8305bd47803b032805c3effb73b20e7d4a5cdda7ffa602f324520460
---
For a specific job, you can use `jobs.<job_id>.permissions` to modify the default permissions granted to the `GITHUB_TOKEN`, adding or removing access as required, so that you only allow the minimum required access. For more information, see [Use GITHUB\_TOKEN for authentication in workflows](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token#modifying-the-permissions-for-the-github_token).

By specifying the permission within a job definition, you can configure a different set of permissions for the `GITHUB_TOKEN` for each job, if required. Alternatively, you can specify the permissions for all jobs in the workflow. For information on defining permissions at the workflow level, see [`permissions`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#permissions).

For each of the available permissions, shown in the table below, you can assign one of the access levels: `read` (if applicable), `write`, or `none`. `write` includes `read`. If you specify the access for any of these permissions, all of those that are not specified are set to `none`.

Available permissions and details of what each allows an action to do:

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
