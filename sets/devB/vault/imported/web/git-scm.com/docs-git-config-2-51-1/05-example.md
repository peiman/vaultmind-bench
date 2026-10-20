---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#05-example.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-05-example
type: reference
title: Git - git-config Documentation › Example
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#05-example
source_hash: 2fe955f24becfc0056d4413a5c90619fed2f2f59e1d3bfdfbcb4905461e1325c
---
```
# Core variables
[core]
	; Don't trust file modes
	filemode = false

# Our diff algorithm
[diff]
	external = /usr/local/bin/diff-wrapper
	renames = true

[branch "devel"]
	remote = origin
	merge = refs/heads/devel

# Proxy settings
[core]
	gitProxy="ssh" for "kernel.org"
	gitProxy=default-proxy ; for the rest

[include]
	path = /path/to/foo.inc ; include by absolute path
	path = foo.inc ; find "foo.inc" relative to the current file
	path = ~/foo.inc ; find "foo.inc" in your `$HOME` directory

; include if $GIT_DIR is /path/to/foo/.git
[includeIf "gitdir:/path/to/foo/.git"]
	path = /path/to/foo.inc

; include for all repositories inside /path/to/group
[includeIf "gitdir:/path/to/group/"]
	path = /path/to/foo.inc

; include for all repositories inside $HOME/to/group
[includeIf "gitdir:~/to/group/"]
	path = /path/to/foo.inc

; relative paths are always relative to the including
; file (if the condition is true); their location is not
; affected by the condition
[includeIf "gitdir:/path/to/group/"]
	path = foo.inc

; include only if we are in a worktree where foo-branch is
; currently checked out
[includeIf "onbranch:foo-branch"]
	path = foo.inc

; include only if a remote with the given URL exists (note
; that such a URL may be provided later in a file or in a
; file read after this file is read, as seen in this example)
[includeIf "hasconfig:remote.*.url:https://example.com/**"]
	path = foo.inc
[remote "origin"]
	url = https://example.com/git
```

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
