---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#40-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-40-variables
type: reference
title: Git - git-config Documentation › Variables (34/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#40-variables
source_hash: efd348b6f8e8fbddf621007db4ce236fadbc041e05a5fdad83c181e5892574fe
---
The location of an augmenting mailmap file. The default mailmap, located in the root of the repository, is loaded first, then the mailmap file pointed to by this variable. The location of the mailmap file may be in a repository subdirectory, or somewhere outside of the repository itself. See [git-shortlog\[1\]](https://git-scm.com/docs/git-shortlog) and [git-blame\[1\]](https://git-scm.com/docs/git-blame).

[](#Documentation/git-config.txt-mailmapblob)mailmap.blob

Like `mailmap.file`, but consider the value as a reference to a blob in the repository. If both `mailmap.file` and `mailmap.blob` are given, both are parsed, with entries from `mailmap.file` taking precedence. In a bare repository, this defaults to `HEAD:.mailmap`. In a non-bare repository, it defaults to empty.

[](#Documentation/git-config.txt-maintenanceauto)maintenance.auto

This boolean config option controls whether some commands run `git` `maintenance` `run` `--auto` after doing their normal work. Defaults to true.

[](#Documentation/git-config.txt-maintenanceautoDetach)maintenance.autoDetach

Many Git commands trigger automatic maintenance after they have written data into the repository. This boolean config option controls whether this automatic maintenance shall happen in the foreground or whether the maintenance process shall detach and continue to run in the background.

If unset, the value of `gc.autoDetach` is used as a fallback. Defaults to true if both are unset, meaning that the maintenance process will detach.

[](#Documentation/git-config.txt-maintenancestrategy)maintenance.strategy

This string config option provides a way to specify one of a few recommended schedules for background maintenance. This only affects which tasks are run during `git` `maintenance` `run` `--schedule=X` commands, provided no `--task=`*&lt;task&gt;* arguments are provided. Further, if a `maintenance.`*&lt;task&gt;*`.schedule` config value is set, then that value is used instead of the one provided by `maintenance.strategy`. The possible strategy strings are:

- `none`: This default setting implies no tasks are run at any schedule.
- `incremental`: This setting optimizes for performing small maintenance activities that do not delete any data. This does not schedule the `gc` task, but runs the `prefetch` and `commit-graph` tasks hourly, the `loose-objects` and `incremental-repack` tasks daily, and the `pack-refs` task weekly.

[](#Documentation/git-config.txt-maintenancetaskenabled)maintenance.&lt;task&gt;.enabled

This boolean config option controls whether the maintenance task with name *&lt;task&gt;* is run when no `--task` option is specified to `git` `maintenance` `run`. These config values are ignored if a `--task` option exists. By default, only `maintenance.gc.enabled` is true.

[](#Documentation/git-config.txt-maintenancetaskschedule)maintenance.&lt;task&gt;.schedule

This config option controls whether or not the given *&lt;task&gt;* runs during a `git` `maintenance` `run` `--schedule=`*&lt;frequency&gt;* command. The value must be one of "hourly", "daily", or "weekly".

[](#Documentation/git-config.txt-maintenancecommit-graphauto)maintenance.commit-graph.auto

This integer config option controls how often the `commit-graph` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `commit-graph` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of reachable commits that are not in the commit-graph file is at least the value of `maintenance.commit-graph.auto`. The default value is 100.

[](#Documentation/git-config.txt-maintenanceloose-objectsauto)maintenance.loose-objects.auto

This integer config option controls how often the `loose-objects` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `loose-objects` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of loose objects is at least the value of `maintenance.loose-objects.auto`. The default value is 100.

[](#Documentation/git-config.txt-maintenanceloose-objectsbatchSize)maintenance.loose-objects.batchSize

This integer config option controls the maximum number of loose objects written into a packfile during the `loose-objects` task. The default is fifty thousand. Use value `0` to indicate no limit.

[](#Documentation/git-config.txt-maintenanceincremental-repackauto)maintenance.incremental-repack.auto

This integer config option controls how often the `incremental-repack` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `incremental-repack` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of pack-files not in the multi-pack-index is at least the value of `maintenance.incremental-repack.auto`. The default value is 10.

[](#Documentation/git-config.txt-maintenancereflog-expireauto)maintenance.reflog-expire.auto

This integer config option controls how often the `reflog-expire` task should be run as part of `git` `maintenance` `run` `--auto`. If zero, then the `reflog-expire` task will not run with the `--auto` option. A negative value will force the task to run every time. Otherwise, a positive value implies the command should run when the number of expired reflog entries in the "HEAD" reflog is at least the value of `maintenance.loose-objects.auto`. The default value is 100.

[](#Documentation/git-config.txt-maintenancererere-gcauto)maintenance.rerere-gc.auto

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
