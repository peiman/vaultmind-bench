---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#45-8-1-http-message-framing.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-45-8-1-http-message-framing
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.1. HTTP Message Framing'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#45-8-1-http-message-framing
source_hash: d79d4d2a4cdd60b2483de1ac444a1c6d8111a7911ca92dbb2f74e6c16b57cd88
---
A client sends an HTTP request on a new stream, using a previously unused [stream identifier](#StreamIdentifiers) ([Section 5.1.1](#StreamIdentifiers)). A server sends an HTTP response on the same stream as the request.[¶](#section-8.1-1)

An HTTP message (request or response) consists of:[¶](#section-8.1-2)

1. one [HEADERS](#HEADERS) frame (followed by zero or more [CONTINUATION](#CONTINUATION) frames) containing the header section (see [Section 6.3](https://www.rfc-editor.org/rfc/rfc9110#section-6.3) of \[[HTTP](#RFC9110)]),[¶](#section-8.1-3.1)
2. zero or more [DATA](#DATA) frames containing the message content (see [Section 6.4](https://www.rfc-editor.org/rfc/rfc9110#section-6.4) of \[[HTTP](#RFC9110)]), and[¶](#section-8.1-3.2)
3. optionally, one [HEADERS](#HEADERS) frame (followed by zero or more [CONTINUATION](#CONTINUATION) frames) containing the trailer section, if present (see [Section 6.5](https://www.rfc-editor.org/rfc/rfc9110#section-6.5) of \[[HTTP](#RFC9110)]).[¶](#section-8.1-3.3)

For a response only, a server MAY send any number of interim responses before the [HEADERS](#HEADERS) frame containing a final response. An interim response consists of a [HEADERS](#HEADERS) frame (which might be followed by zero or more [CONTINUATION](#CONTINUATION) frames) containing the control data and header section of an interim (1xx) HTTP response (see [Section 15](https://www.rfc-editor.org/rfc/rfc9110#section-15) of \[[HTTP](#RFC9110)]). A [HEADERS](#HEADERS) frame with the END\_STREAM flag set that carries an informational status code is [malformed](#malformed) ([Section 8.1.1](#malformed)).[¶](#section-8.1-4)

The last frame in the sequence bears an END\_STREAM flag, noting that a [HEADERS](#HEADERS) frame with the END\_STREAM flag set can be followed by [CONTINUATION](#CONTINUATION) frames that carry any remaining fragments of the field block.[¶](#section-8.1-5)

Other frames (from any stream) MUST NOT occur between the [HEADERS](#HEADERS) frame and any [CONTINUATION](#CONTINUATION) frames that might follow.[¶](#section-8.1-6)

HTTP/2 uses DATA frames to carry message content. The `chunked` transfer encoding defined in [Section 7.1](https://www.rfc-editor.org/rfc/rfc9112#section-7.1) of \[[HTTP/1.1](#RFC9112)] cannot be used in HTTP/2; see [Section 8.2.2](#ConnectionSpecific).[¶](#section-8.1-7)

Trailer fields are carried in a field block that also terminates the stream. That is, trailer fields comprise a sequence starting with a [HEADERS](#HEADERS) frame, followed by zero or more [CONTINUATION](#CONTINUATION) frames, where the [HEADERS](#HEADERS) frame bears an END\_STREAM flag. Trailers MUST NOT include [pseudo-header fields](#PseudoHeaderFields) ([Section 8.3](#PseudoHeaderFields)). An endpoint that receives pseudo-header fields in trailers MUST treat the request or response as [malformed](#malformed) ([Section 8.1.1](#malformed)).[¶](#section-8.1-8)

An endpoint that receives a [HEADERS](#HEADERS) frame without the END\_STREAM flag set after receiving the [HEADERS](#HEADERS) frame that opens a request or after receiving a final (non-informational) status code MUST treat the corresponding request or response as [malformed](#malformed) ([Section 8.1.1](#malformed)).[¶](#section-8.1-9)

An HTTP request/response exchange fully consumes a single stream. A request starts with the [HEADERS](#HEADERS) frame that puts the stream into the "open" state. The request ends with a frame with the END\_STREAM flag set, which causes the stream to become "half-closed (local)" for the client and "half-closed (remote)" for the server. A response stream starts with zero or more interim responses in [HEADERS](#HEADERS) frames, followed by a [HEADERS](#HEADERS) frame containing a final status code.[¶](#section-8.1-10)

An HTTP response is complete after the server sends -- or the client receives -- a frame with the END\_STREAM flag set (including any [CONTINUATION](#CONTINUATION) frames needed to complete a field block). A server can send a complete response prior to the client sending an entire request if the response does not depend on any portion of the request that has not been sent and received. When this is true, a server MAY request that the client abort transmission of a request without error by sending a [RST\_STREAM](#RST_STREAM) with an error code of [NO\_ERROR](#NO_ERROR) after sending a complete response (i.e., a frame with the END\_STREAM flag set). Clients MUST NOT discard responses as a result of receiving such a [RST\_STREAM](#RST_STREAM), though clients can always discard responses at their discretion for other reasons.[¶](#section-8.1-11)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
