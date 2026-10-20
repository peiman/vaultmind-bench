---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#16-on-workflow-run-workflows.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-16-on-workflow-run-workflows
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `on.workflow_run.workflows`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#16-on-workflow-run-workflows
source_hash: a31a872f35f7379cccc4897c0ba872424a1284d5b5ad45b8beec1c17e09b3bd3
---
When using the `workflow_run` event, you can specify which workflows can trigger your workflow.

The `workflows` filters accept glob patterns that use characters like `*`, `**`, `+`, `?`, `!` and others to match more than one workflow name. If a name contains any of these characters and you want a literal match, you need to *escape* each of these special characters with `\`. For more information about glob patterns, see the [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#filter-pattern-cheat-sheet).

For example, a workflow with the following trigger will only run when the workflow named `Build` runs:

```
on:
  workflow_run:
    workflows: ["Build"]
    types: [requested]
```

A workflow with the following trigger will only run when a workflow whose name starts with `Build` completed:

```
on:
  workflow_run:
    workflows: ["Build*"]
    types: [completed]
```

A workflow with the following trigger will only run when the workflow named `Build C++` completed:

```
on:
  workflow_run:
    workflows: ["Build C\\+\\+"]
    types: [completed]
```

## `on.workflow_dispatch`

When using the `workflow_dispatch` event, you can optionally specify inputs that are passed to the workflow.

This trigger only receives events when the workflow file is on the default branch.

## `on.workflow_dispatch.inputs`

The triggered workflow receives the inputs in the `inputs` context. For more information, see [Contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#inputs-context).

Note

- The workflow will also receive the inputs in the `github.event.inputs` context. The information in the `inputs` context and `github.event.inputs` context is identical except that the `inputs` context preserves Boolean values as Booleans instead of converting them to strings. The `choice` type resolves to a string and is a single selectable option.
- The maximum number of top-level properties for `inputs` is 25 .
- The maximum payload for `inputs` is 65,535 characters.

### Example of `on.workflow_dispatch.inputs`

```
on:
  workflow_dispatch:
    inputs:
      logLevel:
        description: 'Log level'
        required: true
        default: 'warning'
        type: choice
        options:
          - info
          - warning
          - debug
      print_tags:
        description: 'True to print to STDOUT'
        required: true
        type: boolean
      tags:
        description: 'Test scenario tags'
        required: true
        type: string
      environment:
        description: 'Environment to run tests against'
        type: environment
        required: true

jobs:
  print-tag:
    runs-on: ubuntu-latest
    if: ${{ inputs.print_tags }} 
    steps:
      - name: Print the input tag to STDOUT
        run: echo  The tags are ${{ inputs.tags }} 
```

## `on.workflow_dispatch.inputs.<input_id>.required`

A boolean specifying whether the input must be supplied.

## `on.workflow_dispatch.inputs.<input_id>.type`

The value of this parameter is a string specifying the data type of the input. This must be one of: `boolean`, `choice`, `number`, `environment` or `string`.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
