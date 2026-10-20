---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#51-example-using-an-action-inside-a-different-private.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-51-example-using-an-action-inside-a-different-private
type: reference
title: 'Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].uses`](#jobsjob_idstepsuses) › Example: Using an action inside a different private repository than the workflow'
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#51-example-using-an-action-inside-a-different-private
source_hash: cf66b71bdb224864a181998d4e2f94e2c1f808d9697dedb972429703d55a5cec
---
If the action is in an internal repository, or in a private repository configured to allow access from your workflow's repository, you can reference the action directly. For more information, see [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) and [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository).

If the action isn't in a repository configured to allow access, you need to check out the repository and reference the action locally. Generate a personal access token and add the token as a secret. The following example shows this method for referencing an action. For more information, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) and [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).

Replace `PERSONAL_ACCESS_TOKEN` in the example with the name of your secret.

```
jobs:
  my_first_job:
    steps:
      - name: Check out repository
        uses: actions/checkout@v6
        with:
          repository: octocat/my-private-repo
          ref: v1.0
          token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
          path: ./.github/actions/my-private-repo
      - name: Run my action
        uses: ./.github/actions/my-private-repo/my-action
```

Alternatively, use a GitHub App instead of a personal access token in order to ensure your workflow continues to run even if the personal access token owner leaves. For more information, see [Making authenticated API requests with a GitHub App in a GitHub Actions workflow](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
