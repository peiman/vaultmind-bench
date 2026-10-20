---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#49-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-49-variables
type: reference
title: Git - git-config Documentation › Variables (43/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#49-variables
source_hash: 3884bf232a93badc449939550f3b81239e01dcb97b837ce8a74a68961688b205
---
[](#Documentation/git-config.txt-rebasemaxLabelLength)rebase.maxLabelLength

When generating label names from commit subjects, truncate the names to this length. By default, the names are truncated to a little less than `NAME_MAX` (to allow e.g. `.lock` files to be written for the corresponding loose refs).

[](#Documentation/git-config.txt-receiveadvertiseAtomic)receive.advertiseAtomic

By default, git-receive-pack will advertise the atomic push capability to its clients. If you don’t want to advertise this capability, set this variable to false.

[](#Documentation/git-config.txt-receiveadvertisePushOptions)receive.advertisePushOptions

When set to true, git-receive-pack will advertise the push options capability to its clients. False by default.

[](#Documentation/git-config.txt-receiveautogc)receive.autogc

By default, git-receive-pack will run "git maintenance run --auto" after receiving data from git-push and updating refs. You can stop it by setting this variable to false.

[](#Documentation/git-config.txt-receivecertNonceSeed)receive.certNonceSeed

By setting this variable to a string, `git` `receive-pack` will accept a `git` `push` `--signed` and verify it by using a "nonce" protected by HMAC using this string as a secret key.

[](#Documentation/git-config.txt-receivecertNonceSlop)receive.certNonceSlop

When a `git` `push` `--signed` sends a push certificate with a "nonce" that was issued by a receive-pack serving the same repository within this many seconds, export the "nonce" found in the certificate to `GIT_PUSH_CERT_NONCE` to the hooks (instead of what the receive-pack asked the sending side to include). This may allow writing checks in `pre-receive` and `post-receive` a bit easier. Instead of checking `GIT_PUSH_CERT_NONCE_SLOP` environment variable that records by how many seconds the nonce is stale to decide if they want to accept the certificate, they only can check `GIT_PUSH_CERT_NONCE_STATUS` is `OK`.

[](#Documentation/git-config.txt-receivefsckObjects)receive.fsckObjects

If it is set to true, git-receive-pack will check all received objects. See `transfer.fsckObjects` for what’s checked. Defaults to false. If not set, the value of `transfer.fsckObjects` is used instead.

[](#Documentation/git-config.txt-receivefsckmsg-id)receive.fsck.&lt;msg-id&gt;

Acts like `fsck.`*&lt;msg-id&gt;*, but is used by [git-receive-pack\[1\]](https://git-scm.com/docs/git-receive-pack) instead of [git-fsck\[1\]](https://git-scm.com/docs/git-fsck). See the `fsck.`*&lt;msg-id&gt;* documentation for details.

[](#Documentation/git-config.txt-receivefsckskipList)receive.fsck.skipList

Acts like `fsck.skipList`, but is used by [git-receive-pack\[1\]](https://git-scm.com/docs/git-receive-pack) instead of [git-fsck\[1\]](https://git-scm.com/docs/git-fsck). See the `fsck.skipList` documentation for details.

[](#Documentation/git-config.txt-receivekeepAlive)receive.keepAlive

After receiving the pack from the client, `receive-pack` may produce no output (if `--quiet` was specified) while processing the pack, causing some networks to drop the TCP connection. With this option set, if `receive-pack` does not transmit any data in this phase for `receive.keepAlive` seconds, it will send a short keepalive packet. The default is 5 seconds; set to 0 to disable keepalives entirely.

[](#Documentation/git-config.txt-receiveunpackLimit)receive.unpackLimit

If the number of objects received in a push is below this limit then the objects will be unpacked into loose object files. However if the number of received objects equals or exceeds this limit then the received pack will be stored as a pack, after adding any missing delta bases. Storing the pack from a push can make the push operation complete faster, especially on slow filesystems. If not set, the value of `transfer.unpackLimit` is used instead.

[](#Documentation/git-config.txt-receivemaxInputSize)receive.maxInputSize

If the size of the incoming pack stream is larger than this limit, then git-receive-pack will error out, instead of accepting the pack file. If not set or set to 0, then the size is unlimited.

[](#Documentation/git-config.txt-receivedenyDeletes)receive.denyDeletes

If set to true, git-receive-pack will deny a ref update that deletes the ref. Use this to prevent such a ref deletion via a push.

[](#Documentation/git-config.txt-receivedenyDeleteCurrent)receive.denyDeleteCurrent

If set to true, git-receive-pack will deny a ref update that deletes the currently checked out branch of a non-bare repository.

[](#Documentation/git-config.txt-receivedenyCurrentBranch)receive.denyCurrentBranch

If set to true or "refuse", git-receive-pack will deny a ref update to the currently checked out branch of a non-bare repository. Such a push is potentially dangerous because it brings the HEAD out of sync with the index and working tree. If set to "warn", print a warning of such a push to stderr, but allow the push to proceed. If set to false or "ignore", allow such pushes with no message. Defaults to "refuse".

Another option is "updateInstead" which will update the working tree if pushing into the current branch. This option is intended for synchronizing working directories when one side is not easily accessible via interactive ssh (e.g. a live web site, hence the requirement that the working directory be clean). This mode also comes in handy when developing inside a VM to test and fix code on different Operating Systems.

By default, "updateInstead" will refuse the push if the working tree or the index have any difference from the HEAD, but the `push-to-checkout` hook can be used to customize this. See [githooks\[5\]](https://git-scm.com/docs/githooks).

[](#Documentation/git-config.txt-receivedenyNonFastForwards)receive.denyNonFastForwards

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
