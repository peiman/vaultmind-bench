---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#48-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-48-variables
type: reference
title: Git - git-config Documentation › Variables (42/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#48-variables
source_hash: 42bcefb959691d1ce94f9e5abd3d5854e3ea993f1a08a8f25d6b7206303ad341
---
May be set to a boolean value, or the string *if-asked*. A true value causes all pushes to be GPG signed, as if `--signed` is passed to [git-push\[1\]](https://git-scm.com/docs/git-push). The string *if-asked* causes pushes to be signed if the server supports it, as if `--signed=if-asked` is passed to *git push*. A false value may override a value from a lower-priority config file. An explicit command-line flag always overrides this config option.

[](#Documentation/git-config.txt-pushpushOption)push.pushOption

When no `--push-option=`*&lt;option&gt;* argument is given from the command line, `git` `push` behaves as if each &lt;value&gt; of this variable is given as `--push-option=`*&lt;value&gt;*.

This is a multi-valued variable, and an empty value can be used in a higher priority configuration file (e.g. `.git/config` in a repository) to clear the values inherited from a lower priority configuration files (e.g. `$HOME/.gitconfig`).

```
Example:

/etc/gitconfig
  push.pushoption = a
  push.pushoption = b

~/.gitconfig
  push.pushoption = c

repo/.git/config
  push.pushoption =
  push.pushoption = b

This will result in only b (a and c are cleared).
```

[](#Documentation/git-config.txt-pushrecurseSubmodules)push.recurseSubmodules

May be "check", "on-demand", "only", or "no", with the same behavior as that of "push --recurse-submodules". If not set, *no* is used by default, unless *submodule.recurse* is set (in which case a *true* value means *on-demand*).

[](#Documentation/git-config.txt-pushuseForceIfIncludes)push.useForceIfIncludes

If set to "true", it is equivalent to specifying `--force-if-includes` as an option to [git-push\[1\]](https://git-scm.com/docs/git-push) in the command line. Adding `--no-force-if-includes` at the time of push overrides this configuration setting.

[](#Documentation/git-config.txt-pushnegotiate)push.negotiate

If set to "true", attempt to reduce the size of the packfile sent by rounds of negotiation in which the client and the server attempt to find commits in common. If "false", Git will rely solely on the server’s ref advertisement to find commits in common.

[](#Documentation/git-config.txt-pushuseBitmaps)push.useBitmaps

If set to "false", disable use of bitmaps for "git push" even if `pack.useBitmaps` is "true", without preventing other git operations from using bitmaps. Default is true.

[](#Documentation/git-config.txt-rebasebackend)rebase.backend

Default backend to use for rebasing. Possible choices are *apply* or *merge*. In the future, if the merge backend gains all remaining capabilities of the apply backend, this setting may become unused.

[](#Documentation/git-config.txt-rebasestat)rebase.stat

Whether to show a diffstat of what changed upstream since the last rebase. False by default.

[](#Documentation/git-config.txt-rebaseautoSquash)rebase.autoSquash

If set to true, enable the `--autosquash` option of [git-rebase\[1\]](https://git-scm.com/docs/git-rebase) by default for interactive mode. This can be overridden with the `--no-autosquash` option.

[](#Documentation/git-config.txt-rebaseautoStash)rebase.autoStash

When set to true, automatically create a temporary stash entry before the operation begins, and apply it after the operation ends. This means that you can run rebase on a dirty worktree. However, use with care: the final stash application after a successful rebase might result in non-trivial conflicts. This option can be overridden by the `--no-autostash` and `--autostash` options of [git-rebase\[1\]](https://git-scm.com/docs/git-rebase). Defaults to false.

[](#Documentation/git-config.txt-rebaseupdateRefs)rebase.updateRefs

If set to true enable `--update-refs` option by default.

[](#Documentation/git-config.txt-rebasemissingCommitsCheck)rebase.missingCommitsCheck

If set to "warn", git rebase -i will print a warning if some commits are removed (e.g. a line was deleted), however the rebase will still proceed. If set to "error", it will print the previous warning and stop the rebase, *git rebase --edit-todo* can then be used to correct the error. If set to "ignore", no checking is done. To drop a commit without warning or error, use the `drop` command in the todo list. Defaults to "ignore".

[](#Documentation/git-config.txt-rebaseinstructionFormat)rebase.instructionFormat

A format string, as specified in [git-log\[1\]](https://git-scm.com/docs/git-log), to be used for the todo list during an interactive rebase. The format will automatically have the commit hash prepended to the format.

[](#Documentation/git-config.txt-rebaseabbreviateCommands)rebase.abbreviateCommands

If set to true, `git` `rebase` will use abbreviated command names in the todo list resulting in something like this:

```
	p deadbee The oneline of the commit
	p fa1afe1 The oneline of the next commit
	...
```

instead of:

```
	pick deadbee The oneline of the commit
	pick fa1afe1 The oneline of the next commit
	...
```

Defaults to false.

[](#Documentation/git-config.txt-rebaserescheduleFailedExec)rebase.rescheduleFailedExec

Automatically reschedule `exec` commands that failed. This only makes sense in interactive mode (or when an `--exec` option was provided). This is the same as specifying the `--reschedule-failed-exec` option.

[](#Documentation/git-config.txt-rebaseforkPoint)rebase.forkPoint

If set to false set `--no-fork-point` option by default.

[](#Documentation/git-config.txt-rebaserebaseMerges)rebase.rebaseMerges

Whether and how to set the `--rebase-merges` option by default. Can be `rebase-cousins`, `no-rebase-cousins`, or a boolean. Setting to true or to `no-rebase-cousins` is equivalent to `--rebase-merges=no-rebase-cousins`, setting to `rebase-cousins` is equivalent to `--rebase-merges=rebase-cousins`, and setting to false is equivalent to `--no-rebase-merges`. Passing `--rebase-merges` on the command line, with or without an argument, overrides any `rebase.rebaseMerges` configuration.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
