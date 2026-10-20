---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#11-popen-objects.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-11-popen-objects
type: reference
title: subprocess — Subprocess management › Popen Objects (1/2)
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#11-popen-objects
source_hash: 9f2dec427636009d44bcfdbdd979ec9d898ca73b41733ec31b4da675b9469a6e
---
Instances of the [`Popen`](#subprocess.Popen "subprocess.Popen") class have the following methods:

Popen.poll()[¶](#subprocess.Popen.poll "Link to this definition")

Check if child process has terminated. Set and return [`returncode`](#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute. Otherwise, returns `None`.

Popen.wait(*timeout=None*)[¶](#subprocess.Popen.wait "Link to this definition")

Wait for child process to terminate. Set and return [`returncode`](#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute.

If the process does not terminate after *timeout* seconds, raise a [`TimeoutExpired`](#subprocess.TimeoutExpired "subprocess.TimeoutExpired") exception. It is safe to catch this exception and retry the wait.

Note

This will deadlock when using `stdout=PIPE` or `stderr=PIPE` and the child process generates enough output to a pipe such that it blocks waiting for the OS pipe buffer to accept more data. Use [`Popen.communicate()`](#subprocess.Popen.communicate "subprocess.Popen.communicate") when using pipes to avoid that.

Note

When the `timeout` parameter is not `None`, then (on POSIX) the function is implemented using a busy loop (non-blocking call and short sleeps). Use the [`asyncio`](https://docs.python.org/3.13/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") module for an asynchronous wait: see [`asyncio.create_subprocess_exec`](https://docs.python.org/3.13/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec").

Changed in version 3.3: *timeout* was added.

Popen.communicate(*input=None*, *timeout=None*)[¶](#subprocess.Popen.communicate "Link to this definition")

Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached. Wait for process to terminate and set the [`returncode`](#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute. The optional *input* argument should be data to be sent to the child process, or `None`, if no data should be sent to the child. If streams were opened in text mode, *input* must be a string. Otherwise, it must be bytes.

`communicate()` returns a tuple `(stdout_data, stderr_data)`. The data will be strings if streams were opened in text mode; otherwise, bytes.

Note that if you want to send data to the process’s stdin, you need to create the Popen object with `stdin=PIPE`. Similarly, to get anything other than `None` in the result tuple, you need to give `stdout=PIPE` and/or `stderr=PIPE` too.

If the process does not terminate after *timeout* seconds, a [`TimeoutExpired`](#subprocess.TimeoutExpired "subprocess.TimeoutExpired") exception will be raised. Catching this exception and retrying communication will not lose any output. Supplying *input* to a subsequent post-timeout `communicate()` call is in undefined behavior and may become an error in the future.

The child process is not killed if the timeout expires, so in order to cleanup properly a well-behaved application should kill the child process and finish communication:

```
proc = subprocess.Popen(...)
try:
    outs, errs = proc.communicate(timeout=15)
except TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()
```

After a call to `communicate()` raises [`TimeoutExpired`](#subprocess.TimeoutExpired "subprocess.TimeoutExpired"), do not call [`wait()`](#subprocess.Popen.wait "subprocess.Popen.wait"). Use an additional `communicate()` call to finish handling pipes and populate the [`returncode`](#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute.

Note

The data read is buffered in memory, so do not use this method if the data size is large or unlimited.

Changed in version 3.3: *timeout* was added.

Popen.send\_signal(*signal*)[¶](#subprocess.Popen.send_signal "Link to this definition")

Sends the signal *signal* to the child.

Do nothing if the process completed.

Note

On Windows, SIGTERM is an alias for [`terminate()`](#subprocess.Popen.terminate "subprocess.Popen.terminate"). CTRL\_C\_EVENT and CTRL\_BREAK\_EVENT can be sent to processes started with a *creationflags* parameter which includes `CREATE_NEW_PROCESS_GROUP`.

Popen.terminate()[¶](#subprocess.Popen.terminate "Link to this definition")

Stop the child. On POSIX OSs the method sends [`SIGTERM`](https://docs.python.org/3.13/library/signal.html#signal.SIGTERM "signal.SIGTERM") to the child. On Windows the Win32 API function `TerminateProcess()` is called to stop the child.

Popen.kill()[¶](#subprocess.Popen.kill "Link to this definition")

Kills the child. On POSIX OSs the function sends SIGKILL to the child. On Windows `kill()` is an alias for [`terminate()`](#subprocess.Popen.terminate "subprocess.Popen.terminate").

The following attributes are also set by the class for you to access. Reassigning them to new values is unsupported:

Popen.args[¶](#subprocess.Popen.args "Link to this definition")

The *args* argument as it was passed to [`Popen`](#subprocess.Popen "subprocess.Popen") – a sequence of program arguments or else a single string.

Added in version 3.3.

Popen.stdin[¶](#subprocess.Popen.stdin "Link to this definition")

If the *stdin* argument was [`PIPE`](#subprocess.PIPE "subprocess.PIPE"), this attribute is a writeable stream object as returned by [`open()`](https://docs.python.org/3.13/builtins/functions.html#open "open"). If the *encoding* or *errors* arguments were specified or the *text* or *universal\_newlines* argument was `True`, the stream is a text stream, otherwise it is a byte stream. If the *stdin* argument was not `PIPE`, this attribute is `None`.

Popen.stdout[¶](#subprocess.Popen.stdout "Link to this definition")

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
