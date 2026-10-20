---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#38-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-38-variables
type: reference
title: Git - git-config Documentation › Variables (32/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#38-variables
source_hash: 2543ab00433d93348052c9ee80a8c1907a45238e4c5c7c89582ba9309a8f82bd
---
[](#Documentation/git-config.txt-imappass)imap.pass

The password to use when logging in to the server.

[](#Documentation/git-config.txt-imapport)imap.port

An integer port number to connect to on the server. Defaults to 143 for imap:// hosts and 993 for imaps:// hosts. Ignored when imap.tunnel is set.

[](#Documentation/git-config.txt-imapsslverify)imap.sslverify

A boolean to enable/disable verification of the server certificate used by the SSL/TLS connection. Default is `true`. Ignored when imap.tunnel is set.

[](#Documentation/git-config.txt-imappreformattedHTML)imap.preformattedHTML

A boolean to enable/disable the use of html encoding when sending a patch. An html encoded patch will be bracketed with &lt;pre&gt; and have a content type of text/html. Ironically, enabling this option causes Thunderbird to send the patch as a plain/text, format=fixed email. Default is `false`.

[](#Documentation/git-config.txt-imapauthMethod)imap.authMethod

Specify the authentication method for authenticating with the IMAP server. If Git was built with the NO\_CURL option, or if your curl version is older than 7.34.0, or if you’re running git-imap-send with the `--no-curl` option, the only supported methods are `PLAIN`, `CRAM-MD5`, `OAUTHBEARER` and `XOAUTH2`. If this is not set then `git` `imap-send` uses the basic IMAP plaintext `LOGIN` command.

[](#Documentation/git-config.txt-includepath)include.path

[](#Documentation/git-config.txt-includeIfconditionpath)includeIf.&lt;condition&gt;.path

Special variables to include other configuration files. See the "CONFIGURATION FILE" section in the main [git-config\[1\]](https://git-scm.com/docs/git-config) documentation, specifically the "Includes" and "Conditional Includes" subsections.

[](#Documentation/git-config.txt-indexrecordEndOfIndexEntries)index.recordEndOfIndexEntries

Specifies whether the index file should include an "End Of Index Entry" section. This reduces index load time on multiprocessor machines but produces a message "ignoring EOIE extension" when reading the index using Git versions before 2.20. Defaults to *true* if index.threads has been explicitly enabled, *false* otherwise.

[](#Documentation/git-config.txt-indexrecordOffsetTable)index.recordOffsetTable

Specifies whether the index file should include an "Index Entry Offset Table" section. This reduces index load time on multiprocessor machines but produces a message "ignoring IEOT extension" when reading the index using Git versions before 2.20. Defaults to *true* if index.threads has been explicitly enabled, *false* otherwise.

[](#Documentation/git-config.txt-indexsparse)index.sparse

When enabled, write the index using sparse-directory entries. This has no effect unless `core.sparseCheckout` and `core.sparseCheckoutCone` are both enabled. Defaults to *false*.

[](#Documentation/git-config.txt-indexthreads)index.threads

Specifies the number of threads to spawn when loading the index. This is meant to reduce index load time on multiprocessor machines. Specifying 0 or *true* will cause Git to auto-detect the number of CPUs and set the number of threads accordingly. Specifying 1 or *false* will disable multithreading. Defaults to *true*.

[](#Documentation/git-config.txt-indexversion)index.version

Specify the version with which new index files should be initialized. This does not affect existing repositories. If `feature.manyFiles` is enabled, then the default is 4.

[](#Documentation/git-config.txt-indexskipHash)index.skipHash

When enabled, do not compute the trailing hash for the index file. This accelerates Git commands that manipulate the index, such as `git` `add`, `git` `commit`, or `git` `status`. Instead of storing the checksum, write a trailing set of bytes with value zero, indicating that the computation was skipped.

If you enable `index.skipHash`, then Git clients older than 2.13.0 will refuse to parse the index and Git clients older than 2.40.0 will report an error during `git` `fsck`.

[](#Documentation/git-config.txt-inittemplateDir)`init.templateDir`

Specify the directory from which templates will be copied. (See the "TEMPLATE DIRECTORY" section of [git-init\[1\]](https://git-scm.com/docs/git-init).)

[](#Documentation/git-config.txt-initdefaultBranch)`init.defaultBranch`

Allows overriding the default branch name e.g. when initializing a new repository.

[](#Documentation/git-config.txt-initdefaultObjectFormat)`init.defaultObjectFormat`

Allows overriding the default object format for new repositories. See `--object-format=` in [git-init\[1\]](https://git-scm.com/docs/git-init). Both the command line option and the `GIT_DEFAULT_HASH` environment variable take precedence over this config.

[](#Documentation/git-config.txt-initdefaultRefFormat)`init.defaultRefFormat`

Allows overriding the default ref storage format for new repositories. See `--ref-format=` in [git-init\[1\]](https://git-scm.com/docs/git-init). Both the command line option and the `GIT_DEFAULT_REF_FORMAT` environment variable take precedence over this config.

[](#Documentation/git-config.txt-instawebbrowser)instaweb.browser

Specify the program that will be used to browse your working repository in gitweb. See [git-instaweb\[1\]](https://git-scm.com/docs/git-instaweb).

[](#Documentation/git-config.txt-instawebhttpd)instaweb.httpd

The HTTP daemon command-line to start gitweb on your working repository. See [git-instaweb\[1\]](https://git-scm.com/docs/git-instaweb).

[](#Documentation/git-config.txt-instaweblocal)instaweb.local

If true the web server started by [git-instaweb\[1\]](https://git-scm.com/docs/git-instaweb) will be bound to the local IP (127.0.0.1).

[](#Documentation/git-config.txt-instawebmodulePath)instaweb.modulePath

The default module path for [git-instaweb\[1\]](https://git-scm.com/docs/git-instaweb) to use instead of /usr/lib/apache2/modules. Only used if httpd is Apache.

[](#Documentation/git-config.txt-instawebport)instaweb.port

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
