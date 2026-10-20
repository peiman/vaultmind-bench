---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#15-module-level-functions.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-15-module-level-functions
type: reference
title: logging — Logging facility for Python › Module-Level Functions (2/3)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#15-module-level-functions
source_hash: 05f20e2601dc05ecdada284846ae62713deee63b2f2e4fca87700ffbfd5db7a3
---
Changed in version 3.7: The *level* parameter was defaulted to level `CRITICAL`. See [bpo-28524](https://bugs.python.org/issue?%40action=redirect&bpo=28524) for more information about this change.

logging.addLevelName(*level*, *levelName*)[¶](#logging.addLevelName "Link to this definition")

Associates level *level* with text *levelName* in an internal dictionary, which is used to map numeric levels to a textual representation, for example when a [`Formatter`](#logging.Formatter "logging.Formatter") formats a message. This function can also be used to define your own levels. The only constraints are that all levels used must be registered using this function, levels should be positive integers and they should increase in increasing order of severity.

Note

If you are thinking of defining your own levels, please see the section on [Custom Levels](https://docs.python.org/3.13/howto/logging.html#custom-levels).

logging.getLevelNamesMapping()[¶](#logging.getLevelNamesMapping "Link to this definition")

Returns a mapping from level names to their corresponding logging levels. For example, the string “CRITICAL” maps to [`CRITICAL`](#logging.CRITICAL "logging.CRITICAL"). The returned mapping is copied from an internal mapping on each call to this function.

Added in version 3.11.

logging.getLevelName(*level*)[¶](#logging.getLevelName "Link to this definition")

Returns the textual or numeric representation of logging level *level*.

If *level* is one of the predefined levels [`CRITICAL`](#logging.CRITICAL "logging.CRITICAL"), [`ERROR`](#logging.ERROR "logging.ERROR"), [`WARNING`](#logging.WARNING "logging.WARNING"), [`INFO`](#logging.INFO "logging.INFO") or [`DEBUG`](#logging.DEBUG "logging.DEBUG") then you get the corresponding string. If you have associated levels with names using [`addLevelName()`](#logging.addLevelName "logging.addLevelName") then the name you have associated with *level* is returned. If a numeric value corresponding to one of the defined levels is passed in, the corresponding string representation is returned.

The *level* parameter also accepts a string representation of the level such as ‘INFO’. In such cases, this functions returns the corresponding numeric value of the level.

If no matching numeric or string value is passed in, the string ‘Level %s’ % level is returned.

Note

Levels are internally integers (as they need to be compared in the logging logic). This function is used to convert between an integer level and the level name displayed in the formatted log output by means of the `%(levelname)s` format specifier (see [LogRecord attributes](#logrecord-attributes)), and vice versa.

Changed in version 3.4: In Python versions earlier than 3.4, this function could also be passed a text level, and would return the corresponding numeric value of the level. This undocumented behaviour was considered a mistake, and was removed in Python 3.4, but reinstated in 3.4.2 due to retain backward compatibility.

logging.getHandlerByName(*name*)[¶](#logging.getHandlerByName "Link to this definition")

Returns a handler with the specified *name*, or `None` if there is no handler with that name.

Added in version 3.12.

logging.getHandlerNames()[¶](#logging.getHandlerNames "Link to this definition")

Returns an immutable set of all known handler names.

Added in version 3.12.

logging.makeLogRecord(*attrdict*)[¶](#logging.makeLogRecord "Link to this definition")

Creates and returns a new [`LogRecord`](#logging.LogRecord "logging.LogRecord") instance whose attributes are defined by *attrdict*. This function is useful for taking a pickled `LogRecord` attribute dictionary, sent over a socket, and reconstituting it as a `LogRecord` instance at the receiving end.

logging.basicConfig(*\*\*kwargs*)[¶](#logging.basicConfig "Link to this definition")

Does basic configuration for the logging system by creating a [`StreamHandler`](https://docs.python.org/3.13/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler") with a default [`Formatter`](#logging.Formatter "logging.Formatter") and adding it to the root logger. The functions [`debug()`](#logging.debug "logging.debug"), [`info()`](#logging.info "logging.info"), [`warning()`](#logging.warning "logging.warning"), [`error()`](#logging.error "logging.error") and [`critical()`](#logging.critical "logging.critical") will call `basicConfig()` automatically if no handlers are defined for the root logger.

This function does nothing if the root logger already has handlers configured, unless the keyword argument *force* is set to `True`.

Note

This function should be called from the main thread before other threads are started. In versions of Python prior to 2.7.1 and 3.2, if this function is called from multiple threads, it is possible (in rare circumstances) that a handler will be added to the root logger more than once, leading to unexpected results such as messages being duplicated in the log.

The following keyword arguments are supported.

Format

Description

*filename*

Specifies that a [`FileHandler`](https://docs.python.org/3.13/library/logging.handlers.html#logging.FileHandler "logging.FileHandler") be created, using the specified filename, rather than a [`StreamHandler`](https://docs.python.org/3.13/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler").

*filemode*

If *filename* is specified, open the file in this [mode](https://docs.python.org/3.13/builtins/functions.html#filemodes). Defaults to `'a'`.

*format*

Use the specified format string for the handler. Defaults to attributes `levelname`, `name` and `message` separated by colons.

*datefmt*

Use the specified date/time format, as accepted by [`time.strftime()`](https://docs.python.org/3.13/library/time.html#time.strftime "time.strftime").

*style*

Part of [[imported/web/docs.python.org/3-13-library-logging]].
