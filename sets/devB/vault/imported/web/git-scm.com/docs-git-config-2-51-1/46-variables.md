---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#46-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-46-variables
type: reference
title: Git - git-config Documentation › Variables (40/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#46-variables
source_hash: b8cc623d4c8f2ec74ec9f93595cb11e22a91ac8db4adfe0911a629c497bba7e5
---
When true, Git will include a "lookup table" section in the bitmap index (if one is written). This table is used to defer loading individual bitmaps as late as possible. This can be beneficial in repositories that have relatively large bitmap indexes. Defaults to false.

[](#Documentation/git-config.txt-packreadReverseIndex)pack.readReverseIndex

When true, git will read any .rev file(s) that may be available (see: [gitformat-pack\[5\]](https://git-scm.com/docs/gitformat-pack)). When false, the reverse index will be generated from scratch and stored in memory. Defaults to true.

[](#Documentation/git-config.txt-packwriteReverseIndex)pack.writeReverseIndex

When true, git will write a corresponding .rev file (see: [gitformat-pack\[5\]](https://git-scm.com/docs/gitformat-pack)) for each new packfile that it writes in all places except for [git-fast-import\[1\]](https://git-scm.com/docs/git-fast-import) and in the bulk checkin mechanism. Defaults to true.

If the value is boolean, turns on or off pagination of the output of a particular Git subcommand when writing to a tty. Otherwise, turns on pagination for the subcommand using the pager specified by the value of `pager.`*&lt;cmd&gt;*. If `--paginate` or `--no-pager` is specified on the command line, it takes precedence over this option. To disable pagination for all commands, set `core.pager` or `GIT_PAGER` to `cat`.

[](#Documentation/git-config.txt-prettyname)pretty.&lt;name&gt;

Alias for a --pretty= format string, as specified in [git-log\[1\]](https://git-scm.com/docs/git-log). Any aliases defined here can be used just as the built-in pretty formats could. For example, running `git` `config` `pretty.changelog` `"format:*` `%H` `%s"` would cause the invocation `git` `log` `--pretty=changelog` to be equivalent to running `git` `log` `"--pretty=format:*` `%H` `%s"`. Note that an alias with the same name as a built-in format will be silently ignored.

[](#Documentation/git-config.txt-promisorquiet)promisor.quiet

If set to "true" assume `--quiet` when fetching additional objects for a partial clone.

[](#Documentation/git-config.txt-promisoradvertise)promisor.advertise

If set to "true", a server will use the "promisor-remote" capability, see [gitprotocol-v2\[5\]](https://git-scm.com/docs/gitprotocol-v2), to advertise the promisor remotes it is using, if it uses some. Default is "false", which means the "promisor-remote" capability is not advertised.

[](#Documentation/git-config.txt-promisoracceptFromServer)promisor.acceptFromServer

If set to "all", a client will accept all the promisor remotes a server might advertise using the "promisor-remote" capability. If set to "knownName" the client will accept promisor remotes which are already configured on the client and have the same name as those advertised by the client. This is not very secure, but could be used in a corporate setup where servers and clients are trusted to not switch name and URLs. If set to "knownUrl", the client will accept promisor remotes which have both the same name and the same URL configured on the client as the name and URL advertised by the server. This is more secure than "all" or "knownName", so it should be used if possible instead of those options. Default is "none", which means no promisor remote advertised by a server will be accepted. By accepting a promisor remote, the client agrees that the server might omit objects that are lazily fetchable from this promisor remote from its responses to "fetch" and "clone" requests from the client. Name and URL comparisons are case sensitive. See [gitprotocol-v2\[5\]](https://git-scm.com/docs/gitprotocol-v2).

[](#Documentation/git-config.txt-protocolallow)protocol.allow

If set, provide a user defined default policy for all protocols which don’t explicitly have a policy (`protocol.`*&lt;name&gt;*`.allow`). By default, if unset, known-safe protocols (http, https, git, ssh) have a default policy of `always`, known-dangerous protocols (ext) have a default policy of `never`, and all other protocols (including file) have a default policy of `user`. Supported policies:

- `always` - protocol is always able to be used.
- `never` - protocol is never able to be used.
- `user` - protocol is only able to be used when `GIT_PROTOCOL_FROM_USER` is either unset or has a value of 1. This policy should be used when you want a protocol to be directly usable by the user but don’t want it used by commands which execute clone/fetch/push commands without user input, e.g. recursive submodule initialization.

[](#Documentation/git-config.txt-protocolnameallow)protocol.&lt;name&gt;.allow

Set a policy to be used by protocol *&lt;name&gt;* with clone/fetch/push commands. See `protocol.allow` above for the available policies.

The protocol names currently used by git are:

- `file`: any local file-based path (including `file://` URLs, or local paths)
- `git`: the anonymous git protocol over a direct TCP connection (or proxy, if configured)
- `ssh`: git over ssh (including `host:path` syntax, `ssh://`, etc).
- `http`: git over http, both "smart http" and "dumb http". Note that this does *not* include `https`; if you want to configure both, you must do so individually.
- any external helpers are named by their protocol (e.g., use `hg` to allow the `git-remote-hg` helper)

[](#Documentation/git-config.txt-protocolversion)protocol.version

If set, clients will attempt to communicate with a server using the specified protocol version. If the server does not support it, communication falls back to version 0. If unset, the default is `2`. Supported versions:

- `0` - the original wire protocol.
- `1` - the original wire protocol with the addition of a version string in the initial response from the server.
- `2` - Wire protocol version 2, see [gitprotocol-v2\[5\]](https://git-scm.com/docs/gitprotocol-v2).

[](#Documentation/git-config.txt-pullff)pull.ff

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
