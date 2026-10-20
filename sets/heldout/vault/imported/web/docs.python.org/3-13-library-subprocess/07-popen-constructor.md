---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#07-popen-constructor.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-07-popen-constructor
type: reference
title: subprocess — Subprocess management › Using the `subprocess` Module › Popen Constructor (3/4)
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#07-popen-constructor
source_hash: 6792bbb5ab3953d88fb49ea413f2de7b390603f3680b2f5ae5fe4f655c8f06ef
---
If *cwd* is not `None`, the function changes the working directory to *cwd* before executing the child. *cwd* can be a string, bytes or [path-like](https://docs.python.org/3.13/glossary.html#term-path-like-object) object. On POSIX, the function looks for *executable* (or for the first item in *args*) relative to *cwd* if the executable path is a relative path.

Changed in version 3.6: *cwd* parameter accepts a [path-like object](https://docs.python.org/3.13/glossary.html#term-path-like-object) on POSIX.

Changed in version 3.7: *cwd* parameter accepts a [path-like object](https://docs.python.org/3.13/glossary.html#term-path-like-object) on Windows.

Changed in version 3.8: *cwd* parameter accepts a bytes object on Windows.

If *restore\_signals* is true (the default) all signals that Python has set to SIG\_IGN are restored to SIG\_DFL in the child process before the exec. Currently this includes the SIGPIPE, SIGXFZ and SIGXFSZ signals. (POSIX only)

Changed in version 3.2: *restore\_signals* was added.

If *start\_new\_session* is true the `setsid()` system call will be made in the child process prior to the execution of the subprocess.

Changed in version 3.2: *start\_new\_session* was added.

If *process\_group* is a non-negative integer, the `setpgid(0, value)` system call will be made in the child process prior to the execution of the subprocess.

Changed in version 3.11: *process\_group* was added.

If *group* is not `None`, the setregid() system call will be made in the child process prior to the execution of the subprocess. If the provided value is a string, it will be looked up via [`grp.getgrnam()`](https://docs.python.org/3.13/library/grp.html#grp.getgrnam "grp.getgrnam") and the value in `gr_gid` will be used. If the value is an integer, it will be passed verbatim. (POSIX only)

Added in version 3.9.

If *extra\_groups* is not `None`, the setgroups() system call will be made in the child process prior to the execution of the subprocess. Strings provided in *extra\_groups* will be looked up via [`grp.getgrnam()`](https://docs.python.org/3.13/library/grp.html#grp.getgrnam "grp.getgrnam") and the values in `gr_gid` will be used. Integer values will be passed verbatim. (POSIX only)

Added in version 3.9.

If *user* is not `None`, the setreuid() system call will be made in the child process prior to the execution of the subprocess. If the provided value is a string, it will be looked up via [`pwd.getpwnam()`](https://docs.python.org/3.13/library/pwd.html#pwd.getpwnam "pwd.getpwnam") and the value in `pw_uid` will be used. If the value is an integer, it will be passed verbatim. (POSIX only)

Note

Specifying *user* will not drop existing supplementary group memberships! The caller must also pass `extra_groups=()` to reduce the group membership of the child process for security purposes.

Added in version 3.9.

If *umask* is not negative, the umask() system call will be made in the child process prior to the execution of the subprocess.

Added in version 3.9.

If *env* is not `None`, it must be a mapping that defines the environment variables for the new process; these are used instead of the default behavior of inheriting the current process’ environment. This mapping can be str to str on any platform or bytes to bytes on POSIX platforms much like [`os.environ`](https://docs.python.org/3.13/library/os.html#os.environ "os.environ") or [`os.environb`](https://docs.python.org/3.13/library/os.html#os.environb "os.environb").

Note

If specified, *env* must provide any variables required for the program to execute. On Windows, in order to run a [side-by-side assembly](https://en.wikipedia.org/wiki/Side-by-Side_Assembly) the specified *env* **must** include a valid `%SystemRoot%`.

If *encoding* or *errors* are specified, or *text* is true, the file objects *stdin*, *stdout* and *stderr* are opened in text mode with the specified *encoding* and *errors*, as described above in [Frequently Used Arguments](#frequently-used-arguments). The *universal\_newlines* argument is equivalent to *text* and is provided for backwards compatibility. By default, file objects are opened in binary mode.

Added in version 3.6: *encoding* and *errors* were added.

Added in version 3.7: *text* was added as a more readable alias for *universal\_newlines*.

If given, *startupinfo* will be a [`STARTUPINFO`](#subprocess.STARTUPINFO "subprocess.STARTUPINFO") object, which is passed to the underlying `CreateProcess` function.

If given, *creationflags*, can be one or more of the following flags:

- [`CREATE_NEW_CONSOLE`](#subprocess.CREATE_NEW_CONSOLE "subprocess.CREATE_NEW_CONSOLE")
- [`CREATE_NEW_PROCESS_GROUP`](#subprocess.CREATE_NEW_PROCESS_GROUP "subprocess.CREATE_NEW_PROCESS_GROUP")
- [`ABOVE_NORMAL_PRIORITY_CLASS`](#subprocess.ABOVE_NORMAL_PRIORITY_CLASS "subprocess.ABOVE_NORMAL_PRIORITY_CLASS")
- [`BELOW_NORMAL_PRIORITY_CLASS`](#subprocess.BELOW_NORMAL_PRIORITY_CLASS "subprocess.BELOW_NORMAL_PRIORITY_CLASS")
- [`HIGH_PRIORITY_CLASS`](#subprocess.HIGH_PRIORITY_CLASS "subprocess.HIGH_PRIORITY_CLASS")
- [`IDLE_PRIORITY_CLASS`](#subprocess.IDLE_PRIORITY_CLASS "subprocess.IDLE_PRIORITY_CLASS")
- [`NORMAL_PRIORITY_CLASS`](#subprocess.NORMAL_PRIORITY_CLASS "subprocess.NORMAL_PRIORITY_CLASS")
- [`REALTIME_PRIORITY_CLASS`](#subprocess.REALTIME_PRIORITY_CLASS "subprocess.REALTIME_PRIORITY_CLASS")
- [`CREATE_NO_WINDOW`](#subprocess.CREATE_NO_WINDOW "subprocess.CREATE_NO_WINDOW")
- [`DETACHED_PROCESS`](#subprocess.DETACHED_PROCESS "subprocess.DETACHED_PROCESS")
- [`CREATE_DEFAULT_ERROR_MODE`](#subprocess.CREATE_DEFAULT_ERROR_MODE "subprocess.CREATE_DEFAULT_ERROR_MODE")
- [`CREATE_BREAKAWAY_FROM_JOB`](#subprocess.CREATE_BREAKAWAY_FROM_JOB "subprocess.CREATE_BREAKAWAY_FROM_JOB")

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
