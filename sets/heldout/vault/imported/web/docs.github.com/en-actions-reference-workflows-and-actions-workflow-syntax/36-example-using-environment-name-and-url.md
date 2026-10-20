---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#36-example-using-environment-name-and-url.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-36-example-using-environment-name-and-url
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.environment` › Example: Using environment name and URL'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#36-example-using-environment-name-and-url
source_hash: ee2a22f48d2e3fb6c81cdc2c7a0d0f4698d599646f63da11f86bb230ca3ae78d
---
```
environment:
  name: production_environment
  url: https://github.com
```

The value of `url` can be an expression. Allowed expression contexts: [`github`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context), [`inputs`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#inputs-context), [`vars`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#vars-context), [`needs`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#needs-context), [`strategy`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#strategy-context), [`matrix`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#matrix-context), [`job`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#job-context), [`runner`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#runner-context), [`env`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#env-context), and [`steps`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#steps-context). For more information about expressions, see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
