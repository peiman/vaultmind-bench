---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#12-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-12-variables
type: reference
title: Git - git-config Documentation › Variables (6/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#12-variables
source_hash: 8f7943c14aef6958db2aeb5f62376c98b13073a3188b60c8f3c08ae314dc14df
---
[](#Documentation/git-config.txt-bundleheuristic)bundle.heuristic

If this string-valued key exists, then the bundle list is designed to work well with incremental `git` `fetch` commands. The heuristic signals that there are additional keys available for each bundle that help determine which subset of bundles the client should download. The only value currently understood is `creationToken`.

[](#Documentation/git-config.txt-bundleid)bundle.&lt;id&gt;.*

The `bundle.`*&lt;id&gt;*`.*` keys are used to describe a single item in the bundle list, grouped under *&lt;id&gt;* for identification purposes.

[](#Documentation/git-config.txt-bundleiduri)bundle.&lt;id&gt;.uri

This string value defines the URI by which Git can reach the contents of this *&lt;id&gt;*. This URI may be a bundle file or another bundle list.

[](#Documentation/git-config.txt-checkoutdefaultRemote)`checkout.defaultRemote`

When you run `git` `checkout` *&lt;something&gt;* or `git` `switch` *&lt;something&gt;* and only have one remote, it may implicitly fall back on checking out and tracking e.g. `origin/`*&lt;something&gt;*. This stops working as soon as you have more than one remote with a *&lt;something&gt;* reference. This setting allows for setting the name of a preferred remote that should always win when it comes to disambiguation. The typical use-case is to set this to `origin`.

Currently this is used by [git-switch\[1\]](https://git-scm.com/docs/git-switch) and [git-checkout\[1\]](https://git-scm.com/docs/git-checkout) when `git` `checkout` *&lt;something&gt;* or `git` `switch` *&lt;something&gt;* will checkout the *&lt;something&gt;* branch on another remote, and by [git-worktree\[1\]](https://git-scm.com/docs/git-worktree) when `git` `worktree` `add` refers to a remote branch. This setting might be used for other checkout-like commands or functionality in the future.

[](#Documentation/git-config.txt-checkoutguess)`checkout.guess`

Provides the default value for the `--guess` or `--no-guess` option in `git` `checkout` and `git` `switch`. See [git-switch\[1\]](https://git-scm.com/docs/git-switch) and [git-checkout\[1\]](https://git-scm.com/docs/git-checkout).

[](#Documentation/git-config.txt-checkoutworkers)`checkout.workers`

The number of parallel workers to use when updating the working tree. The default is one, i.e. sequential execution. If set to a value less than one, Git will use as many workers as the number of logical cores available. This setting and `checkout.thresholdForParallelism` affect all commands that perform checkout. E.g. checkout, clone, reset, sparse-checkout, etc.

Note

Parallel checkout usually delivers better performance for repositories located on SSDs or over NFS. For repositories on spinning disks and/or machines with a small number of cores, the default sequential checkout often performs better. The size and compression level of a repository might also influence how well the parallel version performs.

[](#Documentation/git-config.txt-checkoutthresholdForParallelism)`checkout.thresholdForParallelism`

When running parallel checkout with a small number of files, the cost of subprocess spawning and inter-process communication might outweigh the parallelization gains. This setting allows you to define the minimum number of files for which parallel checkout should be attempted. The default is 100.

[](#Documentation/git-config.txt-cleanrequireForce)clean.requireForce

A boolean to make git-clean refuse to delete files unless -f is given. Defaults to true.

[](#Documentation/git-config.txt-clonedefaultRemoteName)`clone.defaultRemoteName`

The name of the remote to create when cloning a repository. Defaults to `origin`. It can be overridden by passing the `--origin` command-line option to [git-clone\[1\]](https://git-scm.com/docs/git-clone).

[](#Documentation/git-config.txt-clonerejectShallow)`clone.rejectShallow`

Reject cloning a repository if it is a shallow one; this can be overridden by passing the `--reject-shallow` option on the command line. See [git-clone\[1\]](https://git-scm.com/docs/git-clone).

[](#Documentation/git-config.txt-clonefilterSubmodules)`clone.filterSubmodules`

If a partial clone filter is provided (see `--filter` in [git-rev-list\[1\]](https://git-scm.com/docs/git-rev-list)) and `--recurse-submodules` is used, also apply the filter to submodules.

[](#Documentation/git-config.txt-coloradvice)color.advice

A boolean to enable/disable color in hints (e.g. when a push failed, see `advice.*` for a list). May be set to `always`, `false` (or `never`) or `auto` (or `true`), in which case colors are used only when the error output goes to a terminal. If unset, then the value of `color.ui` is used (`auto` by default).

[](#Documentation/git-config.txt-coloradvicehint)color.advice.hint

Use customized color for hints.

[](#Documentation/git-config.txt-colorblamehighlightRecent)color.blame.highlightRecent

Specify the line annotation color for `git` `blame` `--color-by-age` depending upon the age of the line.

This setting should be set to a comma-separated list of color and date settings, starting and ending with a color, the dates should be set from oldest to newest. The metadata will be colored with the specified colors if the line was introduced before the given timestamp, overwriting older timestamped colors.

Instead of an absolute timestamp relative timestamps work as well, e.g. `2.weeks.ago` is valid to address anything older than 2 weeks.

It defaults to `blue,12` `month` `ago,white,1` `month` `ago,red`, which colors everything older than one year blue, recent changes between one month and one year old are kept white, and lines introduced within the last month are colored red.

[](#Documentation/git-config.txt-colorblamerepeatedLines)color.blame.repeatedLines

Use the specified color to colorize line annotations for `git` `blame` `--color-lines`, if they come from the same commit as the preceding line. Defaults to cyan.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
