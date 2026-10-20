---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#57-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-57-variables
type: reference
title: Git - git-config Documentation › Variables (51/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#57-variables
source_hash: 482557162b6658fc62baaa080c0d9adf8c4bac7644c49f898d5ef1836e384bb8
---
Specifies how many submodules are fetched/cloned at the same time. A positive integer allows up to that number of submodules fetched in parallel. A value of 0 will give some reasonable default. If unset, it defaults to 1.

[](#Documentation/git-config.txt-submodulealternateLocation)submodule.alternateLocation

Specifies how the submodules obtain alternates when submodules are cloned. Possible values are `no`, `superproject`. By default `no` is assumed, which doesn’t add references. When the value is set to `superproject` the submodule to be cloned computes its alternates location relative to the superprojects alternate.

[](#Documentation/git-config.txt-submodulealternateErrorStrategy)submodule.alternateErrorStrategy

Specifies how to treat errors with the alternates for a submodule as computed via `submodule.alternateLocation`. Possible values are `ignore`, `info`, `die`. Default is `die`. Note that if set to `ignore` or `info`, and if there is an error with the computed alternate, the clone proceeds as if no alternate was specified.

[](#Documentation/git-config.txt-tagforceSignAnnotated)tag.forceSignAnnotated

A boolean to specify whether annotated tags created should be GPG signed. If `--annotate` is specified on the command line, it takes precedence over this option.

[](#Documentation/git-config.txt-tagsort)tag.sort

This variable controls the sort ordering of tags when displayed by [git-tag\[1\]](https://git-scm.com/docs/git-tag). Without the "--sort=&lt;value&gt;" option provided, the value of this variable will be used as the default.

[](#Documentation/git-config.txt-taggpgSign)tag.gpgSign

A boolean to specify whether all tags should be GPG signed. Use of this option when running in an automated script can result in a large number of tags being signed. It is therefore convenient to use an agent to avoid typing your gpg passphrase several times. Note that this option doesn’t affect tag signing behavior enabled by "-u &lt;keyid&gt;" or "--local-user=&lt;keyid&gt;" options.

[](#Documentation/git-config.txt-tarumask)tar.umask

This variable can be used to restrict the permission bits of tar archive entries. The default is 0002, which turns off the world write bit. The special value "user" indicates that the archiving user’s umask will be used instead. See umask(2) and [git-archive\[1\]](https://git-scm.com/docs/git-archive).

Trace2 config settings are only read from the system and global config files; repository local and worktree config files and `-c` command line arguments are not respected.

[](#Documentation/git-config.txt-trace2normalTarget)trace2.normalTarget

This variable controls the normal target destination. It may be overridden by the `GIT_TRACE2` environment variable. The following table shows possible values.

[](#Documentation/git-config.txt-trace2perfTarget)trace2.perfTarget

This variable controls the performance target destination. It may be overridden by the `GIT_TRACE2_PERF` environment variable. The following table shows possible values.

[](#Documentation/git-config.txt-trace2eventTarget)trace2.eventTarget

This variable controls the event target destination. It may be overridden by the `GIT_TRACE2_EVENT` environment variable. The following table shows possible values.

- `0` or `false` - Disables the target.
- `1` or `true` - Writes to `STDERR`.
- \[`2-9`] - Writes to the already opened file descriptor.
- *&lt;absolute-pathname&gt;* - Writes to the file in append mode. If the target already exists and is a directory, the traces will be written to files (one per process) underneath the given directory.
- `af_unix:`\[*&lt;socket-type&gt;*`:`]*&lt;absolute-pathname&gt;* - Write to a Unix DomainSocket (on platforms that support them). Socket type can be either `stream` or `dgram`; if omitted Git will try both.

[](#Documentation/git-config.txt-trace2normalBrief)trace2.normalBrief

Boolean. When true `time`, `filename`, and `line` fields are omitted from normal output. May be overridden by the `GIT_TRACE2_BRIEF` environment variable. Defaults to false.

[](#Documentation/git-config.txt-trace2perfBrief)trace2.perfBrief

Boolean. When true `time`, `filename`, and `line` fields are omitted from PERF output. May be overridden by the `GIT_TRACE2_PERF_BRIEF` environment variable. Defaults to false.

[](#Documentation/git-config.txt-trace2eventBrief)trace2.eventBrief

Boolean. When true `time`, `filename`, and `line` fields are omitted from event output. May be overridden by the `GIT_TRACE2_EVENT_BRIEF` environment variable. Defaults to false.

[](#Documentation/git-config.txt-trace2eventNesting)trace2.eventNesting

Integer. Specifies desired depth of nested regions in the event output. Regions deeper than this value will be omitted. May be overridden by the `GIT_TRACE2_EVENT_NESTING` environment variable. Defaults to 2.

[](#Documentation/git-config.txt-trace2configParams)trace2.configParams

A comma-separated list of patterns of "important" config settings that should be recorded in the trace2 output. For example, `core.*,remote.*.url` would cause the trace2 output to contain events listing each configured remote. May be overridden by the `GIT_TRACE2_CONFIG_PARAMS` environment variable. Unset by default.

[](#Documentation/git-config.txt-trace2envVars)trace2.envVars

A comma-separated list of "important" environment variables that should be recorded in the trace2 output. For example, `GIT_HTTP_USER_AGENT,GIT_CONFIG` would cause the trace2 output to contain events listing the overrides for HTTP user agent and the location of the Git configuration file (assuming any are set). May be overridden by the `GIT_TRACE2_ENV_VARS` environment variable. Unset by default.

[](#Documentation/git-config.txt-trace2destinationDebug)trace2.destinationDebug

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
