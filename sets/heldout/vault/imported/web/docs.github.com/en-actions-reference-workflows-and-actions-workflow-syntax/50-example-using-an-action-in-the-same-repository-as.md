---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#50-example-using-an-action-in-the-same-repository-as.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-50-example-using-an-action-in-the-same-repository-as
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].uses`](#jobsjob_idstepsuses) › Example: Using an action in the same repository as the workflow'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#50-example-using-an-action-in-the-same-repository-as
source_hash: 3863592907f962eabb9a6dc20fbb6dd139b812d2742fe8b29dcbcfc8f8b97270
---
`./path/to/dir`

The path to the directory that contains the action in your workflow's repository. You must check out your repository before using the action, and the `./` path resolves against the runner's workspace rather than the repository of the running workflow. For most cases, use the `$/` syntax shown above instead.

Example repository file structure:

```
|-- hello-world (repository)
|   |__ .github
|       └── workflows
|           └── my-first-workflow.yml
|       └── actions
|           |__ hello-world-action
|               └── action.yml
```

The path is relative (`./`) to the default working directory (`github.workspace`, `$GITHUB_WORKSPACE`). If the action checks out the repository to a location different than the workflow, the relative path used for local actions must be updated.

Example workflow file:

```
jobs:
  my_first_job:
    runs-on: ubuntu-latest
    steps:
      # This step checks out a copy of your repository.
      - name: My first step - check out repository
        uses: actions/checkout@v6
      # This step references the directory that contains the action.
      - name: Use local hello-world-action
        uses: ./.github/actions/hello-world-action
```

### Example: Using a Docker Hub action

`docker://{image}:{tag}`

A Docker image published on [Docker Hub](https://hub.docker.com/).

```
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://alpine:3.8
```

### Example: Using the GitHub Packages Container registry

`docker://{host}/{image}:{tag}`

A public Docker image in the GitHub Packages Container registry.

```
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://ghcr.io/OWNER/IMAGE_NAME
```

### Example: Using a Docker public registry action

`docker://{host}/{image}:{tag}`

A Docker image in a public registry. This example uses the Google Container Registry at `gcr.io`.

```
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://gcr.io/cloud-builders/gradle
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
