---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#23-converting-an-argument-sequence-to-a-string-on-win.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-23-converting-an-argument-sequence-to-a-string-on-win
type: reference
title: subprocess — Subprocess management › Notes › Converting an argument sequence to a string on Windows
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#23-converting-an-argument-sequence-to-a-string-on-win
source_hash: b05aaf5c8e95e3626933c03d48e37330a69ecb5ab41cbe30774ed72f5f849b12
---
On Windows, an *args* sequence is converted to a string that can be parsed using the following rules (which correspond to the rules used by the MS C runtime):

1. Arguments are delimited by white space, which is either a space or a tab.
2. A string surrounded by double quotation marks is interpreted as a single argument, regardless of white space contained within. A quoted string can be embedded in an argument.
3. A double quotation mark preceded by a backslash is interpreted as a literal double quotation mark.
4. Backslashes are interpreted literally, unless they immediately precede a double quotation mark.
5. If backslashes immediately precede a double quotation mark, every pair of backslashes is interpreted as a literal backslash. If the number of backslashes is odd, the last backslash escapes the next double quotation mark as described in rule 3.

See also

[`shlex`](https://docs.python.org/3.13/library/shlex.html#module-shlex "shlex: Simple lexical analysis for Unix shell-like languages.")

Module which provides function to parse and escape command lines.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
