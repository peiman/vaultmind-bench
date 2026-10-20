---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#22-timeout-behavior.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-22-timeout-behavior
type: reference
title: subprocess — Subprocess management › Notes › Timeout Behavior
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#22-timeout-behavior
source_hash: c576be867faa8cc42961e6fa770385392e0ea82f531499730c401cf583319a41
---
When using the `timeout` parameter in functions like [`run()`](#subprocess.run "subprocess.run"), [`Popen.wait()`](#subprocess.Popen.wait "subprocess.Popen.wait"), or [`Popen.communicate()`](#subprocess.Popen.communicate "subprocess.Popen.communicate"), users should be aware of the following behaviors:

1. **Process Creation Delay**: The initial process creation itself cannot be interrupted on many platform APIs. This means that even when specifying a timeout, you are not guaranteed to see a timeout exception until at least after however long process creation takes.
2. **Extremely Small Timeout Values**: Setting very small timeout values (such as a few milliseconds) may result in almost immediate [`TimeoutExpired`](#subprocess.TimeoutExpired "subprocess.TimeoutExpired") exceptions because process creation and system scheduling inherently require time.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
