---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#35-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-35-variables
type: reference
title: Git - git-config Documentation › Variables (29/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#35-variables
source_hash: 6082ff2aa78b07ddac29fc2b9168b9277ea77ff2e3f37f2d2871e94a590ff6d0
---
Pathname to the file containing the certificate bundle that should be used to verify the proxy with when using an HTTPS proxy. Can be overridden by the `GIT_PROXY_SSL_CAINFO` environment variable.

[](#Documentation/git-config.txt-httpemptyAuth)http.emptyAuth

Attempt authentication without seeking a username or password. This can be used to attempt GSS-Negotiate authentication without specifying a username in the URL, as libcurl normally requires a username for authentication.

[](#Documentation/git-config.txt-httpproactiveAuth)http.proactiveAuth

Attempt authentication without first making an unauthenticated attempt and receiving a 401 response. This can be used to ensure that all requests are authenticated. If `http.emptyAuth` is set to true, this value has no effect.

If the credential helper used specifies an authentication scheme (i.e., via the `authtype` field), that value will be used; if a username and password is provided without a scheme, then Basic authentication is used. The value of the option determines the scheme requested from the helper. Possible values are:

- `basic` - Request Basic authentication from the helper.
- `auto` - Allow the helper to pick an appropriate scheme.
- `none` - Disable proactive authentication.

Note that TLS should always be used with this configuration, since otherwise it is easy to accidentally expose plaintext credentials if Basic authentication is selected.

[](#Documentation/git-config.txt-httpdelegation)http.delegation

Control GSSAPI credential delegation. The delegation is disabled by default in libcurl since version 7.21.7. Set parameter to tell the server what it is allowed to delegate when it comes to user credentials. Used with GSS/kerberos. Possible values are:

- `none` - Don’t allow any delegation.
- `policy` - Delegates if and only if the OK-AS-DELEGATE flag is set in the Kerberos service ticket, which is a matter of realm policy.
- `always` - Unconditionally allow the server to delegate.

Pass an additional HTTP header when communicating with a server. If more than one such entry exists, all of them are added as extra headers. To allow overriding the settings inherited from the system config, an empty value will reset the extra headers to the empty list.

[](#Documentation/git-config.txt-httpcookieFile)http.cookieFile

The pathname of a file containing previously stored cookie lines, which should be used in the Git http session, if they match the server. The file format of the file to read cookies from should be plain HTTP headers or the Netscape/Mozilla cookie file format (see `curl`(`1`)). Set it to an empty string, to accept only new cookies from the server and send them back in successive requests within same connection. NOTE that the file specified with http.cookieFile is used only as input unless http.saveCookies is set.

[](#Documentation/git-config.txt-httpsaveCookies)http.saveCookies

If set, store cookies received during requests to the file specified by http.cookieFile. Has no effect if http.cookieFile is unset, or set to an empty string.

[](#Documentation/git-config.txt-httpversion)http.version

Use the specified HTTP protocol version when communicating with a server. If you want to force the default. The available and default version depend on libcurl. Currently the possible values of this option are:

- HTTP/2
- HTTP/1.1

[](#Documentation/git-config.txt-httpcurloptResolve)http.curloptResolve

Hostname resolution information that will be used first by libcurl when sending HTTP requests. This information should be in one of the following formats:

- \[+]HOST:PORT:ADDRESS\[,ADDRESS]
- -HOST:PORT

The first format redirects all requests to the given `HOST:PORT` to the provided `ADDRESS`(s). The second format clears all previous config values for that `HOST:PORT` combination. To allow easy overriding of all the settings inherited from the system config, an empty value will reset all resolution information to the empty list.

[](#Documentation/git-config.txt-httpsslVersion)http.sslVersion

The SSL version to use when negotiating an SSL connection, if you want to force the default. The available and default version depend on whether libcurl was built against NSS or OpenSSL and the particular configuration of the crypto library in use. Internally this sets the *CURLOPT\_SSL\_VERSION* option; see the libcurl documentation for more details on the format of this option and for the ssl version supported. Currently the possible values of this option are:

- sslv2
- sslv3
- tlsv1
- tlsv1.0
- tlsv1.1
- tlsv1.2
- tlsv1.3

Can be overridden by the `GIT_SSL_VERSION` environment variable. To force git to use libcurl’s default ssl version and ignore any explicit http.sslversion option, set `GIT_SSL_VERSION` to the empty string.

[](#Documentation/git-config.txt-httpsslCipherList)http.sslCipherList

A list of SSL ciphers to use when negotiating an SSL connection. The available ciphers depend on whether libcurl was built against NSS or OpenSSL and the particular configuration of the crypto library in use. Internally this sets the *CURLOPT\_SSL\_CIPHER\_LIST* option; see the libcurl documentation for more details on the format of this list.

Can be overridden by the `GIT_SSL_CIPHER_LIST` environment variable. To force git to use libcurl’s default cipher list and ignore any explicit http.sslCipherList option, set `GIT_SSL_CIPHER_LIST` to the empty string.

[](#Documentation/git-config.txt-httpsslVerify)http.sslVerify

Whether to verify the SSL certificate when fetching or pushing over HTTPS. Defaults to true. Can be overridden by the `GIT_SSL_NO_VERIFY` environment variable.

[](#Documentation/git-config.txt-httpsslCert)http.sslCert

File containing the SSL certificate when fetching or pushing over HTTPS. Can be overridden by the `GIT_SSL_CERT` environment variable.

[](#Documentation/git-config.txt-httpsslKey)http.sslKey

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
