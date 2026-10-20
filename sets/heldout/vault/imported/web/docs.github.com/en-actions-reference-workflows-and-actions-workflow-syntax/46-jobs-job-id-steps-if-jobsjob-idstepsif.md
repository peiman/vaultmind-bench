---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#46-jobs-job-id-steps-if-jobsjob-idstepsif.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-46-jobs-job-id-steps-if-jobsjob-idstepsif
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].if`](#jobsjob_idstepsif)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#46-jobs-job-id-steps-if-jobsjob-idstepsif
source_hash: f58486364f549ca5ae0faabb46b14813729101093d9f7d43529cc4ba568f3dc5
---
You can use the `if` conditional to prevent a step from running unless a condition is met. You can use any supported context and expression to create a conditional. For more information on which contexts are supported in this key, see [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability).

When you use expressions in an `if` conditional, you can, optionally, omit the `${{ }}` expression syntax because GitHub Actions automatically evaluates the `if` conditional as an expression. However, this exception does not apply everywhere.

You must always use the `${{ }}` expression syntax or escape with `''`, `""`, or `()` when the expression starts with `!`, since `!` is reserved notation in YAML format. For example:

```
if: ${{ ! startsWith(github.ref, 'refs/tags/') }}
```

For more information, see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions).

### Example: Using contexts

This step only runs when the event type is a `pull_request` and the event action is `unassigned`.

```
steps:
  - name: My first step
    if: ${{ github.event_name == 'pull_request' && github.event.action == 'unassigned' }}
    run: echo This event is a pull request that had an assignee removed.
```

### Example: Using status check functions

The `my backup step` only runs when the previous step of a job fails. For more information, see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#status-check-functions).

```
steps:
  - name: My first step
    uses: octo-org/action-name@main
  - name: My backup step
    if: ${{ failure() }}
    uses: actions/heroku@1.0.0
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
