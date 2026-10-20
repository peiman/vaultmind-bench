---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#07-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-07-variables
type: reference
title: Git - git-config Documentation › Variables (1/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#07-variables
source_hash: 31191c25bf4436b902372c80024207175136fd4f0274542d6b7daa921b83f9f7
---
Note that this list is non-comprehensive and not necessarily complete. For command-specific variables, you will find a more detailed description in the appropriate manual page.

Other git-related tools may and do use their own variables. When inventing new variables for use in your own tool, make sure their names do not conflict with those that are used by Git itself and other popular tools, and describe them in your documentation.

[](#Documentation/git-config.txt-addignoreErrors)`add.ignoreErrors`

[](#Documentation/git-config.txt-addignore-errorsdeprecated)`add.ignore-errors` (deprecated)

Tells `git` `add` to continue adding files when some files cannot be added due to indexing errors. Equivalent to the `--ignore-errors` option of [git-add\[1\]](https://git-scm.com/docs/git-add). `add.ignore-errors` is deprecated, as it does not follow the usual naming convention for configuration variables.

[](#Documentation/git-config.txt-advice)advice.*

These variables control various optional help messages designed to aid new users. When left unconfigured, Git will give the message alongside instructions on how to squelch it. You can tell Git that you have understood the issue and no longer need a specific help message by setting the corresponding variable to `false`.

As they are intended to help human users, these messages are output to the standard error. When tools that run Git as a subprocess find them disruptive, they can set `GIT_ADVICE=0` in the environment to squelch all advice messages.

[](#Documentation/git-config.txt-addEmbeddedRepo)addEmbeddedRepo

Shown when the user accidentally adds one git repo inside of another.

[](#Documentation/git-config.txt-addEmptyPathspec)addEmptyPathspec

Shown when the user runs `git` `add` without providing the pathspec parameter.

[](#Documentation/git-config.txt-addIgnoredFile)addIgnoredFile

Shown when the user attempts to add an ignored file to the index.

[](#Documentation/git-config.txt-amWorkDir)amWorkDir

Shown when [git-am\[1\]](https://git-scm.com/docs/git-am) fails to apply a patch file, to tell the user the location of the file.

[](#Documentation/git-config.txt-ambiguousFetchRefspec)ambiguousFetchRefspec

Shown when a fetch refspec for multiple remotes maps to the same remote-tracking branch namespace and causes branch tracking set-up to fail.

[](#Documentation/git-config.txt-checkoutAmbiguousRemoteBranchName)checkoutAmbiguousRemoteBranchName

Shown when the argument to [git-checkout\[1\]](https://git-scm.com/docs/git-checkout) and [git-switch\[1\]](https://git-scm.com/docs/git-switch) ambiguously resolves to a remote tracking branch on more than one remote in situations where an unambiguous argument would have otherwise caused a remote-tracking branch to be checked out. See the `checkout.defaultRemote` configuration variable for how to set a given remote to be used by default in some situations where this advice would be printed.

[](#Documentation/git-config.txt-commitBeforeMerge)commitBeforeMerge

Shown when [git-merge\[1\]](https://git-scm.com/docs/git-merge) refuses to merge to avoid overwriting local changes.

[](#Documentation/git-config.txt-detachedHead)detachedHead

Shown when the user uses [git-switch\[1\]](https://git-scm.com/docs/git-switch) or [git-checkout\[1\]](https://git-scm.com/docs/git-checkout) to move to the detached HEAD state, to tell the user how to create a local branch after the fact.

[](#Documentation/git-config.txt-diverging)diverging

Shown when a fast-forward is not possible.

[](#Documentation/git-config.txt-fetchShowForcedUpdates)fetchShowForcedUpdates

Shown when [git-fetch\[1\]](https://git-scm.com/docs/git-fetch) takes a long time to calculate forced updates after ref updates, or to warn that the check is disabled.

[](#Documentation/git-config.txt-forceDeleteBranch)forceDeleteBranch

Shown when the user tries to delete a not fully merged branch without the force option set.

[](#Documentation/git-config.txt-ignoredHook)ignoredHook

Shown when a hook is ignored because the hook is not set as executable.

[](#Documentation/git-config.txt-implicitIdentity)implicitIdentity

Shown when the user’s information is guessed from the system username and domain name, to tell the user how to set their identity configuration.

[](#Documentation/git-config.txt-mergeConflict)mergeConflict

Shown when various commands stop because of conflicts.

[](#Documentation/git-config.txt-nestedTag)nestedTag

Shown when a user attempts to recursively tag a tag object.

[](#Documentation/git-config.txt-pushAlreadyExists)pushAlreadyExists

Shown when [git-push\[1\]](https://git-scm.com/docs/git-push) rejects an update that does not qualify for fast-forwarding (e.g., a tag.)

[](#Documentation/git-config.txt-pushFetchFirst)pushFetchFirst

Shown when [git-push\[1\]](https://git-scm.com/docs/git-push) rejects an update that tries to overwrite a remote ref that points at an object we do not have.

[](#Documentation/git-config.txt-pushNeedsForce)pushNeedsForce

Shown when [git-push\[1\]](https://git-scm.com/docs/git-push) rejects an update that tries to overwrite a remote ref that points at an object that is not a commit-ish, or make the remote ref point at an object that is not a commit-ish.

[](#Documentation/git-config.txt-pushNonFFCurrent)pushNonFFCurrent

Shown when [git-push\[1\]](https://git-scm.com/docs/git-push) fails due to a non-fast-forward update to the current branch.

[](#Documentation/git-config.txt-pushNonFFMatching)pushNonFFMatching

Shown when the user ran [git-push\[1\]](https://git-scm.com/docs/git-push) and pushed "matching refs" explicitly (i.e. used `:`, or specified a refspec that isn’t the current branch) and it resulted in a non-fast-forward error.

[](#Documentation/git-config.txt-pushRefNeedsUpdate)pushRefNeedsUpdate

Shown when [git-push\[1\]](https://git-scm.com/docs/git-push) rejects a forced update of a branch when its remote-tracking ref has updates that we do not have locally.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
