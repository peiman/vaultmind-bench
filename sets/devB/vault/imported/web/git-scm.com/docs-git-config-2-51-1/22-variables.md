---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#22-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-22-variables
type: reference
title: Git - git-config Documentation › Variables (16/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#22-variables
source_hash: 3874ca97e03a13e8712dffa770e364f92ef717f3c90d79d905310f4bc436561a
---
Set the length object names are abbreviated to. If unspecified or set to "auto", an appropriate value is computed based on the approximate number of packed objects in your repository, which hopefully is enough for abbreviated object names to stay unique for some time. If set to "no", no abbreviation is made and the object names are shown in their full length. The minimum length is 4.

[](#Documentation/git-config.txt-coremaxTreeDepth)core.maxTreeDepth

The maximum depth Git is willing to recurse while traversing a tree (e.g., "a/b/cde/f" has a depth of 4). This is a fail-safe to allow Git to abort cleanly, and should not generally need to be adjusted. When Git is compiled with MSVC, the default is 512. Otherwise, the default is 2048.

[](#Documentation/git-config.txt-credentialhelper)credential.helper

Specify an external helper to be called when a username or password credential is needed; the helper may consult external storage to avoid prompting the user for the credentials. This is normally the name of a credential helper with possible arguments, but may also be an absolute path with arguments or, if preceded by `!`, shell commands.

Note that multiple helpers may be defined. See [gitcredentials\[7\]](https://git-scm.com/docs/gitcredentials) for details and examples.

[](#Documentation/git-config.txt-credentialinteractive)credential.interactive

By default, Git and any configured credential helpers will ask for user input when new credentials are required. Many of these helpers will succeed based on stored credentials if those credentials are still valid. To avoid the possibility of user interactivity from Git, set `credential.interactive=false`. Some credential helpers respect this option as well.

[](#Documentation/git-config.txt-credentialuseHttpPath)credential.useHttpPath

When acquiring credentials, consider the "path" component of an http or https URL to be important. Defaults to false. See [gitcredentials\[7\]](https://git-scm.com/docs/gitcredentials) for more information.

[](#Documentation/git-config.txt-credentialsanitizePrompt)credential.sanitizePrompt

By default, user names and hosts that are shown as part of the password prompt are not allowed to contain control characters (they will be URL-encoded by default). Configure this setting to `false` to override that behavior.

[](#Documentation/git-config.txt-credentialprotectProtocol)credential.protectProtocol

By default, Carriage Return characters are not allowed in the protocol that is used when Git talks to a credential helper. This setting allows users to override this default.

[](#Documentation/git-config.txt-credentialusername)credential.username

If no username is set for a network authentication, use this username by default. See credential.&lt;context&gt;.* below, and [gitcredentials\[7\]](https://git-scm.com/docs/gitcredentials).

[](#Documentation/git-config.txt-credentialurl)credential.&lt;url&gt;.*

Any of the credential.* options above can be applied selectively to some credentials. For example, "credential.https://example.com.username" would set the default username only for https connections to example.com. See [gitcredentials\[7\]](https://git-scm.com/docs/gitcredentials) for details on how URLs are matched.

[](#Documentation/git-config.txt-credentialCacheignoreSIGHUP)credentialCache.ignoreSIGHUP

Tell git-credential-cache—​daemon to ignore SIGHUP, instead of quitting.

[](#Documentation/git-config.txt-credentialStorelockTimeoutMS)credentialStore.lockTimeoutMS

The length of time, in milliseconds, for git-credential-store to retry when trying to lock the credentials file. A value of 0 means not to retry at all; -1 means to try indefinitely. Default is 1000 (i.e., retry for 1s).

[](#Documentation/git-config.txt-diffautoRefreshIndex)`diff.autoRefreshIndex`

When using `git` `diff` to compare with work tree files, do not consider stat-only changes as changed. Instead, silently run `git` `update-index` `--refresh` to update the cached stat information for paths whose contents in the work tree match the contents in the index. This option defaults to `true`. Note that this affects only `git` `diff` Porcelain, and not lower level `diff` commands such as `git` `diff-files`.

[](#Documentation/git-config.txt-diffdirstat)`diff.dirstat`

A comma separated list of `--dirstat` parameters specifying the default behavior of the `--dirstat` option to [git-diff\[1\]](https://git-scm.com/docs/git-diff) and friends. The defaults can be overridden on the command line (using `--dirstat=`*&lt;param&gt;*`,...`). The fallback defaults (when not changed by `diff.dirstat`) are `changes,noncumulative,3`. The following parameters are available:

[](#Documentation/git-config.txt-changes)`changes`

Compute the dirstat numbers by counting the lines that have been removed from the source, or added to the destination. This ignores the amount of pure code movements within a file. In other words, rearranging lines in a file is not counted as much as other changes. This is the default behavior when no parameter is given.

[](#Documentation/git-config.txt-lines)`lines`

Compute the dirstat numbers by doing the regular line-based diff analysis, and summing the removed/added line counts. (For binary files, count 64-byte chunks instead, since binary files have no natural concept of lines). This is a more expensive `--dirstat` behavior than the `changes` behavior, but it does count rearranged lines within a file as much as other changes. The resulting output is consistent with what you get from the other `--*stat` options.

[](#Documentation/git-config.txt-files)`files`

Compute the dirstat numbers by counting the number of files changed. Each changed file counts equally in the dirstat analysis. This is the computationally cheapest `--dirstat` behavior, since it does not have to look at the file contents at all.

[](#Documentation/git-config.txt-cumulative)`cumulative`

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
