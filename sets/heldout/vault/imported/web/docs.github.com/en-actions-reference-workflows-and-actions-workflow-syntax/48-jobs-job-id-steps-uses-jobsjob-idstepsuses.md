---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#48-jobs-job-id-steps-uses-jobsjob-idstepsuses.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-48-jobs-job-id-steps-uses-jobsjob-idstepsuses
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].uses`](#jobsjob_idstepsuses)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#48-jobs-job-id-steps-uses-jobsjob-idstepsuses
source_hash: 0cee173e932355efae8a95cdc8d82e003348c16e2ecb7a0cbf0720049fc251a7
---
Selects an action to run as part of a step in your job. An action is a reusable unit of code. You can use an action defined in the same repository as the workflow, a public repository, or in a [published Docker container image](https://hub.docker.com/).

We strongly recommend that you include the version of the action you are using by specifying a Git ref, SHA, or Docker tag. If you don't specify a version, it could break your workflows or cause unexpected behavior when the action owner publishes an update.

- Using the commit SHA of a released action version is the safest for stability and security.
- If the action publishes major version tags, you should expect to receive critical fixes and security patches while still retaining compatibility. Note that this behavior is at the discretion of the action's author.
- Using the default branch of an action may be convenient, but if someone releases a new major version with a breaking change, your workflow could break.

Some actions require inputs that you must set using the [`with`](#jobsjob_idstepswith) keyword. Review the action's README file to determine the inputs required.

Actions can be JavaScript, composite, or Docker container actions. If the action you're using is a Docker container you must run the job in a Linux environment. For more details, see [`runs-on`](#jobsjob_idruns-on).

### Example: Using versioned actions

```
steps:
  # Reference a specific commit
  - uses: actions/checkout@8f4b7f84864484a7bf31766abe9204da3cbe65b3
  # Reference the major version of a release
  - uses: actions/checkout@v6
  # Reference a specific version
  - uses: actions/checkout@v6.2.0
  # Reference a branch
  - uses: actions/checkout@main
```

### Example: Using a public action

`{owner}/{repo}@{ref}`

You can specify a branch, ref, or SHA in a public GitHub repository.

```
jobs:
  my_first_job:
    steps:
      - name: My first step
        # Uses the default branch of a public repository
        uses: actions/heroku@main
      - name: My second step
        # Uses a specific version tag of a public repository
        uses: actions/aws@v2.0.1
```

### Example: Using a public action in a subdirectory

`{owner}/{repo}/{path}@{ref}`

A subdirectory in a public GitHub repository at a specific branch, ref, or SHA.

```
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/aws/ec2@main
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
