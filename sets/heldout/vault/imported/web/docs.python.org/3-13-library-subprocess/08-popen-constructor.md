---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#08-popen-constructor.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-08-popen-constructor
type: reference
title: subprocess — Subprocess management › Using the `subprocess` Module › Popen Constructor (4/4)
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#08-popen-constructor
source_hash: c1124a2c6623e512f90bfefed38246473e45911d053a4c3d7689860092cbb28a
---
*pipesize* can be used to change the size of the pipe when [`PIPE`](#subprocess.PIPE "subprocess.PIPE") is used for *stdin*, *stdout* or *stderr*. The size of the pipe is only changed on platforms that support this (only Linux at this time of writing). Other platforms will ignore this parameter.

Changed in version 3.10: Added the *pipesize* parameter.

Popen objects are supported as context managers via the [`with`](https://docs.python.org/3.13/reference/compound_stmts.html#with) statement: on exit, standard file descriptors are closed, and the process is waited for.

```
with Popen(["ifconfig"], stdout=PIPE) as proc:
    log.write(proc.stdout.read())
```

Popen and the other functions in this module that use it raise an [auditing event](https://docs.python.org/3.13/library/sys.html#auditing) `subprocess.Popen` with arguments `executable`, `args`, `cwd`, and `env`. The value for `args` may be a single string or a list of strings, depending on platform.

Changed in version 3.2: Added context manager support.

Changed in version 3.6: Popen destructor now emits a [`ResourceWarning`](https://docs.python.org/3.13/builtins/exceptions.html#ResourceWarning "ResourceWarning") warning if the child process is still running.

Changed in version 3.8: Popen can use [`os.posix_spawn()`](https://docs.python.org/3.13/library/os.html#os.posix_spawn "os.posix_spawn") in some cases for better performance. On Windows Subsystem for Linux and QEMU User Emulation, Popen constructor using `os.posix_spawn()` no longer raise an exception on errors like missing program, but the child process fails with a non-zero [`returncode`](#subprocess.Popen.returncode "subprocess.Popen.returncode").

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
