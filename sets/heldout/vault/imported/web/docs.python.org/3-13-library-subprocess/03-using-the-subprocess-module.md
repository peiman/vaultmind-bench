---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#03-using-the-subprocess-module.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-03-using-the-subprocess-module
type: reference
title: subprocess — Subprocess management › Using the `subprocess` Module (2/2)
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#03-using-the-subprocess-module
source_hash: cf8a0a11dd777d77ffc7f5bf782719daa18623faabb8a7b69c948bca7334a83a
---
Captured stdout from the child process. A bytes sequence, or a string if [`run()`](#subprocess.run "subprocess.run") was called with an encoding, errors, or text=True. `None` if stdout was not captured.

If you ran the process with `stderr=subprocess.STDOUT`, stdout and stderr will be combined in this attribute, and [`stderr`](#subprocess.CompletedProcess.stderr "subprocess.CompletedProcess.stderr") will be `None`.

stderr[¶](#subprocess.CompletedProcess.stderr "Link to this definition")

Captured stderr from the child process. A bytes sequence, or a string if [`run()`](#subprocess.run "subprocess.run") was called with an encoding, errors, or text=True. `None` if stderr was not captured.

check\_returncode()[¶](#subprocess.CompletedProcess.check_returncode "Link to this definition")

If [`returncode`](#subprocess.CompletedProcess.returncode "subprocess.CompletedProcess.returncode") is non-zero, raise a [`CalledProcessError`](#subprocess.CalledProcessError "subprocess.CalledProcessError").

Added in version 3.5.

subprocess.DEVNULL[¶](#subprocess.DEVNULL "Link to this definition")

Special value that can be used as the *stdin*, *stdout* or *stderr* argument to [`Popen`](#subprocess.Popen "subprocess.Popen") and indicates that the special file [`os.devnull`](https://docs.python.org/3.13/library/os.html#os.devnull "os.devnull") will be used.

Added in version 3.3.

subprocess.PIPE[¶](#subprocess.PIPE "Link to this definition")

Special value that can be used as the *stdin*, *stdout* or *stderr* argument to [`Popen`](#subprocess.Popen "subprocess.Popen") and indicates that a pipe to the standard stream should be opened. Most useful with [`Popen.communicate()`](#subprocess.Popen.communicate "subprocess.Popen.communicate").

subprocess.STDOUT[¶](#subprocess.STDOUT "Link to this definition")

Special value that can be used as the *stderr* argument to [`Popen`](#subprocess.Popen "subprocess.Popen") and indicates that standard error should go into the same handle as standard output.

*exception* subprocess.SubprocessError[¶](#subprocess.SubprocessError "Link to this definition")

Base class for all other exceptions from this module.

Added in version 3.3.

*exception* subprocess.TimeoutExpired[¶](#subprocess.TimeoutExpired "Link to this definition")

Subclass of [`SubprocessError`](#subprocess.SubprocessError "subprocess.SubprocessError"), raised when a timeout expires while waiting for a child process.

cmd[¶](#subprocess.TimeoutExpired.cmd "Link to this definition")

Command that was used to spawn the child process.

timeout[¶](#subprocess.TimeoutExpired.timeout "Link to this definition")

Timeout in seconds.

output[¶](#subprocess.TimeoutExpired.output "Link to this definition")

Output of the child process if it was captured by [`run()`](#subprocess.run "subprocess.run") or [`check_output()`](#subprocess.check_output "subprocess.check_output"). Otherwise, `None`. This is always [`bytes`](https://docs.python.org/3.13/builtins/stdtypes.html#bytes "bytes") when any output was captured regardless of the `text=True` setting. It may remain `None` instead of `b''` when no output was observed.

stdout[¶](#subprocess.TimeoutExpired.stdout "Link to this definition")

Alias for output, for symmetry with [`stderr`](#subprocess.TimeoutExpired.stderr "subprocess.TimeoutExpired.stderr").

stderr[¶](#subprocess.TimeoutExpired.stderr "Link to this definition")

Stderr output of the child process if it was captured by [`run()`](#subprocess.run "subprocess.run"). Otherwise, `None`. This is always [`bytes`](https://docs.python.org/3.13/builtins/stdtypes.html#bytes "bytes") when stderr output was captured regardless of the `text=True` setting. It may remain `None` instead of `b''` when no stderr output was observed.

Added in version 3.3.

Changed in version 3.5: *stdout* and *stderr* attributes added

*exception* subprocess.CalledProcessError[¶](#subprocess.CalledProcessError "Link to this definition")

Subclass of [`SubprocessError`](#subprocess.SubprocessError "subprocess.SubprocessError"), raised when a process run by [`check_call()`](#subprocess.check_call "subprocess.check_call"), [`check_output()`](#subprocess.check_output "subprocess.check_output"), or [`run()`](#subprocess.run "subprocess.run") (with `check=True`) returns a non-zero exit status.

returncode[¶](#subprocess.CalledProcessError.returncode "Link to this definition")

Exit status of the child process, an integer. If the process exited due to a signal, this will be the negative signal number.

cmd[¶](#subprocess.CalledProcessError.cmd "Link to this definition")

Command that was used to spawn the child process.

output[¶](#subprocess.CalledProcessError.output "Link to this definition")

Output of the child process if it was captured by [`run()`](#subprocess.run "subprocess.run") or [`check_output()`](#subprocess.check_output "subprocess.check_output"). Otherwise, `None`.

stdout[¶](#subprocess.CalledProcessError.stdout "Link to this definition")

Alias for output, for symmetry with [`stderr`](#subprocess.CalledProcessError.stderr "subprocess.CalledProcessError.stderr").

stderr[¶](#subprocess.CalledProcessError.stderr "Link to this definition")

Stderr output of the child process if it was captured by [`run()`](#subprocess.run "subprocess.run"). Otherwise, `None`.

Changed in version 3.5: *stdout* and *stderr* attributes added

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
