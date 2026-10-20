---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#12-popen-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-12-popen-objects
type: reference
title: subprocess — Subprocess management › Popen Objects (2/2)
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#12-popen-objects
source_hash: bbbee6832fed1e9de66e874f8fee6cb09edee0ef13b8cc9200b13b9e2239ed11
---
If the *stdout* argument was [`PIPE`](#subprocess.PIPE "subprocess.PIPE"), this attribute is a readable stream object as returned by [`open()`](https://docs.python.org/3.13/builtins/functions.html#open "open"). Reading from the stream provides output from the child process. If the *encoding* or *errors* arguments were specified or the *text* or *universal\_newlines* argument was `True`, the stream is a text stream, otherwise it is a byte stream. If the *stdout* argument was not `PIPE`, this attribute is `None`.

Popen.stderr[¶](#subprocess.Popen.stderr "Link to this definition")

If the *stderr* argument was [`PIPE`](#subprocess.PIPE "subprocess.PIPE"), this attribute is a readable stream object as returned by [`open()`](https://docs.python.org/3.13/builtins/functions.html#open "open"). Reading from the stream provides error output from the child process. If the *encoding* or *errors* arguments were specified or the *text* or *universal\_newlines* argument was `True`, the stream is a text stream, otherwise it is a byte stream. If the *stderr* argument was not `PIPE`, this attribute is `None`.

Warning

Use [`communicate()`](#subprocess.Popen.communicate "subprocess.Popen.communicate") rather than [`.stdin.write`](#subprocess.Popen.stdin "subprocess.Popen.stdin"), [`.stdout.read`](#subprocess.Popen.stdout "subprocess.Popen.stdout") or [`.stderr.read`](#subprocess.Popen.stderr "subprocess.Popen.stderr") to avoid deadlocks due to any of the other OS pipe buffers filling up and blocking the child process.

Popen.pid[¶](#subprocess.Popen.pid "Link to this definition")

The process ID of the child process.

Note that if you set the *shell* argument to `True`, this is the process ID of the spawned shell.

Popen.returncode[¶](#subprocess.Popen.returncode "Link to this definition")

The child return code. Initially `None`, [`returncode`](#subprocess.Popen.returncode "subprocess.Popen.returncode") is set by a call to the [`poll()`](#subprocess.Popen.poll "subprocess.Popen.poll"), [`wait()`](#subprocess.Popen.wait "subprocess.Popen.wait"), or [`communicate()`](#subprocess.Popen.communicate "subprocess.Popen.communicate") methods if they detect that the process has terminated.

A `None` value indicates that the process hadn’t yet terminated at the time of the last method call.

A negative value `-N` indicates that the child was terminated by signal `N` (POSIX only).

When `shell=True`, the return code reflects the exit status of the shell itself (e.g. `/bin/sh`), which may map signals to codes such as `128+N`. See the documentation of the shell (for example, the Bash manual’s Exit Status) for details.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
