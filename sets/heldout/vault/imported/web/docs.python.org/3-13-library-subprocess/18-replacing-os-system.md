---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#18-replacing-os-system.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-18-replacing-os-system
type: reference
title: subprocess — Subprocess management › Replacing Older Functions with the `subprocess` Module › Replacing `os.system()`
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#18-replacing-os-system
source_hash: 4cff75e3297e47f1e80bd8c67503411a6449c96fe8c84c4b756f9da5edb4f543
---
```
sts = os.system("mycmd" + " myarg")
# becomes
retcode = call("mycmd" + " myarg", shell=True)
```

Notes:

- Calling the program through the shell is usually not required.
- The [`call()`](#subprocess.call "subprocess.call") return value is encoded differently to that of [`os.system()`](https://docs.python.org/3.13/library/os.html#os.system "os.system").
- The [`os.system()`](https://docs.python.org/3.13/library/os.html#os.system "os.system") function ignores SIGINT and SIGQUIT signals while the command is running, but the caller must do this separately when using the `subprocess` module.

A more realistic example would look like this:

```
try:
    retcode = call("mycmd" + " myarg", shell=True)
    if retcode < 0:
        print("Child was terminated by signal", -retcode, file=sys.stderr)
    else:
        print("Child returned", retcode, file=sys.stderr)
except OSError as e:
    print("Execution failed:", e, file=sys.stderr)
```

### Replacing the `os.spawn` family

P\_NOWAIT example:

```
pid = os.spawnlp(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg")
==>
pid = Popen(["/bin/mycmd", "myarg"]).pid
```

P\_WAIT example:

```
retcode = os.spawnlp(os.P_WAIT, "/bin/mycmd", "mycmd", "myarg")
==>
retcode = call(["/bin/mycmd", "myarg"])
```

Vector example:

```
os.spawnvp(os.P_NOWAIT, path, args)
==>
Popen([path] + args[1:])
```

Environment example:

```
os.spawnlpe(os.P_NOWAIT, "/bin/mycmd", "mycmd", "myarg", env)
==>
Popen(["/bin/mycmd", "myarg"], env={"PATH": "/usr/bin"})
```

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
