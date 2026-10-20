---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/logging.html#08-formatter-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-logging-08-formatter-objects
type: reference
title: logging — Logging facility for Python › Formatter Objects (2/2)
url: https://docs.python.org/3.13/library/logging.html
source: https://docs.python.org/3.13/library/logging.html#08-formatter-objects
source_hash: 6c3642b496a3642abba2d34bd15cca341a6435d057e317752a784e60bebe8234
---
Changed in version 3.3: Previously, the default format was hard-coded as in this example: `2010-09-06 22:38:15,292` where the part before the comma is handled by a strptime format string (`'%Y-%m-%d %H:%M:%S'`), and the part after the comma is a millisecond value. Because strptime does not have a format placeholder for milliseconds, the millisecond value is appended using another format string, `'%s,%03d'` — and both of these format strings have been hardcoded into this method. With the change, these strings are defined as class-level attributes which can be overridden at the instance level when desired. The names of the attributes are `default_time_format` (for the strptime format string) and `default_msec_format` (for appending the millisecond value).

Changed in version 3.9: The `default_msec_format` can be `None`.

formatException(*exc\_info*)[¶](#logging.Formatter.formatException "Link to this definition")

Formats the specified exception information (a standard exception tuple as returned by [`sys.exc_info()`](https://docs.python.org/3.13/library/sys.html#sys.exc_info "sys.exc_info")) as a string. This default implementation just uses [`traceback.print_exception()`](https://docs.python.org/3.13/library/traceback.html#traceback.print_exception "traceback.print_exception"). The resulting string is returned.

formatStack(*stack\_info*)[¶](#logging.Formatter.formatStack "Link to this definition")

Formats the specified stack information (a string as returned by [`traceback.print_stack()`](https://docs.python.org/3.13/library/traceback.html#traceback.print_stack "traceback.print_stack"), but with the last newline removed) as a string. This default implementation just returns the input value.

*class* logging.BufferingFormatter(*linefmt=None*)[¶](#logging.BufferingFormatter "Link to this definition")

A base formatter class suitable for subclassing when you want to format a number of records. You can pass a [`Formatter`](#logging.Formatter "logging.Formatter") instance which you want to use to format each line (that corresponds to a single record). If not specified, the default formatter (which just outputs the event message) is used as the line formatter.

Return a header for a list of *records*. The base implementation just returns the empty string. You will need to override this method if you want specific behaviour, e.g. to show the count of records, a title or a separator line.

Return a footer for a list of *records*. The base implementation just returns the empty string. You will need to override this method if you want specific behaviour, e.g. to show the count of records or a separator line.

format(*records*)[¶](#logging.BufferingFormatter.format "Link to this definition")

Return formatted text for a list of *records*. The base implementation just returns the empty string if there are no records; otherwise, it returns the concatenation of the header, each record formatted with the line formatter, and the footer.

Part of [[imported/web/docs.python.org/3-13-library-logging]].
