---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#20-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-20-variables
type: reference
title: Git - git-config Documentation › Variables (14/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#20-variables
source_hash: 6acd939406c6dcdce62c896cb77964f433ce6e8c3e53f9af3127c834aa6b757c
---
This configuration variable is useful in cases where you’d like to centrally configure your Git hooks instead of configuring them on a per-repository basis, or as a more flexible and centralized alternative to having an `init.templateDir` where you’ve changed default hooks.

You can also disable all hooks entirely by setting `core.hooksPath` to `/dev/null`. This is usually only advisable for expert users and on a per-command basis using configuration parameters of the form `git` `-c` `core.hooksPath=/dev/null` ....

[](#Documentation/git-config.txt-coreeditor)core.editor

Commands such as `commit` and `tag` that let you edit messages by launching an editor use the value of this variable when it is set, and the environment variable `GIT_EDITOR` is not set. See [git-var\[1\]](https://git-scm.com/docs/git-var).

Commands such as `commit` and `tag` that let you edit messages consider a line that begins with this character commented, and removes them after the editor returns (default *#*).

If set to "auto", `git-commit` would select a character that is not the beginning character of any line in existing commit messages.

Note that these two variables are aliases of each other, and in modern versions of Git you are free to use a string (e.g., `//` or *⁑⁕⁑*) with `commentChar`. Versions of Git prior to v2.45.0 will ignore `commentString` but will reject a value of `commentChar` that consists of more than a single ASCII byte. If you plan to use your config with older and newer versions of Git, you may want to specify both:

```
[core]
# single character for older versions
commentChar = "#"
# string for newer versions (which will override commentChar
# because it comes later in the file)
commentString = "//"
```

[](#Documentation/git-config.txt-corefilesRefLockTimeout)core.filesRefLockTimeout

The length of time, in milliseconds, to retry when trying to lock an individual reference. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 100 (i.e., retry for 100ms).

[](#Documentation/git-config.txt-corepackedRefsTimeout)core.packedRefsTimeout

The length of time, in milliseconds, to retry when trying to lock the `packed-refs` file. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 1000 (i.e., retry for 1 second).

Text viewer for use by Git commands (e.g., *less*). The value is meant to be interpreted by the shell. The order of preference is the `$GIT_PAGER` environment variable, then `core.pager` configuration, then `$PAGER`, and then the default chosen at compile time (usually *less*).

When the `LESS` environment variable is unset, Git sets it to `FRX` (if `LESS` environment variable is set, Git does not change it at all). If you want to selectively override Git’s default setting for `LESS`, you can set `core.pager` to e.g. `less` `-S`. This will be passed to the shell by Git, which will translate the final command to `LESS=FRX` `less` `-S`. The environment does not set the `S` option but the command line does, instructing less to truncate long lines. Similarly, setting `core.pager` to `less` `-+F` will deactivate the `F` option specified by the environment from the command-line, deactivating the "quit if one screen" behavior of `less`. One can specifically activate some flags for particular commands: for example, setting `pager.blame` to `less` `-S` enables line truncation only for `git` `blame`.

Likewise, when the `LV` environment variable is unset, Git sets it to `-c`. You can override this setting by exporting `LV` with another value or setting `core.pager` to `lv` `+c`.

[](#Documentation/git-config.txt-corewhitespace)core.whitespace

A comma separated list of common whitespace problems to notice. *git diff* will use `color.diff.whitespace` to highlight them, and *git apply --whitespace=error* will consider them as errors. You can prefix `-` to disable any of them (e.g. `-trailing-space`):

- `blank-at-eol` treats trailing whitespaces at the end of the line as an error (enabled by default).
- `space-before-tab` treats a space character that appears immediately before a tab character in the initial indent part of the line as an error (enabled by default).
- `indent-with-non-tab` treats a line that is indented with space characters instead of the equivalent tabs as an error (not enabled by default).
- `tab-in-indent` treats a tab character in the initial indent part of the line as an error (not enabled by default).
- `blank-at-eof` treats blank lines added at the end of file as an error (enabled by default).
- `trailing-space` is a short-hand to cover both `blank-at-eol` and `blank-at-eof`.
- `cr-at-eol` treats a carriage-return at the end of line as part of the line terminator, i.e. with it, `trailing-space` does not trigger if the character before such a carriage-return is not a whitespace (not enabled by default).
- `tabwidth=`*&lt;n&gt;* tells how many character positions a tab occupies; this is relevant for `indent-with-non-tab` and when Git fixes `tab-in-indent` errors. The default tab width is 8. Allowed values are 1 to 63.

[](#Documentation/git-config.txt-corefsync)core.fsync

A comma-separated list of components of the repository that should be hardened via the core.fsyncMethod when created or modified. You can disable hardening of any component by prefixing it with a *-*. Items that are not hardened may be lost in the event of an unclean system shutdown. Unless you have special requirements, it is recommended that you leave this option empty or pick one of `committed`, `added`, or `all`.

When this configuration is encountered, the set of components starts with the platform default value, disabled components are removed, and additional components are added. `none` resets the state so that the platform default is ignored.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
