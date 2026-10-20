---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#10-logrecord-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-10-logrecord-objects
type: reference
title: logging — Logging facility for Python › LogRecord Objects
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#10-logrecord-objects
source_hash: e013cac234c21079fee419edbdfa28ca340e1ba9da48126381e343a1b34404df
---
[`LogRecord`](#logging.LogRecord "logging.LogRecord") instances are created automatically by the [`Logger`](#logging.Logger "logging.Logger") every time something is logged, and can be created manually via [`makeLogRecord()`](#logging.makeLogRecord "logging.makeLogRecord") (for example, from a pickled event received over the wire).

*class* logging.LogRecord(*name*, *level*, *pathname*, *lineno*, *msg*, *args*, *exc\_info*, *func=None*, *sinfo=None*)[¶](#logging.LogRecord "Link to this definition")

Contains all the information pertinent to the event being logged.

The primary information is passed in *msg* and *args*, which are combined using `msg % args` to create the `message` attribute of the record.

Parameters:

- **name** ([*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str")) – The name of the logger used to log the event represented by this `LogRecord`. Note that the logger name in the `LogRecord` will always have this value, even though it may be emitted by a handler attached to a different (ancestor) logger.
- **level** ([*int*](https://docs.python.org/3.13/builtins/functions.html#int "int")) – The [numeric level](#levels) of the logging event (such as `10` for `DEBUG`, `20` for `INFO`, etc). Note that this is converted to *two* attributes of the LogRecord: `levelno` for the numeric value and `levelname` for the corresponding level name.
- **pathname** ([*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str")) – The full string path of the source file where the logging call was made.
- **lineno** ([*int*](https://docs.python.org/3.13/builtins/functions.html#int "int")) – The line number in the source file where the logging call was made.
- **msg** ([*Any*](https://docs.python.org/3.13/library/typing.html#typing.Any "typing.Any")) – The event description message, which can be a %-format string with placeholders for variable data, or an arbitrary object (see [Using arbitrary objects as messages](https://docs.python.org/3.13/howto/logging.html#arbitrary-object-messages)).
- **args** ([*tuple*](https://docs.python.org/3.13/builtins/stdtypes.html#tuple "tuple") *|* [*dict*](https://docs.python.org/3.13/builtins/stdtypes.html#dict "dict")*\[*[*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str")*,* [*Any*](https://docs.python.org/3.13/library/typing.html#typing.Any "typing.Any")*]*) – Variable data to merge into the *msg* argument to obtain the event description.
- **exc\_info** ([*tuple*](https://docs.python.org/3.13/builtins/stdtypes.html#tuple "tuple")*\[*[*type*](https://docs.python.org/3.13/builtins/functions.html#type "type")*\[*[*BaseException*](https://docs.python.org/3.13/builtins/exceptions.html#BaseException "BaseException")*], BaseException,* [*types.TracebackType*](https://docs.python.org/3.13/library/types.html#types.TracebackType "types.TracebackType")*] | None*) – An exception tuple with the current exception information, as returned by [`sys.exc_info()`](https://docs.python.org/3.13/library/sys.html#sys.exc_info "sys.exc_info"), or `None` if no exception information is available.
- **func** ([*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str") *| None*) – The name of the function or method from which the logging call was invoked.
- **sinfo** ([*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str") *| None*) – A text string representing stack information from the base of the stack in the current thread, up to the logging call.

getMessage()[¶](#logging.LogRecord.getMessage "Link to this definition")

Returns the message for this `LogRecord` instance after merging any user-supplied arguments with the message. If the user-supplied message argument to the logging call is not a string, [`str()`](https://docs.python.org/3.13/builtins/stdtypes.html#str "str") is called on it to convert it to a string. This allows use of user-defined classes as messages, whose `__str__` method can return the actual format string to be used.

Changed in version 3.2: The creation of a `LogRecord` has been made more configurable by providing a factory which is used to create the record. The factory can be set using [`getLogRecordFactory()`](#logging.getLogRecordFactory "logging.getLogRecordFactory") and [`setLogRecordFactory()`](#logging.setLogRecordFactory "logging.setLogRecordFactory") (see this for the factory’s signature).

This functionality can be used to inject your own values into a `LogRecord` at creation time. You can use the following pattern:

```
old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = 0xdecafbad
    return record

logging.setLogRecordFactory(record_factory)
```

With this pattern, multiple factories could be chained, and as long as they don’t overwrite each other’s attributes or unintentionally overwrite the standard attributes listed above, there should be no surprises.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
