---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#55-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-55-variables
type: reference
title: Git - git-config Documentation › Variables (49/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#55-variables
source_hash: 5bfeea9c396f68c3b7f687f7a3ffb9f3aa2df7ab26af2d4e1b44c4fc5059285d
---
By default, Git determines the command line arguments to use based on the basename of the configured SSH command (configured using the environment variable `GIT_SSH` or `GIT_SSH_COMMAND` or the config setting `core.sshCommand`). If the basename is unrecognized, Git will attempt to detect support of OpenSSH options by first invoking the configured SSH command with the `-G` (print configuration) option and will subsequently use OpenSSH options (if that is successful) or no options besides the host and remote command (if it fails).

The config variable `ssh.variant` can be set to override this detection. Valid values are `ssh` (to use OpenSSH options), `plink`, `putty`, `tortoiseplink`, `simple` (no options except the host and remote command). The default auto-detection can be explicitly requested using the value `auto`. Any other value is treated as `ssh`. This setting can also be overridden via the environment variable `GIT_SSH_VARIANT`.

The current command-line parameters used for each variant are as follows:

- `ssh` - \[-p port] \[-4] \[-6] \[-o option] \[username@]host command
- `simple` - \[username@]host command
- `plink` or `putty` - \[-P port] \[-4] \[-6] \[username@]host command
- `tortoiseplink` - \[-P port] \[-4] \[-6] -batch \[username@]host command

Except for the `simple` variant, command-line parameters are likely to change as git gains new features.

[](#Documentation/git-config.txt-stashshowIncludeUntracked)stash.showIncludeUntracked

If this is set to true, the `git` `stash` `show` command will show the untracked files of a stash entry. Defaults to false. See the description of the *show* command in [git-stash\[1\]](https://git-scm.com/docs/git-stash).

[](#Documentation/git-config.txt-stashshowPatch)stash.showPatch

If this is set to true, the `git` `stash` `show` command without an option will show the stash entry in patch form. Defaults to false. See the description of the *show* command in [git-stash\[1\]](https://git-scm.com/docs/git-stash).

[](#Documentation/git-config.txt-stashshowStat)stash.showStat

If this is set to true, the `git` `stash` `show` command without an option will show a diffstat of the stash entry. Defaults to true. See the description of the *show* command in [git-stash\[1\]](https://git-scm.com/docs/git-stash).

[](#Documentation/git-config.txt-statusrelativePaths)status.relativePaths

By default, [git-status\[1\]](https://git-scm.com/docs/git-status) shows paths relative to the current directory. Setting this variable to `false` shows paths relative to the repository root (this was the default for Git prior to v1.5.4).

[](#Documentation/git-config.txt-statusshort)status.short

Set to true to enable --short by default in [git-status\[1\]](https://git-scm.com/docs/git-status). The option --no-short takes precedence over this variable.

[](#Documentation/git-config.txt-statusbranch)status.branch

Set to true to enable --branch by default in [git-status\[1\]](https://git-scm.com/docs/git-status). The option --no-branch takes precedence over this variable.

[](#Documentation/git-config.txt-statusaheadBehind)status.aheadBehind

Set to true to enable `--ahead-behind` and false to enable `--no-ahead-behind` by default in [git-status\[1\]](https://git-scm.com/docs/git-status) for non-porcelain status formats. Defaults to true.

If set to true, [git-status\[1\]](https://git-scm.com/docs/git-status) will insert a comment prefix before each output line (starting with `core.commentChar`, i.e. `#` by default). This was the behavior of [git-status\[1\]](https://git-scm.com/docs/git-status) in Git 1.8.4 and previous. Defaults to false.

[](#Documentation/git-config.txt-statusrenameLimit)status.renameLimit

The number of files to consider when performing rename detection in [git-status\[1\]](https://git-scm.com/docs/git-status) and [git-commit\[1\]](https://git-scm.com/docs/git-commit). Defaults to the value of diff.renameLimit.

[](#Documentation/git-config.txt-statusrenames)status.renames

Whether and how Git detects renames in [git-status\[1\]](https://git-scm.com/docs/git-status) and [git-commit\[1\]](https://git-scm.com/docs/git-commit) . If set to "false", rename detection is disabled. If set to "true", basic rename detection is enabled. If set to "copies" or "copy", Git will detect copies, as well. Defaults to the value of diff.renames.

[](#Documentation/git-config.txt-statusshowStash)status.showStash

If set to true, [git-status\[1\]](https://git-scm.com/docs/git-status) will display the number of entries currently stashed away. Defaults to false.

[](#Documentation/git-config.txt-statusshowUntrackedFiles)status.showUntrackedFiles

By default, [git-status\[1\]](https://git-scm.com/docs/git-status) and [git-commit\[1\]](https://git-scm.com/docs/git-commit) show files which are not currently tracked by Git. Directories which contain only untracked files, are shown with the directory name only. Showing untracked files means that Git needs to lstat() all the files in the whole repository, which might be slow on some systems. So, this variable controls how the commands display the untracked files. Possible values are:

- `no` - Show no untracked files.
- `normal` - Show untracked files and directories.
- `all` - Show also individual files in untracked directories.

If this variable is not specified, it defaults to *normal*. All usual spellings for Boolean value `true` are taken as `normal` and `false` as `no`. This variable can be overridden with the -u|--untracked-files option of [git-status\[1\]](https://git-scm.com/docs/git-status) and [git-commit\[1\]](https://git-scm.com/docs/git-commit).

[](#Documentation/git-config.txt-statussubmoduleSummary)status.submoduleSummary

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
