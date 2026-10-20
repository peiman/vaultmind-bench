---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#34-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-34-variables
type: reference
title: Git - git-config Documentation › Variables (28/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#34-variables
source_hash: 3440ea75106da81575cf3c8cbb18378fdb00e2de9dc9afbfad13527c78defcf1
---
Don’t rescan the working directory for changes after the tool finishes execution.

[](#Documentation/git-config.txt-guitoolnameconfirm)guitool.&lt;name&gt;.confirm

Show a confirmation dialog before actually running the tool.

[](#Documentation/git-config.txt-guitoolnameargPrompt)guitool.&lt;name&gt;.argPrompt

Request a string argument from the user, and pass it to the tool through the `ARGS` environment variable. Since requesting an argument implies confirmation, the *confirm* option has no effect if this is enabled. If the option is set to *true*, *yes*, or *1*, the dialog uses a built-in generic prompt; otherwise the exact value of the variable is used.

[](#Documentation/git-config.txt-guitoolnamerevPrompt)guitool.&lt;name&gt;.revPrompt

Request a single valid revision from the user, and set the `REVISION` environment variable. In other aspects this option is similar to *argPrompt*, and can be used together with it.

[](#Documentation/git-config.txt-guitoolnamerevUnmerged)guitool.&lt;name&gt;.revUnmerged

Show only unmerged branches in the *revPrompt* subdialog. This is useful for tools similar to merge or rebase, but not for things like checkout or reset.

[](#Documentation/git-config.txt-guitoolnametitle)guitool.&lt;name&gt;.title

Specifies the title to use for the prompt dialog. The default is the tool name.

[](#Documentation/git-config.txt-guitoolnameprompt)guitool.&lt;name&gt;.prompt

Specifies the general prompt string to display at the top of the dialog, before subsections for *argPrompt* and *revPrompt*. The default value includes the actual command.

[](#Documentation/git-config.txt-helpbrowser)help.browser

Specify the browser that will be used to display help in the *web* format. See [git-help\[1\]](https://git-scm.com/docs/git-help).

[](#Documentation/git-config.txt-helpformat)help.format

Override the default help format used by [git-help\[1\]](https://git-scm.com/docs/git-help). Values *man*, *info*, *web* and *html* are supported. *man* is the default. *web* and *html* are the same.

[](#Documentation/git-config.txt-helpautoCorrect)help.autoCorrect

If git detects typos and can identify exactly one valid command similar to the error, git will try to suggest the correct command or even run the suggestion automatically. Possible config values are:

- 0, "false", "off", "no", "show": show the suggested command (default).
- 1, "true", "on", "yes", "immediate": run the suggested command immediately.
- positive number &gt; 1: run the suggested command after specified deciseconds (0.1 sec).
- "never": don’t run or show any suggested command.
- "prompt": show the suggestion and prompt for confirmation to run the command.

[](#Documentation/git-config.txt-helphtmlPath)help.htmlPath

Specify the path where the HTML documentation resides. File system paths and URLs are supported. HTML pages will be prefixed with this path when help is displayed in the *web* format. This defaults to the documentation path of your Git installation.

[](#Documentation/git-config.txt-httpproxy)http.proxy

Override the HTTP proxy, normally configured using the *http\_proxy*, *https\_proxy*, and *all\_proxy* environment variables (see `curl`(`1`)). In addition to the syntax understood by curl, it is possible to specify a proxy string with a user name but no password, in which case git will attempt to acquire one in the same way it does for other credentials. See [gitcredentials\[7\]](https://git-scm.com/docs/gitcredentials) for more information. The syntax thus is *\[protocol://]\[user\[:password]@]proxyhost\[:port]\[/path]*. This can be overridden on a per-remote basis; see remote.&lt;name&gt;.proxy

Any proxy, however configured, must be completely transparent and must not modify, transform, or buffer the request or response in any way. Proxies which are not completely transparent are known to cause various forms of breakage with Git.

[](#Documentation/git-config.txt-httpproxyAuthMethod)http.proxyAuthMethod

Set the method with which to authenticate against the HTTP proxy. This only takes effect if the configured proxy string contains a user name part (i.e. is of the form *user@host* or *user@host:port*). This can be overridden on a per-remote basis; see `remote.`*&lt;name&gt;*`.proxyAuthMethod`. Both can be overridden by the `GIT_HTTP_PROXY_AUTHMETHOD` environment variable. Possible values are:

- `anyauth` - Automatically pick a suitable authentication method. It is assumed that the proxy answers an unauthenticated request with a 407 status code and one or more Proxy-authenticate headers with supported authentication methods. This is the default.
- `basic` - HTTP Basic authentication
- `digest` - HTTP Digest authentication; this prevents the password from being transmitted to the proxy in clear text
- `negotiate` - GSS-Negotiate authentication (compare the --negotiate option of `curl`(`1`))
- `ntlm` - NTLM authentication (compare the --ntlm option of `curl`(`1`))

[](#Documentation/git-config.txt-httpproxySSLCert)http.proxySSLCert

The pathname of a file that stores a client certificate to use to authenticate with an HTTPS proxy. Can be overridden by the `GIT_PROXY_SSL_CERT` environment variable.

[](#Documentation/git-config.txt-httpproxySSLKey)http.proxySSLKey

The pathname of a file that stores a private key to use to authenticate with an HTTPS proxy. Can be overridden by the `GIT_PROXY_SSL_KEY` environment variable.

[](#Documentation/git-config.txt-httpproxySSLCertPasswordProtected)http.proxySSLCertPasswordProtected

Enable Git’s password prompt for the proxy SSL certificate. Otherwise OpenSSL will prompt the user, possibly many times, if the certificate or private key is encrypted. Can be overridden by the `GIT_PROXY_SSL_CERT_PASSWORD_PROTECTED` environment variable.

[](#Documentation/git-config.txt-httpproxySSLCAInfo)http.proxySSLCAInfo

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
