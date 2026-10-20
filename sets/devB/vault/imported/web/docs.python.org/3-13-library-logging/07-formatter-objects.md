---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#07-formatter-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-07-formatter-objects
type: reference
title: logging — Logging facility for Python › Formatter Objects (1/2)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#07-formatter-objects
source_hash: 645638cf9974f62775beae53242fc1010a98dcfcd75de8663e1a6d5235dc67bf
---
*class* logging.Formatter(*fmt=None*, *datefmt=None*, *style='%'*, *validate=True*, *\**, *defaults=None*)[¶](#logging.Formatter "Link to this definition")

Responsible for converting a [`LogRecord`](#logging.LogRecord "logging.LogRecord") to an output string to be interpreted by a human or external system.

Parameters:

- **fmt** ([*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str")) – A format string in the given *style* for the logged output as a whole. The possible mapping keys are drawn from the [`LogRecord`](#logging.LogRecord "logging.LogRecord") object’s [LogRecord attributes](#logrecord-attributes). If not specified, `'%(message)s'` is used, which is just the logged message.
- **datefmt** ([*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str")) – A format string for the date/time portion of the logged output. If not specified, the default described in [`formatTime()`](#logging.Formatter.formatTime "logging.Formatter.formatTime") is used.
- **style** ([*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str")) – Can be one of `'%'`, `'{'` or `'$'` and determines how the format string will be merged with its data: using one of [printf-style String Formatting](https://docs.python.org/3.13/builtins/stdtypes.html#old-string-formatting) (`%`), [`str.format()`](https://docs.python.org/3.13/builtins/stdtypes.html#str.format "str.format") (`{`) or [`string.Template`](https://docs.python.org/3.13/library/string.html#string.Template "string.Template") (`$`). This only applies to *fmt* (e.g. `'%(message)s'` versus `'{message}'`), not to the actual log messages passed to the logging methods. However, there are [other ways](https://docs.python.org/3.13/howto/logging-cookbook.html#formatting-styles) to use `{`- and `$`-formatting for log messages.
- **validate** ([*bool*](https://docs.python.org/3.13/builtins/functions.html#bool "bool")) – If `True` (the default), incorrect or mismatched *fmt* and *style* will raise a [`ValueError`](https://docs.python.org/3.13/builtins/exceptions.html#ValueError "ValueError"); for example, `logging.Formatter('%(asctime)s - %(message)s', style='{')`.
- **defaults** ([*dict*](https://docs.python.org/3.13/builtins/stdtypes.html#dict "dict")*\[*[*str*](https://docs.python.org/3.13/builtins/stdtypes.html#str "str")*, Any]*) – A dictionary with default values to use in custom fields. For example, `logging.Formatter('%(ip)s %(message)s', defaults={"ip": None})`

Changed in version 3.2: Added the *style* parameter.

Changed in version 3.8: Added the *validate* parameter.

Changed in version 3.10: Added the *defaults* parameter.

format(*record*)[¶](#logging.Formatter.format "Link to this definition")

The record’s attribute dictionary is used as the operand to a string formatting operation. Returns the resulting string. Before formatting the dictionary, a couple of preparatory steps are carried out. The *message* attribute of the record is computed using *msg* % *args*. If the formatting string contains `'(asctime)'`, [`formatTime()`](#logging.Formatter.formatTime "logging.Formatter.formatTime") is called to format the event time. If there is exception information, it is formatted using [`formatException()`](#logging.Formatter.formatException "logging.Formatter.formatException") and appended to the message. Note that the formatted exception information is cached in attribute *exc\_text*. This is useful because the exception information can be pickled and sent across the wire, but you should be careful if you have more than one `Formatter` subclass which customizes the formatting of exception information. In this case, you will have to clear the cached value (by setting the *exc\_text* attribute to `None`) after a formatter has done its formatting, so that the next formatter to handle the event doesn’t use the cached value, but recalculates it afresh.

If stack information is available, it’s appended after the exception information, using [`formatStack()`](#logging.Formatter.formatStack "logging.Formatter.formatStack") to transform it if necessary.

formatTime(*record*, *datefmt=None*)[¶](#logging.Formatter.formatTime "Link to this definition")

This method should be called from [`format()`](https://docs.python.org/3.13/builtins/functions.html#format "format") by a formatter which wants to make use of a formatted time. This method can be overridden in formatters to provide for any specific requirement, but the basic behavior is as follows: if *datefmt* (a string) is specified, it is used with [`time.strftime()`](https://docs.python.org/3.13/library/time.html#time.strftime "time.strftime") to format the creation time of the record. Otherwise, the format ‘%Y-%m-%d %H:%M:%S,uuu’ is used, where the uuu part is a millisecond value and the other letters are as per the `time.strftime()` documentation. An example time in this format is `2003-01-23 00:29:50,411`. The resulting string is returned.

This function uses a user-configurable function to convert the creation time to a tuple. By default, [`time.localtime()`](https://docs.python.org/3.13/library/time.html#time.localtime "time.localtime") is used; to change this for a particular formatter instance, set the `converter` attribute to a function with the same signature as `time.localtime()` or [`time.gmtime()`](https://docs.python.org/3.13/library/time.html#time.gmtime "time.gmtime"). To change it for all formatters, for example if you want all logging times to be shown in GMT, set the `converter` attribute in the `Formatter` class.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
