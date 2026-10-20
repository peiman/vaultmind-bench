---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#15-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-15-variables
type: reference
title: Git - git-config Documentation › Variables (9/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#15-variables
source_hash: 2fc3fe4af133fecea5c2535679217cfa982822234f07a00adfd90ed148ee577c
---
A boolean to enable/disable inclusion of status information in the commit message template when using an editor to prepare the commit message. Defaults to `true`.

[](#Documentation/git-config.txt-committemplate)`commit.template`

Specify the pathname of a file to use as the template for new commit messages.

[](#Documentation/git-config.txt-commitverbose)`commit.verbose`

A boolean or int to specify the level of verbosity with `git` `commit`. See [git-commit\[1\]](https://git-scm.com/docs/git-commit) for details.

[](#Documentation/git-config.txt-commitGraphgenerationVersion)commitGraph.generationVersion

Specifies the type of generation number version to use when writing or reading the commit-graph file. If version 1 is specified, then the corrected commit dates will not be written or read. Defaults to 2.

[](#Documentation/git-config.txt-commitGraphmaxNewFilters)commitGraph.maxNewFilters

Specifies the default value for the `--max-new-filters` option of `git` `commit-graph` `write` (c.f., [git-commit-graph\[1\]](https://git-scm.com/docs/git-commit-graph)).

[](#Documentation/git-config.txt-commitGraphreadChangedPaths)commitGraph.readChangedPaths

Deprecated. Equivalent to commitGraph.changedPathsVersion=-1 if true, and commitGraph.changedPathsVersion=0 if false. (If commitGraph.changedPathVersion is also set, commitGraph.changedPathsVersion takes precedence.)

[](#Documentation/git-config.txt-commitGraphchangedPathsVersion)commitGraph.changedPathsVersion

Specifies the version of the changed-path Bloom filters that Git will read and write. May be -1, 0, 1, or 2. Note that values greater than 1 may be incompatible with older versions of Git which do not yet understand those versions. Use caution when operating in a mixed-version environment.

Defaults to -1.

If -1, Git will use the version of the changed-path Bloom filters in the repository, defaulting to 1 if there are none.

If 0, Git will not read any Bloom filters, and will write version 1 Bloom filters when instructed to write.

If 1, Git will only read version 1 Bloom filters, and will write version 1 Bloom filters.

If 2, Git will only read version 2 Bloom filters, and will write version 2 Bloom filters.

[](#Documentation/git-config.txt-completioncommands)completion.commands

This is only used by git-completion.bash to add or remove commands from the list of completed commands. Normally only porcelain commands and a few select others are completed. You can add more commands, separated by space, in this variable. Prefixing the command with *-* will remove it from the existing list.

[](#Documentation/git-config.txt-corefileMode)core.fileMode

Tells Git if the executable bit of files in the working tree is to be honored.

Some filesystems lose the executable bit when a file that is marked as executable is checked out, or checks out a non-executable file with executable bit on. [git-clone\[1\]](https://git-scm.com/docs/git-clone) or [git-init\[1\]](https://git-scm.com/docs/git-init) probe the filesystem to see if it handles the executable bit correctly and this variable is automatically set as necessary.

A repository, however, may be on a filesystem that handles the filemode correctly, and this variable is set to *true* when created, but later may be made accessible from another environment that loses the filemode (e.g. exporting ext4 via CIFS mount, visiting a Cygwin created repository with Git for Windows or Eclipse). In such a case it may be necessary to set this variable to *false*. See [git-update-index\[1\]](https://git-scm.com/docs/git-update-index).

The default is true (when core.filemode is not specified in the config file).

[](#Documentation/git-config.txt-corehideDotFiles)core.hideDotFiles

(Windows-only) If true, mark newly-created directories and files whose name starts with a dot as hidden. If *dotGitOnly*, only the `.git/` directory is hidden, but no other files starting with a dot. The default mode is *dotGitOnly*.

[](#Documentation/git-config.txt-coreignoreCase)core.ignoreCase

Internal variable which enables various workarounds to enable Git to work better on filesystems that are not case sensitive, like APFS, HFS+, FAT, NTFS, etc. For example, if a directory listing finds "makefile" when Git expects "Makefile", Git will assume it is really the same file, and continue to remember it as "Makefile".

The default is false, except [git-clone\[1\]](https://git-scm.com/docs/git-clone) or [git-init\[1\]](https://git-scm.com/docs/git-init) will probe and set core.ignoreCase true if appropriate when the repository is created.

Git relies on the proper configuration of this variable for your operating and file system. Modifying this value may result in unexpected behavior.

[](#Documentation/git-config.txt-coreprecomposeUnicode)core.precomposeUnicode

This option is only used by Mac OS implementation of Git. When core.precomposeUnicode=true, Git reverts the unicode decomposition of filenames done by Mac OS. This is useful when sharing a repository between Mac OS and Linux or Windows. (Git for Windows 1.7.10 or higher is needed, or Git under cygwin 1.7). When false, file names are handled fully transparent by Git, which is backward compatible with older versions of Git.

[](#Documentation/git-config.txt-coreprotectHFS)core.protectHFS

If set to true, do not allow checkout of paths that would be considered equivalent to `.git` on an HFS+ filesystem. Defaults to `true` on Mac OS, and `false` elsewhere.

[](#Documentation/git-config.txt-coreprotectNTFS)core.protectNTFS

If set to true, do not allow checkout of paths that would cause problems with the NTFS filesystem, e.g. conflict with 8.3 "short" names. Defaults to `true` on Windows, and `false` elsewhere.

[](#Documentation/git-config.txt-corefsmonitor)core.fsmonitor

If set to true, enable the built-in file system monitor daemon for this working directory ([git-fsmonitor--daemon\[1\]](https://git-scm.com/docs/git-fsmonitor--daemon)).

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
