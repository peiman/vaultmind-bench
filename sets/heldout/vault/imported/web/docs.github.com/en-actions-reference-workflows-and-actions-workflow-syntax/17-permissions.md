---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#17-permissions.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-17-permissions
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `permissions` (1/3)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#17-permissions
source_hash: 6ccf3d25a269da7ed9b39b3efa0ed94266ebe428ddbdbb3dec867fd06baf7359
---
You can use `permissions` to modify the default permissions granted to the `GITHUB_TOKEN`, adding or removing access as required, so that you only allow the minimum required access. For more information, see [Use GITHUB\_TOKEN for authentication in workflows](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token#modifying-the-permissions-for-the-github_token).

You can use `permissions` either as a top-level key, to apply to all jobs in the workflow, or within specific jobs. When you add the `permissions` key within a specific job, all actions and run commands within that job that use the `GITHUB_TOKEN` gain the access rights you specify. For more information, see [`jobs.<job_id>.permissions`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idpermissions).

Owners of an organization can restrict write access for the `GITHUB_TOKEN` at the repository level. For more information, see [Disabling or limiting GitHub Actions for your organization](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization).

When a workflow is triggered by the [`pull_request_target`](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target) event, the `GITHUB_TOKEN` is granted read/write repository permission, even when it is triggered from a public fork. For more information, see [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request_target).

For each of the available permissions, shown in the table below, you can assign one of the access levels: `read` (if applicable), `write`, or `none`. `write` includes `read`. If you specify the access for any of these permissions, all of those that are not specified are set to `none`.

Available permissions and details of what each allows an action to do:

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
