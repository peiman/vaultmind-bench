---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#12-loggeradapter-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-12-loggeradapter-objects
type: reference
title: logging — Logging facility for Python › LoggerAdapter Objects
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#12-loggeradapter-objects
source_hash: 399434814d7f06fc8a2eb19760482d87d1da88a2a980f5ae51fbeca4698b0891
---
[`LoggerAdapter`](#logging.LoggerAdapter "logging.LoggerAdapter") instances are used to conveniently pass contextual information into logging calls. For a usage example, see the section on [adding contextual information to your logging output](https://docs.python.org/3.13/howto/logging-cookbook.html#context-info).

*class* logging.LoggerAdapter(*logger*, *extra=None*, *merge\_extra=False*)[¶](#logging.LoggerAdapter "Link to this definition")

Returns an instance of `LoggerAdapter` initialized with an underlying [`Logger`](#logging.Logger "logging.Logger") instance, an optional dict-like object (*extra*), and an optional boolean (*merge\_extra*) indicating whether or not the *extra* argument of individual log calls should be merged with the `LoggerAdapter` extra. The default behavior is to ignore the *extra* argument of individual log calls and only use the one of the `LoggerAdapter` instance

process(*msg*, *kwargs*)[¶](#logging.LoggerAdapter.process "Link to this definition")

Modifies the message and/or keyword arguments passed to a logging call in order to insert contextual information. This implementation takes the object passed as *extra* to the constructor and adds it to *kwargs* using key ‘extra’. The return value is a (*msg*, *kwargs*) tuple which has the (possibly modified) versions of the arguments passed in.

manager[¶](#logging.LoggerAdapter.manager "Link to this definition")

Delegates to the underlying `manager` on *logger*.

\_log[¶](#logging.LoggerAdapter._log "Link to this definition")

Delegates to the underlying `_log()` method on *logger*.

In addition to the above, `LoggerAdapter` supports the following methods of [`Logger`](#logging.Logger "logging.Logger"): [`debug()`](#logging.Logger.debug "logging.Logger.debug"), [`info()`](#logging.Logger.info "logging.Logger.info"), [`warning()`](#logging.Logger.warning "logging.Logger.warning"), [`error()`](#logging.Logger.error "logging.Logger.error"), [`exception()`](#logging.Logger.exception "logging.Logger.exception"), [`critical()`](#logging.Logger.critical "logging.Logger.critical"), [`log()`](#logging.Logger.log "logging.Logger.log"), [`isEnabledFor()`](#logging.Logger.isEnabledFor "logging.Logger.isEnabledFor"), [`getEffectiveLevel()`](#logging.Logger.getEffectiveLevel "logging.Logger.getEffectiveLevel"), [`setLevel()`](#logging.Logger.setLevel "logging.Logger.setLevel") and [`hasHandlers()`](#logging.Logger.hasHandlers "logging.Logger.hasHandlers"). These methods have the same signatures as their counterparts in `Logger`, so you can use the two types of instances interchangeably.

Changed in version 3.2: The [`isEnabledFor()`](#logging.Logger.isEnabledFor "logging.Logger.isEnabledFor"), [`getEffectiveLevel()`](#logging.Logger.getEffectiveLevel "logging.Logger.getEffectiveLevel"), [`setLevel()`](#logging.Logger.setLevel "logging.Logger.setLevel") and [`hasHandlers()`](#logging.Logger.hasHandlers "logging.Logger.hasHandlers") methods were added to `LoggerAdapter`. These methods delegate to the underlying logger.

Changed in version 3.6: Attribute `manager` and method `_log()` were added, which delegate to the underlying logger and allow adapters to be nested.

Changed in version 3.10: The *extra* argument is now optional.

Changed in version 3.13: The *merge\_extra* parameter was added.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
