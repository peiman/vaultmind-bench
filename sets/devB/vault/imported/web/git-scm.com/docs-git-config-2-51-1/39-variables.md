---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#39-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-39-variables
type: reference
title: Git - git-config Documentation › Variables (33/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#39-variables
source_hash: 9022ae09d624d9cc3146c86308f223310fd907d9833577e23637acc47452a4db
---
The port number to bind the gitweb httpd to. See [git-instaweb\[1\]](https://git-scm.com/docs/git-instaweb).

[](#Documentation/git-config.txt-interactivesingleKey)interactive.singleKey

When set to true, allow the user to provide one-letter input with a single key (i.e., without hitting the Enter key) in interactive commands. This is currently used by the `--patch` mode of [git-add\[1\]](https://git-scm.com/docs/git-add), [git-checkout\[1\]](https://git-scm.com/docs/git-checkout), [git-restore\[1\]](https://git-scm.com/docs/git-restore), [git-commit\[1\]](https://git-scm.com/docs/git-commit), [git-reset\[1\]](https://git-scm.com/docs/git-reset), and [git-stash\[1\]](https://git-scm.com/docs/git-stash).

[](#Documentation/git-config.txt-interactivediffFilter)interactive.diffFilter

When an interactive command (such as `git` `add` `--patch`) shows a colorized diff, git will pipe the diff through the shell command defined by this configuration variable. The command may mark up the diff further for human consumption, provided that it retains a one-to-one correspondence with the lines in the original diff. Defaults to disabled (no filtering).

[](#Documentation/git-config.txt-logabbrevCommit)`log.abbrevCommit`

If `true`, make [git-log\[1\]](https://git-scm.com/docs/git-log), [git-show\[1\]](https://git-scm.com/docs/git-show), and [git-whatchanged\[1\]](https://git-scm.com/docs/git-whatchanged) assume `--abbrev-commit`. You may override this option with `--no-abbrev-commit`.

[](#Documentation/git-config.txt-logdate)`log.date`

Set the default date-time mode for the `log` command. Setting a value for log.date is similar to using `git` `log`'s `--date` option. See [git-log\[1\]](https://git-scm.com/docs/git-log) for details.

If the format is set to "auto:foo" and the pager is in use, format "foo" will be used for the date format. Otherwise, "default" will be used.

[](#Documentation/git-config.txt-logdecorate)`log.decorate`

Print out the ref names of any commits that are shown by the log command. Possible values are:

[](#Documentation/git-config.txt-short)`short`

the ref name prefixes `refs/heads/`, `refs/tags/` and `refs/remotes/` are not printed.

[](#Documentation/git-config.txt-full)`full`

the full ref name (including prefix) are printed.

[](#Documentation/git-config.txt-auto-1)`auto`

if the output is going to a terminal, the ref names are shown as if `short` were given, otherwise no ref names are shown.

This is the same as the `--decorate` option of the `git` `log`.

[](#Documentation/git-config.txt-loginitialDecorationSet)`log.initialDecorationSet`

By default, `git` `log` only shows decorations for certain known ref namespaces. If *all* is specified, then show all refs as decorations.

[](#Documentation/git-config.txt-logexcludeDecoration)`log.excludeDecoration`

Exclude the specified patterns from the log decorations. This is similar to the `--decorate-refs-exclude` command-line option, but the config option can be overridden by the `--decorate-refs` option.

[](#Documentation/git-config.txt-logdiffMerges)`log.diffMerges`

Set diff format to be used when `--diff-merges=on` is specified, see `--diff-merges` in [git-log\[1\]](https://git-scm.com/docs/git-log) for details. Defaults to `separate`.

[](#Documentation/git-config.txt-logfollow)`log.follow`

If `true`, `git` `log` will act as if the `--follow` option was used when a single &lt;path&gt; is given. This has the same limitations as `--follow`, i.e. it cannot be used to follow multiple files and does not work well on non-linear history.

[](#Documentation/git-config.txt-loggraphColors)`log.graphColors`

A list of colors, separated by commas, that can be used to draw history lines in `git` `log` `--graph`.

[](#Documentation/git-config.txt-logshowRoot)`log.showRoot`

If true, the initial commit will be shown as a big creation event. This is equivalent to a diff against an empty tree. Tools like [git-log\[1\]](https://git-scm.com/docs/git-log) or [git-whatchanged\[1\]](https://git-scm.com/docs/git-whatchanged), which normally hide the root commit will now show it. True by default.

[](#Documentation/git-config.txt-logshowSignature)`log.showSignature`

If true, makes [git-log\[1\]](https://git-scm.com/docs/git-log), [git-show\[1\]](https://git-scm.com/docs/git-show), and [git-whatchanged\[1\]](https://git-scm.com/docs/git-whatchanged) assume `--show-signature`.

[](#Documentation/git-config.txt-logmailmap)`log.mailmap`

If true, makes [git-log\[1\]](https://git-scm.com/docs/git-log), [git-show\[1\]](https://git-scm.com/docs/git-show), and [git-whatchanged\[1\]](https://git-scm.com/docs/git-whatchanged) assume `--use-mailmap`, otherwise assume `--no-use-mailmap`. True by default.

[](#Documentation/git-config.txt-lsrefsunborn)lsrefs.unborn

May be "advertise" (the default), "allow", or "ignore". If "advertise", the server will respond to the client sending "unborn" (as described in [gitprotocol-v2\[5\]](https://git-scm.com/docs/gitprotocol-v2)) and will advertise support for this feature during the protocol v2 capability advertisement. "allow" is the same as "advertise" except that the server will not advertise support for this feature; this is useful for load-balanced servers that cannot be updated atomically (for example), since the administrator could configure "allow", then after a delay, configure "advertise".

[](#Documentation/git-config.txt-mailinfoscissors)mailinfo.scissors

If true, makes [git-mailinfo\[1\]](https://git-scm.com/docs/git-mailinfo) (and therefore [git-am\[1\]](https://git-scm.com/docs/git-am)) act by default as if the --scissors option was provided on the command-line. When active, this feature removes everything from the message body before a scissors line (i.e. consisting mainly of "&gt;8", "8&lt;" and "-").

[](#Documentation/git-config.txt-mailmapfile)mailmap.file

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
