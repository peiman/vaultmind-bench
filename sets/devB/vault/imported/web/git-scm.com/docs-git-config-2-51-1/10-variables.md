---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#10-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-10-variables
type: reference
title: Git - git-config Documentation › Variables (4/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#10-variables
source_hash: 648caebe9f8d9a4f0b89b8a460bc01c2e887565abffdd768f8d9396aa0f8afe8
---
Determines the proportion of non-bitmapped commits (among reference tips) which are selected for inclusion in an unstable pseudo-merge bitmap. Must be between `0` and `1` (inclusive). The default is `1`.

[](#Documentation/git-config.txt-bitmapPseudoMergenamethreshold)bitmapPseudoMerge.&lt;name&gt;.threshold

Determines the minimum age of non-bitmapped commits (among reference tips, as above) which are candidates for inclusion in an unstable pseudo-merge bitmap. The default is `1.week.ago`.

[](#Documentation/git-config.txt-bitmapPseudoMergenamemaxMerges)bitmapPseudoMerge.&lt;name&gt;.maxMerges

Determines the maximum number of pseudo-merge commits among which commits may be distributed.

For pseudo-merge groups whose pattern does not contain any capture groups, this setting is applied for all commits matching the regular expression. For patterns that have one or more capture groups, this setting is applied for each distinct capture group.

For example, if your capture group is `refs/tags/`, then this setting will distribute all tags into a maximum of `maxMerges` pseudo-merge commits. However, if your capture group is, say, `refs/remotes/`(\[`0-9`]`+`)`/tags/`, then this setting will be applied to each remote’s set of tags individually.

Must be non-negative. The default value is 64.

[](#Documentation/git-config.txt-bitmapPseudoMergenamestableThreshold)bitmapPseudoMerge.&lt;name&gt;.stableThreshold

Determines the minimum age of commits (among reference tips, as above, however stable commits are still considered candidates even when they have been covered by a bitmap) which are candidates for a stable a pseudo-merge bitmap. The default is `1.month.ago`.

Setting this threshold to a smaller value (e.g., 1.week.ago) will cause more stable groups to be generated (which impose a one-time generation cost) but those groups will likely become stale over time. Using a larger value incurs the opposite penalty (fewer stable groups which are more useful).

[](#Documentation/git-config.txt-bitmapPseudoMergenamestableSize)bitmapPseudoMerge.&lt;name&gt;.stableSize

Determines the size (in number of commits) of a stable psuedo-merge bitmap. The default is `512`.

[](#Documentation/git-config.txt-blameblankBoundary)blame.blankBoundary

Show blank commit object name for boundary commits in [git-blame\[1\]](https://git-scm.com/docs/git-blame). This option defaults to false.

[](#Documentation/git-config.txt-blamecoloring)blame.coloring

This determines the coloring scheme to be applied to blame output. It can be *repeatedLines*, *highlightRecent*, or *none* which is the default.

[](#Documentation/git-config.txt-blamedate)blame.date

Specifies the format used to output dates in [git-blame\[1\]](https://git-scm.com/docs/git-blame). If unset the iso format is used. For supported values, see the discussion of the `--date` option at [git-log\[1\]](https://git-scm.com/docs/git-log).

[](#Documentation/git-config.txt-blameshowEmail)blame.showEmail

Show the author email instead of author name in [git-blame\[1\]](https://git-scm.com/docs/git-blame). This option defaults to false.

[](#Documentation/git-config.txt-blameshowRoot)blame.showRoot

Do not treat root commits as boundaries in [git-blame\[1\]](https://git-scm.com/docs/git-blame). This option defaults to false.

[](#Documentation/git-config.txt-blameignoreRevsFile)blame.ignoreRevsFile

Ignore revisions listed in the file, one unabbreviated object name per line, in [git-blame\[1\]](https://git-scm.com/docs/git-blame). Whitespace and comments beginning with `#` are ignored. This option may be repeated multiple times. Empty file names will reset the list of ignored revisions. This option will be handled before the command line option `--ignore-revs-file`.

[](#Documentation/git-config.txt-blamemarkUnblamableLines)blame.markUnblamableLines

Mark lines that were changed by an ignored revision that we could not attribute to another commit with a *\** in the output of [git-blame\[1\]](https://git-scm.com/docs/git-blame).

[](#Documentation/git-config.txt-blamemarkIgnoredLines)blame.markIgnoredLines

Mark lines that were changed by an ignored revision that we attributed to another commit with a *?* in the output of [git-blame\[1\]](https://git-scm.com/docs/git-blame).

[](#Documentation/git-config.txt-branchautoSetupMerge)`branch.autoSetupMerge`

Tells `git` `branch`, `git` `switch` and `git` `checkout` to set up new branches so that [git-pull\[1\]](https://git-scm.com/docs/git-pull) will appropriately merge from the starting point branch. Note that even if this option is not set, this behavior can be chosen per-branch using the `--track` and `--no-track` options. This option defaults to `true`. The valid settings are:

[](#Documentation/git-config.txt-false-1)`false`

no automatic setup is done

[](#Documentation/git-config.txt-true-1)`true`

automatic setup is done when the starting point is a remote-tracking branch

[](#Documentation/git-config.txt-always)`always`

automatic setup is done when the starting point is either a local branch or remote-tracking branch

[](#Documentation/git-config.txt-inherit)`inherit`

if the starting point has a tracking configuration, it is copied to the new branch

[](#Documentation/git-config.txt-simple)`simple`

automatic setup is done only when the starting point is a remote-tracking branch and the new branch has the same name as the remote branch.

[](#Documentation/git-config.txt-branchautoSetupRebase)`branch.autoSetupRebase`

When a new branch is created with `git` `branch`, `git` `switch` or `git` `checkout` that tracks another branch, this variable tells Git to set up pull to rebase instead of merge (see `branch.`*&lt;name&gt;*`.rebase`). The valid settings are:

[](#Documentation/git-config.txt-never)`never`

rebase is never automatically set to true.

[](#Documentation/git-config.txt-local-1)`local`

rebase is set to true for tracked branches of other local branches.

[](#Documentation/git-config.txt-remote)`remote`

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
