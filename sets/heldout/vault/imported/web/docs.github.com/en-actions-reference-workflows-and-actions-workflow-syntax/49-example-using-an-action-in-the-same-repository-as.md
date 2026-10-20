---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#49-example-using-an-action-in-the-same-repository-as.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-49-example-using-an-action-in-the-same-repository-as
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].uses`](#jobsjob_idstepsuses) › Example: Using an action in the same repository as the workflow at the running commit (recommended)'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#49-example-using-an-action-in-the-same-repository-as
source_hash: 4b1db189a99ec6871046d48911fee5f94c41b624d60b8d841a69d3a4a6a19906
---
`$/path/to/action`

The `$/` prefix is the self repository reference. It references an action stored in the same repository as the workflow or action that is currently running, and resolves to that repository at the running commit (the same SHA as the running workflow or action). You do not need to check out the repository first, so it is the recommended way to reference an action within its own repository.

The `$/` syntax is not available in GitHub Enterprise Server.

A `$/` reference must not include an `@{ref}` suffix. The ref is always the commit the running workflow or action is using, so a reference such as `$/actions/my-action@v1` is invalid.

`$/` always resolves against the repository of the file it appears in, not the repository that called it. For example, if a reusable workflow in one repository is called by a workflow in another repository, a `$/` reference in the called workflow resolves to the called workflow's repository, not the calling workflow's repository. This makes `$/` reliable for action composition, where a relative `./` path would instead resolve against whatever is checked out in the caller's workspace. For using `$/` in a composite action's steps, see [Metadata syntax reference](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax#runsstepsuses).

The following table compares the ways to reference an action.

SyntaxResolves toRecommended for`$/path/to/action`The same repository as the running workflow or action, at the running commitActions in the same repository`{owner}/{repo}@{ref}`The specified repository at the specified refActions in another repository`./path/to/action`A path in the runner's checked-out workspace, relative to the default working directory (`${{ github.workspace }}`)Edge cases only

```
on: [push]

jobs:
  my_first_job:
    runs-on: ubuntu-latest
    steps:
      # References an action in the same repository at the running commit
      - uses: $/.github/actions/hello-world-action
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
