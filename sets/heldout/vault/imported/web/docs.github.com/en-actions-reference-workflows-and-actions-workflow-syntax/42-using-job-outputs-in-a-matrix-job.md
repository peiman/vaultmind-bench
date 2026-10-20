---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#42-using-job-outputs-in-a-matrix-job.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-42-using-job-outputs-in-a-matrix-job
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.outputs` › Using Job Outputs in a Matrix Job
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#42-using-job-outputs-in-a-matrix-job
source_hash: 9e9e2bbb75cc0817ceb4c9b0358418e350489b813db678046d726240de429171
---
Matrices can be used to generate multiple outputs of different names. When using a matrix, job outputs will be combined from all jobs inside the matrix.

```
jobs:
  job1:
    runs-on: ubuntu-latest
    outputs:
      output_1: ${{ steps.gen_output.outputs.output_1 }}
      output_2: ${{ steps.gen_output.outputs.output_2 }}
      output_3: ${{ steps.gen_output.outputs.output_3 }}
    strategy:
      matrix:
        version: [1, 2, 3]
    steps:
      - name: Generate output
        id: gen_output
        run: |
          version="${{ matrix.version }}"
          echo "output_${version}=${version}" >> "$GITHUB_OUTPUT"
  job2:
    runs-on: ubuntu-latest
    needs: [job1]
    steps:
      # Will show
      # {
      #   "output_1": "1",
      #   "output_2": "2",
      #   "output_3": "3"
      # }
      - run: echo '${{ toJSON(needs.job1.outputs) }}'
```

Warning

Actions does not guarantee the order that matrix jobs will run in. Ensure that the output name is unique, otherwise the last matrix job that runs will override the output value.

## `jobs.<job_id>.env`

A `map` of variables that are available to all steps in the job. You can set variables for the entire workflow or an individual step. For more information, see [`env`](#env) and [`jobs.<job_id>.steps[*].env`](#jobsjob_idstepsenv).

When more than one environment variable is defined with the same name, GitHub uses the most specific variable. For example, an environment variable defined in a step will override job and workflow environment variables with the same name, while the step executes. An environment variable defined for a job will override a workflow variable with the same name, while the job executes.

### Example of `jobs.<job_id>.env`

```
jobs:
  job1:
    env:
      FIRST_NAME: Mona
```

## `jobs.<job_id>.defaults`

Use `jobs.<job_id>.defaults` to create a `map` of default settings that will apply to all steps in the job. You can also set default settings for the entire workflow. For more information, see [`defaults`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaults).

When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
