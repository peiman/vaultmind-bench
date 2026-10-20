---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#37-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-37-variables
type: reference
title: Git - git-config Documentation › Variables (31/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#37-variables
source_hash: fd13dd7b1f45665f3e470545757423b2ec7a6269624ee0680877deb235a5a6ea
---
Specifies how long in seconds to wait between TCP keepalive probes (if supported by the OS). If unset, curl’s default value is used. Can be overridden by the `GIT_HTTP_KEEPALIVE_INTERVAL` environment variable.

[](#Documentation/git-config.txt-httpkeepAliveCount)http.keepAliveCount

Specifies how many TCP keepalive probes to send before giving up and terminating the connection (if supported by the OS). If unset, curl’s default value is used. Can be overridden by the `GIT_HTTP_KEEPALIVE_COUNT` environment variable.

[](#Documentation/git-config.txt-httpnoEPSV)http.noEPSV

A boolean which disables using of EPSV ftp command by curl. This can be helpful with some "poor" ftp servers which don’t support EPSV mode. Can be overridden by the `GIT_CURL_FTP_NO_EPSV` environment variable. Default is false (curl will use EPSV).

[](#Documentation/git-config.txt-httpuserAgent)http.userAgent

The HTTP USER\_AGENT string presented to an HTTP server. The default value represents the version of the Git client such as git/1.7.1. This option allows you to override this value to a more common value such as Mozilla/4.0. This may be necessary, for instance, if connecting through a firewall that restricts HTTP connections to a set of common USER\_AGENT strings (but not including those like git/1.7.1). Can be overridden by the `GIT_HTTP_USER_AGENT` environment variable.

[](#Documentation/git-config.txt-httpfollowRedirects)http.followRedirects

Whether git should follow HTTP redirects. If set to `true`, git will transparently follow any redirect issued by a server it encounters. If set to `false`, git will treat all redirects as errors. If set to `initial`, git will follow redirects only for the initial request to a remote, but not for subsequent follow-up HTTP requests. Since git uses the redirected URL as the base for the follow-up requests, this is generally sufficient. The default is `initial`.

[](#Documentation/git-config.txt-httpurl)http.&lt;url&gt;.*

Any of the http.* options above can be applied selectively to some URLs. For a config key to match a URL, each element of the config key is compared to that of the URL, in the following order:

1. Scheme (e.g., `https` in `https://example.com/`). This field must match exactly between the config key and the URL.
2. Host/domain name (e.g., `example.com` in `https://example.com/`). This field must match between the config key and the URL. It is possible to specify a `*` as part of the host name to match all subdomains at this level. `https://*.example.com/` for example would match `https://foo.example.com/`, but not `https://foo.bar.example.com/`.
3. Port number (e.g., `8080` in `http://example.com:8080/`). This field must match exactly between the config key and the URL. Omitted port numbers are automatically converted to the correct default for the scheme before matching.
4. Path (e.g., `repo.git` in `https://example.com/repo.git`). The path field of the config key must match the path field of the URL either exactly or as a prefix of slash-delimited path elements. This means a config key with path `foo/` matches URL path `foo/bar`. A prefix can only match on a slash (`/`) boundary. Longer matches take precedence (so a config key with path `foo/bar` is a better match to URL path `foo/bar` than a config key with just path `foo/`).
5. User name (e.g., `user` in `https://user@example.com/repo.git`). If the config key has a user name it must match the user name in the URL exactly. If the config key does not have a user name, that config key will match a URL with any user name (including none), but at a lower precedence than a config key with a user name.

The list above is ordered by decreasing precedence; a URL that matches a config key’s path is preferred to one that matches its user name. For example, if the URL is `https://user@example.com/foo/bar` a config key match of `https://example.com/foo` will be preferred over a config key match of `https://user@example.com`.

All URLs are normalized before attempting any matching (the password part, if embedded in the URL, is always ignored for matching purposes) so that equivalent URLs that are simply spelled differently will match properly. Environment variable settings always override any matches. The URLs that are matched against are those given directly to Git commands. This means any URLs visited as a result of a redirection do not participate in matching.

[](#Documentation/git-config.txt-i18ncommitEncoding)i18n.commitEncoding

Character encoding the commit messages are stored in; Git itself does not care per se, but this information is necessary e.g. when importing commits from emails or in the gitk graphical history browser (and possibly in other places in the future or in other porcelains). See e.g. [git-mailinfo\[1\]](https://git-scm.com/docs/git-mailinfo). Defaults to *utf-8*.

[](#Documentation/git-config.txt-i18nlogOutputEncoding)i18n.logOutputEncoding

Character encoding the commit messages are converted to when running *git log* and friends.

[](#Documentation/git-config.txt-imapfolder)imap.folder

The folder to drop the mails into, which is typically the Drafts folder. For example: `INBOX.Drafts`, `INBOX/Drafts` or \[`Gmail`]`/Drafts`. The IMAP folder to interact with MUST be specified; the value of this configuration variable is used as the fallback default value when the `--folder` option is not given.

[](#Documentation/git-config.txt-imaptunnel)imap.tunnel

Command used to set up a tunnel to the IMAP server through which commands will be piped instead of using a direct network connection to the server. Required when imap.host is not set.

[](#Documentation/git-config.txt-imaphost)imap.host

A URL identifying the server. Use an `imap://` prefix for non-secure connections and an `imaps://` prefix for secure connections. Ignored when imap.tunnel is set, but required otherwise.

[](#Documentation/git-config.txt-imapuser)imap.user

The username to use when logging in to the server.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
