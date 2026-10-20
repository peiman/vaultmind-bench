---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#31-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-31-variables
type: reference
title: Git - git-config Documentation › Variables (25/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#31-variables
source_hash: fbcddabf4bab4dad81471bdf5e630629fcba4cd1c853a35fb30b099135d46baa
---
[](#Documentation/git-config.txt-gcreflogExpireUnreachable)gc.reflogExpireUnreachable

[](#Documentation/git-config.txt-gcpatternreflogExpireUnreachable)gc.&lt;pattern&gt;.reflogExpireUnreachable

*git reflog expire* removes reflog entries older than this time and are not reachable from the current tip; defaults to 30 days. The value "now" expires all entries immediately, and "never" suppresses expiration altogether. With "&lt;pattern&gt;" (e.g. "refs/stash") in the middle, the setting applies only to the refs that match the &lt;pattern&gt;.

These types of entries are generally created as a result of using `git` `commit` `--amend` or `git` `rebase` and are the commits prior to the amend or rebase occurring. Since these changes are not part of the current project most users will want to expire them sooner, which is why the default is more aggressive than `gc.reflogExpire`.

[](#Documentation/git-config.txt-gcrecentObjectsHook)gc.recentObjectsHook

When considering whether or not to remove an object (either when generating a cruft pack or storing unreachable objects as loose), use the shell to execute the specified command(s). Interpret their output as object IDs which Git will consider as "recent", regardless of their age. By treating their mtimes as "now", any objects (and their descendants) mentioned in the output will be kept regardless of their true age.

Output must contain exactly one hex object ID per line, and nothing else. Objects which cannot be found in the repository are ignored. Multiple hooks are supported, but all must exit successfully, else the operation (either generating a cruft pack or unpacking unreachable objects) will be halted.

[](#Documentation/git-config.txt-gcrepackFilter)gc.repackFilter

When repacking, use the specified filter to move certain objects into a separate packfile. See the `--filter=`*&lt;filter-spec&gt;* option of [git-repack\[1\]](https://git-scm.com/docs/git-repack).

[](#Documentation/git-config.txt-gcrepackFilterTo)gc.repackFilterTo

When repacking and using a filter, see `gc.repackFilter`, the specified location will be used to create the packfile containing the filtered out objects. **WARNING:** The specified location should be accessible, using for example the Git alternates mechanism, otherwise the repo could be considered corrupt by Git as it might not be able to access the objects in that packfile. See the `--filter-to=`*&lt;dir&gt;* option of [git-repack\[1\]](https://git-scm.com/docs/git-repack) and the `objects/info/alternates` section of [gitrepository-layout\[5\]](https://git-scm.com/docs/gitrepository-layout).

[](#Documentation/git-config.txt-gcrerereResolved)gc.rerereResolved

Records of conflicted merge you resolved earlier are kept for this many days when *git rerere gc* is run. You can also use more human-readable "1.month.ago", etc. The default is 60 days. See [git-rerere\[1\]](https://git-scm.com/docs/git-rerere).

[](#Documentation/git-config.txt-gcrerereUnresolved)gc.rerereUnresolved

Records of conflicted merge you have not resolved are kept for this many days when *git rerere gc* is run. You can also use more human-readable "1.month.ago", etc. The default is 15 days. See [git-rerere\[1\]](https://git-scm.com/docs/git-rerere).

[](#Documentation/git-config.txt-gitcvscommitMsgAnnotation)gitcvs.commitMsgAnnotation

Append this string to each commit message. Set to empty string to disable this feature. Defaults to "via git-CVS emulator".

[](#Documentation/git-config.txt-gitcvsenabled)gitcvs.enabled

Whether the CVS server interface is enabled for this repository. See [git-cvsserver\[1\]](https://git-scm.com/docs/git-cvsserver).

[](#Documentation/git-config.txt-gitcvslogFile)gitcvs.logFile

Path to a log file where the CVS server interface well…​ logs various stuff. See [git-cvsserver\[1\]](https://git-scm.com/docs/git-cvsserver).

[](#Documentation/git-config.txt-gitcvsusecrlfattr)gitcvs.usecrlfattr

If true, the server will look up the end-of-line conversion attributes for files to determine the `-k` modes to use. If the attributes force Git to treat a file as text, the `-k` mode will be left blank so CVS clients will treat it as text. If they suppress text conversion, the file will be set with *-kb* mode, which suppresses any newline munging the client might otherwise do. If the attributes do not allow the file type to be determined, then `gitcvs.allBinary` is used. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes).

[](#Documentation/git-config.txt-gitcvsallBinary)gitcvs.allBinary

This is used if `gitcvs.usecrlfattr` does not resolve the correct *-kb* mode to use. If true, all unresolved files are sent to the client in mode *-kb*. This causes the client to treat them as binary files, which suppresses any newline munging it otherwise might do. Alternatively, if it is set to "guess", then the contents of the file are examined to decide if it is binary, similar to `core.autocrlf`.

[](#Documentation/git-config.txt-gitcvsdbName)gitcvs.dbName

Database used by git-cvsserver to cache revision information derived from the Git repository. The exact meaning depends on the used database driver, for SQLite (which is the default driver) this is a filename. Supports variable substitution (see [git-cvsserver\[1\]](https://git-scm.com/docs/git-cvsserver) for details). May not contain semicolons (*;*). Default: *%Ggitcvs.%m.sqlite*

[](#Documentation/git-config.txt-gitcvsdbDriver)gitcvs.dbDriver

Used Perl DBI driver. You can specify any available driver for this here, but it might not work. git-cvsserver is tested with *DBD::SQLite*, reported to work with *DBD::Pg*, and reported **not** to work with *DBD::mysql*. Experimental feature. May not contain double colons (`:`). Default: *SQLite*. See [git-cvsserver\[1\]](https://git-scm.com/docs/git-cvsserver).

[](#Documentation/git-config.txt-gitcvsdbUser)gitcvs.dbUser

[](#Documentation/git-config.txt-gitcvsdbPass)gitcvs.dbPass

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
