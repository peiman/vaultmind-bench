---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#41-jobs-job-id-outputs.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-41-jobs-job-id-outputs
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.outputs`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#41-jobs-job-id-outputs
source_hash: 0d5963e1e7c736912a8a29c8bfe57c9ac3012dd07196baafd9b9e553dfdbb554
---
You can use `jobs.<job_id>.outputs` to create a `map` of outputs for a job. Job outputs are available to all downstream jobs that depend on this job. For more information on defining job dependencies, see [`jobs.<job_id>.needs`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_idneeds).

Outputs can be a maximum of 1 MB per job. The total of all outputs in a workflow run can be a maximum of 50 MB. Size is approximated based on UTF-16 encoding.

Job outputs containing expressions are evaluated on the runner at the end of each job. Outputs containing secrets are redacted on the runner and not sent to GitHub Actions.

If an output is skipped because it may contain a secret, you will see the following warning message: "Skip output `{output.Key}` since it may contain secret." For more information on how to handle secrets, please refer to the [Example: Masking and passing a secret between jobs or workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#example-masking-and-passing-a-secret-between-jobs-or-workflows).

To use job outputs in a dependent job, you can use the `needs` context. For more information, see [Contexts reference](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#needs-context).

### Example: Defining outputs for a job

```
jobs:
  job1:
    runs-on: ubuntu-latest
    # Map a step output to a job output
    outputs:
      output1: ${{ steps.step1.outputs.test }}
      output2: ${{ steps.step2.outputs.test }}
    steps:
      - id: step1
        run: echo "test=hello" >> "$GITHUB_OUTPUT"
      - id: step2
        run: echo "test=world" >> "$GITHUB_OUTPUT"
  job2:
    runs-on: ubuntu-latest
    needs: job1
    steps:
      - env:
          OUTPUT1: ${{needs.job1.outputs.output1}}
          OUTPUT2: ${{needs.job1.outputs.output2}}
        run: echo "$OUTPUT1 $OUTPUT2"
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
