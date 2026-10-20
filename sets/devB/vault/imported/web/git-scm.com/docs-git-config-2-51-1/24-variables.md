---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#24-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-24-variables
type: reference
title: Git - git-config Documentation › Variables (18/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#24-variables
source_hash: ae5abc15554cb66074ed14a23bbfa53bf75959698add6d6253f117ccd2470d87
---
Whether and how Git detects renames. If set to `false`, rename detection is disabled. If set to `true`, basic rename detection is enabled. If set to `copies` or `copy`, Git will detect copies, as well. Defaults to `true`. Note that this affects only `git` `diff` Porcelain like [git-diff\[1\]](https://git-scm.com/docs/git-diff) and [git-log\[1\]](https://git-scm.com/docs/git-log), and not lower level commands such as [git-diff-files\[1\]](https://git-scm.com/docs/git-diff-files).

[](#Documentation/git-config.txt-diffsuppressBlankEmpty)`diff.suppressBlankEmpty`

A boolean to inhibit the standard behavior of printing a space before each empty output line. Defaults to `false`.

[](#Documentation/git-config.txt-diffsubmodule)`diff.submodule`

Specify the format in which differences in submodules are shown. The `short` format just shows the names of the commits at the beginning and end of the range. The `log` format lists the commits in the range like [git-submodule\[1\]](https://git-scm.com/docs/git-submodule) `summary` does. The `diff` format shows an inline diff of the changed contents of the submodule. Defaults to `short`.

[](#Documentation/git-config.txt-diffwordRegex)`diff.wordRegex`

A POSIX Extended Regular Expression used to determine what is a "word" when performing word-by-word difference calculations. Character sequences that match the regular expression are "words", all other characters are **ignorable** whitespace.

[](#Documentation/git-config.txt-diffdrivercommand)`diff.`*&lt;driver&gt;*`.command`

The custom diff driver command. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-diffdrivertrustExitCode)`diff.`*&lt;driver&gt;*`.trustExitCode`

If this boolean value is set to `true` then the `diff.`*&lt;driver&gt;*`.command` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(1). If it is set to `false`, which is the default, then the command is expected to return exit code 0 regardless of equality. Any other exit code causes Git to report a fatal error.

[](#Documentation/git-config.txt-diffdriverxfuncname)`diff.`*&lt;driver&gt;*`.xfuncname`

The regular expression that the diff driver should use to recognize the hunk header. A built-in pattern may also be used. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-diffdriverbinary)`diff.`*&lt;driver&gt;*`.binary`

Set this option to `true` to make the diff driver treat files as binary. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-diffdrivertextconv)`diff.`*&lt;driver&gt;*`.textconv`

The command that the diff driver should call to generate the text-converted version of a file. The result of the conversion is used to generate a human-readable diff. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-diffdriverwordRegex)`diff.`*&lt;driver&gt;*`.wordRegex`

The regular expression that the diff driver should use to split words in a line. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-diffdrivercachetextconv)`diff.`*&lt;driver&gt;*`.cachetextconv`

Set this option to `true` to make the diff driver cache the text conversion outputs. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-diffindentHeuristic)`diff.indentHeuristic`

Set this option to `false` to disable the default heuristics that shift diff hunk boundaries to make patches easier to read.

[](#Documentation/git-config.txt-diffalgorithm)`diff.algorithm`

Choose a diff algorithm. The variants are as follows:

[](#Documentation/git-config.txt-default)`default`

[](#Documentation/git-config.txt-myers)`myers`

The basic greedy diff algorithm. Currently, this is the default.

[](#Documentation/git-config.txt-minimal)`minimal`

Spend extra time to make sure the smallest possible diff is produced.

[](#Documentation/git-config.txt-patience)`patience`

Use "patience diff" algorithm when generating patches.

[](#Documentation/git-config.txt-histogram)`histogram`

This algorithm extends the patience algorithm to "support low-occurrence common elements".

[](#Documentation/git-config.txt-diffwsErrorHighlight)`diff.wsErrorHighlight`

Highlight whitespace errors in the `context`, `old` or `new` lines of the diff. Multiple values are separated by comma, `none` resets previous values, `default` reset the list to `new` and `all` is a shorthand for `old,new,context`. The whitespace errors are colored with `color.diff.whitespace`. The command line option `--ws-error-highlight=`*&lt;kind&gt;* overrides this setting.

[](#Documentation/git-config.txt-diffcolorMoved)`diff.colorMoved`

If set to either a valid *&lt;mode&gt;* or a `true` value, moved lines in a diff are colored differently. For details of valid modes see `--color-moved` in [git-diff\[1\]](https://git-scm.com/docs/git-diff). If simply set to `true` the default color mode will be used. When set to `false`, moved lines are not colored.

[](#Documentation/git-config.txt-diffcolorMovedWS)`diff.colorMovedWS`

When moved lines are colored using e.g. the `diff.colorMoved` setting, this option controls the mode how spaces are treated. For details of valid modes see `--color-moved-ws` in [git-diff\[1\]](https://git-scm.com/docs/git-diff).

[](#Documentation/git-config.txt-difftool)diff.tool

Controls which diff tool is used by [git-difftool\[1\]](https://git-scm.com/docs/git-difftool). This variable overrides the value configured in `merge.tool`. The list below shows the valid built-in values. Any other value is treated as a custom diff tool and requires that a corresponding difftool.&lt;tool&gt;.cmd variable is defined.

[](#Documentation/git-config.txt-diffguitool)diff.guitool

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
