---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#47-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-47-variables
type: reference
title: Git - git-config Documentation › Variables (41/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#47-variables
source_hash: 5adb9c53b5496cd60e964072edb7f592c6cee4e675a793669e9abd1f1aa8c006
---
By default, Git does not create an extra merge commit when merging a commit that is a descendant of the current commit. Instead, the tip of the current branch is fast-forwarded. When set to `false`, this variable tells Git to create an extra merge commit in such a case (equivalent to giving the `--no-ff` option from the command line). When set to `only`, only such fast-forward merges are allowed (equivalent to giving the `--ff-only` option from the command line). This setting overrides `merge.ff` when pulling.

[](#Documentation/git-config.txt-pullrebase)pull.rebase

When true, rebase branches on top of the fetched branch, instead of merging the default branch from the default remote when "git pull" is run. See "branch.&lt;name&gt;.rebase" for setting this on a per-branch basis.

When `merges` (or just *m*), pass the `--rebase-merges` option to *git rebase* so that the local merge commits are included in the rebase (see [git-rebase\[1\]](https://git-scm.com/docs/git-rebase) for details).

When the value is `interactive` (or just *i*), the rebase is run in interactive mode.

**NOTE**: this is a possibly dangerous operation; do **not** use it unless you understand the implications (see [git-rebase\[1\]](https://git-scm.com/docs/git-rebase) for details).

[](#Documentation/git-config.txt-pulloctopus)pull.octopus

The default merge strategy to use when pulling multiple branches at once.

[](#Documentation/git-config.txt-pullautoStash)pull.autoStash

When set to true, automatically create a temporary stash entry to record the local changes before the operation begins, and restore them after the operation completes. When your "git pull" rebases (instead of merges), this may be convenient, since unlike merging pull that tolerates local changes that do not interfere with the merge, rebasing pull refuses to work with any local changes.

If `pull.autostash` is set (either to true or false), `merge.autostash` and `rebase.autostash` are ignored. If `pull.autostash` is not set at all, depending on the value of `pull.rebase`, `merge.autostash` or `rebase.autostash` is used instead. Can be overridden by the `--`\[`no-`]`autostash` command line option.

[](#Documentation/git-config.txt-pulltwohead)pull.twohead

The default merge strategy to use when pulling a single branch.

[](#Documentation/git-config.txt-pushautoSetupRemote)push.autoSetupRemote

If set to "true" assume `--set-upstream` on default push when no upstream tracking exists for the current branch; this option takes effect with push.default options *simple*, *upstream*, and *current*. It is useful if by default you want new branches to be pushed to the default remote (like the behavior of *push.default=current*) and you also want the upstream tracking to be set. Workflows most likely to benefit from this option are *simple* central workflows where all branches are expected to have the same name on the remote.

[](#Documentation/git-config.txt-pushdefault)push.default

Defines the action `git` `push` should take if no refspec is given (whether from the command-line, config, or elsewhere). Different values are well-suited for specific workflows; for instance, in a purely central workflow (i.e. the fetch source is equal to the push destination), `upstream` is probably what you want. Possible values are:

- `nothing` - do not push anything (error out) unless a refspec is given. This is primarily meant for people who want to avoid mistakes by always being explicit.
- `current` - push the current branch to update a branch with the same name on the receiving end. Works in both central and non-central workflows.
- `upstream` - push the current branch back to the branch whose changes are usually integrated into the current branch (which is called `@{upstream}`). This mode only makes sense if you are pushing to the same repository you would normally pull from (i.e. central workflow).
- `tracking` - This is a deprecated synonym for `upstream`.
- `simple` - push the current branch with the same name on the remote.

If you are working on a centralized workflow (pushing to the same repository you pull from, which is typically `origin`), then you need to configure an upstream branch with the same name.

This mode is the default since Git 2.0, and is the safest option suited for beginners.
- `matching` - push all branches having the same name on both ends. This makes the repository you are pushing to remember the set of branches that will be pushed out (e.g. if you always push *maint* and *master* there and no other branches, the repository you push to will have these two branches, and your local *maint* and *master* will be pushed there).

To use this mode effectively, you have to make sure *all* the branches you would push out are ready to be pushed out before running *git push*, as the whole point of this mode is to allow you to push all of the branches in one go. If you usually finish work on only one branch and push out the result, while other branches are unfinished, this mode is not for you. Also this mode is not suitable for pushing into a shared central repository, as other people may add new branches there, or update the tip of existing branches outside your control.

This used to be the default, but not since Git 2.0 (`simple` is the new default).

[](#Documentation/git-config.txt-pushfollowTags)push.followTags

If set to true, enable `--follow-tags` option by default. You may override this configuration at time of push by specifying `--no-follow-tags`.

[](#Documentation/git-config.txt-pushgpgSign)push.gpgSign

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
