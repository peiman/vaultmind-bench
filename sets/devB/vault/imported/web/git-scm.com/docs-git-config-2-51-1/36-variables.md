---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#36-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-36-variables
type: reference
title: Git - git-config Documentation › Variables (30/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#36-variables
source_hash: 3f50ac91370f8c62f31a1ac34d7db16cfb03b2d919c1f5647a70ef876105348b
---
File containing the SSL private key when fetching or pushing over HTTPS. Can be overridden by the `GIT_SSL_KEY` environment variable.

[](#Documentation/git-config.txt-httpsslCertPasswordProtected)http.sslCertPasswordProtected

Enable Git’s password prompt for the SSL certificate. Otherwise OpenSSL will prompt the user, possibly many times, if the certificate or private key is encrypted. Can be overridden by the `GIT_SSL_CERT_PASSWORD_PROTECTED` environment variable.

[](#Documentation/git-config.txt-httpsslCAInfo)http.sslCAInfo

File containing the certificates to verify the peer with when fetching or pushing over HTTPS. Can be overridden by the `GIT_SSL_CAINFO` environment variable.

[](#Documentation/git-config.txt-httpsslCAPath)http.sslCAPath

Path containing files with the CA certificates to verify the peer with when fetching or pushing over HTTPS. Can be overridden by the `GIT_SSL_CAPATH` environment variable.

[](#Documentation/git-config.txt-httpsslBackend)http.sslBackend

Name of the SSL backend to use (e.g. "openssl" or "schannel"). This option is ignored if cURL lacks support for choosing the SSL backend at runtime.

[](#Documentation/git-config.txt-httpsslCertType)http.sslCertType

Type of client certificate used when fetching or pushing over HTTPS. "PEM", "DER" are supported when using openssl or gnutls backends. "P12" is supported on "openssl", "schannel", "securetransport", and gnutls 8.11+. See also libcurl `CURLOPT_SSLCERTTYPE`. Can be overridden by the `GIT_SSL_CERT_TYPE` environment variable.

[](#Documentation/git-config.txt-httpsslKeyType)http.sslKeyType

Type of client private key used when fetching or pushing over HTTPS. (e.g. "PEM", "DER", or "ENG"). Only applicable when using "openssl" backend. "DER" is not supported with openssl. Particularly useful when set to "ENG" for authenticating with PKCS#11 tokens, with a PKCS#11 URL in sslCert option. See also libcurl `CURLOPT_SSLKEYTYPE`. Can be overridden by the `GIT_SSL_KEY_TYPE` environment variable.

[](#Documentation/git-config.txt-httpschannelCheckRevoke)http.schannelCheckRevoke

Used to enforce or disable certificate revocation checks in cURL when http.sslBackend is set to "schannel". Defaults to `true` if unset. Only necessary to disable this if Git consistently errors and the message is about checking the revocation status of a certificate. This option is ignored if cURL lacks support for setting the relevant SSL option at runtime.

[](#Documentation/git-config.txt-httpschannelUseSSLCAInfo)http.schannelUseSSLCAInfo

As of cURL v7.60.0, the Secure Channel backend can use the certificate bundle provided via `http.sslCAInfo`, but that would override the Windows Certificate Store. Since this is not desirable by default, Git will tell cURL not to use that bundle by default when the `schannel` backend was configured via `http.sslBackend`, unless `http.schannelUseSSLCAInfo` overrides this behavior.

[](#Documentation/git-config.txt-httppinnedPubkey)http.pinnedPubkey

Public key of the https service. It may either be the filename of a PEM or DER encoded public key file or a string starting with *sha256//* followed by the base64 encoded sha256 hash of the public key. See also libcurl *CURLOPT\_PINNEDPUBLICKEY*. git will exit with an error if this option is set but not supported by cURL.

[](#Documentation/git-config.txt-httpsslTry)http.sslTry

Attempt to use AUTH SSL/TLS and encrypted data transfers when connecting via regular FTP protocol. This might be needed if the FTP server requires it for security reasons or you wish to connect securely whenever remote FTP server supports it. Default is false since it might trigger certificate verification errors on misconfigured servers.

[](#Documentation/git-config.txt-httpmaxRequests)http.maxRequests

How many HTTP requests to launch in parallel. Can be overridden by the `GIT_HTTP_MAX_REQUESTS` environment variable. Default is 5.

[](#Documentation/git-config.txt-httpminSessions)http.minSessions

The number of curl sessions (counted across slots) to be kept across requests. They will not be ended with curl\_easy\_cleanup() until http\_cleanup() is invoked. If USE\_CURL\_MULTI is not defined, this value will be capped at 1. Defaults to 1.

[](#Documentation/git-config.txt-httppostBuffer)http.postBuffer

Maximum size in bytes of the buffer used by smart HTTP transports when POSTing data to the remote system. For requests larger than this buffer size, HTTP/1.1 and Transfer-Encoding: chunked is used to avoid creating a massive pack file locally. Default is 1 MiB, which is sufficient for most requests.

Note that raising this limit is only effective for disabling chunked transfer encoding and therefore should be used only where the remote server or a proxy only supports HTTP/1.0 or is noncompliant with the HTTP standard. Raising this is not, in general, an effective solution for most push problems, but can increase memory consumption significantly since the entire buffer is allocated even for small pushes.

[](#Documentation/git-config.txt-httplowSpeedLimit)http.lowSpeedLimit

[](#Documentation/git-config.txt-httplowSpeedTime)http.lowSpeedTime

If the HTTP transfer speed, in bytes per second, is less than *http.lowSpeedLimit* for longer than *http.lowSpeedTime* seconds, the transfer is aborted. Can be overridden by the `GIT_HTTP_LOW_SPEED_LIMIT` and `GIT_HTTP_LOW_SPEED_TIME` environment variables.

[](#Documentation/git-config.txt-httpkeepAliveIdle)http.keepAliveIdle

Specifies how long in seconds to wait on an idle connection before sending TCP keepalive probes (if supported by the OS). If unset, curl’s default value is used. Can be overridden by the `GIT_HTTP_KEEPALIVE_IDLE` environment variable.

[](#Documentation/git-config.txt-httpkeepAliveInterval)http.keepAliveInterval

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
