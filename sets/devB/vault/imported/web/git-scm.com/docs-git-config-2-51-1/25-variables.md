---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#25-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-25-variables
type: reference
title: Git - git-config Documentation › Variables (19/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#25-variables
source_hash: af654758d2ae5fad5c3fea12e858f0ed4cb79c34292c7bea9e754227859f15af
---
Controls which diff tool is used by [git-difftool\[1\]](https://git-scm.com/docs/git-difftool) when the -g/--gui flag is specified. This variable overrides the value configured in `merge.guitool`. The list below shows the valid built-in values. Any other value is treated as a custom diff tool and requires that a corresponding difftool.&lt;guitool&gt;.cmd variable is defined.

- araxis
- bc
- codecompare
- deltawalker
- diffmerge
- diffuse
- ecmerge
- emerge
- examdiff
- guiffy
- gvimdiff
- kdiff3
- kompare
- meld
- nvimdiff
- opendiff
- p4merge
- smerge
- tkdiff
- vimdiff
- vscode
- winmerge
- xxdiff

[](#Documentation/git-config.txt-difftooltoolcmd)difftool.&lt;tool&gt;.cmd

Specify the command to invoke the specified diff tool. The specified command is evaluated in shell with the following variables available: *LOCAL* is set to the name of the temporary file containing the contents of the diff pre-image and *REMOTE* is set to the name of the temporary file containing the contents of the diff post-image.

See the `--tool=`*&lt;tool&gt;* option in [git-difftool\[1\]](https://git-scm.com/docs/git-difftool) for more details.

[](#Documentation/git-config.txt-difftooltoolpath)difftool.&lt;tool&gt;.path

Override the path for the given tool. This is useful in case your tool is not in the PATH.

[](#Documentation/git-config.txt-difftooltrustExitCode)difftool.trustExitCode

Exit difftool if the invoked diff tool returns a non-zero exit status.

See the `--trust-exit-code` option in [git-difftool\[1\]](https://git-scm.com/docs/git-difftool) for more details.

[](#Documentation/git-config.txt-difftoolprompt)difftool.prompt

Prompt before each invocation of the diff tool.

[](#Documentation/git-config.txt-difftoolguiDefault)difftool.guiDefault

Set `true` to use the `diff.guitool` by default (equivalent to specifying the `--gui` argument), or `auto` to select `diff.guitool` or `diff.tool` depending on the presence of a `DISPLAY` environment variable value. The default is `false`, where the `--gui` argument must be provided explicitly for the `diff.guitool` to be used.

[](#Documentation/git-config.txt-extensions)extensions.*

Unless otherwise stated, is an error to specify an extension if `core.repositoryFormatVersion` is not `1`. See [gitrepository-layout\[5\]](https://git-scm.com/docs/gitrepository-layout).

[](#Documentation/git-config.txt-compatObjectFormat)compatObjectFormat

Specify a compatibility hash algorithm to use. The acceptable values are `sha1` and `sha256`. The value specified must be different from the value of `extensions.objectFormat`. This allows client level interoperability between git repositories whose objectFormat matches this compatObjectFormat. In particular when fully implemented the pushes and pulls from a repository in whose objectFormat matches compatObjectFormat. As well as being able to use oids encoded in compatObjectFormat in addition to oids encoded with objectFormat to locally specify objects.

Note that the functionality enabled by this extension is incomplete and subject to change. It currently exists only to allow development and testing of the underlying feature and is not designed to be enabled by end users.

[](#Documentation/git-config.txt-noop)noop

This extension does not change git’s behavior at all. It is useful only for testing format-1 compatibility.

For historical reasons, this extension is respected regardless of the `core.repositoryFormatVersion` setting.

[](#Documentation/git-config.txt-noop-v1)noop-v1

This extension does not change git’s behavior at all. It is useful only for testing format-1 compatibility.

[](#Documentation/git-config.txt-objectFormat)objectFormat

Specify the hash algorithm to use. The acceptable values are `sha1` and `sha256`. If not specified, `sha1` is assumed.

Note that this setting should only be set by [git-init\[1\]](https://git-scm.com/docs/git-init) or [git-clone\[1\]](https://git-scm.com/docs/git-clone). Trying to change it after initialization will not work and will produce hard-to-diagnose issues.

[](#Documentation/git-config.txt-partialClone)partialClone

When enabled, indicates that the repo was created with a partial clone (or later performed a partial fetch) and that the remote may have omitted sending certain unwanted objects. Such a remote is called a "promisor remote" and it promises that all such omitted objects can be fetched from it in the future.

The value of this key is the name of the promisor remote.

For historical reasons, this extension is respected regardless of the `core.repositoryFormatVersion` setting.

[](#Documentation/git-config.txt-preciousObjects)preciousObjects

If enabled, indicates that objects in the repository MUST NOT be deleted (e.g., by `git-prune` or `git` `repack` `-d`).

For historical reasons, this extension is respected regardless of the `core.repositoryFormatVersion` setting.

[](#Documentation/git-config.txt-refStorage)refStorage

Specify the ref storage format to use. The acceptable values are:

- `files` for loose files with packed-refs. This is the default.
- `reftable` for the reftable format. This format is experimental and its internals are subject to change.

Note that this setting should only be set by [git-init\[1\]](https://git-scm.com/docs/git-init) or [git-clone\[1\]](https://git-scm.com/docs/git-clone). Trying to change it after initialization will not work and will produce hard-to-diagnose issues.

[](#Documentation/git-config.txt-relativeWorktrees)relativeWorktrees

If enabled, indicates at least one worktree has been linked with relative paths. Automatically set if a worktree has been created or repaired with either the `--relative-paths` option or with the `worktree.useRelativePaths` config set to `true`.

[](#Documentation/git-config.txt-worktreeConfig)worktreeConfig

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
