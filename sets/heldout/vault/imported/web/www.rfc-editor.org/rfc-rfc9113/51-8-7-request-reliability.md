---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#51-8-7-request-reliability.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-51-8-7-request-reliability
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.7. Request Reliability'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#51-8-7-request-reliability
source_hash: fcf3bcd34bb6adc08e7746a5916a0b59d202020ea551a0db2bf3a4a7904cfaa5
---
In general, an HTTP client is unable to retry a non-idempotent request when an error occurs because there is no means to determine the nature of the error (see [Section 9.2.2](https://www.rfc-editor.org/rfc/rfc9110#section-9.2.2) of \[[HTTP](#RFC9110)]). It is possible that some server processing occurred prior to the error, which could result in undesirable effects if the request were reattempted.[¶](#section-8.7-1)

HTTP/2 provides two mechanisms for providing a guarantee to a client that a request has not been processed:[¶](#section-8.7-2)

- The [GOAWAY](#GOAWAY) frame indicates the highest stream number that might have been processed. Requests on streams with higher numbers are therefore guaranteed to be safe to retry.[¶](#section-8.7-3.1)
- The [REFUSED\_STREAM](#REFUSED_STREAM) error code can be included in a [RST\_STREAM](#RST_STREAM) frame to indicate that the stream is being closed prior to any processing having occurred. Any request that was sent on the reset stream can be safely retried.[¶](#section-8.7-3.2)

Requests that have not been processed have not failed; clients MAY automatically retry them, even those with non-idempotent methods.[¶](#section-8.7-4)

A server MUST NOT indicate that a stream has not been processed unless it can guarantee that fact. If frames that are on a stream are passed to the application layer for any stream, then [REFUSED\_STREAM](#REFUSED_STREAM) MUST NOT be used for that stream, and a [GOAWAY](#GOAWAY) frame MUST include a stream identifier that is greater than or equal to the given stream identifier.[¶](#section-8.7-5)

In addition to these mechanisms, the [PING](#PING) frame provides a way for a client to easily test a connection. Connections that remain idle can become broken, because some middleboxes (for instance, network address translators or load balancers) silently discard connection bindings. The [PING](#PING) frame allows a client to safely test whether a connection is still active without sending a request.[¶](#section-8.7-6)

### 8.8. Examples

This section shows HTTP/1.1 requests and responses, with illustrations of equivalent HTTP/2 requests and responses.[¶](#section-8.8-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
