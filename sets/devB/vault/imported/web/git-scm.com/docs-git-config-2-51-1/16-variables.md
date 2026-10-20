---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#16-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-16-variables
type: reference
title: Git - git-config Documentation › Variables (10/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#16-variables
source_hash: 2f394d6c0cd188de7d14037856bdde49b0737b4975bdc0331ec4e1f3d180aea8
---
Like hook-based file system monitors, the built-in file system monitor can speed up Git commands that need to refresh the Git index (e.g. `git` `status`) in a working directory with many files. The built-in monitor eliminates the need to install and maintain an external third-party tool.

The built-in file system monitor is currently available only on a limited set of supported platforms. Currently, this includes Windows and MacOS.

```
Otherwise, this variable contains the pathname of the "fsmonitor"
hook command.
```

This hook command is used to identify all files that may have changed since the requested date/time. This information is used to speed up git by avoiding unnecessary scanning of files that have not changed.

See the "fsmonitor-watchman" section of [githooks\[5\]](https://git-scm.com/docs/githooks).

Note that if you concurrently use multiple versions of Git, such as one version on the command line and another version in an IDE tool, that the definition of `core.fsmonitor` was extended to allow boolean values in addition to hook pathnames. Git versions 2.35.1 and prior will not understand the boolean values and will consider the "true" or "false" values as hook pathnames to be invoked. Git versions 2.26 thru 2.35.1 default to hook protocol V2 and will fall back to no fsmonitor (full scan). Git versions prior to 2.26 default to hook protocol V1 and will silently assume there were no changes to report (no scan), so status commands may report incomplete results. For this reason, it is best to upgrade all of your Git versions before using the built-in file system monitor.

[](#Documentation/git-config.txt-corefsmonitorHookVersion)core.fsmonitorHookVersion

Sets the protocol version to be used when invoking the "fsmonitor" hook.

There are currently versions 1 and 2. When this is not set, version 2 will be tried first and if it fails then version 1 will be tried. Version 1 uses a timestamp as input to determine which files have changes since that time but some monitors like Watchman have race conditions when used with a timestamp. Version 2 uses an opaque string so that the monitor can return something that can be used to determine what files have changed without race conditions.

[](#Documentation/git-config.txt-coretrustctime)core.trustctime

If false, the ctime differences between the index and the working tree are ignored; useful when the inode change time is regularly modified by something outside Git (file system crawlers and some backup systems). See [git-update-index\[1\]](https://git-scm.com/docs/git-update-index). True by default.

[](#Documentation/git-config.txt-coresplitIndex)core.splitIndex

If true, the split-index feature of the index will be used. See [git-update-index\[1\]](https://git-scm.com/docs/git-update-index). False by default.

[](#Documentation/git-config.txt-coreuntrackedCache)core.untrackedCache

Determines what to do about the untracked cache feature of the index. It will be kept, if this variable is unset or set to `keep`. It will automatically be added if set to `true`. And it will automatically be removed, if set to `false`. Before setting it to `true`, you should check that mtime is working properly on your system. See [git-update-index\[1\]](https://git-scm.com/docs/git-update-index). `keep` by default, unless `feature.manyFiles` is enabled which sets this setting to `true` by default.

[](#Documentation/git-config.txt-corecheckStat)core.checkStat

When missing or is set to `default`, many fields in the stat structure are checked to detect if a file has been modified since Git looked at it. When this configuration variable is set to `minimal`, sub-second part of mtime and ctime, the uid and gid of the owner of the file, the inode number (and the device number, if Git was compiled to use it), are excluded from the check among these fields, leaving only the whole-second part of mtime (and ctime, if `core.trustCtime` is set) and the filesize to be checked.

There are implementations of Git that do not leave usable values in some fields (e.g. JGit); by excluding these fields from the comparison, the `minimal` mode may help interoperability when the same repository is used by these other systems at the same time.

[](#Documentation/git-config.txt-corequotePath)core.quotePath

Commands that output paths (e.g. *ls-files*, *diff*), will quote "unusual" characters in the pathname by enclosing the pathname in double-quotes and escaping those characters with backslashes in the same way C escapes control characters (e.g. *\\t* for TAB, *\\n* for LF, *\\\\* for backslash) or bytes with values larger than 0x80 (e.g. octal *\\302\\265* for "micro" in UTF-8). If this variable is set to false, bytes higher than 0x80 are not considered "unusual" any more. Double-quotes, backslash and control characters are always escaped regardless of the setting of this variable. A simple space character is not considered "unusual". Many commands can output pathnames completely verbatim using the `-z` option. The default value is true.

[](#Documentation/git-config.txt-coreeol)core.eol

Sets the line ending type to use in the working directory for files that are marked as text (either by having the `text` attribute set, or by having `text=auto` and Git auto-detecting the contents as text). Alternatives are *lf*, *crlf* and *native*, which uses the platform’s native line ending. The default value is `native`. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for more information on end-of-line conversion. Note that this value is ignored if `core.autocrlf` is set to `true` or `input`.

[](#Documentation/git-config.txt-coresafecrlf)core.safecrlf

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
