---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#14-module-level-functions.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-14-module-level-functions
type: reference
title: logging — Logging facility for Python › Module-Level Functions (1/3)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#14-module-level-functions
source_hash: 8a4fc63031035dddf09f2500797f5cb12cc5bef2f2d535108cff174971e48285
---
In addition to the classes described above, there are a number of module-level functions.

logging.getLogger(*name=None*)[¶](#logging.getLogger "Link to this definition")

Return a logger with the specified name or, if name is `None`, return the root logger of the hierarchy. If specified, the name is typically a dot-separated hierarchical name like *‘a’*, *‘a.b’* or *‘a.b.c.d’*. Choice of these names is entirely up to the developer who is using logging, though it is recommended that `__name__` be used unless you have a specific reason for not doing that, as mentioned in [Logger Objects](#logger).

All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.

logging.getLoggerClass()[¶](#logging.getLoggerClass "Link to this definition")

Return either the standard [`Logger`](#logging.Logger "logging.Logger") class, or the last class passed to [`setLoggerClass()`](#logging.setLoggerClass "logging.setLoggerClass"). This function may be called from within a new class definition, to ensure that installing a customized `Logger` class will not undo customizations already applied by other code. For example:

```
class MyLogger(logging.getLoggerClass()):
    # ... override behaviour here
```

logging.getLogRecordFactory()[¶](#logging.getLogRecordFactory "Link to this definition")

Return a callable which is used to create a [`LogRecord`](#logging.LogRecord "logging.LogRecord").

Added in version 3.2: This function has been provided, along with [`setLogRecordFactory()`](#logging.setLogRecordFactory "logging.setLogRecordFactory"), to allow developers more control over how the [`LogRecord`](#logging.LogRecord "logging.LogRecord") representing a logging event is constructed.

See [`setLogRecordFactory()`](#logging.setLogRecordFactory "logging.setLogRecordFactory") for more information about the how the factory is called.

logging.debug(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.debug "Link to this definition")

This is a convenience function that calls [`Logger.debug()`](#logging.Logger.debug "logging.Logger.debug"), on the root logger. The handling of the arguments is in every way identical to what is described in that method.

The only difference is that if the root logger has no handlers, then [`basicConfig()`](#logging.basicConfig "logging.basicConfig") is called, prior to calling `debug` on the root logger.

For very short scripts or quick demonstrations of `logging` facilities, `debug` and the other module-level functions may be convenient. However, most programs will want to carefully and explicitly control the logging configuration, and should therefore prefer creating a module-level logger and calling [`Logger.debug()`](#logging.Logger.debug "logging.Logger.debug") (or other level-specific methods) on it, as described at the beginnning of this documentation.

logging.info(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.info "Link to this definition")

Logs a message with level [`INFO`](#logging.INFO "logging.INFO") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](#logging.debug "logging.debug").

logging.warning(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.warning "Link to this definition")

Logs a message with level [`WARNING`](#logging.WARNING "logging.WARNING") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](#logging.debug "logging.debug").

Note

There is an obsolete function `warn` which is functionally identical to `warning`. As `warn` is deprecated, please do not use it - use `warning` instead.

logging.error(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.error "Link to this definition")

Logs a message with level [`ERROR`](#logging.ERROR "logging.ERROR") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](#logging.debug "logging.debug").

logging.critical(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.critical "Link to this definition")

Logs a message with level [`CRITICAL`](#logging.CRITICAL "logging.CRITICAL") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](#logging.debug "logging.debug").

logging.exception(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.exception "Link to this definition")

Logs a message with level [`ERROR`](#logging.ERROR "logging.ERROR") on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](#logging.debug "logging.debug"). Exception info is added to the logging message. This function should only be called from an exception handler.

logging.log(*level*, *msg*, *\*args*, *\*\*kwargs*)[¶](#logging.log "Link to this definition")

Logs a message with level *level* on the root logger. The arguments and behavior are otherwise the same as for [`debug()`](#logging.debug "logging.debug").

logging.disable(*level=CRITICAL*)[¶](#logging.disable "Link to this definition")

Provides an overriding level *level* for all loggers which takes precedence over the logger’s own level. When the need arises to temporarily throttle logging output down across the whole application, this function can be useful. Its effect is to disable all logging calls of severity *level* and below, so that if you call it with a value of INFO, then all INFO and DEBUG events would be discarded, whereas those of severity WARNING and above would be processed according to the logger’s effective level. If `logging.disable(logging.NOTSET)` is called, it effectively removes this overriding level, so that logging output again depends on the effective levels of individual loggers.

Note that if you have defined any custom logging level higher than `CRITICAL` (this is not recommended), you won’t be able to rely on the default value for the *level* parameter, but will have to explicitly supply a suitable value.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
