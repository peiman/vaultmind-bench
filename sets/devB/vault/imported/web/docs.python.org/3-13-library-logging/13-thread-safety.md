---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#13-thread-safety.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-13-thread-safety
type: reference
title: logging — Logging facility for Python › Thread Safety
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#13-thread-safety
source_hash: 086317d9406f38915a0c627013c6a990e454722edd7e64cca73121ff50cb03ea
---
The logging module is intended to be thread-safe without any special work needing to be done by its clients. It achieves this through using threading locks; there is one lock to serialize access to the module’s shared data, and each handler also creates a lock to serialize access to its underlying I/O.

If you are implementing asynchronous signal handlers using the [`signal`](https://docs.python.org/3.13/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") module, you may not be able to use logging from within such handlers. This is because lock implementations in the [`threading`](https://docs.python.org/3.13/library/threading.html#module-threading "threading: Thread-based parallelism.") module are not always re-entrant, and so cannot be invoked from such signal handlers.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
