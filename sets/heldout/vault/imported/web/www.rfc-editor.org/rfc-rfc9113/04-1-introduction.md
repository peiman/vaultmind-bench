---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#04-1-introduction.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-04-1-introduction
type: reference
title: 'RFC 9113: HTTP/2 › 1. Introduction'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#04-1-introduction
source_hash: 9d0179375273a461b8ee218dfbfbf6d7fd6e49ee1c2f9795cfeb96137e0773d7
---
The performance of applications using the Hypertext Transfer Protocol (HTTP, \[[HTTP](#RFC9110)]) is linked to how each version of HTTP uses the underlying transport, and the conditions under which the transport operates.[¶](#section-1-1)

Making multiple concurrent requests can reduce latency and improve application performance. HTTP/1.0 allowed only one request to be outstanding at a time on a given TCP \[[TCP](#RFC0793)] connection. HTTP/1.1 \[[HTTP/1.1](#RFC9112)] added request pipelining, but this only partially addressed request concurrency and still suffers from application-layer head-of-line blocking. Therefore, HTTP/1.0 and HTTP/1.1 clients use multiple connections to a server to make concurrent requests.[¶](#section-1-2)

Furthermore, HTTP fields are often repetitive and verbose, causing unnecessary network traffic as well as causing the initial TCP congestion window to quickly fill. This can result in excessive latency when multiple requests are made on a new TCP connection.[¶](#section-1-3)

HTTP/2 addresses these issues by defining an optimized mapping of HTTP's semantics to an underlying connection. Specifically, it allows interleaving of messages on the same connection and uses an efficient coding for HTTP fields. It also allows prioritization of requests, letting more important requests complete more quickly, further improving performance.[¶](#section-1-4)

The resulting protocol is more friendly to the network because fewer TCP connections can be used in comparison to HTTP/1.x. This means less competition with other flows and longer-lived connections, which in turn lead to better utilization of available network capacity. Note, however, that TCP head-of-line blocking is not addressed by this protocol.[¶](#section-1-5)

Finally, HTTP/2 also enables more efficient processing of messages through use of binary message framing.[¶](#section-1-6)

This document obsoletes RFCs 7540 and 8740. [Appendix B](#revision-updates) lists notable changes.[¶](#section-1-7)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
