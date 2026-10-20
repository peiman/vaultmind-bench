---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#67-filter-pattern-cheat-sheet.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-67-filter-pattern-cheat-sheet
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › Filter pattern cheat sheet
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#67-filter-pattern-cheat-sheet
source_hash: db26fb3ae55dace162c7c982ebd156d883d087d5239d5f5e8231b14eb49c9c60
---
You can use special characters in path, branch, tag, and workflow name filters.

- `*`: Matches zero or more characters, but does not match the `/` character. For example, `Octo*` matches `Octocat`.
- `**`: Matches zero or more of any character.
- `?`: Matches zero or one of the preceding character.
- `+`: Matches one or more of the preceding character.
- `[]` Matches one alphanumeric character listed in the brackets or included in ranges. Ranges can only include `a-z`, `A-Z`, and `0-9`. For example, the range`[0-9a-z]` matches any digit or lowercase letter. For example, `[CB]at` matches `Cat` or `Bat` and `[1-2]00` matches `100` and `200`.
- `!`: At the start of a pattern makes it negate previous positive patterns. It has no special meaning if not the first character.

The characters `*`, `[`, and `!` are special characters in YAML. If you start a pattern with `*`, `[`, or `!`, you must enclose the pattern in quotes. Also, if you use a [flow sequence](https://yaml.org/spec/1.2.2/#flow-sequences) with a pattern containing `[` and/or `]`, the pattern must be enclosed in quotes.

```
# Valid
paths:
  - '**/README.md'

# Invalid - creates a parse error that
# prevents your workflow from running.
paths:
  - **/README.md

# Valid
branches: [ main, 'release/v[0-9].[0-9]' ]

# Invalid - creates a parse error
branches: [ main, release/v[0-9].[0-9] ]
```

For more information about branch, tag, and path filter syntax, see [`on.<push>.<branches|tags>`](#onpushbranchestagsbranches-ignoretags-ignore), [`on.<pull_request>.<branches|tags>`](#onpull_requestpull_request_targetbranchesbranches-ignore), and [`on.<push|pull_request>.paths`](#onpushpull_requestpull_request_targetpathspaths-ignore).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
