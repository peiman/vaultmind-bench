---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#01-about-yaml-syntax-for-workflows.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-01-about-yaml-syntax-for-workflows
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › About YAML syntax for workflows
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#01-about-yaml-syntax-for-workflows
source_hash: 7f478ed18455d4ec99d4b6693953f46100f1bc87042cee1f17981f5185e8b0fd
---
Workflow files use YAML syntax, and must have either a `.yml` or `.yaml` file extension. If you're new to YAML and want to learn more, see [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/).

You must store workflow files in the `.github/workflows` directory of your repository.

Tip

Unlike traditional GitHub Actions workflows that require you to script every decision as YAML job steps, GitHub Agentic Workflows use YAML frontmatter for triggers and configuration, but let you describe what you want in natural-language Markdown—so you don't need to anticipate and encode every scenario in advance. For more information, see [Creating GitHub Agentic Workflows](https://docs.github.com/en/copilot/how-tos/github-agentic-workflows/creating-github-agentic-workflows).

## `name`

The name of the workflow. GitHub displays the names of your workflows under your repository's "Actions" tab. If you omit `name`, GitHub displays the workflow file path relative to the root of the repository.

## `run-name`

The name for workflow runs generated from the workflow. GitHub displays the workflow run name in the list of workflow runs on your repository's "Actions" tab. If `run-name` is omitted or is only whitespace, then the run name is set to event-specific information for the workflow run. For example, for a workflow triggered by a `push` or `pull_request` event, it is set as the commit message or the title of the pull request.

This value can include expressions and can reference the [`github`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context) and [`inputs`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#inputs-context) contexts.

### Example of `run-name`

```
run-name: Deploy to ${{ inputs.deploy_target }} by @${{ github.actor }}
```

## `on`

To automatically trigger a workflow, use `on` to define which events can cause the workflow to run. For a list of available events, see [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

You can define single or multiple events that can trigger a workflow, or set a time schedule. You can also restrict the execution of a workflow to only occur for specific files, tags, or branch changes. These options are described in the following sections.

### Using a single event

For example, a workflow with the following `on` value will run when a push is made to any branch in the workflow's repository:

```
on: push
```

### Using multiple events

You can specify a single event or multiple events. For example, a workflow with the following `on` value will run when a push is made to any branch in the repository or when someone forks the repository:

```
on: [push, fork]
```

If you specify multiple events, only one of those events needs to occur to trigger your workflow. If multiple triggering events for your workflow occur at the same time, multiple workflow runs will be triggered.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
