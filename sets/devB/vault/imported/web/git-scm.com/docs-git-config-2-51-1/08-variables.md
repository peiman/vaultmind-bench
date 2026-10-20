---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#08-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-08-variables
type: reference
title: Git - git-config Documentation › Variables (2/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#08-variables
source_hash: ddb34c095754b03c842b3f25e9dc6c2fbb3873c8f786cb9f999ee9326bb29bab
---
[](#Documentation/git-config.txt-pushUnqualifiedRefname)pushUnqualifiedRefname

Shown when [git-push\[1\]](https://git-scm.com/docs/git-push) gives up trying to guess based on the source and destination refs what remote ref namespace the source belongs in, but where we can still suggest that the user push to either `refs/heads/*` or `refs/tags/*` based on the type of the source object.

[](#Documentation/git-config.txt-pushUpdateRejected)pushUpdateRejected

Set this variable to `false` if you want to disable `pushNonFFCurrent`, `pushNonFFMatching`, `pushAlreadyExists`, `pushFetchFirst`, `pushNeedsForce`, and `pushRefNeedsUpdate` simultaneously.

[](#Documentation/git-config.txt-rebaseTodoError)rebaseTodoError

Shown when there is an error after editing the rebase todo list.

[](#Documentation/git-config.txt-refSyntax)refSyntax

Shown when the user provides an illegal ref name, to tell the user about the ref syntax documentation.

[](#Documentation/git-config.txt-resetNoRefresh)resetNoRefresh

Shown when [git-reset\[1\]](https://git-scm.com/docs/git-reset) takes more than 2 seconds to refresh the index after reset, to tell the user that they can use the `--no-refresh` option.

[](#Documentation/git-config.txt-resolveConflict)resolveConflict

Shown by various commands when conflicts prevent the operation from being performed.

[](#Documentation/git-config.txt-rmHints)rmHints

Shown on failure in the output of [git-rm\[1\]](https://git-scm.com/docs/git-rm), to give directions on how to proceed from the current state.

[](#Documentation/git-config.txt-sequencerInUse)sequencerInUse

Shown when a sequencer command is already in progress.

[](#Documentation/git-config.txt-skippedCherryPicks)skippedCherryPicks

Shown when [git-rebase\[1\]](https://git-scm.com/docs/git-rebase) skips a commit that has already been cherry-picked onto the upstream branch.

[](#Documentation/git-config.txt-sparseIndexExpanded)sparseIndexExpanded

Shown when a sparse index is expanded to a full index, which is likely due to an unexpected set of files existing outside of the sparse-checkout.

[](#Documentation/git-config.txt-statusAheadBehind)statusAheadBehind

Shown when [git-status\[1\]](https://git-scm.com/docs/git-status) computes the ahead/behind counts for a local ref compared to its remote tracking ref, and that calculation takes longer than expected. Will not appear if `status.aheadBehind` is false or the option `--no-ahead-behind` is given.

[](#Documentation/git-config.txt-statusHints)statusHints

Show directions on how to proceed from the current state in the output of [git-status\[1\]](https://git-scm.com/docs/git-status), in the template shown when writing commit messages in [git-commit\[1\]](https://git-scm.com/docs/git-commit), and in the help message shown by [git-switch\[1\]](https://git-scm.com/docs/git-switch) or [git-checkout\[1\]](https://git-scm.com/docs/git-checkout) when switching branches.

[](#Documentation/git-config.txt-statusUoption)statusUoption

Shown when [git-status\[1\]](https://git-scm.com/docs/git-status) takes more than 2 seconds to enumerate untracked files, to tell the user that they can use the `-u` option.

[](#Documentation/git-config.txt-submoduleAlternateErrorStrategyDie)submoduleAlternateErrorStrategyDie

Shown when a submodule.alternateErrorStrategy option configured to "die" causes a fatal error.

[](#Documentation/git-config.txt-submoduleMergeConflict)submoduleMergeConflict

Advice shown when a non-trivial submodule merge conflict is encountered.

[](#Documentation/git-config.txt-submodulesNotUpdated)submodulesNotUpdated

Shown when a user runs a submodule command that fails because `git` `submodule` `update` `--init` was not run.

[](#Documentation/git-config.txt-suggestDetachingHead)suggestDetachingHead

Shown when [git-switch\[1\]](https://git-scm.com/docs/git-switch) refuses to detach HEAD without the explicit `--detach` option.

[](#Documentation/git-config.txt-updateSparsePath)updateSparsePath

Shown when either [git-add\[1\]](https://git-scm.com/docs/git-add) or [git-rm\[1\]](https://git-scm.com/docs/git-rm) is asked to update index entries outside the current sparse checkout.

[](#Documentation/git-config.txt-waitingForEditor)waitingForEditor

Shown when Git is waiting for editor input. Relevant when e.g. the editor is not launched inside the terminal.

[](#Documentation/git-config.txt-worktreeAddOrphan)worktreeAddOrphan

Shown when the user tries to create a worktree from an invalid reference, to tell the user how to create a new unborn branch instead.

[](#Documentation/git-config.txt-alias)alias.*

Command aliases for the [git\[1\]](https://git-scm.com/docs/git) command wrapper - e.g. after defining `alias.last` `=` `cat-file` `commit` `HEAD`, the invocation `git` `last` is equivalent to `git` `cat-file` `commit` `HEAD`. To avoid confusion and troubles with script usage, aliases that hide existing Git commands are ignored except for deprecated commands. Arguments are split by spaces, the usual shell quoting and escaping are supported. A quote pair or a backslash can be used to quote them.

Note that the first word of an alias does not necessarily have to be a command. It can be a command-line option that will be passed into the invocation of `git`. In particular, this is useful when used with `-c` to pass in one-time configurations or `-p` to force pagination. For example, `loud-rebase` `=` `-c` `commit.verbose=true` `rebase` can be defined such that running `git` `loud-rebase` would be equivalent to `git` `-c` `commit.verbose=true` `rebase`. Also, `ps` `=` `-p` `status` would be a helpful alias since `git` `ps` would paginate the output of `git` `status` where the original command does not.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
