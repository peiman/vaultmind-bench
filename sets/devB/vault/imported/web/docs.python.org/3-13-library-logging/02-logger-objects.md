---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#02-logger-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-02-logger-objects
type: reference
title: logging — Logging facility for Python › Logger Objects (1/4)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#02-logger-objects
source_hash: a1dbd90dd4a98c6ba029528be310b49a63697c473c66a053f887083421a7e1b3
---
Loggers have the following attributes and methods. Note that Loggers should *NEVER* be instantiated directly, but always through the module-level function `logging.getLogger(name)`. Multiple calls to [`getLogger()`](#logging.getLogger "logging.getLogger") with the same name will always return a reference to the same Logger object.

The `name` is potentially a period-separated hierarchical value, like `foo.bar.baz` (though it could also be just plain `foo`, for example). Loggers that are further down in the hierarchical list are children of loggers higher up in the list. For example, given a logger with a name of `foo`, loggers with names of `foo.bar`, `foo.bar.baz`, and `foo.bam` are all descendants of `foo`. In addition, all loggers are descendants of the root logger. The logger name hierarchy is analogous to the Python package hierarchy, and identical to it if you organise your loggers on a per-module basis using the recommended construction `logging.getLogger(__name__)`. That’s because in a module, `__name__` is the module’s name in the Python package namespace.

*class* logging.Logger[¶](#logging.Logger "Link to this definition")

name[¶](#logging.Logger.name "Link to this definition")

This is the logger’s name, and is the value that was passed to [`getLogger()`](#logging.getLogger "logging.getLogger") to obtain the logger.

Note

This attribute should be treated as read-only.

level[¶](#logging.Logger.level "Link to this definition")

The threshold of this logger, as set by the [`setLevel()`](#logging.Logger.setLevel "logging.Logger.setLevel") method.

Note

Do not set this attribute directly - always use [`setLevel()`](#logging.Logger.setLevel "logging.Logger.setLevel"), which has checks for the level passed to it.

parent[¶](#logging.Logger.parent "Link to this definition")

The parent logger of this logger. It may change based on later instantiation of loggers which are higher up in the namespace hierarchy.

Note

This value should be treated as read-only.

propagate[¶](#logging.Logger.propagate "Link to this definition")

If this attribute evaluates to true, events logged to this logger will be passed to the handlers of higher level (ancestor) loggers, in addition to any handlers attached to this logger. Messages are passed directly to the ancestor loggers’ handlers - neither the level nor filters of the ancestor loggers in question are considered.

If this evaluates to false, logging messages are not passed to the handlers of ancestor loggers.

Spelling it out with an example: If the propagate attribute of the logger named `A.B.C` evaluates to true, any event logged to `A.B.C` via a method call such as `logging.getLogger('A.B.C').error(...)` will \[subject to passing that logger’s level and filter settings] be passed in turn to any handlers attached to loggers named `A.B`, `A` and the root logger, after first being passed to any handlers attached to `A.B.C`. If any logger in the chain `A.B.C`, `A.B`, `A` has its `propagate` attribute set to false, then that is the last logger whose handlers are offered the event to handle, and propagation stops at that point.

The constructor sets this attribute to `True`.

Note

If you attach a handler to a logger *and* one or more of its ancestors, it may emit the same record multiple times. In general, you should not need to attach a handler to more than one logger - if you just attach it to the appropriate logger which is highest in the logger hierarchy, then it will see all events logged by all descendant loggers, provided that their propagate setting is left set to `True`. A common scenario is to attach handlers only to the root logger, and to let propagation take care of the rest.

handlers[¶](#logging.Logger.handlers "Link to this definition")

The list of handlers directly attached to this logger instance.

Note

This attribute should be treated as read-only; it is normally changed via the [`addHandler()`](#logging.Logger.addHandler "logging.Logger.addHandler") and [`removeHandler()`](#logging.Logger.removeHandler "logging.Logger.removeHandler") methods, which use locks to ensure thread-safe operation.

disabled[¶](#logging.Logger.disabled "Link to this definition")

This attribute disables handling of any events. It is set to `False` in the initializer, and only changed by logging configuration code.

Note

This attribute should be treated as read-only.

setLevel(*level*)[¶](#logging.Logger.setLevel "Link to this definition")

Sets the threshold for this logger to *level*. Logging messages which are less severe than *level* will be ignored; logging messages which have severity *level* or higher will be emitted by whichever handler or handlers service this logger, unless a handler’s level has been set to a higher severity level than *level*.

When a logger is created, the level is set to [`NOTSET`](#logging.NOTSET "logging.NOTSET") (which causes all messages to be processed when the logger is the root logger, or delegation to the parent when the logger is a non-root logger). Note that the root logger is created with level [`WARNING`](#logging.WARNING "logging.WARNING").

The term ‘delegation to the parent’ means that if a logger has a level of NOTSET, its chain of ancestor loggers is traversed until either an ancestor with a level other than NOTSET is found, or the root is reached.

If an ancestor is found with a level other than NOTSET, then that ancestor’s level is treated as the effective level of the logger where the ancestor search began, and is used to determine how a logging event is handled.

If the root is reached, and it has a level of NOTSET, then all messages will be processed. Otherwise, the root’s level will be used as the effective level.

See [Logging Levels](#levels) for a list of levels.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
