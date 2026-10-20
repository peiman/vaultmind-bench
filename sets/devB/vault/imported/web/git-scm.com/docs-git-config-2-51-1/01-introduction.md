---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#01-introduction.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-01-introduction
type: reference
title: Git - git-config Documentation › Introduction
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#01-introduction
source_hash: abbef1779e05ba4fee47618bc9eba2e8f91fba5a12f94ee733ecbe16291715d0
---
The Git configuration file contains a number of variables that affect the Git commands' behavior. The files `.git/config` and optionally `config.worktree` (see the "CONFIGURATION FILE" section of [git-worktree\[1\]](https://git-scm.com/docs/git-worktree)) in each repository are used to store the configuration for that repository, and `$HOME/.gitconfig` is used to store a per-user configuration as fallback values for the `.git/config` file. The file `/etc/gitconfig` can be used to store a system-wide default configuration.

The configuration variables are used by both the Git plumbing and the porcelain commands. The variables are divided into sections, wherein the fully qualified variable name of the variable itself is the last dot-separated segment and the section name is everything before the last dot. The variable names are case-insensitive, allow only alphanumeric characters and `-`, and must start with an alphabetic character. Some variables may appear multiple times; we say then that the variable is multivalued.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
