---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#21-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-21-variables
type: reference
title: Git - git-config Documentation › Variables (15/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#21-variables
source_hash: 2262d014f9014ad4286823c3eb7dbcfc73a4745737426df83dc768c185579b30
---
The empty string resets the fsync configuration to the platform default. The default on most platforms is equivalent to `core.fsync=committed,-loose-object`, which has good performance, but risks losing recent work in the event of an unclean system shutdown.

- `none` clears the set of fsynced components.
- `loose-object` hardens objects added to the repo in loose-object form.
- `pack` hardens objects added to the repo in packfile form.
- `pack-metadata` hardens packfile bitmaps and indexes.
- `commit-graph` hardens the commit-graph file.
- `index` hardens the index when it is modified.
- `objects` is an aggregate option that is equivalent to `loose-object,pack`.
- `reference` hardens references modified in the repo.
- `derived-metadata` is an aggregate option that is equivalent to `pack-metadata,commit-graph`.
- `committed` is an aggregate option that is currently equivalent to `objects`. This mode sacrifices some performance to ensure that work that is committed to the repository with `git` `commit` or similar commands is hardened.
- `added` is an aggregate option that is currently equivalent to `committed,index`. This mode sacrifices additional performance to ensure that the results of commands like `git` `add` and similar operations are hardened.
- `all` is an aggregate option that syncs all individual components above.

[](#Documentation/git-config.txt-corefsyncMethod)core.fsyncMethod

A value indicating the strategy Git will use to harden repository data using fsync and related primitives.

- `fsync` uses the fsync() system call or platform equivalents.
- `writeout-only` issues pagecache writeback requests, but depending on the filesystem and storage hardware, data added to the repository may not be durable in the event of a system crash. This is the default mode on macOS.
- `batch` enables a mode that uses writeout-only flushes to stage multiple updates in the disk writeback cache and then does a single full fsync of a dummy file to trigger the disk cache flush at the end of the operation.

Currently `batch` mode only applies to loose-object files. Other repository data is made durable as if `fsync` was specified. This mode is expected to be as safe as `fsync` on macOS for repos stored on HFS+ or APFS filesystems and on Windows for repos stored on NTFS or ReFS filesystems.

[](#Documentation/git-config.txt-corefsyncObjectFiles)core.fsyncObjectFiles

This boolean will enable *fsync()* when writing object files. This setting is deprecated. Use core.fsync instead.

This setting affects data added to the Git repository in loose-object form. When set to true, Git will issue an fsync or similar system call to flush caches so that loose-objects remain consistent in the face of a unclean system shutdown.

[](#Documentation/git-config.txt-corepreloadIndex)core.preloadIndex

Enable parallel index preload for operations like *git diff*

This can speed up operations like *git diff* and *git status* especially on filesystems like NFS that have weak caching semantics and thus relatively high IO latencies. When enabled, Git will do the index comparison to the filesystem data in parallel, allowing overlapping IO’s. Defaults to true.

[](#Documentation/git-config.txt-coreunsetenvvars)core.unsetenvvars

Windows-only: comma-separated list of environment variables' names that need to be unset before spawning any other process. Defaults to `PERL5LIB` to account for the fact that Git for Windows insists on using its own Perl interpreter.

[](#Documentation/git-config.txt-corecreateObject)core.createObject

You can set this to *link*, in which case a hardlink followed by a delete of the source are used to make sure that object creation will not overwrite existing objects.

On some file system/operating system combinations, this is unreliable. Set this config setting to *rename* there; however, this will remove the check that makes sure that existing object files will not get overwritten.

[](#Documentation/git-config.txt-corenotesRef)core.notesRef

When showing commit messages, also show notes which are stored in the given ref. The ref must be fully qualified. If the given ref does not exist, it is not an error but means that no notes should be printed.

This setting defaults to "refs/notes/commits", and it can be overridden by the `GIT_NOTES_REF` environment variable. See [git-notes\[1\]](https://git-scm.com/docs/git-notes).

[](#Documentation/git-config.txt-corecommitGraph)core.commitGraph

If true, then git will read the commit-graph file (if it exists) to parse the graph structure of commits. Defaults to true. See [git-commit-graph\[1\]](https://git-scm.com/docs/git-commit-graph) for more information.

[](#Documentation/git-config.txt-coreuseReplaceRefs)core.useReplaceRefs

If set to `false`, behave as if the `--no-replace-objects` option was given on the command line. See [git\[1\]](https://git-scm.com/docs/git) and [git-replace\[1\]](https://git-scm.com/docs/git-replace) for more information.

[](#Documentation/git-config.txt-coremultiPackIndex)core.multiPackIndex

Use the multi-pack-index file to track multiple packfiles using a single index. See [git-multi-pack-index\[1\]](https://git-scm.com/docs/git-multi-pack-index) for more information. Defaults to true.

[](#Documentation/git-config.txt-coresparseCheckout)core.sparseCheckout

Enable "sparse checkout" feature. See [git-sparse-checkout\[1\]](https://git-scm.com/docs/git-sparse-checkout) for more information.

[](#Documentation/git-config.txt-coresparseCheckoutCone)core.sparseCheckoutCone

Enables the "cone mode" of the sparse checkout feature. When the sparse-checkout file contains a limited set of patterns, this mode provides significant performance advantages. The "non-cone mode" can be requested to allow specifying more flexible patterns by setting this variable to *false*. See [git-sparse-checkout\[1\]](https://git-scm.com/docs/git-sparse-checkout) for more information.

[](#Documentation/git-config.txt-coreabbrev)core.abbrev

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
