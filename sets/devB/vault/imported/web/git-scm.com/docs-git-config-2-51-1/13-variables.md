---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#13-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-13-variables
type: reference
title: Git - git-config Documentation › Variables (7/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#13-variables
source_hash: 72be21c57033fb16a46f9c59fe15e389e9402d40ec3fde9f0626025c0c94f588
---
[](#Documentation/git-config.txt-colorbranch)color.branch

A boolean to enable/disable color in the output of [git-branch\[1\]](https://git-scm.com/docs/git-branch). May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the output is to a terminal. If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-colorbranchslot)color.branch.&lt;slot&gt;

Use customized color for branch coloration. *&lt;slot&gt;* is one of `current` (the current branch), `local` (a local branch), `remote` (a remote-tracking branch in refs/remotes/), `upstream` (upstream tracking branch), `plain` (other refs).

[](#Documentation/git-config.txt-colordiff)color.diff

Whether to use ANSI escape sequences to add color to patches. If this is set to `always`, [git-diff\[1\]](https://git-scm.com/docs/git-diff), [git-log\[1\]](https://git-scm.com/docs/git-log), and [git-show\[1\]](https://git-scm.com/docs/git-show) will use color for all patches. If it is set to `true` or `auto`, those commands will only use color when output is to the terminal. If unset, then the value of `color.ui` is used (`auto` by default).

This does not affect [git-format-patch\[1\]](https://git-scm.com/docs/git-format-patch) or the *git-diff-\** plumbing commands. Can be overridden on the command line with the `--color`\[`=`*&lt;when&gt;*] option.

[](#Documentation/git-config.txt-colordiffslot)color.diff.&lt;slot&gt;

Use customized color for diff colorization. *&lt;slot&gt;* specifies which part of the patch to use the specified color, and is one of `context` (context text - `plain` is a historical synonym), `meta` (metainformation), `frag` (hunk header), *func* (function in hunk header), `old` (removed lines), `new` (added lines), `commit` (commit headers), `whitespace` (highlighting whitespace errors), `oldMoved` (deleted lines), `newMoved` (added lines), `oldMovedDimmed`, `oldMovedAlternative`, `oldMovedAlternativeDimmed`, `newMovedDimmed`, `newMovedAlternative` `newMovedAlternativeDimmed` (See the *&lt;mode&gt;* setting of *--color-moved* in [git-diff\[1\]](https://git-scm.com/docs/git-diff) for details), `contextDimmed`, `oldDimmed`, `newDimmed`, `contextBold`, `oldBold`, and `newBold` (see [git-range-diff\[1\]](https://git-scm.com/docs/git-range-diff) for details).

[](#Documentation/git-config.txt-colordecorateslot)color.decorate.&lt;slot&gt;

Use customized color for *git log --decorate* output. *&lt;slot&gt;* is one of `branch`, `remoteBranch`, `tag`, `stash` or `HEAD` for local branches, remote-tracking branches, tags, stash and HEAD, respectively and `grafted` for grafted commits.

[](#Documentation/git-config.txt-colorgrep)color.grep

When set to `always`, always highlight matches. When `false` (or `never`), never. When set to `true` or `auto`, use color only when the output is written to the terminal. If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-colorgrepslot)color.grep.&lt;slot&gt;

Use customized color for grep colorization. *&lt;slot&gt;* specifies which part of the line to use the specified color, and is one of

[](#Documentation/git-config.txt-context)`context`

non-matching text in context lines (when using `-A`, `-B`, or `-C`)

[](#Documentation/git-config.txt-filename)`filename`

filename prefix (when not using `-h`)

[](#Documentation/git-config.txt-function)`function`

function name lines (when using `-p`)

[](#Documentation/git-config.txt-lineNumber)`lineNumber`

line number prefix (when using `-n`)

[](#Documentation/git-config.txt-column)`column`

column number prefix (when using `--column`)

[](#Documentation/git-config.txt-match)`match`

matching text (same as setting `matchContext` and `matchSelected`)

[](#Documentation/git-config.txt-matchContext)`matchContext`

matching text in context lines

[](#Documentation/git-config.txt-matchSelected)`matchSelected`

matching text in selected lines. Also, used to customize the following [git-log\[1\]](https://git-scm.com/docs/git-log) subcommands: `--grep`, `--author`, and `--committer`.

[](#Documentation/git-config.txt-selected)`selected`

non-matching text in selected lines. Also, used to customize the following [git-log\[1\]](https://git-scm.com/docs/git-log) subcommands: `--grep`, `--author` and `--committer`.

[](#Documentation/git-config.txt-separator)`separator`

separators between fields on a line (`:`, `-`, and `=`) and between hunks (`--`)

[](#Documentation/git-config.txt-colorinteractive)color.interactive

When set to `always`, always use colors for interactive prompts and displays (such as those used by "git-add --interactive" and "git-clean --interactive"). When false (or `never`), never. When set to `true` or `auto`, use colors only when the output is to the terminal. If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-colorinteractiveslot)color.interactive.&lt;slot&gt;

Use customized color for *git add --interactive* and *git clean --interactive* output. *&lt;slot&gt;* may be `prompt`, `header`, `help` or `error`, for four distinct types of normal output from interactive commands.

A boolean to specify whether `auto` color modes should colorize output going to the pager. Defaults to true; set this to false if your pager does not understand ANSI color codes.

[](#Documentation/git-config.txt-colorpush)color.push

A boolean to enable/disable color in push errors. May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the error output goes to a terminal. If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-colorpusherror)color.push.error

Use customized color for push errors.

[](#Documentation/git-config.txt-colorremote)color.remote

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
