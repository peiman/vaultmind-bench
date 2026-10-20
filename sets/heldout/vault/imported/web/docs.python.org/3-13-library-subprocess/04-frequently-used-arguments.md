---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#04-frequently-used-arguments.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-04-frequently-used-arguments
type: reference
title: subprocess — Subprocess management › Using the `subprocess` Module › Frequently Used Arguments
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#04-frequently-used-arguments
source_hash: 1f3a8252581b8d2f69ac1c347bc3819feea1afc8a3d93c26b10950edf73683e8
---
To support a wide variety of use cases, the [`Popen`](#subprocess.Popen "subprocess.Popen") constructor (and the convenience functions) accept a large number of optional arguments. For most typical use cases, many of these arguments can be safely left at their default values. The arguments that are most commonly needed are:

> *args* is required for all calls and should be a string, or a sequence of program arguments. Providing a sequence of arguments is generally preferred, as it allows the module to take care of any required escaping and quoting of arguments (e.g. to permit spaces in file names). If passing a single string, either *shell* must be [`True`](https://docs.python.org/3.13/builtins/constants.html#True "True") (see below) or else the string must simply name the program to be executed without specifying any arguments.
> 
> *stdin*, *stdout* and *stderr* specify the executed program’s standard input, standard output and standard error file handles, respectively. Valid values are `None`, [`PIPE`](#subprocess.PIPE "subprocess.PIPE"), [`DEVNULL`](#subprocess.DEVNULL "subprocess.DEVNULL"), an existing file descriptor (a positive integer), and an existing [file object](https://docs.python.org/3.13/glossary.html#term-file-object) with a valid file descriptor. With the default settings of `None`, no redirection will occur. `PIPE` indicates that a new pipe to the child should be created. `DEVNULL` indicates that the special file [`os.devnull`](https://docs.python.org/3.13/library/os.html#os.devnull "os.devnull") will be used. Additionally, *stderr* can be [`STDOUT`](#subprocess.STDOUT "subprocess.STDOUT"), which indicates that the stderr data from the child process should be captured into the same file handle as for *stdout*.
> 
> If *encoding* or *errors* are specified, or *text* (also known as *universal\_newlines*) is true, the file objects *stdin*, *stdout* and *stderr* will be opened in text mode using the *encoding* and *errors* specified in the call or the defaults for [`io.TextIOWrapper`](https://docs.python.org/3.13/library/io.html#io.TextIOWrapper "io.TextIOWrapper").
> 
> For *stdin*, line ending characters `'\n'` in the input will be converted to the default line separator [`os.linesep`](https://docs.python.org/3.13/library/os.html#os.linesep "os.linesep"). For *stdout* and *stderr*, all line endings in the output will be converted to `'\n'`. For more information see the documentation of the [`io.TextIOWrapper`](https://docs.python.org/3.13/library/io.html#io.TextIOWrapper "io.TextIOWrapper") class when the *newline* argument to its constructor is `None`.
> 
> If text mode is not used, *stdin*, *stdout* and *stderr* will be opened as binary streams. No encoding or line ending conversion is performed.
> 
> Changed in version 3.6: Added the *encoding* and *errors* parameters.
> 
> Changed in version 3.7: Added the *text* parameter as an alias for *universal\_newlines*.
> 
> Note
> 
> The newlines attribute of the file objects [`Popen.stdin`](#subprocess.Popen.stdin "subprocess.Popen.stdin"), [`Popen.stdout`](#subprocess.Popen.stdout "subprocess.Popen.stdout") and [`Popen.stderr`](#subprocess.Popen.stderr "subprocess.Popen.stderr") are not updated by the [`Popen.communicate()`](#subprocess.Popen.communicate "subprocess.Popen.communicate") method.
> 
> If *shell* is `True`, the specified command will be executed through the shell. This can be useful if you are using Python primarily for the enhanced control flow it offers over most system shells and still want convenient access to other shell features such as shell pipes, filename wildcards, environment variable expansion, and expansion of `~` to a user’s home directory. However, note that Python itself offers implementations of many shell-like features (in particular, [`glob`](https://docs.python.org/3.13/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion."), [`fnmatch`](https://docs.python.org/3.13/library/fnmatch.html#module-fnmatch "fnmatch: Unix shell style filename pattern matching."), [`os.walk()`](https://docs.python.org/3.13/library/os.html#os.walk "os.walk"), [`os.path.expandvars()`](https://docs.python.org/3.13/library/os.path.html#os.path.expandvars "os.path.expandvars"), [`os.path.expanduser()`](https://docs.python.org/3.13/library/os.path.html#os.path.expanduser "os.path.expanduser"), and [`shutil`](https://docs.python.org/3.13/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.")).
> 
> Changed in version 3.3: When *universal\_newlines* is `True`, the class uses the encoding [`locale.getpreferredencoding(False)`](https://docs.python.org/3.13/library/locale.html#locale.getpreferredencoding "locale.getpreferredencoding") instead of `locale.getpreferredencoding()`. See the [`io.TextIOWrapper`](https://docs.python.org/3.13/library/io.html#io.TextIOWrapper "io.TextIOWrapper") class for more information on this change.
> 
> Note
> 
> Read the [Security Considerations](#security-considerations) section before using `shell=True`.

These options, along with all of the other options, are described in more detail in the [`Popen`](#subprocess.Popen "subprocess.Popen") constructor documentation.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
