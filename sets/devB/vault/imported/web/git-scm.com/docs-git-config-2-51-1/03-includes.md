---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#03-includes.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-03-includes
type: reference
title: Git - git-config Documentation › Includes
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#03-includes
source_hash: 254616bd8b5285d105442a1f5b31fa6c9f43e7846bcedf51cc3b83ce39a1a07a
---
The `include` and `includeIf` sections allow you to include config directives from another source. These sections behave identically to each other with the exception that `includeIf` sections may be ignored if their condition does not evaluate to true; see "Conditional includes" below.

You can include a config file from another by setting the special `include.path` (or `includeIf.*.path`) variable to the name of the file to be included. The variable takes a pathname as its value, and is subject to tilde expansion. These variables can be given multiple times.

The contents of the included file are inserted immediately, as if they had been found at the location of the include directive. If the value of the variable is a relative path, the path is considered to be relative to the configuration file in which the include directive was found. See below for examples.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
