---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#19-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-19-variables
type: reference
title: Git - git-config Documentation › Variables (13/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#19-variables
source_hash: ab20293407642665580ab1b26532fd8ed31c4e1ea458c395f53f72cbce8dcff0
---
An integer -1..9, indicating the compression level for objects that are not in a pack file. -1 is the zlib default. 0 means no compression, and 1..9 are various speed/size tradeoffs, 9 being slowest. If not set, defaults to core.compression. If that is not set, defaults to 1 (best speed).

[](#Documentation/git-config.txt-corepackedGitWindowSize)core.packedGitWindowSize

Number of bytes of a pack file to map into memory in a single mapping operation. Larger window sizes may allow your system to process a smaller number of large pack files more quickly. Smaller window sizes will negatively affect performance due to increased calls to the operating system’s memory manager, but may improve performance when accessing a large number of large pack files.

Default is 1 MiB if NO\_MMAP was set at compile time, otherwise 32 MiB on 32 bit platforms and 1 GiB on 64 bit platforms. This should be reasonable for all users/operating systems. You probably do not need to adjust this value.

Common unit suffixes of *k*, *m*, or *g* are supported.

[](#Documentation/git-config.txt-corepackedGitLimit)core.packedGitLimit

Maximum number of bytes to map simultaneously into memory from pack files. If Git needs to access more than this many bytes at once to complete an operation it will unmap existing regions to reclaim virtual address space within the process.

Default is 256 MiB on 32 bit platforms and 32 TiB (effectively unlimited) on 64 bit platforms. This should be reasonable for all users/operating systems, except on the largest projects. You probably do not need to adjust this value.

Common unit suffixes of *k*, *m*, or *g* are supported.

[](#Documentation/git-config.txt-coredeltaBaseCacheLimit)core.deltaBaseCacheLimit

Maximum number of bytes per thread to reserve for caching base objects that may be referenced by multiple deltified objects. By storing the entire decompressed base objects in a cache Git is able to avoid unpacking and decompressing frequently used base objects multiple times.

Default is 96 MiB on all platforms. This should be reasonable for all users/operating systems, except on the largest projects. You probably do not need to adjust this value.

Common unit suffixes of *k*, *m*, or *g* are supported.

[](#Documentation/git-config.txt-corebigFileThreshold)core.bigFileThreshold

The size of files considered "big", which as discussed below changes the behavior of numerous git commands, as well as how such files are stored within the repository. The default is 512 MiB. Common unit suffixes of *k*, *m*, or *g* are supported.

Files above the configured limit will be:

- Stored deflated in packfiles, without attempting delta compression.

The default limit is primarily set with this use-case in mind. With it, most projects will have their source code and other text files delta compressed, but not larger binary media files.

Storing large files without delta compression avoids excessive memory usage, at the slight expense of increased disk usage.
- Will be treated as if they were labeled "binary" (see [gitattributes\[5\]](https://git-scm.com/docs/gitattributes)). e.g. [git-log\[1\]](https://git-scm.com/docs/git-log) and [git-diff\[1\]](https://git-scm.com/docs/git-diff) will not compute diffs for files above this limit.
- Will generally be streamed when written, which avoids excessive memory usage, at the cost of some fixed overhead. Commands that make use of this include [git-archive\[1\]](https://git-scm.com/docs/git-archive), [git-fast-import\[1\]](https://git-scm.com/docs/git-fast-import), [git-index-pack\[1\]](https://git-scm.com/docs/git-index-pack), [git-unpack-objects\[1\]](https://git-scm.com/docs/git-unpack-objects) and [git-fsck\[1\]](https://git-scm.com/docs/git-fsck).

[](#Documentation/git-config.txt-coreexcludesFile)core.excludesFile

Specifies the pathname to the file that contains patterns to describe paths that are not meant to be tracked, in addition to `.gitignore` (per-directory) and `.git/info/exclude`. Defaults to `$XDG_CONFIG_HOME/git/ignore`. If `$XDG_CONFIG_HOME` is either not set or empty, `$HOME/.config/git/ignore` is used instead. See [gitignore\[5\]](https://git-scm.com/docs/gitignore).

[](#Documentation/git-config.txt-coreaskPass)core.askPass

Some commands (e.g. svn and http interfaces) that interactively ask for a password can be told to use an external program given via the value of this variable. Can be overridden by the `GIT_ASKPASS` environment variable. If not set, fall back to the value of the `SSH_ASKPASS` environment variable or, failing that, a simple password prompt. The external program shall be given a suitable prompt as command-line argument and write the password on its STDOUT.

[](#Documentation/git-config.txt-coreattributesFile)core.attributesFile

In addition to `.gitattributes` (per-directory) and `.git/info/attributes`, Git looks into this file for attributes (see [gitattributes\[5\]](https://git-scm.com/docs/gitattributes)). Path expansions are made the same way as for `core.excludesFile`. Its default value is `$XDG_CONFIG_HOME/git/attributes`. If `$XDG_CONFIG_HOME` is either not set or empty, `$HOME/.config/git/attributes` is used instead.

[](#Documentation/git-config.txt-corehooksPath)core.hooksPath

By default Git will look for your hooks in the `$GIT_DIR/hooks` directory. Set this to different path, e.g. `/etc/git/hooks`, and Git will try to find your hooks in that directory, e.g. `/etc/git/hooks/pre-receive` instead of in `$GIT_DIR/hooks/pre-receive`.

The path can be either absolute or relative. A relative path is taken as relative to the directory where the hooks are run (see the "DESCRIPTION" section of [githooks\[5\]](https://git-scm.com/docs/githooks)).

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
