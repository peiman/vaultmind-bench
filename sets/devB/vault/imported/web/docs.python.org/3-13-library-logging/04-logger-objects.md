---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#04-logger-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-04-logger-objects
type: reference
title: logging — Logging facility for Python › Logger Objects (3/4)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#04-logger-objects
source_hash: c7e2608d3e4ea8c80c8d76500bfa4593a2c3edd83735f8b5abadf7a6d7820bff
---
The keys in the dictionary passed in *extra* should not clash with the keys used by the logging system. (See the section on [LogRecord attributes](#logrecord-attributes) for more information on which keys are used by the logging system.)

If you choose to use these attributes in logged messages, you need to exercise some care. In the above example, for instance, the [`Formatter`](#logging.Formatter "logging.Formatter") has been set up with a format string which expects ‘clientip’ and ‘user’ in the attribute dictionary of the [`LogRecord`](#logging.LogRecord "logging.LogRecord"). If these are missing, the message will not be logged because a string formatting exception will occur. So in this case, you always need to pass the *extra* dictionary with these keys.

While this might be annoying, this feature is intended for use in specialized circumstances, such as multi-threaded servers where the same code executes in many contexts, and interesting conditions which arise are dependent on this context (such as remote client IP address and authenticated user name, in the above example). In such circumstances, it is likely that specialized [`Formatter`](#logging.Formatter "logging.Formatter")s would be used with particular [`Handler`](#logging.Handler "logging.Handler")s.

If no handler is attached to this logger (or any of its ancestors, taking into account the relevant [`Logger.propagate`](#logging.Logger.propagate "logging.Logger.propagate") attributes), the message will be sent to the handler set on [`lastResort`](#logging.lastResort "logging.lastResort").

Changed in version 3.2: The *stack\_info* parameter was added.

Changed in version 3.5: The *exc\_info* parameter can now accept exception instances.

Changed in version 3.8: The *stacklevel* parameter was added.

info(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.Logger.info "Link to this definition")

Logs a message with level [`INFO`](#logging.INFO "logging.INFO") on this logger. The arguments are interpreted as for [`debug()`](#logging.debug "logging.debug").

warning(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.Logger.warning "Link to this definition")

Logs a message with level [`WARNING`](#logging.WARNING "logging.WARNING") on this logger. The arguments are interpreted as for [`debug()`](#logging.debug "logging.debug").

Note

There is an obsolete method `warn` which is functionally identical to `warning`. As `warn` is deprecated, please do not use it - use `warning` instead.

error(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.Logger.error "Link to this definition")

Logs a message with level [`ERROR`](#logging.ERROR "logging.ERROR") on this logger. The arguments are interpreted as for [`debug()`](#logging.debug "logging.debug").

critical(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.Logger.critical "Link to this definition")

Logs a message with level [`CRITICAL`](#logging.CRITICAL "logging.CRITICAL") on this logger. The arguments are interpreted as for [`debug()`](#logging.debug "logging.debug").

log(*level*, *msg*, *\*args*, *\*\*kwargs*)[¶](#logging.Logger.log "Link to this definition")

Logs a message with integer level *level* on this logger. The other arguments are interpreted as for [`debug()`](#logging.debug "logging.debug").

exception(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.Logger.exception "Link to this definition")

Logs a message with level [`ERROR`](#logging.ERROR "logging.ERROR") on this logger. The arguments are interpreted as for [`debug()`](#logging.debug "logging.debug"). Exception info is added to the logging message. This method should only be called from an exception handler.

addFilter(*filter*)[¶](#logging.Logger.addFilter "Link to this definition")

Adds the specified filter *filter* to this logger.

removeFilter(*filter*)[¶](#logging.Logger.removeFilter "Link to this definition")

Removes the specified filter *filter* from this logger.

filter(*record*)[¶](#logging.Logger.filter "Link to this definition")

Apply this logger’s filters to the record and return `True` if the record is to be processed. The filters are consulted in turn, until one of them returns a false value. If none of them return a false value, the record will be processed (passed to handlers). If one returns a false value, no further processing of the record occurs.

addHandler(*hdlr*)[¶](#logging.Logger.addHandler "Link to this definition")

Adds the specified handler *hdlr* to this logger.

removeHandler(*hdlr*)[¶](#logging.Logger.removeHandler "Link to this definition")

Removes the specified handler *hdlr* from this logger.

findCaller(*stack\_info=False*, *stacklevel=1*)[¶](#logging.Logger.findCaller "Link to this definition")

Finds the caller’s source filename and line number. Returns the filename, line number, function name and stack information as a 4-element tuple. The stack information is returned as `None` unless *stack\_info* is `True`.

The *stacklevel* parameter is passed from code calling the [`debug()`](#logging.debug "logging.debug") and other APIs. If greater than 1, the excess is used to skip stack frames before determining the values to be returned. This will generally be useful when calling logging APIs from helper/wrapper code, so that the information in the event log refers not to the helper/wrapper code, but to the code that calls it.

handle(*record*)[¶](#logging.Logger.handle "Link to this definition")

Handles a record by passing it to all handlers associated with this logger and its ancestors (until a false value of *propagate* is found). This method is used for unpickled records received from a socket, as well as those created locally. Logger-level filtering is applied using [`filter()`](#logging.Logger.filter "logging.Logger.filter").

makeRecord(*name*, *level*, *fn*, *lno*, *msg*, *args*, *exc\_info*, *func=None*, *extra=None*, *sinfo=None*)[¶](#logging.Logger.makeRecord "Link to this definition")

Part of [[imported/web/docs.python.org/3-13-library-logging]].
