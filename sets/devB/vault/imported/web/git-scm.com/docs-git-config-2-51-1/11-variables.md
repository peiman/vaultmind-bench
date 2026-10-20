---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#11-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-11-variables
type: reference
title: Git - git-config Documentation › Variables (5/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#11-variables
source_hash: 2e6f9af968a1d36febd6622076691a4ce7829f1f3c8691cb14ab4d1fbb236975
---
rebase is set to true for tracked branches of remote-tracking branches.

[](#Documentation/git-config.txt-always-1)`always`

rebase will be set to true for all tracking branches.

See `branch.autoSetupMerge` for details on how to set up a branch to track another branch. This option defaults to `never`.

[](#Documentation/git-config.txt-branchsort)`branch.sort`

This variable controls the sort ordering of branches when displayed by [git-branch\[1\]](https://git-scm.com/docs/git-branch). Without the `--sort=`*&lt;value&gt;* option provided, the value of this variable will be used as the default. See [git-for-each-ref\[1\]](https://git-scm.com/docs/git-for-each-ref) field names for valid values.

[](#Documentation/git-config.txt-branchnameremote)`branch.`*&lt;name&gt;*`.remote`

When on branch *&lt;name&gt;*, it tells `git` `fetch` and `git` `push` which remote to fetch from or push to. The remote to push to may be overridden with `remote.pushDefault` (for all branches). The remote to push to, for the current branch, may be further overridden by `branch.`*&lt;name&gt;*`.pushRemote`. If no remote is configured, or if you are not on any branch and there is more than one remote defined in the repository, it defaults to `origin` for fetching and `remote.pushDefault` for pushing. Additionally, `.` (a period) is the current local repository (a dot-repository), see `branch.`*&lt;name&gt;*`.merge`'s final note below.

[](#Documentation/git-config.txt-branchnamepushRemote)`branch.`*&lt;name&gt;*`.pushRemote`

When on branch *&lt;name&gt;*, it overrides `branch.`*&lt;name&gt;*`.remote` for pushing. It also overrides `remote.pushDefault` for pushing from branch *&lt;name&gt;*. When you pull from one place (e.g. your upstream) and push to another place (e.g. your own publishing repository), you would want to set `remote.pushDefault` to specify the remote to push to for all branches, and use this option to override it for a specific branch.

[](#Documentation/git-config.txt-branchnamemerge)`branch.`*&lt;name&gt;*`.merge`

Defines, together with `branch.`*&lt;name&gt;*`.remote`, the upstream branch for the given branch. It tells `git` `fetch`/`git` `pull`/`git` `rebase` which branch to merge and can also affect `git` `push` (see `push.default`). When in branch *&lt;name&gt;*, it tells `git` `fetch` the default refspec to be marked for merging in `FETCH_HEAD`. The value is handled like the remote part of a refspec, and must match a ref which is fetched from the remote given by `branch.`*&lt;name&gt;*`.remote`. The merge information is used by `git` `pull` (which first calls `git` `fetch`) to lookup the default branch for merging. Without this option, `git` `pull` defaults to merge the first refspec fetched. Specify multiple values to get an octopus merge. If you wish to setup `git` `pull` so that it merges into *&lt;name&gt;* from another branch in the local repository, you can point `branch.`*&lt;name&gt;*`.merge` to the desired branch, and use the relative path setting `.` (a period) for `branch.`*&lt;name&gt;*`.remote`.

[](#Documentation/git-config.txt-branchnamemergeOptions)`branch.`*&lt;name&gt;*`.mergeOptions`

Sets default options for merging into branch *&lt;name&gt;*. The syntax and supported options are the same as those of [git-merge\[1\]](https://git-scm.com/docs/git-merge), but option values containing whitespace characters are currently not supported.

[](#Documentation/git-config.txt-branchnamerebase)`branch.`*&lt;name&gt;*`.rebase`

When true, rebase the branch *&lt;name&gt;* on top of the fetched branch, instead of merging the default branch from the default remote when `git` `pull` is run. See `pull.rebase` for doing this in a non branch-specific manner.

When `merges` (or just `m`), pass the `--rebase-merges` option to `git` `rebase` so that the local merge commits are included in the rebase (see [git-rebase\[1\]](https://git-scm.com/docs/git-rebase) for details).

When the value is `interactive` (or just `i`), the rebase is run in interactive mode.

**NOTE**: this is a possibly dangerous operation; do **not** use it unless you understand the implications (see [git-rebase\[1\]](https://git-scm.com/docs/git-rebase) for details).

[](#Documentation/git-config.txt-branchnamedescription)`branch.`*&lt;name&gt;*`.description`

Branch description, can be edited with `git` `branch` `--edit-description`. Branch description is automatically added to the `format-patch` cover letter or `request-pull` summary.

[](#Documentation/git-config.txt-browsertoolcmd)browser.&lt;tool&gt;.cmd

Specify the command to invoke the specified browser. The specified command is evaluated in shell with the URLs passed as arguments. (See [git-web--browse\[1\]](https://git-scm.com/docs/git-web--browse).)

[](#Documentation/git-config.txt-browsertoolpath)browser.&lt;tool&gt;.path

Override the path for the given tool that may be used to browse HTML help (see `-w` option in [git-help\[1\]](https://git-scm.com/docs/git-help)) or a working repository in gitweb (see [git-instaweb\[1\]](https://git-scm.com/docs/git-instaweb)).

[](#Documentation/git-config.txt-bundle)bundle.*

The `bundle.*` keys may appear in a bundle list file found via the `git` `clone` `--bundle-uri` option. These keys currently have no effect if placed in a repository config file, though this will change in the future. See [the bundle URI design document](https://git-scm.com/docs/bundle-uri) for more details.

[](#Documentation/git-config.txt-bundleversion)bundle.version

This integer value advertises the version of the bundle list format used by the bundle list. Currently, the only accepted value is `1`.

[](#Documentation/git-config.txt-bundlemode)bundle.mode

This string value should be either `all` or `any`. This value describes whether all of the advertised bundles are required to unbundle a complete understanding of the bundled information (`all`) or if any one of the listed bundle URIs is sufficient (`any`).

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
