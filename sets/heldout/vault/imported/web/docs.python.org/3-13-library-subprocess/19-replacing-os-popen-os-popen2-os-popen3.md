---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#19-replacing-os-popen-os-popen2-os-popen3.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-19-replacing-os-popen-os-popen2-os-popen3
type: reference
title: subprocess — Subprocess management › Replacing Older Functions with the `subprocess` Module › Replacing `os.popen()`, `os.popen2()`, `os.popen3()`
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#19-replacing-os-popen-os-popen2-os-popen3
source_hash: 7eef0c48bd1e8bc1fdee705a8f20d3780efe8d0e32339b158de1834d4991de70
---
```
(child_stdin, child_stdout) = os.popen2(cmd, mode, bufsize)
==>
p = Popen(cmd, shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, close_fds=True)
(child_stdin, child_stdout) = (p.stdin, p.stdout)
```

```
(child_stdin,
 child_stdout,
 child_stderr) = os.popen3(cmd, mode, bufsize)
==>
p = Popen(cmd, shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
(child_stdin,
 child_stdout,
 child_stderr) = (p.stdin, p.stdout, p.stderr)
```

```
(child_stdin, child_stdout_and_stderr) = os.popen4(cmd, mode, bufsize)
==>
p = Popen(cmd, shell=True, bufsize=bufsize,
          stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
(child_stdin, child_stdout_and_stderr) = (p.stdin, p.stdout)
```

Return code handling translates as follows:

```
pipe = os.popen(cmd, 'w')
...
rc = pipe.close()
if rc is not None and rc >> 8:
    print("There were some errors")
==>
process = Popen(cmd, stdin=PIPE)
...
process.stdin.close()
if process.wait() != 0:
    print("There were some errors")
```

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
