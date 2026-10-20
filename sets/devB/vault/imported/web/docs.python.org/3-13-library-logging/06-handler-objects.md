---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#06-handler-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-06-handler-objects
type: reference
title: logging — Logging facility for Python › Handler Objects
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#06-handler-objects
source_hash: 63c98f33294ec1ef1e28a4a1cf79acfec7616916a94fda7305f9eb6a16efdd23
---
Handlers have the following attributes and methods. Note that [`Handler`](#logging.Handler "logging.Handler") is never instantiated directly; this class acts as a base for more useful subclasses. However, the `__init__()` method in subclasses needs to call [`Handler.__init__()`](#logging.Handler.__init__ "logging.Handler.__init__").

*class* logging.Handler[¶](#logging.Handler "Link to this definition")

\_\_init\_\_(*level=NOTSET*)[¶](#logging.Handler.__init__ "Link to this definition")

Initializes the `Handler` instance by setting its level, setting the list of filters to the empty list and creating a lock (using [`createLock()`](#logging.Handler.createLock "logging.Handler.createLock")) for serializing access to an I/O mechanism.

createLock()[¶](#logging.Handler.createLock "Link to this definition")

Initializes a thread lock which can be used to serialize access to underlying I/O functionality which may not be threadsafe.

acquire()[¶](#logging.Handler.acquire "Link to this definition")

Acquires the thread lock created with [`createLock()`](#logging.Handler.createLock "logging.Handler.createLock").

release()[¶](#logging.Handler.release "Link to this definition")

Releases the thread lock acquired with [`acquire()`](#logging.Handler.acquire "logging.Handler.acquire").

setLevel(*level*)[¶](#logging.Handler.setLevel "Link to this definition")

Sets the threshold for this handler to *level*. Logging messages which are less severe than *level* will be ignored. When a handler is created, the level is set to [`NOTSET`](#logging.NOTSET "logging.NOTSET") (which causes all messages to be processed).

See [Logging Levels](#levels) for a list of levels.

Changed in version 3.2: The *level* parameter now accepts a string representation of the level such as ‘INFO’ as an alternative to the integer constants such as [`INFO`](#logging.INFO "logging.INFO").

setFormatter(*fmt*)[¶](#logging.Handler.setFormatter "Link to this definition")

Sets the formatter for this handler to *fmt*. The *fmt* argument must be a [`Formatter`](#logging.Formatter "logging.Formatter") instance or `None`.

addFilter(*filter*)[¶](#logging.Handler.addFilter "Link to this definition")

Adds the specified filter *filter* to this handler.

removeFilter(*filter*)[¶](#logging.Handler.removeFilter "Link to this definition")

Removes the specified filter *filter* from this handler.

filter(*record*)[¶](#logging.Handler.filter "Link to this definition")

Apply this handler’s filters to the record and return `True` if the record is to be processed. The filters are consulted in turn, until one of them returns a false value. If none of them return a false value, the record will be emitted. If one returns a false value, the handler will not emit the record.

flush()[¶](#logging.Handler.flush "Link to this definition")

Ensure all logging output has been flushed. This version does nothing and is intended to be implemented by subclasses.

close()[¶](#logging.Handler.close "Link to this definition")

Tidy up any resources used by the handler. This version does no output but removes the handler from an internal map of handlers, which is used for handler lookup by name.

Subclasses should ensure that this gets called from overridden `close()` methods.

handle(*record*)[¶](#logging.Handler.handle "Link to this definition")

Conditionally emits the specified logging record, depending on filters which may have been added to the handler. Wraps the actual emission of the record with acquisition/release of the I/O thread lock.

handleError(*record*)[¶](#logging.Handler.handleError "Link to this definition")

This method should be called from handlers when an exception is encountered during an [`emit()`](#logging.Handler.emit "logging.Handler.emit") call. If the module-level attribute [`raiseExceptions`](#logging.raiseExceptions "logging.raiseExceptions") is `False`, exceptions get silently ignored. This is what is mostly wanted for a logging system - most users will not care about errors in the logging system, they are more interested in application errors. You could, however, replace this with a custom handler if you wish. The specified record is the one which was being processed when the exception occurred. (The default value of `raiseExceptions` is `True`, as that is more useful during development).

format(*record*)[¶](#logging.Handler.format "Link to this definition")

Do formatting for a record - if a formatter is set, use it. Otherwise, use the default formatter for the module.

emit(*record*)[¶](#logging.Handler.emit "Link to this definition")

Do whatever it takes to actually log the specified logging record. This version is intended to be implemented by subclasses and so raises a [`NotImplementedError`](https://docs.python.org/3.13/builtins/exceptions.html#NotImplementedError "NotImplementedError").

Warning

This method is called after a handler-level lock is acquired, which is released after this method returns. When you override this method, note that you should be careful when calling anything that invokes other parts of the logging API which might do locking, because that might result in a deadlock. Specifically:

- Logging configuration APIs acquire the module-level lock, and then individual handler-level locks as those handlers are configured.
- Many logging APIs lock the module-level lock. If such an API is called from this method, it could cause a deadlock if a configuration call is made on another thread, because that thread will try to acquire the module-level lock *before* the handler-level lock, whereas this thread tries to acquire the module-level lock *after* the handler-level lock (because in this method, the handler-level lock has already been acquired).

For a list of handlers included as standard, see [`logging.handlers`](https://docs.python.org/3.13/library/logging.handlers.html#module-logging.handlers "logging.handlers: Handlers for the logging module.").

Part of [[imported/web/docs.python.org/3-13-library-logging]].
