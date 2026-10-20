---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#56-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-56-variables
type: reference
title: Git - git-config Documentation › Variables (50/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#56-variables
source_hash: 981067547745ba08ac29531144067aafbbcaa6813551d7205a2aa85fdf17d57e
---
Defaults to false. If this is set to a non-zero number or true (identical to -1 or an unlimited number), the submodule summary will be enabled and a summary of commits for modified submodules will be shown (see --summary-limit option of [git-submodule\[1\]](https://git-scm.com/docs/git-submodule)). Please note that the summary output command will be suppressed for all submodules when `diff.ignoreSubmodules` is set to *all* or only for those submodules where `submodule.`*&lt;name&gt;*`.ignore=all`. The only exception to that rule is that status and commit will show staged submodule changes. To also view the summary for ignored submodules you can either use the --ignore-submodules=dirty command-line option or the *git submodule summary* command, which shows a similar output but does not honor these settings.

[](#Documentation/git-config.txt-submodulenameurl)submodule.&lt;name&gt;.url

The URL for a submodule. This variable is copied from the .gitmodules file to the git config via *git submodule init*. The user can change the configured URL before obtaining the submodule via *git submodule update*. If neither submodule.&lt;name&gt;.active nor submodule.active are set, the presence of this variable is used as a fallback to indicate whether the submodule is of interest to git commands. See [git-submodule\[1\]](https://git-scm.com/docs/git-submodule) and [gitmodules\[5\]](https://git-scm.com/docs/gitmodules) for details.

[](#Documentation/git-config.txt-submodulenameupdate)submodule.&lt;name&gt;.update

The method by which a submodule is updated by *git submodule update*, which is the only affected command, others such as *git checkout --recurse-submodules* are unaffected. It exists for historical reasons, when *git submodule* was the only command to interact with submodules; settings like `submodule.active` and `pull.rebase` are more specific. It is populated by `git` `submodule` `init` from the [gitmodules\[5\]](https://git-scm.com/docs/gitmodules) file. See description of *update* command in [git-submodule\[1\]](https://git-scm.com/docs/git-submodule).

[](#Documentation/git-config.txt-submodulenamebranch)submodule.&lt;name&gt;.branch

The remote branch name for a submodule, used by `git` `submodule` `update` `--remote`. Set this option to override the value found in the `.gitmodules` file. See [git-submodule\[1\]](https://git-scm.com/docs/git-submodule) and [gitmodules\[5\]](https://git-scm.com/docs/gitmodules) for details.

[](#Documentation/git-config.txt-submodulenamefetchRecurseSubmodules)submodule.&lt;name&gt;.fetchRecurseSubmodules

This option can be used to control recursive fetching of this submodule. It can be overridden by using the --\[no-]recurse-submodules command-line option to "git fetch" and "git pull". This setting will override that from in the [gitmodules\[5\]](https://git-scm.com/docs/gitmodules) file.

[](#Documentation/git-config.txt-submodulenameignore)submodule.&lt;name&gt;.ignore

Defines under what circumstances "git status" and the diff family show a submodule as modified. When set to "all", it will never be considered modified (but it will nonetheless show up in the output of status and commit when it has been staged), "dirty" will ignore all changes to the submodule’s work tree and takes only differences between the HEAD of the submodule and the commit recorded in the superproject into account. "untracked" will additionally let submodules with modified tracked files in their work tree show up. Using "none" (the default when this option is not set) also shows submodules that have untracked files in their work tree as changed. This setting overrides any setting made in .gitmodules for this submodule, both settings can be overridden on the command line by using the "--ignore-submodules" option. The *git submodule* commands are not affected by this setting.

[](#Documentation/git-config.txt-submodulenameactive)submodule.&lt;name&gt;.active

Boolean value indicating if the submodule is of interest to git commands. This config option takes precedence over the submodule.active config option. See [gitsubmodules\[7\]](https://git-scm.com/docs/gitsubmodules) for details.

[](#Documentation/git-config.txt-submoduleactive)submodule.active

A repeated field which contains a pathspec used to match against a submodule’s path to determine if the submodule is of interest to git commands. See [gitsubmodules\[7\]](https://git-scm.com/docs/gitsubmodules) for details.

[](#Documentation/git-config.txt-submodulerecurse)submodule.recurse

A boolean indicating if commands should enable the `--recurse-submodules` option by default. Defaults to false.

When set to true, it can be deactivated via the `--no-recurse-submodules` option. Note that some Git commands lacking this option may call some of the above commands affected by `submodule.recurse`; for instance `git` `remote` `update` will call `git` `fetch` but does not have a `--no-recurse-submodules` option. For these commands a workaround is to temporarily change the configuration value by using `git` `-c` `submodule.recurse=0`.

The following list shows the commands that accept `--recurse-submodules` and whether they are supported by this setting.

- `checkout`, `fetch`, `grep`, `pull`, `push`, `read-tree`, `reset`, `restore` and `switch` are always supported.
- `clone` and `ls-files` are not supported.
- `branch` is supported only if `submodule.propagateBranches` is enabled

[](#Documentation/git-config.txt-submodulepropagateBranches)submodule.propagateBranches

\[EXPERIMENTAL] A boolean that enables branching support when using `--recurse-submodules` or `submodule.recurse=true`. Enabling this will allow certain commands to accept `--recurse-submodules` and certain commands that already accept `--recurse-submodules` will now consider branches. Defaults to false.

[](#Documentation/git-config.txt-submodulefetchJobs)submodule.fetchJobs

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
