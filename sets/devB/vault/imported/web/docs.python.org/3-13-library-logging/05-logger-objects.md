---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#05-logger-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-05-logger-objects
type: reference
title: logging — Logging facility for Python › Logger Objects (4/4)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#05-logger-objects
source_hash: 5303ca398cf28f8fff19305cbabcb1a91eaa1caa1142238f07b5c29622c0415a
---
This is a factory method which can be overridden in subclasses to create specialized [`LogRecord`](#logging.LogRecord "logging.LogRecord") instances.

hasHandlers()[¶](#logging.Logger.hasHandlers "Link to this definition")

Checks to see if this logger has any handlers configured. This is done by looking for handlers in this logger and its parents in the logger hierarchy. Returns `True` if a handler was found, else `False`. The method stops searching up the hierarchy whenever a logger with the ‘propagate’ attribute set to false is found - that will be the last logger which is checked for the existence of handlers.

Added in version 3.2.

Changed in version 3.7: Loggers can now be pickled and unpickled.

## Logging Levels

The numeric values of logging levels are given in the following table. These are primarily of interest if you want to define your own levels, and need them to have specific values relative to the predefined levels. If you define a level with the same numeric value, it overwrites the predefined value; the predefined name is lost.

Level

Numeric value

What it means / When to use it

logging.NOTSET[¶](#logging.NOTSET "Link to this definition")

0

When set on a logger, indicates that ancestor loggers are to be consulted to determine the effective level. If that still resolves to `NOTSET`, then all events are logged. When set on a handler, all events are handled.

logging.DEBUG[¶](#logging.DEBUG "Link to this definition")

10

Detailed information, typically only of interest to a developer trying to diagnose a problem.

logging.INFO[¶](#logging.INFO "Link to this definition")

20

Confirmation that things are working as expected.

logging.WARNING[¶](#logging.WARNING "Link to this definition")

30

An indication that something unexpected happened, or that a problem might occur in the near future (e.g. ‘disk space low’). The software is still working as expected.

logging.ERROR[¶](#logging.ERROR "Link to this definition")

40

Due to a more serious problem, the software has not been able to perform some function.

logging.CRITICAL[¶](#logging.CRITICAL "Link to this definition")

50

A serious error, indicating that the program itself may be unable to continue running.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
