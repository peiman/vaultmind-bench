---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#20-replacing-functions-from-the-popen2-module.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-20-replacing-functions-from-the-popen2-module
type: reference
title: subprocess — Subprocess management › Replacing Older Functions with the `subprocess` Module › Replacing functions from the `popen2` module
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#20-replacing-functions-from-the-popen2-module
source_hash: 84f77a1c429c9de5ac80bb1240a705886831a92465b5f7f3384d8af413387940
---
Note

If the cmd argument to popen2 functions is a string, the command is executed through /bin/sh. If it is a list, the command is directly executed.

```
(child_stdout, child_stdin) = popen2.popen2("somestring", bufsize, mode)
==>
p = Popen("somestring", shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, close_fds=True)
(child_stdout, child_stdin) = (p.stdout, p.stdin)
```

```
(child_stdout, child_stdin) = popen2.popen2(["mycmd", "myarg"], bufsize, mode)
==>
p = Popen(["mycmd", "myarg"], bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, close_fds=True)
(child_stdout, child_stdin) = (p.stdout, p.stdin)
```

`popen2.Popen3` and `popen2.Popen4` basically work as [`subprocess.Popen`](#subprocess.Popen "subprocess.Popen"), except that:

- [`Popen`](#subprocess.Popen "subprocess.Popen") raises an exception if the execution fails.
- The *capturestderr* argument is replaced with the *stderr* argument.
- `stdin=PIPE` and `stdout=PIPE` must be specified.
- popen2 closes all file descriptors by default, but you have to specify `close_fds=True` with [`Popen`](#subprocess.Popen "subprocess.Popen") to guarantee this behavior on all platforms or past Python versions.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
