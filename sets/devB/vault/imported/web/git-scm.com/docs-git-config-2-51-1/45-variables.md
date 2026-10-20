---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#45-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-45-variables
type: reference
title: Git - git-config Documentation › Variables (39/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#45-variables
source_hash: 7202432977126a1103f483d03d782d68a98ee6c7dd9fd5b646a0aee25d3bd357
---
[](#Documentation/git-config.txt-packindexVersion)pack.indexVersion

Specify the default pack index version. Valid values are 1 for legacy pack index used by Git versions prior to 1.5.2, and 2 for the new pack index with capabilities for packs larger than 4 GB as well as proper protection against the repacking of corrupted packs. Version 2 is the default. Note that version 2 is enforced and this config option is ignored whenever the corresponding pack is larger than 2 GB.

If you have an old Git that does not understand the version 2 `*.idx` file, cloning or fetching over a non-native protocol (e.g. "http") that will copy both `*.pack` file and corresponding `*.idx` file from the other side may give you a repository that cannot be accessed with your older version of Git. If the `*.pack` file is smaller than 2 GB, however, you can use [git-index-pack\[1\]](https://git-scm.com/docs/git-index-pack) on the \*.pack file to regenerate the `*.idx` file.

[](#Documentation/git-config.txt-packpackSizeLimit)pack.packSizeLimit

The maximum size of a pack. This setting only affects packing to a file when repacking, i.e. the git:// protocol is unaffected. It can be overridden by the `--max-pack-size` option of [git-repack\[1\]](https://git-scm.com/docs/git-repack). Reaching this limit results in the creation of multiple packfiles.

Note that this option is rarely useful, and may result in a larger total on-disk size (because Git will not store deltas between packs) and worse runtime performance (object lookup within multiple packs is slower than a single pack, and optimizations like reachability bitmaps cannot cope with multiple packs).

If you need to actively run Git using smaller packfiles (e.g., because your filesystem does not support large files), this option may help. But if your goal is to transmit a packfile over a medium that supports limited sizes (e.g., removable media that cannot store the whole repository), you are likely better off creating a single large packfile and splitting it using a generic multi-volume archive tool (e.g., Unix `split`).

The minimum size allowed is limited to 1 MiB. The default is unlimited. Common unit suffixes of *k*, *m*, or *g* are supported.

[](#Documentation/git-config.txt-packuseBitmaps)pack.useBitmaps

When true, git will use pack bitmaps (if available) when packing to stdout (e.g., during the server side of a fetch). Defaults to true. You should not generally need to turn this off unless you are debugging pack bitmaps.

[](#Documentation/git-config.txt-packuseBitmapBoundaryTraversal)pack.useBitmapBoundaryTraversal

When true, Git will use an experimental algorithm for computing reachability queries with bitmaps. Instead of building up complete bitmaps for all of the negated tips and then OR-ing them together, consider negated tips with existing bitmaps as additive (i.e. OR-ing them into the result if they exist, ignoring them otherwise), and build up a bitmap at the boundary instead.

When using this algorithm, Git may include too many objects as a result of not opening up trees belonging to certain UNINTERESTING commits. This inexactness matches the non-bitmap traversal algorithm.

In many cases, this can provide a speed-up over the exact algorithm, particularly when there is poor bitmap coverage of the negated side of the query.

[](#Documentation/git-config.txt-packuseSparse)pack.useSparse

When true, git will default to using the *--sparse* option in *git pack-objects* when the *--revs* option is present. This algorithm only walks trees that appear in paths that introduce new objects. This can have significant performance benefits when computing a pack to send a small change. However, it is possible that extra objects are added to the pack-file if the included commits contain certain types of direct renames. Default is `true`.

[](#Documentation/git-config.txt-packusePathWalk)pack.usePathWalk

Enable the `--path-walk` option by default for `git` `pack-objects` processes. See [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects) for full details.

[](#Documentation/git-config.txt-packpreferBitmapTips)pack.preferBitmapTips

When selecting which commits will receive bitmaps, prefer a commit at the tip of any reference that is a suffix of any value of this configuration over any other commits in the "selection window".

Note that setting this configuration to `refs/foo` does not mean that the commits at the tips of `refs/foo/bar` and `refs/foo/baz` will necessarily be selected. This is because commits are selected for bitmaps from within a series of windows of variable length.

If a commit at the tip of any reference which is a suffix of any value of this configuration is seen in a window, it is immediately given preference over any other commit in that window.

[](#Documentation/git-config.txt-packwriteBitmapsdeprecated)pack.writeBitmaps (deprecated)

This is a deprecated synonym for `repack.writeBitmaps`.

[](#Documentation/git-config.txt-packwriteBitmapHashCache)pack.writeBitmapHashCache

When true, git will include a "hash cache" section in the bitmap index (if one is written). This cache can be used to feed git’s delta heuristics, potentially leading to better deltas between bitmapped and non-bitmapped objects (e.g., when serving a fetch between an older, bitmapped pack and objects that have been pushed since the last gc). The downside is that it consumes 4 bytes per object of disk space. Defaults to true.

When writing a multi-pack reachability bitmap, no new namehashes are computed; instead, any namehashes stored in an existing bitmap are permuted into their appropriate location when writing a new bitmap.

[](#Documentation/git-config.txt-packwriteBitmapLookupTable)pack.writeBitmapLookupTable

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
