---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#60-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-60-variables
type: reference
title: Git - git-config Documentation › Variables (54/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#60-variables
source_hash: a72c5c6bd8c907ad11570b6036dc3640303108b3b375202138ee2f258cec0ea9
---
String(s) `receive-pack` and `upload-pack` use to decide which refs to omit from their initial advertisements. Use more than one definition to specify multiple prefix strings. A ref that is under the hierarchies listed in the value of this variable is excluded, and is hidden when responding to `git` `push` or `git` `fetch`. See `receive.hideRefs` and `uploadpack.hideRefs` for program-specific versions of this config.

You may also include a `!` in front of the ref name to negate the entry, explicitly exposing it, even if an earlier entry marked it as hidden. If you have multiple hideRefs values, later entries override earlier ones (and entries in more-specific config files override less-specific ones).

If a namespace is in use, the namespace prefix is stripped from each reference before it is matched against `transfer.hiderefs` patterns. In order to match refs before stripping, add a `^` in front of the ref name. If you combine `!` and `^`, `!` must be specified first.

For example, if `refs/heads/master` is specified in `transfer.hideRefs` and the current namespace is `foo`, then `refs/namespaces/foo/refs/heads/master` is omitted from the advertisements. If `uploadpack.allowRefInWant` is set, `upload-pack` will treat `want-ref` `refs/heads/master` in a protocol v2 `fetch` command as if `refs/namespaces/foo/refs/heads/master` did not exist. `receive-pack`, on the other hand, will still advertise the object id the ref is pointing to without mentioning its name (a so-called ".have" line).

Even if you hide refs, a client may still be able to steal the target objects via the techniques described in the "SECURITY" section of the [gitnamespaces\[7\]](https://git-scm.com/docs/gitnamespaces) man page; it’s best to keep private data in a separate repository.

[](#Documentation/git-config.txt-transferunpackLimit)transfer.unpackLimit

When `fetch.unpackLimit` or `receive.unpackLimit` are not set, the value of this variable is used instead. The default value is 100.

[](#Documentation/git-config.txt-transferadvertiseSID)transfer.advertiseSID

Boolean. When true, client and server processes will advertise their unique session IDs to their remote counterpart. Defaults to false.

[](#Documentation/git-config.txt-transferbundleURI)transfer.bundleURI

When `true`, local `git` `clone` commands will request bundle information from the remote server (if advertised) and download bundles before continuing the clone through the Git protocol. Defaults to `false`.

[](#Documentation/git-config.txt-transferadvertiseObjectInfo)transfer.advertiseObjectInfo

When `true`, the `object-info` capability is advertised by servers. Defaults to false.

[](#Documentation/git-config.txt-uploadarchiveallowUnreachable)uploadarchive.allowUnreachable

If true, allow clients to use `git` `archive` `--remote` to request any tree, whether reachable from the ref tips or not. See the discussion in the "SECURITY" section of [git-upload-archive\[1\]](https://git-scm.com/docs/git-upload-archive) for more details. Defaults to `false`.

[](#Documentation/git-config.txt-uploadpackhideRefs)uploadpack.hideRefs

This variable is the same as `transfer.hideRefs`, but applies only to `upload-pack` (and so affects only fetches, not pushes). An attempt to fetch a hidden ref by `git` `fetch` will fail. See also `uploadpack.allowTipSHA1InWant`.

[](#Documentation/git-config.txt-uploadpackallowTipSHA1InWant)uploadpack.allowTipSHA1InWant

When `uploadpack.hideRefs` is in effect, allow `upload-pack` to accept a fetch request that asks for an object at the tip of a hidden ref (by default, such a request is rejected). See also `uploadpack.hideRefs`. Even if this is false, a client may be able to steal objects via the techniques described in the "SECURITY" section of the [gitnamespaces\[7\]](https://git-scm.com/docs/gitnamespaces) man page; it’s best to keep private data in a separate repository.

[](#Documentation/git-config.txt-uploadpackallowReachableSHA1InWant)uploadpack.allowReachableSHA1InWant

Allow `upload-pack` to accept a fetch request that asks for an object that is reachable from any ref tip. However, note that calculating object reachability is computationally expensive. Defaults to `false`. Even if this is false, a client may be able to steal objects via the techniques described in the "SECURITY" section of the [gitnamespaces\[7\]](https://git-scm.com/docs/gitnamespaces) man page; it’s best to keep private data in a separate repository.

[](#Documentation/git-config.txt-uploadpackallowAnySHA1InWant)uploadpack.allowAnySHA1InWant

Allow `upload-pack` to accept a fetch request that asks for any object at all. It implies `uploadpack.allowTipSHA1InWant` and `uploadpack.allowReachableSHA1InWant`. If set to `true` it will enable both of them, it set to `false` it will disable both of them. By default not set.

[](#Documentation/git-config.txt-uploadpackkeepAlive)uploadpack.keepAlive

When `upload-pack` has started `pack-objects`, there may be a quiet period while `pack-objects` prepares the pack. Normally it would output progress information, but if `--quiet` was used for the fetch, `pack-objects` will output nothing at all until the pack data begins. Some clients and networks may consider the server to be hung and give up. Setting this option instructs `upload-pack` to send an empty keepalive packet every `uploadpack.keepAlive` seconds. Setting this option to 0 disables keepalive packets entirely. The default is 5 seconds.

[](#Documentation/git-config.txt-uploadpackpackObjectsHook)uploadpack.packObjectsHook

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
