---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#41-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-41-variables
type: reference
title: Git - git-config Documentation › Variables (35/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#41-variables
source_hash: c170691b644d4ee7f2d24312fc45511aeaf21b993f520c9baa819d781dbf4f4a
---
This integer config option controls how often the `rerere-gc` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `rerere-gc` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, any positive value implies the command will run when the "rr-cache" directory exists and has at least one entry, regardless of whether it is stale or not. This heuristic may be refined in the future. The default value is 1.

[](#Documentation/git-config.txt-maintenanceworktree-pruneauto)maintenance.worktree-prune.auto

This integer config option controls how often the `worktree-prune` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `worktree-prune` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of prunable worktrees exceeds the value. The default value is 1.

[](#Documentation/git-config.txt-manviewer)man.viewer

Specify the programs that may be used to display help in the *man* format. See [git-help\[1\]](https://git-scm.com/docs/git-help).

[](#Documentation/git-config.txt-mantoolcmd)man.&lt;tool&gt;.cmd

Specify the command to invoke the specified man viewer. The specified command is evaluated in shell with the man page passed as an argument. (See [git-help\[1\]](https://git-scm.com/docs/git-help).)

[](#Documentation/git-config.txt-mantoolpath)man.&lt;tool&gt;.path

Override the path for the given tool that may be used to display help in the *man* format. See [git-help\[1\]](https://git-scm.com/docs/git-help).

[](#Documentation/git-config.txt-mergeconflictStyle)`merge.conflictStyle`

Specify the style in which conflicted hunks are written out to working tree files upon merge. The default is "merge", which shows a *&lt;&lt;&lt;&lt;&lt;&lt;&lt;* conflict marker, changes made by one side, a `=======` marker, changes made by the other side, and then a *&gt;&gt;&gt;&gt;&gt;&gt;&gt;* marker. An alternate style, "diff3", adds a ||||||| marker and the original text before the `=======` marker. The "merge" style tends to produce smaller conflict regions than diff3, both because of the exclusion of the original text, and because when a subset of lines match on the two sides, they are just pulled out of the conflict region. Another alternate style, "zdiff3", is similar to diff3 but removes matching lines on the two sides from the conflict region when those matching lines appear near either the beginning or end of a conflict region.

[](#Documentation/git-config.txt-mergedefaultToUpstream)`merge.defaultToUpstream`

If merge is called without any commit argument, merge the upstream branches configured for the current branch by using their last observed values stored in their remote-tracking branches. The values of the *branch.&lt;current branch&gt;.merge* that name the branches at the remote named by `branch.`*&lt;current-branch&gt;*`.remote` are consulted, and then they are mapped via `remote.`*&lt;remote&gt;*`.fetch` to their corresponding remote-tracking branches, and the tips of these tracking branches are merged. Defaults to true.

[](#Documentation/git-config.txt-mergeff)`merge.ff`

By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to `false`, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the `--no-ff` option from the command line). When set to `only`, only such fast-forward merges are allowed (equivalent to giving the `--ff-only` option from the command line).

[](#Documentation/git-config.txt-mergeverifySignatures)`merge.verifySignatures`

If true, this is equivalent to the `--verify-signatures` command line option. See [git-merge\[1\]](https://git-scm.com/docs/git-merge) for details.

[](#Documentation/git-config.txt-mergebranchdesc)`merge.branchdesc`

In addition to branch names, populate the log message with the branch description text associated with them. Defaults to false.

[](#Documentation/git-config.txt-mergelog)`merge.log`

In addition to branch names, populate the log message with at most the specified number of one-line descriptions from the actual commits that are being merged. Defaults to false, and true is a synonym for 20.

[](#Documentation/git-config.txt-mergesuppressDest)`merge.suppressDest`

By adding a glob that matches the names of integration branches to this multi-valued configuration variable, the default merge message computed for merges into these integration branches will omit "into *&lt;branch-name&gt;*" from its title.

An element with an empty value can be used to clear the list of globs accumulated from previous configuration entries. When there is no `merge.suppressDest` variable defined, the default value of `master` is used for backward compatibility.

[](#Documentation/git-config.txt-mergerenameLimit)`merge.renameLimit`

The number of files to consider in the exhaustive portion of rename detection during a merge. If not specified, defaults to the value of `diff.renameLimit`. If neither `merge.renameLimit` nor `diff.renameLimit` are specified, currently defaults to 7000. This setting has no effect if rename detection is turned off.

[](#Documentation/git-config.txt-mergerenames)`merge.renames`

Whether Git detects renames. If set to `false`, rename detection is disabled. If set to `true`, basic rename detection is enabled. Defaults to the value of diff.renames.

[](#Documentation/git-config.txt-mergedirectoryRenames)`merge.directoryRenames`

Whether Git detects directory renames, affecting what happens at merge time to new files added to a directory on one side of history when that directory was renamed on the other side of history. Possible values are:

[](#Documentation/git-config.txt-false-1-1)`false`

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
