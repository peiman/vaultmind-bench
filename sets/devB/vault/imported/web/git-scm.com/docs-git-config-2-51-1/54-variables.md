---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#54-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-54-variables
type: reference
title: Git - git-config Documentation › Variables (48/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#54-variables
source_hash: dacd721351811609b17a6730606439a136109acb63caf6c70e8f9a6612a2b8ea
---
[](#Documentation/git-config.txt-sendemailsmtpServer)sendemail.smtpServer

[](#Documentation/git-config.txt-sendemailsmtpServerPort)sendemail.smtpServerPort

[](#Documentation/git-config.txt-sendemailsmtpServerOption)sendemail.smtpServerOption

[](#Documentation/git-config.txt-sendemailsmtpUser)sendemail.smtpUser

[](#Documentation/git-config.txt-sendemailthread)sendemail.thread

[](#Documentation/git-config.txt-sendemailtransferEncoding)sendemail.transferEncoding

[](#Documentation/git-config.txt-sendemailvalidate)sendemail.validate

[](#Documentation/git-config.txt-sendemailxmailer)sendemail.xmailer

These configuration variables all provide a default for [git-send-email\[1\]](https://git-scm.com/docs/git-send-email) command-line options. See its documentation for details.

[](#Documentation/git-config.txt-sendemailoutlookidfix)sendemail.outlookidfix

If `true`, makes [git-send-email\[1\]](https://git-scm.com/docs/git-send-email) assume `--outlook-id-fix`, and if `false` assume `--no-outlook-id-fix`. If not specified, it will behave the same way as if `--outlook-id-fix` is not specified.

[](#Documentation/git-config.txt-sendemailsignedOffCcdeprecated)sendemail.signedOffCc (deprecated)

Deprecated alias for `sendemail.signedOffByCc`.

[](#Documentation/git-config.txt-sendemailsmtpBatchSize)sendemail.smtpBatchSize

Number of messages to be sent per connection, after that a relogin will happen. If the value is `0` or undefined, send all messages in one connection. See also the `--batch-size` option of [git-send-email\[1\]](https://git-scm.com/docs/git-send-email).

[](#Documentation/git-config.txt-sendemailsmtpReloginDelay)sendemail.smtpReloginDelay

Seconds to wait before reconnecting to the smtp server. See also the `--relogin-delay` option of [git-send-email\[1\]](https://git-scm.com/docs/git-send-email).

[](#Documentation/git-config.txt-sendemailforbidSendmailVariables)sendemail.forbidSendmailVariables

To avoid common misconfiguration mistakes, [git-send-email\[1\]](https://git-scm.com/docs/git-send-email) will abort with a warning if any configuration options for `sendmail` exist. Set this variable to bypass the check.

[](#Documentation/git-config.txt-sequenceeditor)sequence.editor

Text editor used by `git` `rebase` `-i` for editing the rebase instruction file. The value is meant to be interpreted by the shell when it is used. It can be overridden by the `GIT_SEQUENCE_EDITOR` environment variable. When not configured, the default commit message editor is used instead.

[](#Documentation/git-config.txt-showBranchdefault)showBranch.default

The default set of branches for [git-show-branch\[1\]](https://git-scm.com/docs/git-show-branch). See [git-show-branch\[1\]](https://git-scm.com/docs/git-show-branch).

[](#Documentation/git-config.txt-sparseexpectFilesOutsideOfPatterns)sparse.expectFilesOutsideOfPatterns

Typically with sparse checkouts, files not matching any sparsity patterns are marked with a SKIP\_WORKTREE bit in the index and are missing from the working tree. Accordingly, Git will ordinarily check whether files with the SKIP\_WORKTREE bit are in fact present in the working tree contrary to expectations. If Git finds any, it marks those paths as present by clearing the relevant SKIP\_WORKTREE bits. This option can be used to tell Git that such present-despite-skipped files are expected and to stop checking for them.

The default is `false`, which allows Git to automatically recover from the list of files in the index and working tree falling out of sync.

Set this to `true` if you are in a setup where some external factor relieves Git of the responsibility for maintaining the consistency between the presence of working tree files and sparsity patterns. For example, if you have a Git-aware virtual file system that has a robust mechanism for keeping the working tree and the sparsity patterns up to date based on access patterns.

Regardless of this setting, Git does not check for present-despite-skipped files unless sparse checkout is enabled, so this config option has no effect unless `core.sparseCheckout` is `true`.

[](#Documentation/git-config.txt-splitIndexmaxPercentChange)splitIndex.maxPercentChange

When the split index feature is used, this specifies the percent of entries the split index can contain compared to the total number of entries in both the split index and the shared index before a new shared index is written. The value should be between 0 and 100. If the value is 0, then a new shared index is always written; if it is 100, a new shared index is never written. By default, the value is 20, so a new shared index is written if the number of entries in the split index would be greater than 20 percent of the total number of entries. See [git-update-index\[1\]](https://git-scm.com/docs/git-update-index).

[](#Documentation/git-config.txt-splitIndexsharedIndexExpire)splitIndex.sharedIndexExpire

When the split index feature is used, shared index files that were not modified since the time this variable specifies will be removed when a new shared index file is created. The value "now" expires all entries immediately, and "never" suppresses expiration altogether. The default value is "2.weeks.ago". Note that a shared index file is considered modified (for the purpose of expiration) each time a new split-index file is either created based on it or read from it. See [git-update-index\[1\]](https://git-scm.com/docs/git-update-index).

[](#Documentation/git-config.txt-sshvariant)ssh.variant

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
