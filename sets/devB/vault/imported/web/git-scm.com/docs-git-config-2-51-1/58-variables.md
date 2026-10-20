---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#58-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-58-variables
type: reference
title: Git - git-config Documentation › Variables (52/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#58-variables
source_hash: 9a66809b1b7e669f8234f35e8780f50c6e200b4b2450fc9661c53c4160b8f640
---
Boolean. When true Git will print error messages when a trace target destination cannot be opened for writing. By default, these errors are suppressed and tracing is silently disabled. May be overridden by the `GIT_TRACE2_DST_DEBUG` environment variable.

[](#Documentation/git-config.txt-trace2maxFiles)trace2.maxFiles

Integer. When writing trace files to a target directory, do not write additional traces if doing so would exceed this many files. Instead, write a sentinel file that will block further tracing to this directory. Defaults to 0, which disables this check.

[](#Documentation/git-config.txt-trailerseparators)trailer.separators

This option tells which characters are recognized as trailer separators. By default only *:* is recognized as a trailer separator, except that *=* is always accepted on the command line for compatibility with other git commands.

The first character given by this option will be the default character used when another separator is not specified in the config for this trailer.

For example, if the value for this option is "%=$", then only lines using the format *&lt;key&gt;&lt;sep&gt;&lt;value&gt;* with &lt;sep&gt; containing *%*, *=* or *$* and then spaces will be considered trailers. And *%* will be the default separator used, so by default trailers will appear like: *&lt;key&gt;% &lt;value&gt;* (one percent sign and one space will appear between the key and the value).

[](#Documentation/git-config.txt-trailerwhere)trailer.where

This option tells where a new trailer will be added.

This can be `end`, which is the default, `start`, `after` or `before`.

If it is `end`, then each new trailer will appear at the end of the existing trailers.

If it is `start`, then each new trailer will appear at the start, instead of the end, of the existing trailers.

If it is `after`, then each new trailer will appear just after the last trailer with the same &lt;key&gt;.

If it is `before`, then each new trailer will appear just before the first trailer with the same &lt;key&gt;.

[](#Documentation/git-config.txt-trailerifexists)trailer.ifexists

This option makes it possible to choose what action will be performed when there is already at least one trailer with the same &lt;key&gt; in the input.

The valid values for this option are: `addIfDifferentNeighbor` (this is the default), `addIfDifferent`, `add`, `replace` or `doNothing`.

With `addIfDifferentNeighbor`, a new trailer will be added only if no trailer with the same (&lt;key&gt;, &lt;value&gt;) pair is above or below the line where the new trailer will be added.

With `addIfDifferent`, a new trailer will be added only if no trailer with the same (&lt;key&gt;, &lt;value&gt;) pair is already in the input.

With `add`, a new trailer will be added, even if some trailers with the same (&lt;key&gt;, &lt;value&gt;) pair are already in the input.

With `replace`, an existing trailer with the same &lt;key&gt; will be deleted and the new trailer will be added. The deleted trailer will be the closest one (with the same &lt;key&gt;) to the place where the new one will be added.

With `doNothing`, nothing will be done; that is no new trailer will be added if there is already one with the same &lt;key&gt; in the input.

[](#Documentation/git-config.txt-trailerifmissing)trailer.ifmissing

This option makes it possible to choose what action will be performed when there is not yet any trailer with the same &lt;key&gt; in the input.

The valid values for this option are: `add` (this is the default) and `doNothing`.

With `add`, a new trailer will be added.

With `doNothing`, nothing will be done.

[](#Documentation/git-config.txt-trailerkeyAliaskey)trailer.&lt;keyAlias&gt;.key

Defines a &lt;keyAlias&gt; for the &lt;key&gt;. The &lt;keyAlias&gt; must be a prefix (case does not matter) of the &lt;key&gt;. For example, in `git` `config` `trailer.ack.key` `"Acked-by"` the "Acked-by" is the &lt;key&gt; and the "ack" is the &lt;keyAlias&gt;. This configuration allows the shorter `--trailer` `"ack:..."` invocation on the command line using the "ack" &lt;keyAlias&gt; instead of the longer `--trailer` `"Acked-by:..."`.

At the end of the &lt;key&gt;, a separator can appear and then some space characters. By default the only valid separator is *:*, but this can be changed using the `trailer.separators` config variable.

If there is a separator in the key, then it overrides the default separator when adding the trailer.

[](#Documentation/git-config.txt-trailerkeyAliaswhere)trailer.&lt;keyAlias&gt;.where

This option takes the same values as the *trailer.where* configuration variable and it overrides what is specified by that option for trailers with the specified &lt;keyAlias&gt;.

[](#Documentation/git-config.txt-trailerkeyAliasifexists)trailer.&lt;keyAlias&gt;.ifexists

This option takes the same values as the *trailer.ifexists* configuration variable and it overrides what is specified by that option for trailers with the specified &lt;keyAlias&gt;.

[](#Documentation/git-config.txt-trailerkeyAliasifmissing)trailer.&lt;keyAlias&gt;.ifmissing

This option takes the same values as the *trailer.ifmissing* configuration variable and it overrides what is specified by that option for trailers with the specified &lt;keyAlias&gt;.

[](#Documentation/git-config.txt-trailerkeyAliascommand)trailer.&lt;keyAlias&gt;.command

Deprecated in favor of *trailer.&lt;keyAlias&gt;.cmd*. This option behaves in the same way as *trailer.&lt;keyAlias&gt;.cmd*, except that it doesn’t pass anything as argument to the specified command. Instead the first occurrence of substring $ARG is replaced by the &lt;value&gt; that would be passed as argument.

Note that $ARG in the user’s command is only replaced once and that the original way of replacing $ARG is not safe.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
