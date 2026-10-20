---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#14-on-workflow-call-inputs.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-14-on-workflow-call-inputs
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `on.workflow_call.inputs`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#14-on-workflow-call-inputs
source_hash: 951785caeedb64421747b9fb5b6d1d68c3ed99ad021da1a671233e21a96087a7
---
When using the `workflow_call` keyword, you can optionally specify inputs that are passed to the called workflow from the caller workflow. For more information about the `workflow_call` keyword, see [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#workflow_call).

In addition to the standard input parameters that are available, `on.workflow_call.inputs` requires a `type` parameter. For more information, see [`on.workflow_call.inputs.<input_id>.type`](#onworkflow_callinputsinput_idtype).

If a `default` parameter is not set, the default value of the input is `false` for a boolean, `0` for a number, and `""` for a string.

Within the called workflow, you can use the `inputs` context to refer to an input. For more information, see [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#inputs-context).

If a caller workflow passes an input that is not specified in the called workflow, this results in an error.

### Example of `on.workflow_call.inputs`

```
on:
  workflow_call:
    inputs:
      username:
        description: 'A username passed from the caller workflow'
        default: 'john-doe'
        required: false
        type: string

jobs:
  print-username:
    runs-on: ubuntu-latest

    steps:
      - name: Print the input name to STDOUT
        run: echo The username is ${{ inputs.username }}
```

For more information, see [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

## `on.workflow_call.inputs.<input_id>.type`

Required if input is defined for the `on.workflow_call` keyword. The value of this parameter is a string specifying the data type of the input. This must be one of: `boolean`, `number`, or `string`.

## `on.workflow_call.outputs`

A map of outputs for a called workflow. Called workflow outputs are available to all downstream jobs in the caller workflow. Each output has an identifier, an optional `description,` and a `value.` The `value` must be set to the value of an output from a job within the called workflow.

In the example below, two outputs are defined for this reusable workflow: `workflow_output1` and `workflow_output2`. These are mapped to outputs called `job_output1` and `job_output2`, both from a job called `my_job`.

### Example of `on.workflow_call.outputs`

```
on:
  workflow_call:
    # Map the workflow outputs to job outputs
    outputs:
      workflow_output1:
        description: "The first job output"
        value: ${{ jobs.my_job.outputs.job_output1 }}
      workflow_output2:
        description: "The second job output"
        value: ${{ jobs.my_job.outputs.job_output2 }}
```

For information on how to reference a job output, see [`jobs.<job_id>.outputs`](#jobsjob_idoutputs). For more information, see [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

## `on.workflow_call.secrets`

A map of the secrets that can be used in the called workflow.

Within the called workflow, you can use the `secrets` context to refer to a secret.

Note

If you are passing the secret to a nested reusable workflow, then you must use [`jobs.<job_id>.secrets`](#jobsjob_idsecrets) again to pass the secret. For more information, see [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows#passing-secrets-to-nested-workflows).

If a caller workflow passes a secret that is not specified in the called workflow, this results in an error.

### Example of `on.workflow_call.secrets`

```
on:
  workflow_call:
    secrets:
      access-token:
        description: 'A token passed from the caller workflow'
        required: false

jobs:

  pass-secret-to-action:
    runs-on: ubuntu-latest
    steps:
    # passing the secret to an action
      - name: Pass the received secret to an action
        uses: ./.github/actions/my-action
        with:
          token: ${{ secrets.access-token }}

  # passing the secret to a nested reusable workflow
  pass-secret-to-workflow:
    uses: ./.github/workflows/my-workflow
    secrets:
       token: ${{ secrets.access-token }}
```

## `on.workflow_call.secrets.<secret_id>`

A string identifier to associate with the secret.

## `on.workflow_call.secrets.<secret_id>.required`

A boolean specifying whether the secret must be supplied.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
