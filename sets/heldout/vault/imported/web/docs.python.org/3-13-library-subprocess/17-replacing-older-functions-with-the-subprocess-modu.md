---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#17-replacing-older-functions-with-the-subprocess-modu.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-17-replacing-older-functions-with-the-subprocess-modu
type: reference
title: subprocess — Subprocess management › Replacing Older Functions with the `subprocess` Module
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#17-replacing-older-functions-with-the-subprocess-modu
source_hash: 4e5e2a39d0529caf8e89dfe070b3b14abd1fefb11fa49e8460814a7ebce7dfe2
---
In this section, “a becomes b” means that b can be used as a replacement for a.

Note

All “a” functions in this section fail (more or less) silently if the executed program cannot be found; the “b” replacements raise [`OSError`](https://docs.python.org/3.13/builtins/exceptions.html#OSError "OSError") instead.

In addition, the replacements using [`check_output()`](#subprocess.check_output "subprocess.check_output") will fail with a [`CalledProcessError`](#subprocess.CalledProcessError "subprocess.CalledProcessError") if the requested operation produces a non-zero return code. The output is still available as the [`output`](#subprocess.CalledProcessError.output "subprocess.CalledProcessError.output") attribute of the raised exception.

In the following examples, we assume that the relevant functions have already been imported from the `subprocess` module.

### Replacing **/bin/sh** shell command substitution

```
output=$(mycmd myarg)
```

becomes:

```
output = check_output(["mycmd", "myarg"])
```

### Replacing shell pipeline

```
output=$(dmesg | grep hda)
```

becomes:

```
p1 = Popen(["dmesg"], stdout=PIPE)
p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]
```

The `p1.stdout.close()` call after starting the p2 is important in order for p1 to receive a SIGPIPE if p2 exits before p1.

Alternatively, for trusted input, the shell’s own pipeline support may still be used directly:

```
output=$(dmesg | grep hda)
```

becomes:

```
output = check_output("dmesg | grep hda", shell=True)
```

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
