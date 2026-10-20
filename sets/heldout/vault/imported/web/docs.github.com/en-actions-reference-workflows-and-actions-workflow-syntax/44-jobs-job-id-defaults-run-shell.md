---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#44-jobs-job-id-defaults-run-shell.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-44-jobs-job-id-defaults-run-shell
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.defaults.run.shell`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#44-jobs-job-id-defaults-run-shell
source_hash: a3fe58164dbe9c9c9dc88e8cf6e8d39f3a942826e15fc264bbd9b1205df7a5ac
---
Use `shell` to define the `shell` for a step. This keyword can reference several contexts. For more information, see [Contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability).

Supported platform`shell` parameterDescriptionCommand run internallyLinux / macOSunspecifiedThe default shell on non-Windows platforms. Note that this runs a different command to when `bash` is specified explicitly. If `bash` is not found in the path, this is treated as `sh`.`bash -e {0}`All`bash`The default shell on non-Windows platforms with a fallback to `sh`. When specifying a bash shell on Windows, the bash shell included with Git for Windows is used.`bash --noprofile --norc -eo pipefail {0}`All`pwsh`The PowerShell Core. GitHub appends the extension `.ps1` to your script name.`pwsh -command ". '{0}'"`All`python`Executes the python command.`python {0}`Linux / macOS`sh`The fallback behavior for non-Windows platforms if no shell is provided and `bash` is not found in the path.`sh -e {0}`Windows`cmd`GitHub appends the extension `.cmd` to your script name and substitutes for `{0}`.`%ComSpec% /D /E:ON /V:OFF /S /C "CALL "{0}""`.Windows`pwsh`This is the default shell used on Windows. The PowerShell Core. GitHub appends the extension `.ps1` to your script name. If your self-hosted Windows runner does not have *PowerShell Core* installed, then *PowerShell Desktop* is used instead.`pwsh -command ". '{0}'"`.Windows`powershell`The PowerShell Desktop. GitHub appends the extension `.ps1` to your script name.`powershell -command ". '{0}'"`.

When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.

## `jobs.<job_id>.defaults.run.working-directory`

Use `working-directory` to define the working directory for the `shell` for a step. This keyword can reference several contexts. For more information, see [Contexts](https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability).

Tip

Ensure the `working-directory` you assign exists on the runner before you run your shell in it. When more than one default setting is defined with the same name, GitHub uses the most specific default setting. For example, a default setting defined in a job will override a default setting that has the same name defined in a workflow.

### Example: Setting default `run` step options for a job

```
jobs:
  job1:
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash
        working-directory: ./scripts
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
