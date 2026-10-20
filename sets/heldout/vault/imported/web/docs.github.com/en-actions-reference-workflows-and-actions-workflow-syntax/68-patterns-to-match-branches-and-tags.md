---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#68-patterns-to-match-branches-and-tags.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-68-patterns-to-match-branches-and-tags
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › Filter pattern cheat sheet › Patterns to match branches and tags
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#68-patterns-to-match-branches-and-tags
source_hash: c2391cd478080d84f423b04efd029011a3cf64b89ba8b5dab361acc4b4079e43
---
PatternDescriptionExample matches`feature/*`The `*` wildcard matches any character, but does not match slash (`/`).`feature/my-branch`

`feature/your-branch`

`feature/**`The `**` wildcard matches any character including slash (`/`) in branch and tag names.`feature/beta-a/my-branch`

`feature/your-branch`

`feature/mona/the/octocat`

`main`

`releases/mona-the-octocat`

Matches the exact name of a branch or tag name.`main`

`releases/mona-the-octocat`

`'*'`Matches all branch and tag names that don't contain a slash (`/`). The `*` character is a special character in YAML. When you start a pattern with `*`, you must use quotes.`main`

`releases`

`'**'`Matches all branch and tag names. This is the default behavior when you don't use a `branches` or `tags` filter.`all/the/branches`

`every/tag`

`'*feature'`The `*` character is a special character in YAML. When you start a pattern with `*`, you must use quotes.`mona-feature`

`feature`

`ver-10-feature`

`v2*`Matches branch and tag names that start with `v2`.`v2`

`v2.0`

`v2.9`

`v[12].[0-9]+.[0-9]+`Matches all semantic versioning branches and tags with major version 1 or 2.`v1.10.1`

`v2.0.0`

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
