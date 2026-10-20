---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#66-jobs-job-id-uses.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-66-jobs-job-id-uses
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.uses`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#66-jobs-job-id-uses
source_hash: d52ed8507ecd3d4b879861608aa7f1c5a863d8fa098f171a3b17bf816fd46743
---
The location and version of a reusable workflow file to run as a job. Use one of the following syntaxes:

- `$/.github/workflows/{filename}` for a reusable workflow in the same repository. This is the recommended syntax for referencing a reusable workflow in the same repository. This syntax is not available in GitHub Enterprise Server.
- `{owner}/{repo}/.github/workflows/{filename}@{ref}` for reusable workflows in public and private repositories.
- `./.github/workflows/{filename}` for reusable workflows in the same repository.

When you reference a reusable workflow with `{owner}/{repo}` and `@{ref}`, the `{ref}` can be a SHA, a release tag, or a branch name. If a release tag and a branch have the same name, the release tag takes precedence over the branch name. Using the commit SHA is the safest option for stability and security. For more information, see [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use#reusing-third-party-workflows).

When you reference a reusable workflow in the same repository using `$/` or `./` (without `{owner}/{repo}` and `@{ref}`), the called workflow is from the same commit as the caller workflow. A `$/` reference must not include an `@{ref}` suffix, and `$/` is not available in GitHub Enterprise Server. Ref prefixes such as `refs/heads` and `refs/tags` are not allowed. You cannot use contexts or expressions in this keyword.

### Example of `jobs.<job_id>.uses`

```
jobs:
  call-workflow-1-in-local-repo:
    uses: octo-org/this-repo/.github/workflows/workflow-1.yml@172239021f7ba04fe7327647b213799853a9eb89
  call-workflow-2-in-local-repo:
    uses: ./.github/workflows/workflow-2.yml
  # The `$/` syntax is not available in GitHub Enterprise Server.
  call-workflow-in-same-repo-at-running-commit:
    uses: $/.github/workflows/workflow-2.yml
  call-workflow-in-another-repo:
    uses: octo-org/another-repo/.github/workflows/workflow.yml@v1
```

For more information, see [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

## `jobs.<job_id>.with`

When a job is used to call a reusable workflow, you can use `with` to provide a map of inputs that are passed to the called workflow.

Any inputs that you pass must match the input specifications defined in the called workflow.

Unlike [`jobs.<job_id>.steps[*].with`](#jobsjob_idstepswith), the inputs you pass with `jobs.<job_id>.with` are not available as environment variables in the called workflow. Instead, you can reference the inputs by using the `inputs` context.

### Example of `jobs.<job_id>.with`

```
jobs:
  call-workflow:
    uses: octo-org/example-repo/.github/workflows/called-workflow.yml@main
    with:
      username: mona
```

## `jobs.<job_id>.with.<input_id>`

A pair consisting of a string identifier for the input and the value of the input. The identifier must match the name of an input defined by [`on.workflow_call.inputs.<inputs_id>`](https://docs.github.com/en/actions/reference/workflows-and-actions/metadata-syntax#inputsinput_id) in the called workflow. The data type of the value must match the type defined by [`on.workflow_call.inputs.<input_id>.type`](#onworkflow_callinputsinput_idtype) in the called workflow.

Allowed expression contexts: `github`, and `needs`.

## `jobs.<job_id>.secrets`

When a job is used to call a reusable workflow, you can use `secrets` to provide a map of secrets that are passed to the called workflow.

Any secrets that you pass must match the names defined in the called workflow.

### Example of `jobs.<job_id>.secrets`

```
jobs:
  call-workflow:
    uses: octo-org/example-repo/.github/workflows/called-workflow.yml@main
    secrets:
      access-token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
```

## `jobs.<job_id>.secrets.inherit`

Use the `inherit` keyword to pass all the calling workflow's secrets to the called workflow. This includes all secrets the calling workflow has access to, namely organization, repository, and environment secrets. The `inherit` keyword can be used to pass secrets across repositories within the same organization, or across organizations within the same enterprise.

### Example of `jobs.<job_id>.secrets.inherit`

```
on:
  workflow_dispatch:

jobs:
  pass-secrets-to-workflow:
    uses: ./.github/workflows/called-workflow.yml
    secrets: inherit
```

```
on:
  workflow_call:

jobs:
  pass-secret-to-action:
    runs-on: ubuntu-latest
    steps:
      - name: Use a repo or org secret from the calling workflow.
        run: echo ${{ secrets.CALLING_WORKFLOW_SECRET }}
```

## `jobs.<job_id>.secrets.<secret_id>`

A pair consisting of a string identifier for the secret and the value of the secret. The identifier must match the name of a secret defined by [`on.workflow_call.secrets.<secret_id>`](#onworkflow_callsecretssecret_id) in the called workflow.

Allowed expression contexts: `github`, `needs`, and `secrets`.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
