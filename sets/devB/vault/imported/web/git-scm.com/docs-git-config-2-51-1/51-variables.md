---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#51-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-51-variables
type: reference
title: Git - git-config Documentation › Variables (45/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#51-variables
source_hash: bc29051672e152e59a486920e35448eb157afbf0a4e801e615a86bd66685aa08
---
[](#Documentation/git-config.txt-remotenameproxy)remote.&lt;name&gt;.proxy

For remotes that require curl (http, https and ftp), the URL to the proxy to use for that remote. Set to the empty string to disable proxying for that remote.

[](#Documentation/git-config.txt-remotenameproxyAuthMethod)remote.&lt;name&gt;.proxyAuthMethod

For remotes that require curl (http, https and ftp), the method to use for authenticating against the proxy in use (probably set in `remote.`*&lt;name&gt;*`.proxy`). See `http.proxyAuthMethod`.

[](#Documentation/git-config.txt-remotenamefetch)remote.&lt;name&gt;.fetch

The default set of "refspec" for [git-fetch\[1\]](https://git-scm.com/docs/git-fetch). See [git-fetch\[1\]](https://git-scm.com/docs/git-fetch).

[](#Documentation/git-config.txt-remotenamepush)remote.&lt;name&gt;.push

The default set of "refspec" for [git-push\[1\]](https://git-scm.com/docs/git-push). See [git-push\[1\]](https://git-scm.com/docs/git-push).

[](#Documentation/git-config.txt-remotenamemirror)remote.&lt;name&gt;.mirror

If true, pushing to this remote will automatically behave as if the `--mirror` option was given on the command line.

[](#Documentation/git-config.txt-remotenameskipDefaultUpdate)remote.&lt;name&gt;.skipDefaultUpdate

A deprecated synonym to `remote.`*&lt;name&gt;*`.skipFetchAll` (if both are set in the configuration files with different values, the value of the last occurrence will be used).

[](#Documentation/git-config.txt-remotenameskipFetchAll)remote.&lt;name&gt;.skipFetchAll

If true, this remote will be skipped when updating using [git-fetch\[1\]](https://git-scm.com/docs/git-fetch), the `update` subcommand of [git-remote\[1\]](https://git-scm.com/docs/git-remote), and ignored by the prefetch task of `git` `maintenance`.

[](#Documentation/git-config.txt-remotenamereceivepack)remote.&lt;name&gt;.receivepack

The default program to execute on the remote side when pushing. See option --receive-pack of [git-push\[1\]](https://git-scm.com/docs/git-push).

[](#Documentation/git-config.txt-remotenameuploadpack)remote.&lt;name&gt;.uploadpack

The default program to execute on the remote side when fetching. See option --upload-pack of [git-fetch-pack\[1\]](https://git-scm.com/docs/git-fetch-pack).

[](#Documentation/git-config.txt-remotenametagOpt)remote.&lt;name&gt;.tagOpt

Setting this value to --no-tags disables automatic tag following when fetching from remote &lt;name&gt;. Setting it to --tags will fetch every tag from remote &lt;name&gt;, even if they are not reachable from remote branch heads. Passing these flags directly to [git-fetch\[1\]](https://git-scm.com/docs/git-fetch) can override this setting. See options --tags and --no-tags of [git-fetch\[1\]](https://git-scm.com/docs/git-fetch).

[](#Documentation/git-config.txt-remotenamevcs)remote.&lt;name&gt;.vcs

Setting this to a value &lt;vcs&gt; will cause Git to interact with the remote with the git-remote-&lt;vcs&gt; helper.

[](#Documentation/git-config.txt-remotenameprune)remote.&lt;name&gt;.prune

When set to true, fetching from this remote by default will also remove any remote-tracking references that no longer exist on the remote (as if the `--prune` option was given on the command line). Overrides `fetch.prune` settings, if any.

[](#Documentation/git-config.txt-remotenamepruneTags)remote.&lt;name&gt;.pruneTags

When set to true, fetching from this remote by default will also remove any local tags that no longer exist on the remote if pruning is activated in general via `remote.`*&lt;name&gt;*`.prune`, `fetch.prune` or `--prune`. Overrides `fetch.pruneTags` settings, if any.

See also `remote.`*&lt;name&gt;*`.prune` and the PRUNING section of [git-fetch\[1\]](https://git-scm.com/docs/git-fetch).

[](#Documentation/git-config.txt-remotenamepromisor)remote.&lt;name&gt;.promisor

When set to true, this remote will be used to fetch promisor objects.

[](#Documentation/git-config.txt-remotenamepartialclonefilter)remote.&lt;name&gt;.partialclonefilter

The filter that will be applied when fetching from this promisor remote. Changing or clearing this value will only affect fetches for new commits. To fetch associated objects for commits already present in the local object database, use the `--refetch` option of [git-fetch\[1\]](https://git-scm.com/docs/git-fetch).

[](#Documentation/git-config.txt-remotenameserverOption)remote.&lt;name&gt;.serverOption

The default set of server options used when fetching from this remote. These server options can be overridden by the `--server-option=` command line arguments.

This is a multi-valued variable, and an empty value can be used in a higher priority configuration file (e.g. `.git/config` in a repository) to clear the values inherited from a lower priority configuration files (e.g. `$HOME/.gitconfig`).

[](#Documentation/git-config.txt-remotenamefollowRemoteHEAD)remote.&lt;name&gt;.followRemoteHEAD

How [git-fetch\[1\]](https://git-scm.com/docs/git-fetch) should handle updates to `remotes/`*&lt;name&gt;*`/HEAD` when fetching using the configured refspecs of a remote. The default value is "create", which will create `remotes/`*&lt;name&gt;*`/HEAD` if it exists on the remote, but not locally; this will not touch an already existing local reference. Setting it to "warn" will print a message if the remote has a different value than the local one; in case there is no local reference, it behaves like "create". A variant on "warn" is "warn-if-not-$branch", which behaves like "warn", but if `HEAD` on the remote is `$branch` it will be silent. Setting it to "always" will silently update `remotes/`*&lt;name&gt;*`/HEAD` to the value on the remote. Finally, setting it to "never" will never change or create the local reference.

[](#Documentation/git-config.txt-remotesgroup)remotes.&lt;group&gt;

The list of remotes which are fetched by "git remote update &lt;group&gt;". See [git-remote\[1\]](https://git-scm.com/docs/git-remote).

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
