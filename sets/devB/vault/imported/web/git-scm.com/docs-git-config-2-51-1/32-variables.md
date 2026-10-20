---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#32-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-32-variables
type: reference
title: Git - git-config Documentation › Variables (26/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#32-variables
source_hash: 3662e8b967bb2b2f456ff1c12899a0ba8e27b949e067bb69c00d1c2e613171cb
---
Database user and password. Only useful if setting `gitcvs.dbDriver`, since SQLite has no concept of database users and/or passwords. *gitcvs.dbUser* supports variable substitution (see [git-cvsserver\[1\]](https://git-scm.com/docs/git-cvsserver) for details).

[](#Documentation/git-config.txt-gitcvsdbTableNamePrefix)gitcvs.dbTableNamePrefix

Database table name prefix. Prepended to the names of any database tables used, allowing a single database to be used for several repositories. Supports variable substitution (see [git-cvsserver\[1\]](https://git-scm.com/docs/git-cvsserver) for details). Any non-alphabetic characters will be replaced with underscores.

All gitcvs variables except for `gitcvs.usecrlfattr` and `gitcvs.allBinary` can also be specified as *gitcvs.&lt;access\_method&gt;.&lt;varname&gt;* (where *access\_method* is one of "ext" and "pserver") to make them apply only for the given access method.

[](#Documentation/git-config.txt-gitwebcategory)gitweb.category

[](#Documentation/git-config.txt-gitwebdescription)gitweb.description

[](#Documentation/git-config.txt-gitwebowner)gitweb.owner

[](#Documentation/git-config.txt-gitweburl)gitweb.url

See [gitweb\[1\]](https://git-scm.com/docs/gitweb) for description.

[](#Documentation/git-config.txt-gitwebavatar)gitweb.avatar

[](#Documentation/git-config.txt-gitwebblame)gitweb.blame

[](#Documentation/git-config.txt-gitwebgrep)gitweb.grep

[](#Documentation/git-config.txt-gitwebhighlight)gitweb.highlight

[](#Documentation/git-config.txt-gitwebpatches)gitweb.patches

[](#Documentation/git-config.txt-gitwebpickaxe)gitweb.pickaxe

[](#Documentation/git-config.txt-gitwebremoteheads)gitweb.remote\_heads

[](#Documentation/git-config.txt-gitwebshowSizes)gitweb.showSizes

[](#Documentation/git-config.txt-gitwebsnapshot)gitweb.snapshot

See [gitweb.conf\[5\]](https://git-scm.com/docs/gitweb.conf) for description.

[](#Documentation/git-config.txt-gpgprogram)gpg.program

Pathname of the program to use instead of "`gpg`" when making or verifying a PGP signature. The program must support the same command-line interface as GPG, namely, to verify a detached signature, "*gpg --verify $signature - &lt;$file*" is run, and the program is expected to signal a good signature by exiting with code 0. To generate an ASCII-armored detached signature, the standard input of "`gpg` `-bsau` `$key`" is fed with the contents to be signed, and the program is expected to send the result to its standard output.

[](#Documentation/git-config.txt-gpgformat)gpg.format

Specifies which key format to use when signing with `--gpg-sign`. Default is "openpgp". Other possible values are "x509", "ssh".

See [gitformat-signature\[5\]](https://git-scm.com/docs/gitformat-signature) for the signature format, which differs based on the selected `gpg.format`.

[](#Documentation/git-config.txt-gpgformatprogram)gpg.&lt;format&gt;.program

Use this to customize the program used for the signing format you chose. (see `gpg.program` and `gpg.format`) `gpg.program` can still be used as a legacy synonym for `gpg.openpgp.program`. The default value for `gpg.x509.program` is "gpgsm" and `gpg.ssh.program` is "ssh-keygen".

[](#Documentation/git-config.txt-gpgminTrustLevel)gpg.minTrustLevel

Specifies a minimum trust level for signature verification. If this option is unset, then signature verification for merge operations requires a key with at least `marginal` trust. Other operations that perform signature verification require a key with at least `undefined` trust. Setting this option overrides the required trust-level for all operations. Supported values, in increasing order of significance:

- `undefined`
- `never`
- `marginal`
- `fully`
- `ultimate`

[](#Documentation/git-config.txt-gpgsshdefaultKeyCommand)gpg.ssh.defaultKeyCommand

This command will be run when user.signingkey is not set and a ssh signature is requested. On successful exit a valid ssh public key prefixed with `key::` is expected in the first line of its output. This allows for a script doing a dynamic lookup of the correct public key when it is impractical to statically configure `user.signingKey`. For example when keys or SSH Certificates are rotated frequently or selection of the right key depends on external factors unknown to git.

[](#Documentation/git-config.txt-gpgsshallowedSignersFile)gpg.ssh.allowedSignersFile

A file containing ssh public keys which you are willing to trust. The file consists of one or more lines of principals followed by an ssh public key. e.g.: `user1@example.com,user2@example.com` `ssh-rsa` `AAAAX1...` See ssh-keygen(1) "ALLOWED SIGNERS" for details. The principal is only used to identify the key and is available when verifying a signature.

SSH has no concept of trust levels like gpg does. To be able to differentiate between valid signatures and trusted signatures the trust level of a signature verification is set to `fully` when the public key is present in the allowedSignersFile. Otherwise the trust level is `undefined` and git verify-commit/tag will fail.

This file can be set to a location outside of the repository and every developer maintains their own trust store. A central repository server could generate this file automatically from ssh keys with push access to verify the code against. In a corporate setting this file is probably generated at a global location from automation that already handles developer ssh keys.

A repository that only allows signed commits can store the file in the repository itself using a path relative to the top-level of the working tree. This way only committers with an already valid key can add or change keys in the keyring.

Since OpensSSH 8.8 this file allows specifying a key lifetime using valid-after & valid-before options. Git will mark signatures as valid if the signing key was valid at the time of the signature’s creation. This allows users to change a signing key without invalidating all previously made signatures.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
