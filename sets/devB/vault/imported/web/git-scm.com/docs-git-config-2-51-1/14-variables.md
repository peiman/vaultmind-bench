---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#14-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-14-variables
type: reference
title: Git - git-config Documentation › Variables (8/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#14-variables
source_hash: 845657960108c271014931f3f08dd6871678f6e0128812641accac2bfcc8613f
---
If set, keywords at the start of the line are highlighted. The keywords are "error", "warning", "hint" and "success", and are matched case-insensitively. May be set to `always`, `false` (or `never`) or `auto` (or `true`). If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-colorremoteslot)color.remote.&lt;slot&gt;

Use customized color for each remote keyword. *&lt;slot&gt;* may be `hint`, `warning`, `success` or `error` which match the corresponding keyword.

[](#Documentation/git-config.txt-colorshowBranch)color.showBranch

A boolean to enable/disable color in the output of [git-show-branch\[1\]](https://git-scm.com/docs/git-show-branch). May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the output is to a terminal. If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-colorstatus)color.status

A boolean to enable/disable color in the output of [git-status\[1\]](https://git-scm.com/docs/git-status). May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the output is to a terminal. If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-colorstatusslot)color.status.&lt;slot&gt;

Use customized color for status colorization. *&lt;slot&gt;* is one of `header` (the header text of the status message), `added` or `updated` (files which are added but not committed), `changed` (files which are changed but not added in the index), `untracked` (files which are not tracked by Git), `branch` (the current branch), `nobranch` (the color the *no branch* warning is shown in, defaulting to red), `localBranch` or `remoteBranch` (the local and remote branch names, respectively, when branch and tracking information is displayed in the status short-format), or `unmerged` (files which have unmerged changes).

[](#Documentation/git-config.txt-colortransport)color.transport

A boolean to enable/disable color when pushes are rejected. May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the error output goes to a terminal. If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-colortransportrejected)color.transport.rejected

Use customized color when a push was rejected.

[](#Documentation/git-config.txt-colorui)color.ui

This variable determines the default value for variables such as `color.diff` and `color.grep` that control the use of color per command family. Its scope will expand as more commands learn configuration to set a default for the `--color` option. Set it to `false` or `never` if you prefer Git commands not to use color unless enabled explicitly with some other configuration or the `--color` option. Set it to `always` if you want all output not intended for machine consumption to use color, to `true` or `auto` (this is the default since Git 1.8.4) if you want such output to use color when written to the terminal.

[](#Documentation/git-config.txt-columnui)column.ui

Specify whether supported commands should output in columns. This variable consists of a list of tokens separated by spaces or commas:

These options control when the feature should be enabled (defaults to *never*):

[](#Documentation/git-config.txt-always-1-1)`always`

always show in columns

[](#Documentation/git-config.txt-never-1)`never`

never show in columns

[](#Documentation/git-config.txt-auto)`auto`

show in columns if the output is to the terminal

These options control layout (defaults to *column*). Setting any of these implies *always* if none of *always*, *never*, or *auto* are specified.

[](#Documentation/git-config.txt-column-1)`column`

fill columns before rows

[](#Documentation/git-config.txt-row)`row`

fill rows before columns

[](#Documentation/git-config.txt-plain)`plain`

show in one column

Finally, these options can be combined with a layout option (defaults to *nodense*):

[](#Documentation/git-config.txt-dense)`dense`

make unequal size columns to utilize more space

[](#Documentation/git-config.txt-nodense)`nodense`

make equal size columns

[](#Documentation/git-config.txt-columnbranch)column.branch

Specify whether to output branch listing in `git` `branch` in columns. See `column.ui` for details.

[](#Documentation/git-config.txt-columnclean)column.clean

Specify the layout when listing items in `git` `clean` `-i`, which always shows files and directories in columns. See `column.ui` for details.

[](#Documentation/git-config.txt-columnstatus)column.status

Specify whether to output untracked files in `git` `status` in columns. See `column.ui` for details.

[](#Documentation/git-config.txt-columntag)column.tag

Specify whether to output tag listings in `git` `tag` in columns. See `column.ui` for details.

[](#Documentation/git-config.txt-commitcleanup)`commit.cleanup`

This setting overrides the default of the `--cleanup` option in `git` `commit`. See [git-commit\[1\]](https://git-scm.com/docs/git-commit) for details. Changing the default can be useful when you always want to keep lines that begin with the comment character (`core.commentChar`, default `#`) in your log message, in which case you would do `git` `config` `commit.cleanup` `whitespace` (note that you will have to remove the help lines that begin with the comment character in the commit log template yourself, if you do this).

[](#Documentation/git-config.txt-commitgpgSign)`commit.gpgSign`

A boolean to specify whether all commits should be GPG signed. Use of this option when doing operations such as rebase can result in a large number of commits being signed. It may be convenient to use an agent to avoid typing your GPG passphrase several times.

[](#Documentation/git-config.txt-commitstatus)`commit.status`

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
