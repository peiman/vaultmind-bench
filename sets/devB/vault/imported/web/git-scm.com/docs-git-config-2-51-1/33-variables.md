---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#33-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-33-variables
type: reference
title: Git - git-config Documentation › Variables (27/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#33-variables
source_hash: 972d496ec8b76aa41344e1099e6fcea487fa7f38dc279e55f51cae12bf4b86df
---
Using a SSH CA key with the cert-authority option (see ssh-keygen(1) "CERTIFICATES") is also valid.

[](#Documentation/git-config.txt-gpgsshrevocationFile)gpg.ssh.revocationFile

Either a SSH KRL or a list of revoked public keys (without the principal prefix). See ssh-keygen(1) for details. If a public key is found in this file then it will always be treated as having trust level "never" and signatures will show as invalid.

[](#Documentation/git-config.txt-greplineNumber)grep.lineNumber

If set to true, enable `-n` option by default.

[](#Documentation/git-config.txt-grepcolumn)grep.column

If set to true, enable the `--column` option by default.

[](#Documentation/git-config.txt-greppatternType)grep.patternType

Set the default matching behavior. Using a value of *basic*, *extended*, *fixed*, or *perl* will enable the `--basic-regexp`, `--extended-regexp`, `--fixed-strings`, or `--perl-regexp` option accordingly, while the value *default* will use the `grep.extendedRegexp` option to choose between *basic* and *extended*.

[](#Documentation/git-config.txt-grepextendedRegexp)grep.extendedRegexp

If set to true, enable `--extended-regexp` option by default. This option is ignored when the `grep.patternType` option is set to a value other than *default*.

[](#Documentation/git-config.txt-grepthreads)grep.threads

Number of grep worker threads to use. If unset (or set to 0), Git will use as many threads as the number of logical cores available.

[](#Documentation/git-config.txt-grepfullName)grep.fullName

If set to true, enable `--full-name` option by default.

[](#Documentation/git-config.txt-grepfallbackToNoIndex)grep.fallbackToNoIndex

If set to true, fall back to `git` `grep` `--no-index` if `git` `grep` is executed outside of a git repository. Defaults to false.

[](#Documentation/git-config.txt-guicommitMsgWidth)gui.commitMsgWidth

Defines how wide the commit message window is in the [git-gui\[1\]](https://git-scm.com/docs/git-gui). "75" is the default.

[](#Documentation/git-config.txt-guidiffContext)gui.diffContext

Specifies how many context lines should be used in calls to diff made by the [git-gui\[1\]](https://git-scm.com/docs/git-gui). The default is "5".

[](#Documentation/git-config.txt-guidisplayUntracked)gui.displayUntracked

Determines if [git-gui\[1\]](https://git-scm.com/docs/git-gui) shows untracked files in the file list. The default is "true".

[](#Documentation/git-config.txt-guiencoding)gui.encoding

Specifies the default character encoding to use for displaying of file contents in [git-gui\[1\]](https://git-scm.com/docs/git-gui) and [gitk\[1\]](https://git-scm.com/docs/gitk). It can be overridden by setting the *encoding* attribute for relevant files (see [gitattributes\[5\]](https://git-scm.com/docs/gitattributes)). If this option is not set, the tools default to the locale encoding.

[](#Documentation/git-config.txt-guimatchTrackingBranch)gui.matchTrackingBranch

Determines if new branches created with [git-gui\[1\]](https://git-scm.com/docs/git-gui) should default to tracking remote branches with matching names or not. Default: "false".

[](#Documentation/git-config.txt-guinewBranchTemplate)gui.newBranchTemplate

Is used as a suggested name when creating new branches using the [git-gui\[1\]](https://git-scm.com/docs/git-gui).

[](#Documentation/git-config.txt-guipruneDuringFetch)gui.pruneDuringFetch

"true" if [git-gui\[1\]](https://git-scm.com/docs/git-gui) should prune remote-tracking branches when performing a fetch. The default value is "false".

[](#Documentation/git-config.txt-guitrustmtime)gui.trustmtime

Determines if [git-gui\[1\]](https://git-scm.com/docs/git-gui) should trust the file modification timestamp or not. By default the timestamps are not trusted.

[](#Documentation/git-config.txt-guispellingDictionary)gui.spellingDictionary

Specifies the dictionary used for spell checking commit messages in the [git-gui\[1\]](https://git-scm.com/docs/git-gui). When set to "none" spell checking is turned off.

[](#Documentation/git-config.txt-guifastCopyBlame)gui.fastCopyBlame

If true, *git gui blame* uses `-C` instead of `-C` `-C` for original location detection. It makes blame significantly faster on huge repositories at the expense of less thorough copy detection.

[](#Documentation/git-config.txt-guicopyBlameThreshold)gui.copyBlameThreshold

Specifies the threshold to use in *git gui blame* original location detection, measured in alphanumeric characters. See the [git-blame\[1\]](https://git-scm.com/docs/git-blame) manual for more information on copy detection.

[](#Documentation/git-config.txt-guiblamehistoryctx)gui.blamehistoryctx

Specifies the radius of history context in days to show in [gitk\[1\]](https://git-scm.com/docs/gitk) for the selected commit, when the `Show` `History` `Context` menu item is invoked from *git gui blame*. If this variable is set to zero, the whole history is shown.

[](#Documentation/git-config.txt-guitoolnamecmd)guitool.&lt;name&gt;.cmd

Specifies the shell command line to execute when the corresponding item of the [git-gui\[1\]](https://git-scm.com/docs/git-gui) `Tools` menu is invoked. This option is mandatory for every tool. The command is executed from the root of the working directory, and in the environment it receives the name of the tool as `GIT_GUITOOL`, the name of the currently selected file as *FILENAME*, and the name of the current branch as *CUR\_BRANCH* (if the head is detached, *CUR\_BRANCH* is empty).

[](#Documentation/git-config.txt-guitoolnameneedsFile)guitool.&lt;name&gt;.needsFile

Run the tool only if a diff is selected in the GUI. It guarantees that *FILENAME* is not empty.

[](#Documentation/git-config.txt-guitoolnamenoConsole)guitool.&lt;name&gt;.noConsole

Run the command silently, without creating a window to display its output.

[](#Documentation/git-config.txt-guitoolnamenoRescan)guitool.&lt;name&gt;.noRescan

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
