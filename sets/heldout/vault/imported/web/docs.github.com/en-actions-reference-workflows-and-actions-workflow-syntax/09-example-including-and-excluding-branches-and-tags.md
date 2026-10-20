---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#09-example-including-and-excluding-branches-and-tags.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-09-example-including-and-excluding-branches-and-tags
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › `on.merge_group.<branches|branches-ignore>` › Example: Including and excluding branches and tags'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#09-example-including-and-excluding-branches-and-tags
source_hash: 602b356ef73475d7cc02289003be2c56d68517be63794faaaea0be2a047fb81c
---
You can't use `branches` and `branches-ignore` to filter the same event in a single workflow. Similarly, you can't use `tags` and `tags-ignore` to filter the same event in a single workflow. If you want to both include and exclude branch or tag patterns for a single event, use the `branches` or `tags` filter along with the `!` character to indicate which branches or tags should be excluded.

If you define a branch with the `!` character, you must also define at least one branch without the `!` character. If you only want to exclude branches, use `branches-ignore` instead. Similarly, if you define a tag with the `!` character, you must also define at least one tag without the `!` character. If you only want to exclude tags, use `tags-ignore` instead.

The order that you define patterns matters.

- A matching negative pattern (prefixed with `!`) after a positive match will exclude the Git ref.
- A matching positive pattern after a negative match will include the Git ref again.

The following workflow will run on pushes to `releases/10` or `releases/beta/mona`, but not on `releases/10-alpha` or `releases/beta/3-alpha` because the negative pattern `!releases/**-alpha` follows the positive pattern.

```
on:
  push:
    branches:
      - 'releases/**'
      - '!releases/**-alpha'
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
