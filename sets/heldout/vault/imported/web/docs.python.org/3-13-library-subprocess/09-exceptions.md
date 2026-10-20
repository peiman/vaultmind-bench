---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#09-exceptions.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-09-exceptions
type: reference
title: subprocess — Subprocess management › Using the `subprocess` Module › Exceptions
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#09-exceptions
source_hash: 02f4b41aa50829f70c5f52b8dd1a8a4d41544981c3fea5dae4ad56080d30d1fd
---
Exceptions raised in the child process, before the new program has started to execute, will be re-raised in the parent.

The most common exception raised is [`OSError`](https://docs.python.org/3.13/builtins/exceptions.html#OSError "OSError"). This occurs, for example, when trying to execute a non-existent file. Applications should prepare for `OSError` exceptions. Note that, when `shell=True`, `OSError` will be raised by the child only if the selected shell itself was not found. To determine if the shell failed to find the requested application, it is necessary to check the return code or output from the subprocess.

A [`ValueError`](https://docs.python.org/3.13/builtins/exceptions.html#ValueError "ValueError") will be raised if [`Popen`](#subprocess.Popen "subprocess.Popen") is called with invalid arguments.

[`check_call()`](#subprocess.check_call "subprocess.check_call") and [`check_output()`](#subprocess.check_output "subprocess.check_output") will raise [`CalledProcessError`](#subprocess.CalledProcessError "subprocess.CalledProcessError") if the called process returns a non-zero return code.

All of the functions and methods that accept a *timeout* parameter, such as [`run()`](#subprocess.run "subprocess.run") and [`Popen.communicate()`](#subprocess.Popen.communicate "subprocess.Popen.communicate") will raise [`TimeoutExpired`](#subprocess.TimeoutExpired "subprocess.TimeoutExpired") if the timeout expires before the process exits.

Exceptions defined in this module all inherit from [`SubprocessError`](#subprocess.SubprocessError "subprocess.SubprocessError").

Added in version 3.3: The [`SubprocessError`](#subprocess.SubprocessError "subprocess.SubprocessError") base class was added.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
