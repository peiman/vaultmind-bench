---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#16-older-high-level-api.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-16-older-high-level-api
type: reference
title: subprocess — Subprocess management › Older high-level API
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#16-older-high-level-api
source_hash: fc722ece1bfb886fba19ed7b4b1f29e809a1b62a2123e77f4ad9af8dc7efd6e0
---
Prior to Python 3.5, these three functions comprised the high level API to subprocess. You can now use [`run()`](#subprocess.run "subprocess.run") in many cases, but lots of existing code calls these functions.

subprocess.call(*args*, *\**, *stdin=None*, *stdout=None*, *stderr=None*, *shell=False*, *cwd=None*, *timeout=None*, *\*\*other\_popen\_kwargs*)[¶](#subprocess.call "Link to this definition")

Run the command described by *args*. Wait for command to complete, then return the [`returncode`](#subprocess.Popen.returncode "subprocess.Popen.returncode") attribute.

Code needing to capture stdout or stderr should use [`run()`](#subprocess.run "subprocess.run") instead:

```
run(...).returncode
```

To suppress stdout or stderr, supply a value of [`DEVNULL`](#subprocess.DEVNULL "subprocess.DEVNULL").

The arguments shown above are merely some common ones. The full function signature is the same as that of the [`Popen`](#subprocess.Popen "subprocess.Popen") constructor - this function passes all supplied arguments other than *timeout* directly through to that interface.

Note

Do not use `stdout=PIPE` or `stderr=PIPE` with this function. The child process will block if it generates enough output to a pipe to fill up the OS pipe buffer as the pipes are not being read from.

Changed in version 3.3: *timeout* was added.

Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.

subprocess.check\_call(*args*, *\**, *stdin=None*, *stdout=None*, *stderr=None*, *shell=False*, *cwd=None*, *timeout=None*, *\*\*other\_popen\_kwargs*)[¶](#subprocess.check_call "Link to this definition")

Run command with arguments. Wait for command to complete. If the return code was zero then return, otherwise raise [`CalledProcessError`](#subprocess.CalledProcessError "subprocess.CalledProcessError"). The `CalledProcessError` object will have the return code in the [`returncode`](#subprocess.CalledProcessError.returncode "subprocess.CalledProcessError.returncode") attribute. If `check_call()` was unable to start the process it will propagate the exception that was raised.

Code needing to capture stdout or stderr should use [`run()`](#subprocess.run "subprocess.run") instead:

```
run(..., check=True)
```

To suppress stdout or stderr, supply a value of [`DEVNULL`](#subprocess.DEVNULL "subprocess.DEVNULL").

The arguments shown above are merely some common ones. The full function signature is the same as that of the [`Popen`](#subprocess.Popen "subprocess.Popen") constructor - this function passes all supplied arguments other than *timeout* directly through to that interface.

Note

Do not use `stdout=PIPE` or `stderr=PIPE` with this function. The child process will block if it generates enough output to a pipe to fill up the OS pipe buffer as the pipes are not being read from.

Changed in version 3.3: *timeout* was added.

Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.

subprocess.check\_output(*args*, *\**, *stdin=None*, *stderr=None*, *shell=False*, *cwd=None*, *encoding=None*, *errors=None*, *universal\_newlines=None*, *timeout=None*, *text=None*, *\*\*other\_popen\_kwargs*)[¶](#subprocess.check_output "Link to this definition")

Run command with arguments and return its output.

If the return code was non-zero it raises a [`CalledProcessError`](#subprocess.CalledProcessError "subprocess.CalledProcessError"). The `CalledProcessError` object will have the return code in the [`returncode`](#subprocess.CalledProcessError.returncode "subprocess.CalledProcessError.returncode") attribute and any output in the [`output`](#subprocess.CalledProcessError.output "subprocess.CalledProcessError.output") attribute.

This is equivalent to:

```
run(..., check=True, stdout=PIPE).stdout
```

The arguments shown above are merely some common ones. The full function signature is largely the same as that of [`run()`](#subprocess.run "subprocess.run") - most arguments are passed directly through to that interface. One API deviation from `run()` behavior exists: passing `input=None` will behave the same as `input=b''` (or `input=''`, depending on other arguments) rather than using the parent’s standard input file handle.

By default, this function will return the data as encoded bytes. The actual encoding of the output data may depend on the command being invoked, so the decoding to text will often need to be handled at the application level.

This behaviour may be overridden by setting *text*, *encoding*, *errors*, or *universal\_newlines* to `True` as described in [Frequently Used Arguments](#frequently-used-arguments) and [`run()`](#subprocess.run "subprocess.run").

To also capture standard error in the result, use `stderr=subprocess.STDOUT`:

```
>>> subprocess.check_output(
...     "ls non_existent_file; exit 0",
...     stderr=subprocess.STDOUT,
...     shell=True)
'ls: non_existent_file: No such file or directory\n'
```

Added in version 3.1.

Changed in version 3.3: *timeout* was added.

Changed in version 3.4: Support for the *input* keyword argument was added.

Changed in version 3.6: *encoding* and *errors* were added. See [`run()`](#subprocess.run "subprocess.run") for details.

Added in version 3.7: *text* was added as a more readable alias for *universal\_newlines*.

Changed in version 3.12: Changed Windows shell search order for `shell=True`. The current directory and `%PATH%` are replaced with `%COMSPEC%` and `%SystemRoot%\System32\cmd.exe`. As a result, dropping a malicious program named `cmd.exe` into a current directory no longer works.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
