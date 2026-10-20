---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#03-logger-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-03-logger-objects
type: reference
title: logging — Logging facility for Python › Logger Objects (2/4)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#03-logger-objects
source_hash: f81c532d17fe8612cf4640ab5e028974305ae8674d2c4306f34901d09e3ec249
---
Changed in version 3.2: The *level* parameter now accepts a string representation of the level such as ‘INFO’ as an alternative to the integer constants such as [`INFO`](#logging.INFO "logging.INFO"). Note, however, that levels are internally stored as integers, and methods such as e.g. [`getEffectiveLevel()`](#logging.Logger.getEffectiveLevel "logging.Logger.getEffectiveLevel") and [`isEnabledFor()`](#logging.Logger.isEnabledFor "logging.Logger.isEnabledFor") will return/expect to be passed integers.

isEnabledFor(*level*)[¶](#logging.Logger.isEnabledFor "Link to this definition")

Indicates if a message of severity *level* would be processed by this logger. This method checks first the module-level level set by `logging.disable(level)` and then the logger’s effective level as determined by [`getEffectiveLevel()`](#logging.Logger.getEffectiveLevel "logging.Logger.getEffectiveLevel").

getEffectiveLevel()[¶](#logging.Logger.getEffectiveLevel "Link to this definition")

Indicates the effective level for this logger. If a value other than [`NOTSET`](#logging.NOTSET "logging.NOTSET") has been set using [`setLevel()`](#logging.Logger.setLevel "logging.Logger.setLevel"), it is returned. Otherwise, the hierarchy is traversed towards the root until a value other than `NOTSET` is found, and that value is returned. The value returned is an integer, typically one of [`logging.DEBUG`](#logging.DEBUG "logging.DEBUG"), [`logging.INFO`](#logging.INFO "logging.INFO") etc.

getChild(*suffix*)[¶](#logging.Logger.getChild "Link to this definition")

Returns a logger which is a descendant to this logger, as determined by the suffix. Thus, `logging.getLogger('abc').getChild('def.ghi')` would return the same logger as would be returned by `logging.getLogger('abc.def.ghi')`. This is a convenience method, useful when the parent logger is named using e.g. `__name__` rather than a literal string.

Added in version 3.2.

getChildren()[¶](#logging.Logger.getChildren "Link to this definition")

Returns a set of loggers which are immediate children of this logger. So for example `logging.getLogger().getChildren()` might return a set containing loggers named `foo` and `bar`, but a logger named `foo.bar` wouldn’t be included in the set. Likewise, `logging.getLogger('foo').getChildren()` might return a set including a logger named `foo.bar`, but it wouldn’t include one named `foo.bar.baz`.

Added in version 3.12.

debug(*msg*, *\*args*, *\*\*kwargs*)[¶](#logging.Logger.debug "Link to this definition")

Logs a message with level [`DEBUG`](#logging.DEBUG "logging.DEBUG") on this logger. The *msg* is the message format string, and the *args* are the arguments which are merged into *msg* using the string formatting operator. (Note that this means that you can use keywords in the format string, together with a single dictionary argument.) No % formatting operation is performed on *msg* when no *args* are supplied.

There are four keyword arguments in *kwargs* which are inspected: *exc\_info*, *stack\_info*, *stacklevel* and *extra*.

If *exc\_info* does not evaluate as false, it causes exception information to be added to the logging message. If an exception tuple (in the format returned by [`sys.exc_info()`](https://docs.python.org/3.13/library/sys.html#sys.exc_info "sys.exc_info")) or an exception instance is provided, it is used; otherwise, `sys.exc_info()` is called to get the exception information.

The second optional keyword argument is *stack\_info*, which defaults to `False`. If true, stack information is added to the logging message, including the actual logging call. Note that this is not the same stack information as that displayed through specifying *exc\_info*: The former is stack frames from the bottom of the stack up to the logging call in the current thread, whereas the latter is information about stack frames which have been unwound, following an exception, while searching for exception handlers.

You can specify *stack\_info* independently of *exc\_info*, e.g. to just show how you got to a certain point in your code, even when no exceptions were raised. The stack frames are printed following a header line which says:

```
Stack (most recent call last):
```

This mimics the `Traceback (most recent call last):` which is used when displaying exception frames.

The third optional keyword argument is *stacklevel*, which defaults to `1`. If greater than 1, the corresponding number of stack frames are skipped when computing the line number and function name set in the [`LogRecord`](#logging.LogRecord "logging.LogRecord") created for the logging event. This can be used in logging helpers so that the function name, filename and line number recorded are not the information for the helper function/method, but rather its caller. The name of this parameter mirrors the equivalent one in the [`warnings`](https://docs.python.org/3.13/library/warnings.html#module-warnings "warnings: Issue warning messages and control their disposition.") module.

The fourth keyword argument is *extra* which can be used to pass a dictionary which is used to populate the [`__dict__`](https://docs.python.org/3.13/reference/datamodel.html#object.__dict__ "object.__dict__") of the [`LogRecord`](#logging.LogRecord "logging.LogRecord") created for the logging event with user-defined attributes. These custom attributes can then be used as you like. For example, they could be incorporated into logged messages. For example:

```
FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)
```

would print something like

```
2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset
```

Part of [[imported/web/docs.python.org/3-13-library-logging]].
