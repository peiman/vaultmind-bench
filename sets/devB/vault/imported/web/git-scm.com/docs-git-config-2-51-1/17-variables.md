---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#17-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-17-variables
type: reference
title: Git - git-config Documentation › Variables (11/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#17-variables
source_hash: 8d94c04ed43d9451595f8a8d5b3b060f3245503c4247675496f1c80a22022ac6
---
If true, makes Git check if converting `CRLF` is reversible when end-of-line conversion is active. Git will verify if a command modifies a file in the work tree either directly or indirectly. For example, committing a file followed by checking out the same file should yield the original file in the work tree. If this is not the case for the current setting of `core.autocrlf`, Git will reject the file. The variable can be set to "warn", in which case Git will only warn about an irreversible conversion but continue the operation.

CRLF conversion bears a slight chance of corrupting data. When it is enabled, Git will convert CRLF to LF during commit and LF to CRLF during checkout. A file that contains a mixture of LF and CRLF before the commit cannot be recreated by Git. For text files this is the right thing to do: it corrects line endings such that we have only LF line endings in the repository. But for binary files that are accidentally classified as text the conversion can corrupt data.

If you recognize such corruption early you can easily fix it by setting the conversion type explicitly in .gitattributes. Right after committing you still have the original file in your work tree and this file is not yet corrupted. You can explicitly tell Git that this file is binary and Git will handle the file appropriately.

Unfortunately, the desired effect of cleaning up text files with mixed line endings and the undesired effect of corrupting binary files cannot be distinguished. In both cases CRLFs are removed in an irreversible way. For text files this is the right thing to do because CRLFs are line endings, while for binary files converting CRLFs corrupts data.

Note, this safety check does not mean that a checkout will generate a file identical to the original file for a different setting of `core.eol` and `core.autocrlf`, but only for the current one. For example, a text file with `LF` would be accepted with `core.eol=lf` and could later be checked out with `core.eol=crlf`, in which case the resulting file would contain `CRLF`, although the original file contained `LF`. However, in both work trees the line endings would be consistent, that is either all `LF` or all `CRLF`, but never mixed. A file with mixed line endings would be reported by the `core.safecrlf` mechanism.

[](#Documentation/git-config.txt-coreautocrlf)core.autocrlf

Setting this variable to "true" is the same as setting the `text` attribute to "auto" on all files and core.eol to "crlf". Set to true if you want to have `CRLF` line endings in your working directory and the repository has LF line endings. This variable can be set to *input*, in which case no output conversion is performed.

[](#Documentation/git-config.txt-corecheckRoundtripEncoding)core.checkRoundtripEncoding

A comma and/or whitespace separated list of encodings that Git performs UTF-8 round trip checks on if they are used in an `working-tree-encoding` attribute (see [gitattributes\[5\]](https://git-scm.com/docs/gitattributes)). The default value is `SHIFT-JIS`.

[](#Documentation/git-config.txt-coresymlinks)core.symlinks

If false, symbolic links are checked out as small plain files that contain the link text. [git-update-index\[1\]](https://git-scm.com/docs/git-update-index) and [git-add\[1\]](https://git-scm.com/docs/git-add) will not change the recorded type to regular file. Useful on filesystems like FAT that do not support symbolic links.

The default is true, except [git-clone\[1\]](https://git-scm.com/docs/git-clone) or [git-init\[1\]](https://git-scm.com/docs/git-init) will probe and set core.symlinks false if appropriate when the repository is created.

[](#Documentation/git-config.txt-coregitProxy)core.gitProxy

A "proxy command" to execute (as *command host port*) instead of establishing direct connection to the remote server when using the Git protocol for fetching. If the variable value is in the "COMMAND for DOMAIN" format, the command is applied only on hostnames ending with the specified domain string. This variable may be set multiple times and is matched in the given order; the first match wins.

Can be overridden by the `GIT_PROXY_COMMAND` environment variable (which always applies universally, without the special "for" handling).

The special string `none` can be used as the proxy command to specify that no proxy be used for a given domain pattern. This is useful for excluding servers inside a firewall from proxy use, while defaulting to a common proxy for external domains.

[](#Documentation/git-config.txt-coresshCommand)core.sshCommand

If this variable is set, `git` `fetch` and `git` `push` will use the specified command instead of `ssh` when they need to connect to a remote system. The command is in the same form as the `GIT_SSH_COMMAND` environment variable and is overridden when the environment variable is set.

[](#Documentation/git-config.txt-coreignoreStat)core.ignoreStat

If true, Git will avoid using lstat() calls to detect if files have changed by setting the "assume-unchanged" bit for those tracked files which it has updated identically in both the index and working tree.

When files are modified outside of Git, the user will need to stage the modified files explicitly (e.g. see *Examples* section in [git-update-index\[1\]](https://git-scm.com/docs/git-update-index)). Git will not normally detect changes to those files.

This is useful on systems where lstat() calls are very slow, such as CIFS/Microsoft Windows.

False by default.

[](#Documentation/git-config.txt-corepreferSymlinkRefs)core.preferSymlinkRefs

Instead of the default "symref" format for HEAD and other symbolic reference files, use symbolic links. This is sometimes needed to work with old scripts that expect HEAD to be a symbolic link.

[](#Documentation/git-config.txt-corealternateRefsCommand)core.alternateRefsCommand

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
