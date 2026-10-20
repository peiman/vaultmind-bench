---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#23-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-23-variables
type: reference
title: Git - git-config Documentation › Variables (17/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#23-variables
source_hash: e103330a18fae84a1c4a183be8ea061605f33655fe197b89d26ba4e804a3f92c
---
Count changes in a child directory for the parent directory as well. Note that when using `cumulative`, the sum of the percentages reported may exceed 100%. The default (non-cumulative) behavior can be specified with the `noncumulative` parameter.

[](#Documentation/git-config.txt-limit)*&lt;limit&gt;*

An integer parameter specifies a cut-off percent (3% by default). Directories contributing less than this percentage of the changes are not shown in the output.

Example: The following will count changed files, while ignoring directories with less than 10% of the total amount of changed files, and accumulating child directory counts in the parent directories: `files,10,cumulative`.

[](#Documentation/git-config.txt-diffstatNameWidth)`diff.statNameWidth`

Limit the width of the filename part in `--stat` output. If set, applies to all commands generating `--stat` output except `format-patch`.

[](#Documentation/git-config.txt-diffstatGraphWidth)`diff.statGraphWidth`

Limit the width of the graph part in `--stat` output. If set, applies to all commands generating `--stat` output except `format-patch`.

[](#Documentation/git-config.txt-diffcontext)`diff.context`

Generate diffs with *&lt;n&gt;* lines of context instead of the default of 3. This value is overridden by the `-U` option.

[](#Documentation/git-config.txt-diffinterHunkContext)`diff.interHunkContext`

Show the context between diff hunks, up to the specified number of lines, thereby fusing the hunks that are close to each other. This value serves as the default for the `--inter-hunk-context` command line option.

[](#Documentation/git-config.txt-diffexternal)`diff.external`

If this config variable is set, diff generation is not performed using the internal diff machinery, but using the given command. Can be overridden with the `GIT_EXTERNAL_DIFF` environment variable. The command is called with parameters as described under "git Diffs" in [git\[1\]](https://git-scm.com/docs/git). Note: if you want to use an external diff program only on a subset of your files, you might want to use [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) instead.

[](#Documentation/git-config.txt-difftrustExitCode)`diff.trustExitCode`

If this boolean value is set to `true` then the `diff.external` command is expected to return exit code 0 if it considers the input files to be equal or 1 if it considers them to be different, like `diff`(1). If it is set to `false`, which is the default, then the command is expected to return exit code `0` regardless of equality. Any other exit code causes Git to report a fatal error.

[](#Documentation/git-config.txt-diffignoreSubmodules)`diff.ignoreSubmodules`

Sets the default value of `--ignore-submodules`. Note that this affects only `git` `diff` Porcelain, and not lower level `diff` commands such as `git` `diff-files`. `git` `checkout` and `git` `switch` also honor this setting when reporting uncommitted changes. Setting it to `all` disables the submodule summary normally shown by `git` `commit` and `git` `status` when `status.submoduleSummary` is set unless it is overridden by using the `--ignore-submodules` command-line option. The `git` `submodule` commands are not affected by this setting. By default this is set to untracked so that any untracked submodules are ignored.

[](#Documentation/git-config.txt-diffmnemonicPrefix)`diff.mnemonicPrefix`

If set, `git` `diff` uses a prefix pair that is different from the standard `a/` and `b/` depending on what is being compared. When this configuration is in effect, reverse diff output also swaps the order of the prefixes:

[](#Documentation/git-config.txt-gitdiff)`git` `diff`

compares the (i)ndex and the (w)ork tree;

[](#Documentation/git-config.txt-gitdiffHEAD)`git` `diff` `HEAD`

compares a (c)ommit and the (w)ork tree;

[](#Documentation/git-config.txt-gitdiff--cached)`git` `diff` `--cached`

compares a (c)ommit and the (i)ndex;

[](#Documentation/git-config.txt-gitdiffHEADfile1file2)`git` `diff` `HEAD:`*&lt;file1&gt;* *&lt;file2&gt;*

compares an (o)bject and a (w)ork tree entity;

[](#Documentation/git-config.txt-gitdiff--no-indexab)`git` `diff` `--no-index` *&lt;a&gt;* *&lt;b&gt;*

compares two non-git things *&lt;a&gt;* and *&lt;b&gt;*.

[](#Documentation/git-config.txt-diffnoPrefix)`diff.noPrefix`

If set, `git` `diff` does not show any source or destination prefix.

[](#Documentation/git-config.txt-diffsrcPrefix)`diff.srcPrefix`

If set, `git` `diff` uses this source prefix. Defaults to `a/`.

[](#Documentation/git-config.txt-diffdstPrefix)`diff.dstPrefix`

If set, `git` `diff` uses this destination prefix. Defaults to `b/`.

[](#Documentation/git-config.txt-diffrelative)`diff.relative`

If set to `true`, `git` `diff` does not show changes outside of the directory and show pathnames relative to the current directory.

[](#Documentation/git-config.txt-difforderFile)`diff.orderFile`

File indicating how to order files within a diff. See the `-O` option to [git-diff\[1\]](https://git-scm.com/docs/git-diff) for details. If `diff.orderFile` is a relative pathname, it is treated as relative to the top of the working tree.

[](#Documentation/git-config.txt-diffrenameLimit)`diff.renameLimit`

The number of files to consider in the exhaustive portion of copy/rename detection; equivalent to the `git` `diff` option `-l`. If not set, the default value is currently 1000. This setting has no effect if rename detection is turned off.

[](#Documentation/git-config.txt-diffrenames)`diff.renames`

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
