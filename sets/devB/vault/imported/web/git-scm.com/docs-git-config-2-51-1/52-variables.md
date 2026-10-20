---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#52-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-52-variables
type: reference
title: Git - git-config Documentation › Variables (46/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#52-variables
source_hash: 24f58d5d254370cf54f622a31251a04d4239af3486c19658e02c15aea26ce2e1
---
[](#Documentation/git-config.txt-repackuseDeltaBaseOffset)repack.useDeltaBaseOffset

By default, [git-repack\[1\]](https://git-scm.com/docs/git-repack) creates packs that use delta-base offset. If you need to share your repository with Git older than version 1.4.4, either directly or via a dumb protocol such as http, then you need to set this option to "false" and repack. Access from old Git versions over the native protocol are unaffected by this option.

[](#Documentation/git-config.txt-repackpackKeptObjects)repack.packKeptObjects

If set to true, makes `git` `repack` act as if `--pack-kept-objects` was passed. See [git-repack\[1\]](https://git-scm.com/docs/git-repack) for details. Defaults to `false` normally, but `true` if a bitmap index is being written (either via `--write-bitmap-index` or `repack.writeBitmaps`).

[](#Documentation/git-config.txt-repackuseDeltaIslands)repack.useDeltaIslands

If set to true, makes `git` `repack` act as if `--delta-islands` was passed. Defaults to `false`.

[](#Documentation/git-config.txt-repackwriteBitmaps)repack.writeBitmaps

When true, git will write a bitmap index when packing all objects to disk (e.g., when `git` `repack` `-a` is run). This index can speed up the "counting objects" phase of subsequent packs created for clones and fetches, at the cost of some disk space and extra time spent on the initial repack. This has no effect if multiple packfiles are created. Defaults to true on bare repos, false otherwise.

[](#Documentation/git-config.txt-repackupdateServerInfo)repack.updateServerInfo

If set to false, [git-repack\[1\]](https://git-scm.com/docs/git-repack) will not run [git-update-server-info\[1\]](https://git-scm.com/docs/git-update-server-info). Defaults to true. Can be overridden when true by the `-n` option of [git-repack\[1\]](https://git-scm.com/docs/git-repack).

[](#Documentation/git-config.txt-repackcruftWindow)repack.cruftWindow

[](#Documentation/git-config.txt-repackcruftWindowMemory)repack.cruftWindowMemory

[](#Documentation/git-config.txt-repackcruftDepth)repack.cruftDepth

[](#Documentation/git-config.txt-repackcruftThreads)repack.cruftThreads

Parameters used by [git-pack-objects\[1\]](https://git-scm.com/docs/git-pack-objects) when generating a cruft pack and the respective parameters are not given over the command line. See similarly named `pack.*` configuration variables for defaults and meaning.

[](#Documentation/git-config.txt-repackmidxMustContainCruft)repack.midxMustContainCruft

When set to true, [git-repack\[1\]](https://git-scm.com/docs/git-repack) will unconditionally include cruft pack(s), if any, in the multi-pack index when invoked with `--write-midx`. When false, cruft packs are only included in the MIDX when necessary (e.g., because they might be required to form a reachability closure with MIDX bitmaps). Defaults to true.

[](#Documentation/git-config.txt-rerereautoUpdate)rerere.autoUpdate

When set to true, `git-rerere` updates the index with the resulting contents after it cleanly resolves conflicts using previously recorded resolutions. Defaults to false.

[](#Documentation/git-config.txt-rerereenabled)rerere.enabled

Activate recording of resolved conflicts, so that identical conflict hunks can be resolved automatically, should they be encountered again. By default, [git-rerere\[1\]](https://git-scm.com/docs/git-rerere) is enabled if there is an `rr-cache` directory under the `$GIT_DIR`, e.g. if "rerere" was previously used in the repository.

[](#Documentation/git-config.txt-revertreference)revert.reference

Setting this variable to true makes `git` `revert` behave as if the `--reference` option is given.

[](#Documentation/git-config.txt-safebareRepository)safe.bareRepository

Specifies which bare repositories Git will work with. The currently supported values are:

- `all`: Git works with all bare repositories. This is the default.
- `explicit`: Git only works with bare repositories specified via the top-level `--git-dir` command-line option, or the `GIT_DIR` environment variable (see [git\[1\]](https://git-scm.com/docs/git)).

If you do not use bare repositories in your workflow, then it may be beneficial to set `safe.bareRepository` to `explicit` in your global config. This will protect you from attacks that involve cloning a repository that contains a bare repository and running a Git command within that directory.

This config setting is only respected in protected configuration (see [SCOPES](#SCOPES)). This prevents untrusted repositories from tampering with this value.

[](#Documentation/git-config.txt-safedirectory)safe.directory

These config entries specify Git-tracked directories that are considered safe even if they are owned by someone other than the current user. By default, Git will refuse to even parse a Git config of a repository owned by someone else, let alone run its hooks, and this config setting allows users to specify exceptions, e.g. for intentionally shared repositories (see the `--shared` option in [git-init\[1\]](https://git-scm.com/docs/git-init)).

This is a multi-valued setting, i.e. you can add more than one directory via `git` `config` `--add`. To reset the list of safe directories (e.g. to override any such directories specified in the system config), add a `safe.directory` entry with an empty value.

This config setting is only respected in protected configuration (see [SCOPES](#SCOPES)). This prevents untrusted repositories from tampering with this value.

The value of this setting is interpolated, i.e. `~/`*&lt;path&gt;* expands to a path relative to the home directory and `%`(`prefix`)`/`*&lt;path&gt;* expands to a path relative to Git’s (runtime) prefix.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
