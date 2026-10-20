---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#05-popen-constructor.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-05-popen-constructor
type: reference
title: subprocess — Subprocess management › Using the `subprocess` Module › Popen Constructor (1/4)
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#05-popen-constructor
source_hash: 230e9f6e37f706058019715859a1fdfcce8249cc63be3900185c2659fd5d68da
---
The underlying process creation and management in this module is handled by the [`Popen`](#subprocess.Popen "subprocess.Popen") class. It offers a lot of flexibility so that developers are able to handle the less common cases not covered by the convenience functions.

*class* subprocess.Popen(*args*, *bufsize=-1*, *executable=None*, *stdin=None*, *stdout=None*, *stderr=None*, *preexec\_fn=None*, *close\_fds=True*, *shell=False*, *cwd=None*, *env=None*, *universal\_newlines=None*, *startupinfo=None*, *creationflags=0*, *restore\_signals=True*, *start\_new\_session=False*, *pass\_fds=()*, *\**, *group=None*, *extra\_groups=None*, *user=None*, *umask=-1*, *encoding=None*, *errors=None*, *text=None*, *pipesize=-1*, *process\_group=None*)[¶](#subprocess.Popen "Link to this definition")

Execute a child program in a new process. On POSIX, the class uses [`os.execvpe()`](https://docs.python.org/3.13/library/os.html#os.execvpe "os.execvpe")-like behavior to execute the child program. On Windows, the class uses the Windows `CreateProcess()` function. The arguments to `Popen` are as follows.

*args* should be a sequence of program arguments or else a single string or [path-like object](https://docs.python.org/3.13/glossary.html#term-path-like-object). By default, the program to execute is the first item in *args* if *args* is a sequence. If *args* is a string, the interpretation is platform-dependent and described below. See the *shell* and *executable* arguments for additional differences from the default behavior. Unless otherwise stated, it is recommended to pass *args* as a sequence.

Warning

For maximum reliability, use a fully qualified path for the executable. To search for an unqualified name on `PATH`, use [`shutil.which()`](https://docs.python.org/3.13/library/shutil.html#shutil.which "shutil.which"). On all platforms, passing [`sys.executable`](https://docs.python.org/3.13/library/sys.html#sys.executable "sys.executable") is the recommended way to launch the current Python interpreter again, and use the `-m` command-line format to launch an installed module.

Resolving the path of *executable* (or the first item of *args*) is platform dependent. For POSIX, see [`os.execvpe()`](https://docs.python.org/3.13/library/os.html#os.execvpe "os.execvpe"), and note that when resolving or searching for the executable path, *cwd* overrides the current working directory and *env* can override the `PATH` environment variable. For Windows, see the documentation of the `lpApplicationName` and `lpCommandLine` parameters of WinAPI `CreateProcess`, and note that when resolving or searching for the executable path with `shell=False`, *cwd* does not override the current working directory and *env* cannot override the `PATH` environment variable. Using a full path avoids all of these variations.

An example of passing some arguments to an external program as a sequence is:

```
Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])
```

On POSIX, if *args* is a string, the string is interpreted as the name or path of the program to execute. However, this can only be done if not passing arguments to the program.

Note

It may not be obvious how to break a shell command into a sequence of arguments, especially in complex cases. [`shlex.split()`](https://docs.python.org/3.13/library/shlex.html#shlex.split "shlex.split") can illustrate how to determine the correct tokenization for *args*:

```
>>> import shlex, subprocess
>>> command_line = input()
/bin/vikings -input eggs.txt -output "spam spam.txt" -cmd "echo '$MONEY'"
>>> args = shlex.split(command_line)
>>> print(args)
['/bin/vikings', '-input', 'eggs.txt', '-output', 'spam spam.txt', '-cmd', "echo '$MONEY'"]
>>> p = subprocess.Popen(args) # Success!
```

Note in particular that options (such as *-input*) and arguments (such as *eggs.txt*) that are separated by whitespace in the shell go in separate list elements, while arguments that need quoting or backslash escaping when used in the shell (such as filenames containing spaces or the *echo* command shown above) are single list elements.

On Windows, if *args* is a sequence, it will be converted to a string in a manner described in [Converting an argument sequence to a string on Windows](#converting-argument-sequence). This is because the underlying `CreateProcess()` operates on strings.

Changed in version 3.6: *args* parameter accepts a [path-like object](https://docs.python.org/3.13/glossary.html#term-path-like-object) if *shell* is `False` and a sequence containing path-like objects on POSIX.

Changed in version 3.8: *args* parameter accepts a [path-like object](https://docs.python.org/3.13/glossary.html#term-path-like-object) if *shell* is `False` and a sequence containing bytes and path-like objects on Windows.

The *shell* argument (which defaults to `False`) specifies whether to use the shell as the program to execute. If *shell* is `True`, it is recommended to pass *args* as a string rather than as a sequence.

On POSIX with `shell=True`, the shell defaults to `/bin/sh`. If *args* is a string, the string specifies the command to execute through the shell. This means that the string must be formatted exactly as it would be when typed at the shell prompt. This includes, for example, quoting or backslash escaping filenames with spaces in them. If *args* is a sequence, the first item specifies the command string, and any additional items will be treated as additional arguments to the shell itself. That is to say, `Popen` does the equivalent of:

```
Popen(['/bin/sh', '-c', args[0], args[1], ...])
```

On Windows with `shell=True`, the `COMSPEC` environment variable specifies the default shell. The only time you need to specify `shell=True` on Windows is when the command you wish to execute is built into the shell (e.g. **dir** or **copy**). You do not need `shell=True` to run a batch file or console-based executable.

Note

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
