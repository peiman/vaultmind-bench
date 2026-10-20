---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#10-security-considerations.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-10-security-considerations
type: reference
title: subprocess — Subprocess management › Security Considerations
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#10-security-considerations
source_hash: 9457b782858dcc864962d47f69245d8eea25007d10f2da0f63dca035e27b7f51
---
Unlike some other popen functions, this library will not implicitly choose to call a system shell. This means that all characters, including shell metacharacters, can safely be passed to child processes. If the shell is invoked explicitly, via `shell=True`, it is the application’s responsibility to ensure that all whitespace and metacharacters are quoted appropriately to avoid [shell injection](https://en.wikipedia.org/wiki/Shell_injection#Shell_injection) vulnerabilities. On [some platforms](https://docs.python.org/3.13/library/shlex.html#shlex-quote-warning), it is possible to use [`shlex.quote()`](https://docs.python.org/3.13/library/shlex.html#shlex.quote "shlex.quote") for this escaping.

On Windows, batch files (`*.bat` or `*.cmd`) may be launched by the operating system in a system shell regardless of the arguments passed to this library. This could result in arguments being parsed according to shell rules, but without any escaping added by Python. If you are intentionally launching a batch file with arguments from untrusted sources, consider passing `shell=True` to allow Python to escape special characters. See [gh-114539](https://github.com/python/cpython/issues/114539) for additional discussion.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
