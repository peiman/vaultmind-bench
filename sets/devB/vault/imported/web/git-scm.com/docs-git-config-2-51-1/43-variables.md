---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#43-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-43-variables
type: reference
title: Git - git-config Documentation › Variables (37/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#43-variables
source_hash: c9616b8acdce8f90d8d1f9fa67a6d9052c7d795a175cbea5f75fc6518c39c1c3
---
[](#Documentation/git-config.txt-mergetoolmeldhasOutput)`mergetool.meld.hasOutput`

Older versions of `meld` do not support the `--output` option. Git will attempt to detect whether `meld` supports `--output` by inspecting the output of `meld` `--help`. Configuring `mergetool.meld.hasOutput` will make Git skip these checks and use the configured value instead. Setting `mergetool.meld.hasOutput` to `true` tells Git to unconditionally use the `--output` option, and `false` avoids using `--output`.

[](#Documentation/git-config.txt-mergetoolmelduseAutoMerge)`mergetool.meld.useAutoMerge`

When the `--auto-merge` is given, meld will merge all non-conflicting parts automatically, highlight the conflicting parts, and wait for user decision. Setting `mergetool.meld.useAutoMerge` to `true` tells Git to unconditionally use the `--auto-merge` option with `meld`. Setting this value to `auto` makes git detect whether `--auto-merge` is supported and will only use `--auto-merge` when available. A value of `false` avoids using `--auto-merge` altogether, and is the default value.

[](#Documentation/git-config.txt-mergetoolvariantlayout)`mergetool.`*&lt;variant&gt;*`.layout`

Configure the split window layout for vimdiff’s *&lt;variant&gt;*, which is any of `vimdiff`, `nvimdiff`, `gvimdiff`. Upon launching `git` `mergetool` with `--tool=`*&lt;variant&gt;* (or without `--tool` if `merge.tool` is configured as *&lt;variant&gt;*), Git will consult `mergetool.`*&lt;variant&gt;*`.layout` to determine the tool’s layout. If the variant-specific configuration is not available, `vimdiff` ' s is used as fallback. If that too is not available, a default layout with 4 windows will be used. To configure the layout, see the *BACKEND SPECIFIC HINTS* section in [git-mergetool\[1\]](https://git-scm.com/docs/git-mergetool).

[](#Documentation/git-config.txt-mergetoolhideResolved)`mergetool.hideResolved`

During a merge, Git will automatically resolve as many conflicts as possible and write the `$MERGED` file containing conflict markers around any conflicts that it cannot resolve; `$LOCAL` and `$REMOTE` normally are the versions of the file from before Git’s conflict resolution. This flag causes `$LOCAL` and `$REMOTE` to be overwritten so that only the unresolved conflicts are presented to the merge tool. Can be configured per-tool via the `mergetool.`*&lt;tool&gt;*`.hideResolved` configuration variable. Defaults to `false`.

[](#Documentation/git-config.txt-mergetoolkeepBackup)`mergetool.keepBackup`

After performing a merge, the original file with conflict markers can be saved as a file with a `.orig` extension. If this variable is set to `false` then this file is not preserved. Defaults to `true` (i.e. keep the backup files).

[](#Documentation/git-config.txt-mergetoolkeepTemporaries)`mergetool.keepTemporaries`

When invoking a custom merge tool, Git uses a set of temporary files to pass to the tool. If the tool returns an error and this variable is set to `true`, then these temporary files will be preserved; otherwise, they will be removed after the tool has exited. Defaults to `false`.

[](#Documentation/git-config.txt-mergetoolwriteToTemp)`mergetool.writeToTemp`

Git writes temporary `BASE`, `LOCAL`, and `REMOTE` versions of conflicting files in the worktree by default. Git will attempt to use a temporary directory for these files when set `true`. Defaults to `false`.

[](#Documentation/git-config.txt-mergetoolprompt)`mergetool.prompt`

Prompt before each invocation of the merge resolution program.

[](#Documentation/git-config.txt-mergetoolguiDefault)`mergetool.guiDefault`

Set `true` to use the `merge.guitool` by default (equivalent to specifying the `--gui` argument), or `auto` to select `merge.guitool` or `merge.tool` depending on the presence of a `DISPLAY` environment variable value. The default is `false`, where the `--gui` argument must be provided explicitly for the `merge.guitool` to be used.

[](#Documentation/git-config.txt-notesmergeStrategy)`notes.mergeStrategy`

Which merge strategy to choose by default when resolving notes conflicts. Must be one of `manual`, `ours`, `theirs`, `union`, or `cat_sort_uniq`. Defaults to `manual`. See the "NOTES MERGE STRATEGIES" section of [git-notes\[1\]](https://git-scm.com/docs/git-notes) for more information on each strategy.

This setting can be overridden by passing the `--strategy` option to [git-notes\[1\]](https://git-scm.com/docs/git-notes).

[](#Documentation/git-config.txt-notesnamemergeStrategy)`notes.`*&lt;name&gt;*`.mergeStrategy`

Which merge strategy to choose when doing a notes merge into `refs/notes/`*&lt;name&gt;*. This overrides the more general `notes.mergeStrategy`. See the "NOTES MERGE STRATEGIES" section in [git-notes\[1\]](https://git-scm.com/docs/git-notes) for more information on the available strategies.

[](#Documentation/git-config.txt-notesdisplayRef)`notes.displayRef`

Which ref (or refs, if a glob or specified more than once), in addition to the default set by `core.notesRef` or `GIT_NOTES_REF`, to read notes from when showing commit messages with the `git` `log` family of commands.

This setting can be overridden with the `GIT_NOTES_DISPLAY_REF` environment variable, which must be a colon separated list of refs or globs.

A warning will be issued for refs that do not exist, but a glob that does not match any refs is silently ignored.

This setting can be disabled by the `--no-notes` option to the [git-log\[1\]](https://git-scm.com/docs/git-log) family of commands, or by the `--notes=`*&lt;ref&gt;* option accepted by those commands.

The effective value of `core.notesRef` (possibly overridden by `GIT_NOTES_REF`) is also implicitly added to the list of refs to be displayed.

[](#Documentation/git-config.txt-notesrewritecommand)`notes.rewrite.`*&lt;command&gt;*

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
