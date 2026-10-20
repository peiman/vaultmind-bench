---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#62-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-62-variables
type: reference
title: Git - git-config Documentation › Variables (56/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#62-variables
source_hash: 380333e5c052715651ff6536a96d875825220eb6775716d8f73c2b3322de710a
---
If [git-tag\[1\]](https://git-scm.com/docs/git-tag) or [git-commit\[1\]](https://git-scm.com/docs/git-commit) is not selecting the key you want it to automatically when creating a signed tag or commit, you can override the default selection with this variable. This option is passed unchanged to gpg’s --local-user parameter, so you may specify a key using any method that gpg supports. If gpg.format is set to `ssh` this can contain the path to either your private ssh key or the public key when ssh-agent is used. Alternatively it can contain a public key prefixed with `key::` directly (e.g.: "key::ssh-rsa XXXXXX identifier"). The private key needs to be available via ssh-agent. If not set Git will call gpg.ssh.defaultKeyCommand (e.g.: "ssh-add -L") and try to use the first key available. For backward compatibility, a raw key which begins with "ssh-", such as "ssh-rsa XXXXXX identifier", is treated as "key::ssh-rsa XXXXXX identifier", but this form is deprecated; use the `key::` form instead.

[](#Documentation/git-config.txt-versionsortprereleaseSuffixdeprecated)versionsort.prereleaseSuffix (deprecated)

Deprecated alias for `versionsort.suffix`. Ignored if `versionsort.suffix` is set.

[](#Documentation/git-config.txt-versionsortsuffix)versionsort.suffix

Even when version sort is used in [git-tag\[1\]](https://git-scm.com/docs/git-tag), tagnames with the same base version but different suffixes are still sorted lexicographically, resulting e.g. in prerelease tags appearing after the main release (e.g. "1.0-rc1" after "1.0"). This variable can be specified to determine the sorting order of tags with different suffixes.

By specifying a single suffix in this variable, any tagname containing that suffix will appear before the corresponding main release. E.g. if the variable is set to "-rc", then all "1.0-rcX" tags will appear before "1.0". If specified multiple times, once per suffix, then the order of suffixes in the configuration will determine the sorting order of tagnames with those suffixes. E.g. if "-pre" appears before "-rc" in the configuration, then all "1.0-preX" tags will be listed before any "1.0-rcX" tags. The placement of the main release tag relative to tags with various suffixes can be determined by specifying the empty suffix among those other suffixes. E.g. if the suffixes "-rc", "", "-ck", and "-bfs" appear in the configuration in this order, then all "v4.8-rcX" tags are listed first, followed by "v4.8", then "v4.8-ckX" and finally "v4.8-bfsX".

If more than one suffix matches the same tagname, then that tagname will be sorted according to the suffix which starts at the earliest position in the tagname. If more than one different matching suffix starts at that earliest position, then that tagname will be sorted according to the longest of those suffixes. The sorting order between different suffixes is undefined if they are in multiple config files.

[](#Documentation/git-config.txt-webbrowser)web.browser

Specify a web browser that may be used by some commands. Currently only [git-instaweb\[1\]](https://git-scm.com/docs/git-instaweb) and [git-help\[1\]](https://git-scm.com/docs/git-help) may use it.

[](#Documentation/git-config.txt-worktreeguessRemote)worktree.guessRemote

If no branch is specified and neither `-b` nor `-B` nor `--detach` is used, then `git` `worktree` `add` defaults to creating a new branch from HEAD. If `worktree.guessRemote` is set to true, `worktree` `add` tries to find a remote-tracking branch whose name uniquely matches the new branch name. If such a branch exists, it is checked out and set as "upstream" for the new branch. If no such match can be found, it falls back to creating a new branch from the current HEAD.

[](#Documentation/git-config.txt-worktreeuseRelativePaths)worktree.useRelativePaths

Link worktrees using relative paths (when "true") or absolute paths (when "false"). This is particularly useful for setups where the repository and worktrees may be moved between different locations or environments. Defaults to "false".

Note that setting `worktree.useRelativePaths` to "true" implies enabling the `extensions.relativeWorktrees` config (see [git-config\[1\]](https://git-scm.com/docs/git-config)), thus making it incompatible with older versions of Git.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
