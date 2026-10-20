---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#05-2-http-2-protocol-overview.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-05-2-http-2-protocol-overview
type: reference
title: 'RFC 9113: HTTP/2 › 2. HTTP/2 Protocol Overview'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#05-2-http-2-protocol-overview
source_hash: c95b99d12f63168e33b0ac46858bc6d7acf63dd9b3a7ba667ff855c6ec03e353
---
HTTP/2 provides an optimized transport for HTTP semantics. HTTP/2 supports all of the core features of HTTP but aims to be more efficient than HTTP/1.1.[¶](#section-2-1)

HTTP/2 is a connection-oriented application-layer protocol that runs over a TCP connection (\[[TCP](#RFC0793)]). The client is the TCP connection initiator.[¶](#section-2-2)

The basic protocol unit in HTTP/2 is a [frame](#FrameHeader) ([Section 4.1](#FrameHeader)). Each frame type serves a different purpose. For example, [HEADERS](#HEADERS) and [DATA](#DATA) frames form the basis of [HTTP requests and responses](#HttpFraming) ([Section 8.1](#HttpFraming)); other frame types like [SETTINGS](#SETTINGS), [WINDOW\_UPDATE](#WINDOW_UPDATE), and [PUSH\_PROMISE](#PUSH_PROMISE) are used in support of other HTTP/2 features.[¶](#section-2-3)

Multiplexing of requests is achieved by having each HTTP request/response exchange associated with its own [stream](#StreamsLayer) ([Section 5](#StreamsLayer)). Streams are largely independent of each other, so a blocked or stalled request or response does not prevent progress on other streams.[¶](#section-2-4)

Effective use of multiplexing depends on flow control and prioritization. [Flow control](#FlowControl) ([Section 5.2](#FlowControl)) ensures that it is possible to efficiently use multiplexed streams by restricting data that is transmitted to what the receiver is able to handle. [Prioritization](#StreamPriority) ([Section 5.3](#StreamPriority)) ensures that limited resources are used most effectively. This revision of HTTP/2 deprecates the priority signaling scheme from \[[RFC7540](#RFC7540)].[¶](#section-2-5)

Because HTTP fields used in a connection can contain large amounts of redundant data, frames that contain them are [compressed](#FieldBlock) ([Section 4.3](#FieldBlock)). This has especially advantageous impact upon request sizes in the common case, allowing many requests to be compressed into one packet.[¶](#section-2-6)

Finally, HTTP/2 adds a new, optional interaction mode whereby a server can [push responses to a client](#PushResources) ([Section 8.4](#PushResources)). This is intended to allow a server to speculatively send data to a client that the server anticipates the client will need, trading off some network usage against a potential latency gain. The server does this by synthesizing a request, which it sends as a [PUSH\_PROMISE](#PUSH_PROMISE) frame. The server is then able to send a response to the synthetic request on a separate stream.[¶](#section-2-7)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
