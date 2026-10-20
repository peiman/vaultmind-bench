---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#52-jobs-job-id-steps-run-jobsjob-idstepsrun.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-52-jobs-job-id-steps-run-jobsjob-idstepsrun
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].run`](#jobsjob_idstepsrun)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#52-jobs-job-id-steps-run-jobsjob-idstepsrun
source_hash: cfbd918b39f63bde02a4d14e917a2a328350295227669b108d04b250192850c6
---
Runs command-line programs that do not exceed 21,000 characters using the operating system's shell. If you do not provide a `name`, the step name will default to the text specified in the `run` command.

Commands run using non-login shells by default. You can choose a different shell and customize the shell used to run commands. For more information, see [`jobs.<job_id>.steps[*].shell`](#jobsjob_idstepsshell).

Each `run` keyword represents a new process and shell in the runner environment. When you provide multi-line commands, each line runs in the same shell. For example:

- A single-line command:
  
  ```
  - name: Install Dependencies
    run: npm install
  ```
- A multi-line command:
  
  ```
  - name: Clean install dependencies and build
    run: |
      npm ci
      npm run build
  ```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
