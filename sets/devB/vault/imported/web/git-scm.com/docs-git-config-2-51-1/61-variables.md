---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#61-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-61-variables
type: reference
title: Git - git-config Documentation › Variables (55/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#61-variables
source_hash: c82c333ee322a90c1fab7a89af220e7511a61817b20587ba8a720f5496fded2a
---
If this option is set, when `upload-pack` would run `git` `pack-objects` to create a packfile for a client, it will run this shell command instead. The `pack-objects` command and arguments it *would* have run (including the `git` `pack-objects` at the beginning) are appended to the shell command. The stdin and stdout of the hook are treated as if `pack-objects` itself was run. I.e., `upload-pack` will feed input intended for `pack-objects` to the hook, and expects a completed packfile on stdout.

Note that this configuration variable is only respected when it is specified in protected configuration (see [SCOPES](#SCOPES)). This is a safety measure against fetching from untrusted repositories.

[](#Documentation/git-config.txt-uploadpackallowFilter)uploadpack.allowFilter

If this option is set, `upload-pack` will support partial clone and partial fetch object filtering.

[](#Documentation/git-config.txt-uploadpackfilterallow)uploadpackfilter.allow

Provides a default value for unspecified object filters (see: the below configuration variable). If set to `true`, this will also enable all filters which get added in the future. Defaults to `true`.

[](#Documentation/git-config.txt-uploadpackfilterfilterallow)uploadpackfilter.&lt;filter&gt;.allow

Explicitly allow or ban the object filter corresponding to *&lt;filter&gt;*, where *&lt;filter&gt;* may be one of: `blob:none`, `blob:limit`, `object:type`, `tree`, `sparse:oid`, or `combine`. If using combined filters, both `combine` and all of the nested filter kinds must be allowed. Defaults to `uploadpackfilter.allow`.

[](#Documentation/git-config.txt-uploadpackfiltertreemaxDepth)uploadpackfilter.tree.maxDepth

Only allow `--filter=tree:`*&lt;n&gt;* when *&lt;n&gt;* is no more than the value of `uploadpackfilter.tree.maxDepth`. If set, this also implies `uploadpackfilter.tree.allow=true`, unless this configuration variable had already been set. Has no effect if unset.

[](#Documentation/git-config.txt-uploadpackallowRefInWant)uploadpack.allowRefInWant

If this option is set, `upload-pack` will support the `ref-in-want` feature of the protocol version 2 `fetch` command. This feature is intended for the benefit of load-balanced servers which may not have the same view of what OIDs their refs point to due to replication delay.

[](#Documentation/git-config.txt-urlbaseinsteadOf)url.&lt;base&gt;.insteadOf

Any URL that starts with this value will be rewritten to start, instead, with &lt;base&gt;. In cases where some site serves a large number of repositories, and serves them with multiple access methods, and some users need to use different access methods, this feature allows people to specify any of the equivalent URLs and have Git automatically rewrite the URL to the best alternative for the particular user, even for a never-before-seen repository on the site. When more than one insteadOf strings match a given URL, the longest match is used.

Note that any protocol restrictions will be applied to the rewritten URL. If the rewrite changes the URL to use a custom protocol or remote helper, you may need to adjust the `protocol.*.allow` config to permit the request. In particular, protocols you expect to use for submodules must be set to `always` rather than the default of `user`. See the description of `protocol.allow` above.

[](#Documentation/git-config.txt-urlbasepushInsteadOf)url.&lt;base&gt;.pushInsteadOf

Any URL that starts with this value will not be pushed to; instead, it will be rewritten to start with &lt;base&gt;, and the resulting URL will be pushed to. In cases where some site serves a large number of repositories, and serves them with multiple access methods, some of which do not allow push, this feature allows people to specify a pull-only URL and have Git automatically use an appropriate URL to push, even for a never-before-seen repository on the site. When more than one pushInsteadOf strings match a given URL, the longest match is used. If a remote has an explicit pushurl, Git will ignore this setting for that remote.

[](#Documentation/git-config.txt-username)user.name

[](#Documentation/git-config.txt-useremail)user.email

[](#Documentation/git-config.txt-authoremail)author.email

[](#Documentation/git-config.txt-committername)committer.name

[](#Documentation/git-config.txt-committeremail)committer.email

The `user.name` and `user.email` variables determine what ends up in the `author` and `committer` fields of commit objects. If you need the `author` or `committer` to be different, the `author.name`, `author.email`, `committer.name`, or `committer.email` variables can be set. All of these can be overridden by the `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME`, `GIT_COMMITTER_EMAIL`, and `EMAIL` environment variables.

Note that the `name` forms of these variables conventionally refer to some form of a personal name. See [git-commit\[1\]](https://git-scm.com/docs/git-commit) and the environment variables section of [git\[1\]](https://git-scm.com/docs/git) for more information on these settings and the `credential.username` option if you’re looking for authentication credentials instead.

[](#Documentation/git-config.txt-useruseConfigOnly)user.useConfigOnly

Instruct Git to avoid trying to guess defaults for `user.email` and `user.name`, and instead retrieve the values only from the configuration. For example, if you have multiple email addresses and would like to use a different one for each repository, then with this configuration option set to `true` in the global config along with a name, Git will prompt you to set up an email before making new commits in a newly cloned repository. Defaults to `false`.

[](#Documentation/git-config.txt-usersigningKey)user.signingKey

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
