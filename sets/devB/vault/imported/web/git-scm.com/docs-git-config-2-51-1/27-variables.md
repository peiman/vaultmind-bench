---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#27-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-27-variables
type: reference
title: Git - git-config Documentation › Variables (21/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#27-variables
source_hash: c14a9605dd2487ab3f67428ba7b8b3ceab150893d961122ec5a8c13e18765d0a
---
Acts like `fsck.skipList`, but is used by [git-fetch-pack\[1\]](https://git-scm.com/docs/git-fetch-pack) instead of [git-fsck\[1\]](https://git-scm.com/docs/git-fsck). See the `fsck.skipList` documentation for details.

[](#Documentation/git-config.txt-fetchunpackLimit)fetch.unpackLimit

If the number of objects fetched over the Git native transfer is below this limit, then the objects will be unpacked into loose object files. However if the number of received objects equals or exceeds this limit then the received pack will be stored as a pack, after adding any missing delta bases. Storing the pack from a push can make the push operation complete faster, especially on slow filesystems. If not set, the value of `transfer.unpackLimit` is used instead.

[](#Documentation/git-config.txt-fetchprune)fetch.prune

If true, fetch will automatically behave as if the `--prune` option was given on the command line. See also `remote.`*&lt;name&gt;*`.prune` and the PRUNING section of [git-fetch\[1\]](https://git-scm.com/docs/git-fetch).

[](#Documentation/git-config.txt-fetchpruneTags)fetch.pruneTags

If true, fetch will automatically behave as if the `refs/tags/*:refs/tags/*` refspec was provided when pruning, if not set already. This allows for setting both this option and `fetch.prune` to maintain a 1=1 mapping to upstream refs. See also `remote.`*&lt;name&gt;*`.pruneTags` and the PRUNING section of [git-fetch\[1\]](https://git-scm.com/docs/git-fetch).

[](#Documentation/git-config.txt-fetchall)fetch.all

If true, fetch will attempt to update all available remotes. This behavior can be overridden by passing `--no-all` or by explicitly specifying one or more remote(s) to fetch from. Defaults to false.

[](#Documentation/git-config.txt-fetchoutput)fetch.output

Control how ref update status is printed. Valid values are `full` and `compact`. Default value is `full`. See the OUTPUT section in [git-fetch\[1\]](https://git-scm.com/docs/git-fetch) for details.

[](#Documentation/git-config.txt-fetchnegotiationAlgorithm)fetch.negotiationAlgorithm

Control how information about the commits in the local repository is sent when negotiating the contents of the packfile to be sent by the server. Set to "consecutive" to use an algorithm that walks over consecutive commits checking each one. Set to "skipping" to use an algorithm that skips commits in an effort to converge faster, but may result in a larger-than-necessary packfile; or set to "noop" to not send any information at all, which will almost certainly result in a larger-than-necessary packfile, but will skip the negotiation step. Set to "default" to override settings made previously and use the default behaviour. The default is normally "consecutive", but if `feature.experimental` is true, then the default is "skipping". Unknown values will cause *git fetch* to error out.

See also the `--negotiate-only` and `--negotiation-tip` options to [git-fetch\[1\]](https://git-scm.com/docs/git-fetch).

[](#Documentation/git-config.txt-fetchshowForcedUpdates)fetch.showForcedUpdates

Set to false to enable `--no-show-forced-updates` in [git-fetch\[1\]](https://git-scm.com/docs/git-fetch) and [git-pull\[1\]](https://git-scm.com/docs/git-pull) commands. Defaults to true.

[](#Documentation/git-config.txt-fetchparallel)fetch.parallel

Specifies the maximal number of fetch operations to be run in parallel at a time (submodules, or remotes when the `--multiple` option of [git-fetch\[1\]](https://git-scm.com/docs/git-fetch) is in effect).

A value of 0 will give some reasonable default. If unset, it defaults to 1.

For submodules, this setting can be overridden using the `submodule.fetchJobs` config setting.

[](#Documentation/git-config.txt-fetchwriteCommitGraph)fetch.writeCommitGraph

Set to true to write a commit-graph after every `git` `fetch` command that downloads a pack-file from a remote. Using the `--split` option, most executions will create a very small commit-graph file on top of the existing commit-graph file(s). Occasionally, these files will merge and the write may take longer. Having an updated commit-graph file helps performance of many Git commands, including `git` `merge-base`, `git` `push` `-f`, and `git` `log` `--graph`. Defaults to false.

[](#Documentation/git-config.txt-fetchbundleURI)fetch.bundleURI

This value stores a URI for downloading Git object data from a bundle URI before performing an incremental fetch from the origin Git server. This is similar to how the `--bundle-uri` option behaves in [git-clone\[1\]](https://git-scm.com/docs/git-clone). `git` `clone` `--bundle-uri` will set the `fetch.bundleURI` value if the supplied bundle URI contains a bundle list that is organized for incremental fetches.

If you modify this value and your repository has a `fetch.bundleCreationToken` value, then remove that `fetch.bundleCreationToken` value before fetching from the new bundle URI.

[](#Documentation/git-config.txt-fetchbundleCreationToken)fetch.bundleCreationToken

When using `fetch.bundleURI` to fetch incrementally from a bundle list that uses the "creationToken" heuristic, this config value stores the maximum `creationToken` value of the downloaded bundles. This value is used to prevent downloading bundles in the future if the advertised `creationToken` is not strictly larger than this value.

The creation token values are chosen by the provider serving the specific bundle URI. If you modify the URI at `fetch.bundleURI`, then be sure to remove the value for the `fetch.bundleCreationToken` value before fetching.

[](#Documentation/git-config.txt-filterdriverclean)filter.&lt;driver&gt;.clean

The command which is used to convert the content of a worktree file to a blob upon checkin. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-filterdriversmudge)filter.&lt;driver&gt;.smudge

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
