---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#35-choosing-self-hosted-runners.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-35-choosing-self-hosted-runners
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.runs-on` › Choosing self-hosted runners
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#35-choosing-self-hosted-runners
source_hash: 79d51d6776828a99cffbc6afde5e44744f849eafe45c82ef4aa0029ce986c007
---
To specify a self-hosted runner for your job, configure `runs-on` in your workflow file with self-hosted runner labels.

Self-hosted runners may have the `self-hosted` label. When setting up a self-hosted runner, by default we will include the label `self-hosted`. You may pass in the `--no-default-labels` flag to prevent the self-hosted label from being applied. Labels can be used to create targeting options for runners, such as operating system or architecture, we recommend providing an array of labels that begins with `self-hosted` (this must be listed first) and then includes additional labels as needed. When you specify an array of labels, jobs will be queued on runners that have all the labels that you specify.

Note

Actions Runner Controller does not support the `self-hosted` label.

#### Example: Using labels for runner selection

```
runs-on: [self-hosted, linux]
```

For more information, see [Self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners) and [Using self-hosted runners in a workflow](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/use-in-a-workflow).

### Choosing runners in a group

You can use `runs-on` to target runner groups, so that the job will execute on any runner that is a member of that group. For more granular control, you can also combine runner groups with labels.

Runner groups can only have [larger runners](https://docs.github.com/en/actions/concepts/runners/larger-runners) or [self-hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners) as members.

#### Example: Using groups to control where jobs are run

In this example, runners have been added to a group called `build-runners`. The `runs-on` key sends the job to any available runner in the `build-runners` group:

```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on: 
      group: build-runners
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v7
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```

#### Example: Combining groups and labels

When you combine groups and labels, the runner must meet both requirements to be eligible to run the job.

In this example, the `runs-on` key combines `group` and `labels` so that the job is routed to any available runner within the group that also has a matching label:

```
name: learn-github-actions
on: [push]
jobs:
  check-bats-version:
    runs-on:
      group: ubuntu-runners
      labels: ubuntu-24.04-16core
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v7
        with:
          node-version: '14'
      - run: npm install -g bats
      - run: bats -v
```

## `jobs.<job_id>.snapshot`

You can use `jobs.<job_id>.snapshot` to generate a custom image.

Add the snapshot keyword to the job, using either the string syntax or mapping syntax as shown in [Generating a custom image](https://docs.github.com/en/actions/how-tos/manage-runners/larger-runners/use-custom-images#generating-a-custom-image).

Each job that includes the snapshot keyword creates a separate image. To generate only one image or image version, include all workflow steps in a single job. Each successful run of a job that includes the snapshot keyword creates a new version of that image.

For more information, see [Using custom images](https://docs.github.com/en/actions/how-tos/manage-runners/larger-runners/use-custom-images).

## `jobs.<job_id>.environment`

Use `jobs.<job_id>.environment` to define the environment that the job references.

You can provide the environment as only the environment `name`, or as an environment object with the `name` and `url`. The URL maps to `environment_url` in the deployments API. For more information about the deployments API, see [REST API endpoints for repositories](https://docs.github.com/en/rest/repos#deployments).

### Example: Using a single environment name

```
environment: staging_environment
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
