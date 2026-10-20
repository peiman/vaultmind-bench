---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#17-module-level-attributes.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-17-module-level-attributes
type: reference
title: logging — Logging facility for Python › Module-Level Attributes
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#17-module-level-attributes
source_hash: b854cf55b07ae264e0cd8a46b6b2ce8d6bf06bdd2d682217730ee8039d88c09c
---
logging.lastResort[¶](#logging.lastResort "Link to this definition")

A “handler of last resort” is available through this attribute. This is a [`StreamHandler`](https://docs.python.org/3.13/library/logging.handlers.html#logging.StreamHandler "logging.StreamHandler") writing to `sys.stderr` with a level of `WARNING`, and is used to handle logging events in the absence of any logging configuration. The end result is to just print the message to `sys.stderr`. This replaces the earlier error message saying that “no handlers could be found for logger XYZ”. If you need the earlier behaviour for some reason, `lastResort` can be set to `None`.

Added in version 3.2.

logging.raiseExceptions[¶](#logging.raiseExceptions "Link to this definition")

Used to see if exceptions during handling should be propagated.

Default: `True`.

If `raiseExceptions` is `False`, exceptions get silently ignored. This is what is mostly wanted for a logging system - most users will not care about errors in the logging system, they are more interested in application errors.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
