---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#16-module-level-functions.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-16-module-level-functions
type: reference
title: logging — Logging facility for Python › Module-Level Functions (3/3)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#16-module-level-functions
source_hash: 54a16ecdf7d2d994954074a60d92a635af0a1aab29bc2ed34989dc8500031fe4
---
If *format* is specified, use this style for the format string. One of `'%'`, `'{'` or `'$'` for [printf-style](https://docs.python.org/3.13/builtins/stdtypes.html#old-string-formatting), [`str.format()`](https://docs.python.org/3.13/builtins/stdtypes.html#str.format "str.format") or [`string.Template`](https://docs.python.org/3.13/library/string.html#string.Template "string.Template") respectively. Defaults to `'%'`.

*level*

Set the root logger level to the specified [level](#levels).

*stream*

Use the specified stream to initialize the [`StreamHandler`](https://docs.python.org/3.13/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler"). Note that this argument is incompatible with *filename* - if both are present, a `ValueError` is raised.

*handlers*

If specified, this should be an iterable of already created handlers to add to the root logger. Any handlers which don’t already have a formatter set will be assigned the default formatter created in this function. Note that this argument is incompatible with *filename* or *stream* - if both are present, a `ValueError` is raised.

*force*

If this keyword argument is specified as true, any existing handlers attached to the root logger are removed and closed, before carrying out the configuration as specified by the other arguments.

*encoding*

If this keyword argument is specified along with *filename*, its value is used when the [`FileHandler`](https://docs.python.org/3.13/library/logging.handlers.html#logging.FileHandler "logging.FileHandler") is created, and thus used when opening the output file.

*errors*

If this keyword argument is specified along with *filename*, its value is used when the [`FileHandler`](https://docs.python.org/3.13/library/logging.handlers.html#logging.FileHandler "logging.FileHandler") is created, and thus used when opening the output file. If not specified, the value ‘backslashreplace’ is used. Note that if `None` is specified, it will be passed as such to [`open()`](https://docs.python.org/3.13/builtins/functions.html#open "open"), which means that it will be treated the same as passing ‘errors’.

Changed in version 3.2: The *style* argument was added.

Changed in version 3.3: The *handlers* argument was added. Additional checks were added to catch situations where incompatible arguments are specified (e.g. *handlers* together with *stream* or *filename*, or *stream* together with *filename*).

Changed in version 3.8: The *force* argument was added.

Changed in version 3.9: The *encoding* and *errors* arguments were added.

logging.shutdown()[¶](#logging.shutdown "Link to this definition")

Informs the logging system to perform an orderly shutdown by flushing and closing all handlers. This should be called at application exit and no further use of the logging system should be made after this call.

When the logging module is imported, it registers this function as an exit handler (see [`atexit`](https://docs.python.org/3.13/library/atexit.html#module-atexit "atexit: Register and execute cleanup functions.")), so normally there’s no need to do that manually.

logging.setLoggerClass(*klass*)[¶](#logging.setLoggerClass "Link to this definition")

Tells the logging system to use the class *klass* when instantiating a logger. The class should define `__init__()` such that only a name argument is required, and the `__init__()` should call `Logger.__init__()`. This function is typically called before any loggers are instantiated by applications which need to use custom logger behavior. After this call, as at any other time, do not instantiate loggers directly using the subclass: continue to use the [`logging.getLogger()`](#logging.getLogger "logging.getLogger") API to get your loggers.

logging.setLogRecordFactory(*factory*)[¶](#logging.setLogRecordFactory "Link to this definition")

Set a callable which is used to create a [`LogRecord`](#logging.LogRecord "logging.LogRecord").

Parameters:

**factory** – The factory callable to be used to instantiate a log record.

Added in version 3.2: This function has been provided, along with [`getLogRecordFactory()`](#logging.getLogRecordFactory "logging.getLogRecordFactory"), to allow developers more control over how the [`LogRecord`](#logging.LogRecord "logging.LogRecord") representing a logging event is constructed.

The factory has the following signature:

`factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)`

> name:
> 
> The logger name.
> 
> level:
> 
> The logging level (numeric).
> 
> fn:
> 
> The full pathname of the file where the logging call was made.
> 
> lno:
> 
> The line number in the file where the logging call was made.
> 
> msg:
> 
> The logging message.
> 
> args:
> 
> The arguments for the logging message.
> 
> exc\_info:
> 
> An exception tuple, or `None`.
> 
> func:
> 
> The name of the function or method which invoked the logging call.
> 
> sinfo:
> 
> A stack traceback such as is provided by [`traceback.print_stack()`](https://docs.python.org/3.13/library/traceback.html#traceback.print_stack "traceback.print_stack"), showing the call hierarchy.
> 
> kwargs:
> 
> Additional keyword arguments.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
