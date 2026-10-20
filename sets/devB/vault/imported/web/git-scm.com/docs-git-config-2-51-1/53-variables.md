---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#53-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-53-variables
type: reference
title: Git - git-config Documentation › Variables (47/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#53-variables
source_hash: af2620fc31132254686442623d8b03d4924e80d8f9e2d85ffc23f228eb4fa9cb
---
To completely opt-out of this security check, set `safe.directory` to the string `*`. This will allow all repositories to be treated as if their directory was listed in the `safe.directory` list. If `safe.directory=*` is set in system config and you want to re-enable this protection, then initialize your list with an empty value before listing the repositories that you deem safe. Giving a directory with `/*` appended to it will allow access to all repositories under the named directory.

As explained, Git only allows you to access repositories owned by yourself, i.e. the user who is running Git, by default. When Git is running as *root* in a non Windows platform that provides sudo, however, git checks the SUDO\_UID environment variable that sudo creates and will allow access to the uid recorded as its value in addition to the id from *root*. This is to make it easy to perform a common sequence during installation "make && sudo make install". A git process running under *sudo* runs as *root* but the *sudo* command exports the environment variable to record which id the original user has. If that is not what you would prefer and want git to only trust repositories that are owned by root instead, then you can remove the `SUDO_UID` variable from root’s environment before invoking git.

[](#Documentation/git-config.txt-sendemailidentity)sendemail.identity

A configuration identity. When given, causes values in the `sendemail.`*&lt;identity&gt;* subsection to take precedence over values in the `sendemail` section. The default identity is the value of `sendemail.identity`.

[](#Documentation/git-config.txt-sendemailsmtpEncryption)sendemail.smtpEncryption

See [git-send-email\[1\]](https://git-scm.com/docs/git-send-email) for description. Note that this setting is not subject to the `identity` mechanism.

[](#Documentation/git-config.txt-sendemailsmtpSSLCertPath)sendemail.smtpSSLCertPath

Path to ca-certificates (either a directory or a single file). Set it to an empty string to disable certificate verification.

[](#Documentation/git-config.txt-sendemailidentity-1)sendemail.&lt;identity&gt;.*

Identity-specific versions of the `sendemail.*` parameters found below, taking precedence over those when this identity is selected, through either the command-line or `sendemail.identity`.

[](#Documentation/git-config.txt-sendemailmultiEdit)sendemail.multiEdit

If `true` (default), a single editor instance will be spawned to edit files you have to edit (patches when `--annotate` is used, and the summary when `--compose` is used). If `false`, files will be edited one after the other, spawning a new editor each time.

[](#Documentation/git-config.txt-sendemailconfirm)sendemail.confirm

Sets the default for whether to confirm before sending. Must be one of `always`, `never`, `cc`, `compose`, or `auto`. See `--confirm` in the [git-send-email\[1\]](https://git-scm.com/docs/git-send-email) documentation for the meaning of these values.

[](#Documentation/git-config.txt-sendemailmailmap)sendemail.mailmap

If `true`, makes [git-send-email\[1\]](https://git-scm.com/docs/git-send-email) assume `--mailmap`, otherwise assume `--no-mailmap`. `False` by default.

[](#Documentation/git-config.txt-sendemailmailmapfile)sendemail.mailmap.file

The location of a [git-send-email\[1\]](https://git-scm.com/docs/git-send-email) specific augmenting mailmap file. The default mailmap and `mailmap.file` are loaded first. Thus, entries in this file take precedence over entries in the default mailmap locations. See [gitmailmap\[5\]](https://git-scm.com/docs/gitmailmap).

[](#Documentation/git-config.txt-sendemailmailmapblob)sendemail.mailmap.blob

Like `sendemail.mailmap.file`, but consider the value as a reference to a blob in the repository. Entries in `sendemail.mailmap.file` take precedence over entries here. See [gitmailmap\[5\]](https://git-scm.com/docs/gitmailmap).

[](#Documentation/git-config.txt-sendemailaliasesFile)sendemail.aliasesFile

To avoid typing long email addresses, point this to one or more email aliases files. You must also supply `sendemail.aliasFileType`.

[](#Documentation/git-config.txt-sendemailaliasFileType)sendemail.aliasFileType

Format of the file(s) specified in sendemail.aliasesFile. Must be one of `mutt`, `mailrc`, `pine`, `elm`, `gnus`, or `sendmail`.

What an alias file in each format looks like can be found in the documentation of the email program of the same name. The differences and limitations from the standard formats are described below:

[](#Documentation/git-config.txt-sendmail)sendmail

- Quoted aliases and quoted addresses are not supported: lines that contain a `"` symbol are ignored.
- Redirection to a file (`/path/name`) or pipe (|`command`) is not supported.
- File inclusion (`:include:` `/path/name`) is not supported.
- Warnings are printed on the standard error output for any explicitly unsupported constructs, and any other lines that are not recognized by the parser.

[](#Documentation/git-config.txt-sendemailannotate)sendemail.annotate

[](#Documentation/git-config.txt-sendemailbcc)sendemail.bcc

[](#Documentation/git-config.txt-sendemailcc)sendemail.cc

[](#Documentation/git-config.txt-sendemailccCmd)sendemail.ccCmd

[](#Documentation/git-config.txt-sendemailchainReplyTo)sendemail.chainReplyTo

[](#Documentation/git-config.txt-sendemailenvelopeSender)sendemail.envelopeSender

[](#Documentation/git-config.txt-sendemailfrom)sendemail.from

[](#Documentation/git-config.txt-sendemailsignedOffByCc)sendemail.signedOffByCc

[](#Documentation/git-config.txt-sendemailsmtpPass)sendemail.smtpPass

[](#Documentation/git-config.txt-sendemailsuppressCc)sendemail.suppressCc

[](#Documentation/git-config.txt-sendemailsuppressFrom)sendemail.suppressFrom

[](#Documentation/git-config.txt-sendemailto)sendemail.to

[](#Documentation/git-config.txt-sendemailtoCmd)sendemail.toCmd

[](#Documentation/git-config.txt-sendemailsmtpDomain)sendemail.smtpDomain

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
