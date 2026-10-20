---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#04-conditional-includes.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-04-conditional-includes
type: reference
title: Git - git-config Documentation › Conditional includes
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#04-conditional-includes
source_hash: d2ec8a6b5411094a7a99fbb8516d191cd92914e11e60f2c75b06a93313b76374
---
You can conditionally include a config file from another by setting an `includeIf.`*&lt;condition&gt;*`.path` variable to the name of the file to be included.

The condition starts with a keyword followed by a colon and some data whose format and meaning depends on the keyword. Supported keywords are:

[](#Documentation/git-config.txt-gitdir)`gitdir`

The data that follows the keyword `gitdir` and a colon is used as a glob pattern. If the location of the .git directory matches the pattern, the include condition is met.

The .git location may be auto-discovered, or come from `$GIT_DIR` environment variable. If the repository is auto-discovered via a .git file (e.g. from submodules, or a linked worktree), the .git location would be the final location where the .git directory is, not where the .git file is.

The pattern can contain standard globbing wildcards and two additional ones, `**/` and `/**`, that can match multiple path components. Please refer to [gitignore\[5\]](https://git-scm.com/docs/gitignore) for details. For convenience:

- If the pattern starts with `~/`, `~` will be substituted with the content of the environment variable `HOME`.
- If the pattern starts with `./`, it is replaced with the directory containing the current config file.
- If the pattern does not start with either `~/`, `./` or `/`, `**/` will be automatically prepended. For example, the pattern `foo/bar` becomes `**/foo/bar` and would match `/any/path/to/foo/bar`.
- If the pattern ends with `/`, `**` will be automatically added. For example, the pattern `foo/` becomes `foo/**`. In other words, it matches "foo" and everything inside, recursively.

[](#Documentation/git-config.txt-gitdiri)`gitdir/i`

This is the same as `gitdir` except that matching is done case-insensitively (e.g. on case-insensitive file systems)

[](#Documentation/git-config.txt-onbranch)`onbranch`

The data that follows the keyword `onbranch` and a colon is taken to be a pattern with standard globbing wildcards and two additional ones, `**/` and `/**`, that can match multiple path components. If we are in a worktree where the name of the branch that is currently checked out matches the pattern, the include condition is met.

If the pattern ends with `/`, `**` will be automatically added. For example, the pattern `foo/` becomes `foo/**`. In other words, it matches all branches that begin with `foo/`. This is useful if your branches are organized hierarchically and you would like to apply a configuration to all the branches in that hierarchy.

[](#Documentation/git-config.txt-hasconfigremoteurl)`hasconfig:remote.*.url`

The data that follows this keyword and a colon is taken to be a pattern with standard globbing wildcards and two additional ones, `**/` and `/**`, that can match multiple components. The first time this keyword is seen, the rest of the config files will be scanned for remote URLs (without applying any values). If there exists at least one remote URL that matches this pattern, the include condition is met.

Files included by this option (directly or indirectly) are not allowed to contain remote URLs.

Note that unlike other includeIf conditions, resolving this condition relies on information that is not yet known at the point of reading the condition. A typical use case is this option being present as a system-level or global-level config, and the remote URL being in a local-level config; hence the need to scan ahead when resolving this condition. In order to avoid the chicken-and-egg problem in which potentially-included files can affect whether such files are potentially included, Git breaks the cycle by prohibiting these files from affecting the resolution of these conditions (thus, prohibiting them from declaring remote URLs).

As for the naming of this keyword, it is for forwards compatibility with a naming scheme that supports more variable-based include conditions, but currently Git only supports the exact keyword described above.

A few more notes on matching via `gitdir` and `gitdir/i`:

- Symlinks in `$GIT_DIR` are not resolved before matching.
- Both the symlink & realpath versions of paths will be matched outside of `$GIT_DIR`. E.g. if ~/git is a symlink to /mnt/storage/git, both `gitdir:~/git` and `gitdir:/mnt/storage/git` will match.
  
  This was not the case in the initial release of this feature in v2.13.0, which only matched the realpath version. Configuration that wants to be compatible with the initial release of this feature needs to either specify only the realpath version, or both versions.
- Note that "../" is not special and will match literally, which is unlikely what you want.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
