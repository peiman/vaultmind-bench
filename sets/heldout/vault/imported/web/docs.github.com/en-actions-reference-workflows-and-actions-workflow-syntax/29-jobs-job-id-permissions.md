---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#29-jobs-job-id-permissions.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-29-jobs-job-id-permissions
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.permissions` (3/3)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#29-jobs-job-id-permissions
source_hash: 274839c13c3fe890ea70553598fdd1f6188143aa66e14ce6a956b4211fbded8c
---
`statuses`Work with commit statuses. For example, `statuses:read` permits an action to list the commit statuses for a given reference. For more information, see [Permissions required for GitHub Apps](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-commit-statuses).`vulnerability-alerts`Read Dependabot alerts. For example, `vulnerability-alerts: read` permits an action to list Dependabot alerts for the repository. Only `read` and `none` are supported; `write` is not valid. When `write-all` or `read-all` is used, `vulnerability-alerts` is automatically included as `read`. For more information, see [Repository permissions for "Dependabot alerts"](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps?apiVersion=2022-11-28#repository-permissions-for-dependabot-alerts).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
