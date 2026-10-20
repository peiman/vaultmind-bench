---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#30-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-30-variables
type: reference
title: Git - git-config Documentation › Variables (24/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#30-variables
source_hash: a3813b763b5488e0e27fd5ae480f10c9959184f817cdccf711095c8d5cfc53d7
---
[](#Documentation/git-config.txt-gcaggressiveDepth)gc.aggressiveDepth

The depth parameter used in the delta compression algorithm used by *git gc --aggressive*. This defaults to 50, which is the default for the `--depth` option when `--aggressive` isn’t in use.

See the documentation for the `--depth` option in [git-repack\[1\]](https://git-scm.com/docs/git-repack) for more details.

[](#Documentation/git-config.txt-gcaggressiveWindow)gc.aggressiveWindow

The window size parameter used in the delta compression algorithm used by *git gc --aggressive*. This defaults to 250, which is a much more aggressive window size than the default `--window` of 10.

See the documentation for the `--window` option in [git-repack\[1\]](https://git-scm.com/docs/git-repack) for more details.

[](#Documentation/git-config.txt-gcauto)gc.auto

When there are approximately more than this many loose objects in the repository, `git` `gc` `--auto` will pack them. Some Porcelain commands use this command to perform a light-weight garbage collection from time to time. The default value is 6700.

Setting this to 0 disables not only automatic packing based on the number of loose objects, but also any other heuristic `git` `gc` `--auto` will otherwise use to determine if there’s work to do, such as `gc.autoPackLimit`.

[](#Documentation/git-config.txt-gcautoPackLimit)gc.autoPackLimit

When there are more than this many packs that are not marked with `*.keep` file in the repository, `git` `gc` `--auto` consolidates them into one larger pack. The default value is 50. Setting this to 0 disables it. Setting `gc.auto` to 0 will also disable this.

See the `gc.bigPackThreshold` configuration variable below. When in use, it’ll affect how the auto pack limit works.

[](#Documentation/git-config.txt-gcautoDetach)gc.autoDetach

Make `git` `gc` `--auto` return immediately and run in the background if the system supports it. Default is true. This config variable acts as a fallback in case `maintenance.autoDetach` is not set.

[](#Documentation/git-config.txt-gcbigPackThreshold)gc.bigPackThreshold

If non-zero, all non-cruft packs larger than this limit are kept when `git` `gc` is run. This is very similar to `--keep-largest-pack` except that all non-cruft packs that meet the threshold are kept, not just the largest pack. Defaults to zero. Common unit suffixes of *k*, *m*, or *g* are supported.

Note that if the number of kept packs is more than gc.autoPackLimit, this configuration variable is ignored, all packs except the base pack will be repacked. After this the number of packs should go below gc.autoPackLimit and gc.bigPackThreshold should be respected again.

If the amount of memory estimated for `git` `repack` to run smoothly is not available and `gc.bigPackThreshold` is not set, the largest pack will also be excluded (this is the equivalent of running `git` `gc` with `--keep-largest-pack`).

[](#Documentation/git-config.txt-gcwriteCommitGraph)gc.writeCommitGraph

If true, then gc will rewrite the commit-graph file when [git-gc\[1\]](https://git-scm.com/docs/git-gc) is run. When using `git` `gc` `--auto` the commit-graph will be updated if housekeeping is required. Default is true. See [git-commit-graph\[1\]](https://git-scm.com/docs/git-commit-graph) for details.

[](#Documentation/git-config.txt-gclogExpiry)gc.logExpiry

If the file gc.log exists, then `git` `gc` `--auto` will print its content and exit with status zero instead of running unless that file is more than *gc.logExpiry* old. Default is "1.day". See `gc.pruneExpire` for more ways to specify its value.

[](#Documentation/git-config.txt-gcpackRefs)gc.packRefs

Running `git` `pack-refs` in a repository renders it unclonable by Git versions prior to 1.5.1.2 over dumb transports such as HTTP. This variable determines whether *git gc* runs `git` `pack-refs`. This can be set to `notbare` to enable it within all non-bare repos or it can be set to a boolean value. The default is `true`.

[](#Documentation/git-config.txt-gccruftPacks)gc.cruftPacks

Store unreachable objects in a cruft pack (see [git-repack\[1\]](https://git-scm.com/docs/git-repack)) instead of as loose objects. The default is `true`.

[](#Documentation/git-config.txt-gcmaxCruftSize)gc.maxCruftSize

Limit the size of new cruft packs when repacking. When specified in addition to `--max-cruft-size`, the command line option takes priority. See the `--max-cruft-size` option of [git-repack\[1\]](https://git-scm.com/docs/git-repack).

[](#Documentation/git-config.txt-gcpruneExpire)gc.pruneExpire

When *git gc* is run, it will call *prune --expire 2.weeks.ago* (and *repack --cruft --cruft-expiration 2.weeks.ago* if using cruft packs via `gc.cruftPacks` or `--cruft`). Override the grace period with this config variable. The value "now" may be used to disable this grace period and always prune unreachable objects immediately, or "never" may be used to suppress pruning. This feature helps prevent corruption when *git gc* runs concurrently with another process writing to the repository; see the "NOTES" section of [git-gc\[1\]](https://git-scm.com/docs/git-gc).

[](#Documentation/git-config.txt-gcworktreePruneExpire)gc.worktreePruneExpire

When *git gc* is run, it calls *git worktree prune --expire 3.months.ago*. This config variable can be used to set a different grace period. The value "now" may be used to disable the grace period and prune `$GIT_DIR/worktrees` immediately, or "never" may be used to suppress pruning.

[](#Documentation/git-config.txt-gcreflogExpire)gc.reflogExpire

[](#Documentation/git-config.txt-gcpatternreflogExpire)gc.&lt;pattern&gt;.reflogExpire

*git reflog expire* removes reflog entries older than this time; defaults to 90 days. The value "now" expires all entries immediately, and "never" suppresses expiration altogether. With "&lt;pattern&gt;" (e.g. "refs/stash") in the middle the setting applies only to the refs that match the &lt;pattern&gt;.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
