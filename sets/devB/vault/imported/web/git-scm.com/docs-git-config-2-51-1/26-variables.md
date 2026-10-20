---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#26-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-26-variables
type: reference
title: Git - git-config Documentation › Variables (20/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#26-variables
source_hash: 0a60959cf1da9c76449653a0b1f93ec2c034efabdaee4e900fdc595908c4eaf0
---
If enabled, then worktrees will load config settings from the `$GIT_DIR/config.worktree` file in addition to the `$GIT_COMMON_DIR/config` file. Note that `$GIT_COMMON_DIR` and `$GIT_DIR` are the same for the main working tree, while other working trees have `$GIT_DIR` equal to `$GIT_COMMON_DIR/worktrees/`*&lt;id&gt;*`/`. The settings in the `config.worktree` file will override settings from any other config files.

When enabling this extension, you must be careful to move certain values from the common config file to the main working tree’s `config.worktree` file, if present:

- `core.worktree` must be moved from `$GIT_COMMON_DIR/config` to `$GIT_COMMON_DIR/config.worktree`.
- If `core.bare` is true, then it must be moved from `$GIT_COMMON_DIR/config` to `$GIT_COMMON_DIR/config.worktree`.

It may also be beneficial to adjust the locations of `core.sparseCheckout` and `core.sparseCheckoutCone` depending on your desire for customizable sparse-checkout settings for each worktree. By default, the `git` `sparse-checkout` builtin enables this extension, assigns these config values on a per-worktree basis, and uses the `$GIT_DIR/info/sparse-checkout` file to specify the sparsity for each worktree independently. See [git-sparse-checkout\[1\]](https://git-scm.com/docs/git-sparse-checkout) for more details.

For historical reasons, this extension is respected regardless of the `core.repositoryFormatVersion` setting.

[](#Documentation/git-config.txt-fastimportunpackLimit)fastimport.unpackLimit

If the number of objects imported by [git-fast-import\[1\]](https://git-scm.com/docs/git-fast-import) is below this limit, then the objects will be unpacked into loose object files. However, if the number of imported objects equals or exceeds this limit, then the pack will be stored as a pack. Storing the pack from a fast-import can make the import operation complete faster, especially on slow filesystems. If not set, the value of `transfer.unpackLimit` is used instead.

[](#Documentation/git-config.txt-feature)feature.*

The config settings that start with `feature.` modify the defaults of a group of other config settings. These groups are created by the Git developer community as recommended defaults and are subject to change. In particular, new config options may be added with different defaults.

[](#Documentation/git-config.txt-featureexperimental)feature.experimental

Enable config options that are new to Git, and are being considered for future defaults. Config settings included here may be added or removed with each release, including minor version updates. These settings may have unintended interactions since they are so new. Please enable this setting if you are interested in providing feedback on experimental features. The new default values are:

- `fetch.negotiationAlgorithm=skipping` may improve fetch negotiation times by skipping more commits at a time, reducing the number of round trips.
- `pack.useBitmapBoundaryTraversal=true` may improve bitmap traversal times by walking fewer objects.
- `pack.allowPackReuse=multi` may improve the time it takes to create a pack by reusing objects from multiple packs instead of just one.
- `pack.usePathWalk` may speed up packfile creation and make the packfiles be significantly smaller in the presence of certain filename collisions with Git’s default name-hash.
- `init.defaultRefFormat=reftable` causes newly initialized repositories to use the reftable format for storing references. This new format solves issues with case-insensitive filesystems, compresses better and performs significantly better with many use cases. Refer to Documentation/technical/reftable.adoc for more information on this new storage format.

[](#Documentation/git-config.txt-featuremanyFiles)feature.manyFiles

Enable config options that optimize for repos with many files in the working directory. With many files, commands such as `git` `status` and `git` `checkout` may be slow and these new defaults improve performance:

- `index.skipHash=true` speeds up index writes by not computing a trailing checksum. Note that this will cause Git versions earlier than 2.13.0 to refuse to parse the index and Git versions earlier than 2.40.0 will report a corrupted index during `git` `fsck`.
- `index.version=4` enables path-prefix compression in the index.
- `core.untrackedCache=true` enables the untracked cache. This setting assumes that mtime is working on your machine.

[](#Documentation/git-config.txt-fetchrecurseSubmodules)fetch.recurseSubmodules

This option controls whether `git` `fetch` (and the underlying fetch in `git` `pull`) will recursively fetch into populated submodules. This option can be set either to a boolean value or to *on-demand*. Setting it to a boolean changes the behavior of fetch and pull to recurse unconditionally into submodules when set to true or to not recurse at all when set to false. When set to *on-demand*, fetch and pull will only recurse into a populated submodule when its superproject retrieves a commit that updates the submodule’s reference. Defaults to *on-demand*, or to the value of *submodule.recurse* if set.

[](#Documentation/git-config.txt-fetchfsckObjects)fetch.fsckObjects

If it is set to true, git-fetch-pack will check all fetched objects. See `transfer.fsckObjects` for what’s checked. Defaults to false. If not set, the value of `transfer.fsckObjects` is used instead.

[](#Documentation/git-config.txt-fetchfsckmsg-id)fetch.fsck.&lt;msg-id&gt;

Acts like `fsck.`*&lt;msg-id&gt;*, but is used by [git-fetch-pack\[1\]](https://git-scm.com/docs/git-fetch-pack) instead of [git-fsck\[1\]](https://git-scm.com/docs/git-fsck). See the `fsck.`*&lt;msg-id&gt;* documentation for details.

[](#Documentation/git-config.txt-fetchfsckskipList)fetch.fsck.skipList

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
