---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#42-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-42-variables
type: reference
title: Git - git-config Documentation › Variables (36/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#42-variables
source_hash: 4aa063538116bee75006bf7a449ce5d4731cd9502c756870b9552728af714aa5
---
Directory rename detection is disabled, meaning that such new files will be left behind in the old directory.

[](#Documentation/git-config.txt-true-1-1)`true`

Directory rename detection is enabled, meaning that such new files will be moved into the new directory.

[](#Documentation/git-config.txt-conflict)`conflict`

A conflict will be reported for such paths.

If `merge.renames` is `false`, `merge.directoryRenames` is ignored and treated as `false`. Defaults to `conflict`.

[](#Documentation/git-config.txt-mergerenormalize)`merge.renormalize`

Tell Git that canonical representation of files in the repository has changed over time (e.g. earlier commits record text files with *CRLF* line endings, but recent ones use *LF* line endings). In such a repository, for each file where a three-way content merge is needed, Git can convert the data recorded in commits to a canonical form before performing a merge to reduce unnecessary conflicts. For more information, see section "Merging branches with differing checkin/checkout attributes" in [gitattributes\[5\]](https://git-scm.com/docs/gitattributes).

[](#Documentation/git-config.txt-mergestat)`merge.stat`

What, if anything, to print between `ORIG_HEAD` and the merge result at the end of the merge. Possible values are:

[](#Documentation/git-config.txt-false-1-1-1)`false`

Show nothing.

[](#Documentation/git-config.txt-true-1-1-1)`true`

Show `git` `diff` `--diffstat` `--summary` `ORIG_HEAD`.

[](#Documentation/git-config.txt-compact)`compact`

Show `git` `diff` `--compact-summary` `ORIG_HEAD`.

but any unrecognised value (e.g., a value added by a future version of Git) is taken as `true` instead of triggering an error. Defaults to `true`.

[](#Documentation/git-config.txt-mergeautoStash)`merge.autoStash`

When set to `true`, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run merge on a dirty worktree. However, use with care: the final stash application after a successful merge might result in non-trivial conflicts. This option can be overridden by the `--no-autostash` and `--autostash` options of [git-merge\[1\]](https://git-scm.com/docs/git-merge). Defaults to `false`.

[](#Documentation/git-config.txt-mergetool)`merge.tool`

Controls which merge tool is used by [git-mergetool\[1\]](https://git-scm.com/docs/git-mergetool). The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding `mergetool.`*&lt;tool&gt;*`.cmd` variable is defined.

[](#Documentation/git-config.txt-mergeguitool)`merge.guitool`

Controls which merge tool is used by [git-mergetool\[1\]](https://git-scm.com/docs/git-mergetool) when the `-g`/`--gui` flag is specified. The list below shows the valid built-in values. Any other value is treated as a custom merge tool and requires that a corresponding `mergetool.`*&lt;guitool&gt;*`.cmd` variable is defined.

- araxis
- bc
- codecompare
- deltawalker
- diffmerge
- diffuse
- ecmerge
- emerge
- examdiff
- guiffy
- gvimdiff
- kdiff3
- meld
- nvimdiff
- opendiff
- p4merge
- smerge
- tkdiff
- tortoisemerge
- vimdiff
- vscode
- winmerge
- xxdiff

[](#Documentation/git-config.txt-mergeverbosity)`merge.verbosity`

Controls the amount of output shown by the recursive merge strategy. Level 0 outputs nothing except a final error message if conflicts were detected. Level 1 outputs only conflicts, 2 outputs conflicts and file changes. Level 5 and above outputs debugging information. The default is level 2. Can be overridden by the `GIT_MERGE_VERBOSITY` environment variable.

[](#Documentation/git-config.txt-mergedrivername)`merge.`*&lt;driver&gt;*`.name`

Defines a human-readable name for a custom low-level merge driver. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-mergedriverdriver)`merge.`*&lt;driver&gt;*`.driver`

Defines the command that implements a custom low-level merge driver. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-mergedriverrecursive)`merge.`*&lt;driver&gt;*`.recursive`

Names a low-level merge driver to be used when performing an internal merge between common ancestors. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-mergetooltoolpath)`mergetool.`*&lt;tool&gt;*`.path`

Override the path for the given tool. This is useful in case your tool is not in the `$PATH`.

[](#Documentation/git-config.txt-mergetooltoolcmd)`mergetool.`*&lt;tool&gt;*`.cmd`

Specify the command to invoke the specified merge tool. The specified command is evaluated in shell with the following variables available: `BASE` is the name of a temporary file containing the common base of the files to be merged, if available; `LOCAL` is the name of a temporary file containing the contents of the file on the current branch; `REMOTE` is the name of a temporary file containing the contents of the file from the branch being merged; `MERGED` contains the name of the file to which the merge tool should write the results of a successful merge.

[](#Documentation/git-config.txt-mergetooltoolhideResolved)`mergetool.`*&lt;tool&gt;*`.hideResolved`

Allows the user to override the global `mergetool.hideResolved` value for a specific tool. See `mergetool.hideResolved` for the full description.

[](#Documentation/git-config.txt-mergetooltooltrustExitCode)`mergetool.`*&lt;tool&gt;*`.trustExitCode`

For a custom merge command, specify whether the exit code of the merge command can be used to determine whether the merge was successful. If this is not set to true then the merge target file timestamp is checked, and the merge is assumed to have been successful if the file has been updated; otherwise, the user is prompted to indicate the success of the merge.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
