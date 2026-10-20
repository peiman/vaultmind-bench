---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#21-legacy-shell-invocation-functions.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-21-legacy-shell-invocation-functions
type: reference
title: subprocess — Subprocess management › Legacy Shell Invocation Functions
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#21-legacy-shell-invocation-functions
source_hash: 07b6cce845b8200e8e2f7e3a7e7f39d4a5d2b7bd048ec93728aa04805960ddd0
---
This module also provides the following legacy functions from the 2.x `commands` module. These operations implicitly invoke the system shell and none of the guarantees described above regarding security and exception handling consistency are valid for these functions.

subprocess.getstatusoutput(*cmd*, *\**, *encoding=None*, *errors=None*)[¶](#subprocess.getstatusoutput "Link to this definition")

Return `(exitcode, output)` of executing *cmd* in a shell.

Execute the string *cmd* in a shell with [`check_output()`](#subprocess.check_output "subprocess.check_output") and return a 2-tuple `(exitcode, output)`. *encoding* and *errors* are used to decode output; see the notes on [Frequently Used Arguments](#frequently-used-arguments) for more details.

A trailing newline is stripped from the output. The exit code for the command can be interpreted as the return code of subprocess. Example:

```
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')
>>> subprocess.getstatusoutput('cat /bin/junk')
(1, 'cat: /bin/junk: No such file or directory')
>>> subprocess.getstatusoutput('/bin/junk')
(127, 'sh: /bin/junk: not found')
>>> subprocess.getstatusoutput('/bin/kill $$')
(-15, '')
```

Changed in version 3.3.4: Windows support was added.

The function now returns (exitcode, output) instead of (status, output) as it did in Python 3.3.3 and earlier. exitcode has the same value as [`returncode`](#subprocess.Popen.returncode "subprocess.Popen.returncode").

Changed in version 3.11: Added the *encoding* and *errors* parameters.

subprocess.getoutput(*cmd*, *\**, *encoding=None*, *errors=None*)[¶](#subprocess.getoutput "Link to this definition")

Return output (stdout and stderr) of executing *cmd* in a shell.

Like [`getstatusoutput()`](#subprocess.getstatusoutput "subprocess.getstatusoutput"), except the exit code is ignored and the return value is a string containing the command’s output. Example:

```
>>> subprocess.getoutput('ls /bin/ls')
'/bin/ls'
```

Changed in version 3.3.4: Windows support added

Changed in version 3.11: Added the *encoding* and *errors* parameters.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
