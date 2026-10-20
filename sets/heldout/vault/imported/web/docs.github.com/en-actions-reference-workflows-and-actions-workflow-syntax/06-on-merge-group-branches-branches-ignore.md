---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#06-on-merge-group-branches-branches-ignore.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-06-on-merge-group-branches-branches-ignore
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `on.merge_group.<branches|branches-ignore>`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#06-on-merge-group-branches-branches-ignore
source_hash: bbd44230fcb4da18fca1cb21b1ce1575d833e5739cb4ca7b14a755e006b3c470
---
When using the `merge_group` event, you can configure a workflow to run only for merge groups that target specific branches.

Use the `branches` filter when you want to include branch name patterns or when you want to both include and exclude branch name patterns. Use `branches-ignore` when you only want to exclude branch name patterns. You cannot use both `branches` and `branches-ignore` for the same event in a workflow.

The `branches` and `branches-ignore` filters accept glob patterns that use characters like `*`, `**`, `+`, `?`, `!` and others to match more than one branch name. If a name contains any of these characters and you want a literal match, you need to escape each of these special characters with `\`. For more information about glob patterns, see [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet).

### Example: Including branches

The patterns defined in `branches` are evaluated against the target branch's name. For example, the following workflow will run whenever there is a `merge_group` event for a merge group that targets:

- A branch named `main`
- A branch whose name starts with `releases/`

```
on:
  merge_group:
    types: [checks_requested]
    branches:
      - main
      - 'releases/**'
```

### Example: Excluding branches

When a pattern matches the `branches-ignore` pattern, the workflow will not run. The patterns defined in `branches-ignore` are evaluated against the target branch's name. For example, the following workflow will run whenever there is a `merge_group` event unless the merge group targets:

- A branch named `canary`
- A branch whose name matches `releases/**-alpha`, like `releases/beta/3-alpha`

```
on:
  merge_group:
    types: [checks_requested]
    branches-ignore:
      - canary
      - 'releases/**-alpha'
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
