---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#44-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-44-variables
type: reference
title: Git - git-config Documentation › Variables (38/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#44-variables
source_hash: 45b7c344a76a8bb758de1cfbb9620ec44c9bac43652a89df231b9c4741b00552
---
When rewriting commits with *&lt;command&gt;* (currently `amend` or `rebase`), if this variable is `false`, git will not copy notes from the original to the rewritten commit. Defaults to `true`. See also `notes.rewriteRef` below.

This setting can be overridden with the `GIT_NOTES_REWRITE_REF` environment variable, which must be a colon separated list of refs or globs.

[](#Documentation/git-config.txt-notesrewriteMode)`notes.rewriteMode`

When copying notes during a rewrite (see the `notes.rewrite.`*&lt;command&gt;* option), determines what to do if the target commit already has a note. Must be one of `overwrite`, `concatenate`, `cat_sort_uniq`, or `ignore`. Defaults to `concatenate`.

This setting can be overridden with the `GIT_NOTES_REWRITE_MODE` environment variable.

[](#Documentation/git-config.txt-notesrewriteRef)`notes.rewriteRef`

When copying notes during a rewrite, specifies the (fully qualified) ref whose notes should be copied. May be a glob, in which case notes in all matching refs will be copied. You may also specify this configuration several times.

Does not have a default value; you must configure this variable to enable note rewriting. Set it to `refs/notes/commits` to enable rewriting for the default commit notes.

Can be overridden with the `GIT_NOTES_REWRITE_REF` environment variable. See `notes.rewrite.`*&lt;command&gt;* above for a further description of its format.

[](#Documentation/git-config.txt-packwindow)pack.window

The size of the window used by [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects) when no window size is given on the command line. Defaults to 10.

[](#Documentation/git-config.txt-packdepth)pack.depth

The maximum delta depth used by [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects) when no maximum depth is given on the command line. Defaults to 50. Maximum value is 4095.

[](#Documentation/git-config.txt-packwindowMemory)pack.windowMemory

The maximum size of memory that is consumed by each thread in [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects) for pack window memory when no limit is given on the command line. The value can be suffixed with "k", "m", or "g". When left unconfigured (or set explicitly to 0), there will be no limit.

[](#Documentation/git-config.txt-packcompression)pack.compression

An integer -1..9, indicating the compression level for objects in a pack file. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If not set, defaults to core.compression. If that is not set, defaults to -1, the zlib default, which is "a default compromise between speed and compression (currently equivalent to level 6)."

Note that changing the compression level will not automatically recompress all existing objects. You can force recompression by passing the -F option to [git-repack\[1\]](https://git-scm.com/docs/git-repack).

[](#Documentation/git-config.txt-packallowPackReuse)pack.allowPackReuse

When true or "single", and when reachability bitmaps are enabled, pack-objects will try to send parts of the bitmapped packfile verbatim. When "multi", and when a multi-pack reachability bitmap is available, pack-objects will try to send parts of all packs in the MIDX.

If only a single pack bitmap is available, and `pack.allowPackReuse` is set to "multi", reuse parts of just the bitmapped packfile. This can reduce memory and CPU usage to serve fetches, but might result in sending a slightly larger pack. Defaults to true.

[](#Documentation/git-config.txt-packisland)pack.island

An extended regular expression configuring a set of delta islands. See "DELTA ISLANDS" in [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects) for details.

[](#Documentation/git-config.txt-packislandCore)pack.islandCore

Specify an island name which gets to have its objects be packed first. This creates a kind of pseudo-pack at the front of one pack, so that the objects from the specified island are hopefully faster to copy into any pack that should be served to a user requesting these objects. In practice this means that the island specified should likely correspond to what is the most commonly cloned in the repo. See also "DELTA ISLANDS" in [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects).

[](#Documentation/git-config.txt-packdeltaCacheSize)pack.deltaCacheSize

The maximum memory in bytes used for caching deltas in [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects) before writing them out to a pack. This cache is used to speed up the writing object phase by not having to recompute the final delta result once the best match for all objects is found. Repacking large repositories on machines which are tight with memory might be badly impacted by this though, especially if this cache pushes the system into swapping. A value of 0 means no limit. The smallest size of 1 byte may be used to virtually disable this cache. Defaults to 256 MiB.

[](#Documentation/git-config.txt-packdeltaCacheLimit)pack.deltaCacheLimit

The maximum size of a delta, that is cached in [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects). This cache is used to speed up the writing object phase by not having to recompute the final delta result once the best match for all objects is found. Defaults to 1000. Maximum value is 65535.

[](#Documentation/git-config.txt-packthreads)pack.threads

Specifies the number of threads to spawn when searching for best delta matches. This requires that [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects) be compiled with pthreads otherwise this option is ignored with a warning. This is meant to reduce packing time on multiprocessor machines. The required amount of memory for the delta search window is however multiplied by the number of threads. Specifying 0 will cause Git to auto-detect the number of CPUs and set the number of threads accordingly.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
