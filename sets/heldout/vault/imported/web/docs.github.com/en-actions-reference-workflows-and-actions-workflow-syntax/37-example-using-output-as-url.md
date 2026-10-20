---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#37-example-using-output-as-url.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-37-example-using-output-as-url
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.environment` › Example: Using output as URL'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#37-example-using-output-as-url
source_hash: ba1f9063ec5a47f7364ef2505b56900afac29f89c59a144b331b974338f204f7
---
```
environment:
  name: production_environment
  url: ${{ steps.step_id.outputs.url_output }}
```

The value of `name` can be an expression. Allowed expression contexts: [`github`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#github-context), [`inputs`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#inputs-context), [`vars`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#vars-context), [`needs`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#needs-context), [`strategy`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#strategy-context), and [`matrix`](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#matrix-context). For more information about expressions, see [Evaluate expressions in workflows and actions](https://docs.github.com/en/actions/reference/workflows-and-actions/expressions).

### Example: Using an expression as environment name

```
environment:
  name: ${{ github.ref_name }}
```

### Example: Using an environment without creating a deployment

Set `deployment` to `false` to use an environment's secrets and variables without creating a deployment object.

```
environment:
  name: testing
  deployment: false
```

Setting `deployment: false` is not compatible with custom deployment protection rules. For more information, see [Deploying with GitHub Actions](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments#using-environments-without-deployments).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
