---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#50-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-50-variables
type: reference
title: Git - git-config Documentation › Variables (44/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#50-variables
source_hash: 90172cec87fa355f571147fa38a50f82405f843f9b74882494a048a637831caf
---
If set to true, git-receive-pack will deny a ref update which is not a fast-forward. Use this to prevent such an update via a push, even if that push is forced. This configuration variable is set when initializing a shared repository.

[](#Documentation/git-config.txt-receivehideRefs)receive.hideRefs

This variable is the same as `transfer.hideRefs`, but applies only to `receive-pack` (and so affects pushes, but not fetches). An attempt to update or delete a hidden ref by `git` `push` is rejected.

[](#Documentation/git-config.txt-receiveprocReceiveRefs)receive.procReceiveRefs

This is a multi-valued variable that defines reference prefixes to match the commands in `receive-pack`. Commands matching the prefixes will be executed by an external hook "proc-receive", instead of the internal `execute_commands` function. If this variable is not defined, the "proc-receive" hook will never be used, and all commands will be executed by the internal `execute_commands` function.

For example, if this variable is set to "refs/for", pushing to reference such as "refs/for/master" will not create or update a reference named "refs/for/master", but may create or update a pull request directly by running the hook "proc-receive".

Optional modifiers can be provided in the beginning of the value to filter commands for specific actions: create (a), modify (m), delete (d). A `!` can be included in the modifiers to negate the reference prefix entry. E.g.:

```
git config --system --add receive.procReceiveRefs ad:refs/heads
git config --system --add receive.procReceiveRefs !:refs/heads
```

[](#Documentation/git-config.txt-receiveupdateServerInfo)receive.updateServerInfo

If set to true, git-receive-pack will run git-update-server-info after receiving data from git-push and updating refs.

[](#Documentation/git-config.txt-receiveshallowUpdate)receive.shallowUpdate

If set to true, .git/shallow can be updated when new refs require new shallow roots. Otherwise those refs are rejected.

[](#Documentation/git-config.txt-reftableblockSize)reftable.blockSize

The size in bytes used by the reftable backend when writing blocks. The block size is determined by the writer, and does not have to be a power of 2. The block size must be larger than the longest reference name or log entry used in the repository, as references cannot span blocks.

Powers of two that are friendly to the virtual memory system or filesystem (such as 4kB or 8kB) are recommended. Larger sizes (64kB) can yield better compression, with a possible increased cost incurred by readers during access.

The largest block size is `16777215` bytes (15.99 MiB). The default value is `4096` bytes (4kB). A value of `0` will use the default value.

[](#Documentation/git-config.txt-reftablerestartInterval)reftable.restartInterval

The interval at which to create restart points. The reftable backend determines the restart points at file creation. Every 16 may be more suitable for smaller block sizes (4k or 8k), every 64 for larger block sizes (64k).

More frequent restart points reduces prefix compression and increases space consumed by the restart table, both of which increase file size.

Less frequent restart points makes prefix compression more effective, decreasing overall file size, with increased penalties for readers walking through more records after the binary search step.

A maximum of `65535` restart points per block is supported.

The default value is to create restart points every 16 records. A value of `0` will use the default value.

[](#Documentation/git-config.txt-reftableindexObjects)reftable.indexObjects

Whether the reftable backend shall write object blocks. Object blocks are a reverse mapping of object ID to the references pointing to them.

The default value is `true`.

[](#Documentation/git-config.txt-reftablegeometricFactor)reftable.geometricFactor

Whenever the reftable backend appends a new table to the stack, it performs auto compaction to ensure that there is only a handful of tables. The backend does this by ensuring that tables form a geometric sequence regarding the respective sizes of each table.

By default, the geometric sequence uses a factor of 2, meaning that for any table, the next-biggest table must at least be twice as big. A maximum factor of 256 is supported.

[](#Documentation/git-config.txt-reftablelockTimeout)reftable.lockTimeout

Whenever the reftable backend appends a new table to the stack, it has to lock the central "tables.list" file before updating it. This config controls how long the process will wait to acquire the lock in case another process has already acquired it. Value 0 means not to retry at all; -1 means to try indefinitely. Default is 100 (i.e., retry for 100ms).

[](#Documentation/git-config.txt-remotepushDefault)remote.pushDefault

The remote to push to by default. Overrides `branch.`*&lt;name&gt;*`.remote` for all branches, and is overridden by `branch.`*&lt;name&gt;*`.pushRemote` for specific branches.

[](#Documentation/git-config.txt-remotenameurl)remote.&lt;name&gt;.url

The URL of a remote repository. See [git-fetch\[1\]](https://git-scm.com/docs/git-fetch) or [git-push\[1\]](https://git-scm.com/docs/git-push). A configured remote can have multiple URLs; in this case the first is used for fetching, and all are used for pushing (assuming no `remote.`*&lt;name&gt;*`.pushurl` is defined). Setting this key to the empty string clears the list of urls, allowing you to override earlier config.

[](#Documentation/git-config.txt-remotenamepushurl)remote.&lt;name&gt;.pushurl

The push URL of a remote repository. See [git-push\[1\]](https://git-scm.com/docs/git-push). If a `pushurl` option is present in a configured remote, it is used for pushing instead of `remote.`*&lt;name&gt;*`.url`. A configured remote can have multiple push URLs; in this case a push goes to all of them. Setting this key to the empty string clears the list of urls, allowing you to override earlier config.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
