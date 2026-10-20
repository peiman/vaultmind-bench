---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#54-jobs-job-id-steps-shell-jobsjob-idstepsshell.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-54-jobs-job-id-steps-shell-jobsjob-idstepsshell
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].shell`](#jobsjob_idstepsshell)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#54-jobs-job-id-steps-shell-jobsjob-idstepsshell
source_hash: adf9c69c6ee21be3268a76265897442c667c4f4a2cdae3d3f56405ca55070780
---
You can override the default shell settings in the runner's operating system and the job's default using the `shell` keyword. You can use built-in `shell` keywords, or you can define a custom set of shell options. The shell command that is run internally executes a temporary file that contains the commands specified in the `run` keyword.

Supported platform`shell` parameterDescriptionCommand run internallyLinux / macOSunspecifiedThe default shell on non-Windows platforms. Note that this runs a different command to when `bash` is specified explicitly. If `bash` is not found in the path, this is treated as `sh`.`bash -e {0}`All`bash`The default shell on non-Windows platforms with a fallback to `sh`. When specifying a bash shell on Windows, the bash shell included with Git for Windows is used.`bash --noprofile --norc -eo pipefail {0}`All`pwsh`The PowerShell Core. GitHub appends the extension `.ps1` to your script name.`pwsh -command ". '{0}'"`All`python`Executes the python command.`python {0}`Linux / macOS`sh`The fallback behavior for non-Windows platforms if no shell is provided and `bash` is not found in the path.`sh -e {0}`Windows`cmd`GitHub appends the extension `.cmd` to your script name and substitutes for `{0}`.`%ComSpec% /D /E:ON /V:OFF /S /C "CALL "{0}""`.Windows`pwsh`This is the default shell used on Windows. The PowerShell Core. GitHub appends the extension `.ps1` to your script name. If your self-hosted Windows runner does not have *PowerShell Core* installed, then *PowerShell Desktop* is used instead.`pwsh -command ". '{0}'"`.Windows`powershell`The PowerShell Desktop. GitHub appends the extension `.ps1` to your script name.`powershell -command ". '{0}'"`.

Alternatively, you can specify a default shell for all `run` steps in a job, or for all `run` steps in the entire workflow. For more information, see [`defaults.run.shell`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrunshell) and [`jobs.<job_id>.defaults.run.shell`](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#jobsjob_iddefaultsrunshell).

### Example: Running a command using Bash

```
steps:
  - name: Display the path
    shell: bash
    run: echo $PATH
```

### Example: Running a command using Windows `cmd`

```
steps:
  - name: Display the path
    shell: cmd
    run: echo %PATH%
```

### Example: Running a command using PowerShell Core

```
steps:
  - name: Display the path
    shell: pwsh
    run: echo ${env:PATH}
```

### Example: Using PowerShell Desktop to run a command

```
steps:
  - name: Display the path
    shell: powershell
    run: echo ${env:PATH}
```

### Example: Running an inline Python script

```
steps:
  - name: Display the path
    shell: python
    run: |
      import os
      print(os.environ['PATH'])
```

### Custom shell

You can set the `shell` value to a template string using `command [options] {0} [more_options]`. GitHub interprets the first whitespace-delimited word of the string as the command, and inserts the file name for the temporary script at `{0}`.

For example:

```
steps:
  - name: Display the environment variables and their values
    shell: perl {0}
    run: |
      print %ENV
```

The command used, `perl` in this example, must be installed on the runner.

For information about the software included on GitHub-hosted runners, see [GitHub-hosted runners](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners#preinstalled-software-for-github-owned-images).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
