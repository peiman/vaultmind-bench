---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#18-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-18-variables
type: reference
title: Git - git-config Documentation › Variables (12/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#18-variables
source_hash: bc9e68921ea7373a882d12513d7cca1495966d64c78ff2dd76d427f881510ae1
---
When advertising tips of available history from an alternate, use the shell to execute the specified command instead of [git-for-each-ref\[1\]](https://git-scm.com/docs/git-for-each-ref). The first argument is the absolute path of the alternate. Output must contain one hex object id per line (i.e., the same as produced by `git` `for-each-ref` `--format='%`(`objectname`)).

Note that you cannot generally put `git` `for-each-ref` directly into the config value, as it does not take a repository path as an argument (but you can wrap the command above in a shell script).

[](#Documentation/git-config.txt-corealternateRefsPrefixes)core.alternateRefsPrefixes

When listing references from an alternate, list only references that begin with the given prefix. Prefixes match as if they were given as arguments to [git-for-each-ref\[1\]](https://git-scm.com/docs/git-for-each-ref). To list multiple prefixes, separate them with whitespace. If `core.alternateRefsCommand` is set, setting `core.alternateRefsPrefixes` has no effect.

[](#Documentation/git-config.txt-corebare)core.bare

If true this repository is assumed to be *bare* and has no working directory associated with it. If this is the case a number of commands that require a working directory will be disabled, such as [git-add\[1\]](https://git-scm.com/docs/git-add) or [git-merge\[1\]](https://git-scm.com/docs/git-merge).

This setting is automatically guessed by [git-clone\[1\]](https://git-scm.com/docs/git-clone) or [git-init\[1\]](https://git-scm.com/docs/git-init) when the repository was created. By default a repository that ends in "/.git" is assumed to be not bare (bare = false), while all other repositories are assumed to be bare (bare = true).

[](#Documentation/git-config.txt-coreworktree)core.worktree

Set the path to the root of the working tree. If `GIT_COMMON_DIR` environment variable is set, core.worktree is ignored and not used for determining the root of working tree. This can be overridden by the `GIT_WORK_TREE` environment variable and the `--work-tree` command-line option. The value can be an absolute path or relative to the path to the .git directory, which is either specified by --git-dir or GIT\_DIR, or automatically discovered. If --git-dir or GIT\_DIR is specified but none of --work-tree, GIT\_WORK\_TREE and core.worktree is specified, the current working directory is regarded as the top level of your working tree.

Note that this variable is honored even when set in a configuration file in a ".git" subdirectory of a directory and its value differs from the latter directory (e.g. "/path/to/.git/config" has core.worktree set to "/different/path"), which is most likely a misconfiguration. Running Git commands in the "/path/to" directory will still use "/different/path" as the root of the work tree and can cause confusion unless you know what you are doing (e.g. you are creating a read-only snapshot of the same index to a location different from the repository’s usual working tree).

[](#Documentation/git-config.txt-corelogAllRefUpdates)core.logAllRefUpdates

Enable the reflog. Updates to a ref &lt;ref&gt; is logged to the file "`$GIT_DIR/logs/`*&lt;ref&gt;*", by appending the new and old SHA-1, the date/time and the reason of the update, but only when the file exists. If this configuration variable is set to `true`, missing "`$GIT_DIR/logs/`*&lt;ref&gt;*" file is automatically created for branch heads (i.e. under `refs/heads/`), remote refs (i.e. under `refs/remotes/`), note refs (i.e. under `refs/notes/`), and the symbolic ref `HEAD`. If it is set to `always`, then a missing reflog is automatically created for any ref under `refs/`.

This information can be used to determine what commit was the tip of a branch "2 days ago".

This value is true by default in a repository that has a working directory associated with it, and false by default in a bare repository.

[](#Documentation/git-config.txt-corerepositoryFormatVersion)core.repositoryFormatVersion

Internal variable identifying the repository format and layout version. See [gitrepository-layout\[5\]](https://git-scm.com/docs/gitrepository-layout).

[](#Documentation/git-config.txt-coresharedRepository)core.sharedRepository

When *group* (or *true*), the repository is made shareable between several users in a group (making sure all the files and objects are group-writable). When *all* (or *world* or *everybody*), the repository will be readable by all users, additionally to being group-shareable. When *umask* (or *false*), Git will use permissions reported by umask(2). When *0xxx*, where *0xxx* is an octal number, files in the repository will have this mode value. *0xxx* will override user’s umask value (whereas the other options will only override requested parts of the user’s umask value). Examples: *0660* will make the repo read/write-able for the owner and group, but inaccessible to others (equivalent to *group* unless umask is e.g. *0022*). *0640* is a repository that is group-readable but not group-writable. See [git-init\[1\]](https://git-scm.com/docs/git-init). False by default.

[](#Documentation/git-config.txt-corewarnAmbiguousRefs)core.warnAmbiguousRefs

If true, Git will warn you if the ref name you passed it is ambiguous and might match multiple refs in the repository. True by default.

[](#Documentation/git-config.txt-corecompression)core.compression

An integer -1..9, indicating a default compression level. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If set, this provides a default to other compression variables, such as `core.looseCompression` and `pack.compression`.

[](#Documentation/git-config.txt-corelooseCompression)core.looseCompression

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
