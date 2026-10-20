---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#06-popen-constructor.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-06-popen-constructor
type: reference
title: subprocess — Subprocess management › Using the `subprocess` Module › Popen Constructor (2/4)
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#06-popen-constructor
source_hash: 9c393f173d5d0774cc4b7098638854a65d633a02fb1820007587e09b1bd4e66c
---
Read the [Security Considerations](#security-considerations) section before using `shell=True`.

*bufsize* will be supplied as the corresponding argument to the [`open()`](https://docs.python.org/3.13/builtins/functions.html#open "open") function when creating the stdin/stdout/stderr pipe file objects:

- `0` means unbuffered (read and write are one system call and can return short)
- `1` means line buffered (only usable if `text=True` or `universal_newlines=True`)
- any other positive value means use a buffer of approximately that size
- negative bufsize (the default) means the system default of io.DEFAULT\_BUFFER\_SIZE will be used.

Changed in version 3.3.1: *bufsize* now defaults to -1 to enable buffering by default to match the behavior that most code expects. In versions prior to Python 3.2.4 and 3.3.1 it incorrectly defaulted to `0` which was unbuffered and allowed short reads. This was unintentional and did not match the behavior of Python 2 as most code expected.

The *executable* argument specifies a replacement program to execute. It is very seldom needed. When `shell=False`, *executable* replaces the program to execute specified by *args*. However, the original *args* is still passed to the program. Most programs treat the program specified by *args* as the command name, which can then be different from the program actually executed. On POSIX, the *args* name becomes the display name for the executable in utilities such as **ps**. If `shell=True`, on POSIX the *executable* argument specifies a replacement shell for the default `/bin/sh`.

Changed in version 3.6: *executable* parameter accepts a [path-like object](https://docs.python.org/3.13/glossary.html#term-path-like-object) on POSIX.

Changed in version 3.8: *executable* parameter accepts a bytes and [path-like object](https://docs.python.org/3.13/glossary.html#term-path-like-object) on Windows.

Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.

*stdin*, *stdout* and *stderr* specify the executed program’s standard input, standard output and standard error file handles, respectively. Valid values are `None`, [`PIPE`](#subprocess.PIPE "subprocess.PIPE"), [`DEVNULL`](#subprocess.DEVNULL "subprocess.DEVNULL"), an existing file descriptor (a positive integer), and an existing [file object](https://docs.python.org/3.13/glossary.html#term-file-object) with a valid file descriptor. With the default settings of `None`, no redirection will occur. `PIPE` indicates that a new pipe to the child should be created. `DEVNULL` indicates that the special file [`os.devnull`](https://docs.python.org/3.13/library/os.html#os.devnull "os.devnull") will be used. Additionally, *stderr* can be [`STDOUT`](#subprocess.STDOUT "subprocess.STDOUT"), which indicates that the stderr data from the applications should be captured into the same file handle as for *stdout*.

If *preexec\_fn* is set to a callable object, this object will be called in the child process just before the child is executed. (POSIX only)

Warning

The *preexec\_fn* parameter is NOT SAFE to use in the presence of threads in your application. The child process could deadlock before exec is called.

Note

If you need to modify the environment for the child use the *env* parameter rather than doing it in a *preexec\_fn*. The *start\_new\_session* and *process\_group* parameters should take the place of code using *preexec\_fn* to call [`os.setsid()`](https://docs.python.org/3.13/library/os.html#os.setsid "os.setsid") or [`os.setpgid()`](https://docs.python.org/3.13/library/os.html#os.setpgid "os.setpgid") in the child.

Changed in version 3.8: The *preexec\_fn* parameter is no longer supported in subinterpreters. The use of the parameter in a subinterpreter raises [`RuntimeError`](https://docs.python.org/3.13/builtins/exceptions.html#RuntimeError "RuntimeError"). The new restriction may affect applications that are deployed in mod\_wsgi, uWSGI, and other embedded environments.

If *close\_fds* is true, all file descriptors except `0`, `1` and `2` will be closed before the child process is executed. Otherwise when *close\_fds* is false, file descriptors obey their inheritable flag as described in [Inheritance of File Descriptors](https://docs.python.org/3.13/library/os.html#fd-inheritance).

On Windows, if *close\_fds* is true then no handles will be inherited by the child process unless explicitly passed in the `handle_list` element of [`STARTUPINFO.lpAttributeList`](#subprocess.STARTUPINFO.lpAttributeList "subprocess.STARTUPINFO.lpAttributeList"), or by standard handle redirection.

Changed in version 3.2: The default for *close\_fds* was changed from [`False`](https://docs.python.org/3.13/builtins/constants.html#False "False") to what is described above.

Changed in version 3.7: On Windows the default for *close\_fds* was changed from [`False`](https://docs.python.org/3.13/builtins/constants.html#False "False") to [`True`](https://docs.python.org/3.13/builtins/constants.html#True "True") when redirecting the standard handles. It’s now possible to set *close\_fds* to `True` when redirecting the standard handles.

*pass\_fds* is an optional sequence of file descriptors to keep open between the parent and child. Providing any *pass\_fds* forces *close\_fds* to be [`True`](https://docs.python.org/3.13/builtins/constants.html#True "True"). (POSIX only)

Changed in version 3.2: The *pass\_fds* parameter was added.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
