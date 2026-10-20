---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#19-5-1-1-stream-identifiers.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-19-5-1-1-stream-identifiers
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.1. Stream States › 5.1.1. Stream Identifiers'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#19-5-1-1-stream-identifiers
source_hash: e76efac1ae200a28b54fc4651a9669fdcaff9bb4d8f3a227eade32999becf512
---
Streams are identified by an unsigned 31-bit integer. Streams initiated by a client MUST use odd-numbered stream identifiers; those initiated by the server MUST use even-numbered stream identifiers. A stream identifier of zero (0x00) is used for connection control messages; the stream identifier of zero cannot be used to establish a new stream.[¶](#section-5.1.1-1)

The identifier of a newly established stream MUST be numerically greater than all streams that the initiating endpoint has opened or reserved. This governs streams that are opened using a [HEADERS](#HEADERS) frame and streams that are reserved using [PUSH\_PROMISE](#PUSH_PROMISE). An endpoint that receives an unexpected stream identifier MUST respond with a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-5.1.1-2)

A [HEADERS](#HEADERS) frame will transition the client-initiated stream identified by the stream identifier in the frame header from "idle" to "open". A [PUSH\_PROMISE](#PUSH_PROMISE) frame will transition the server-initiated stream identified by the Promised Stream ID field in the frame payload from "idle" to "reserved (local)" or "reserved (remote)". When a stream transitions out of the "idle" state, all streams in the "idle" state that might have been opened by the peer with a lower-valued stream identifier immediately transition to "closed". That is, an endpoint may skip a stream identifier, with the effect being that the skipped stream is immediately closed.[¶](#section-5.1.1-3)

Stream identifiers cannot be reused. Long-lived connections can result in an endpoint exhausting the available range of stream identifiers. A client that is unable to establish a new stream identifier can establish a new connection for new streams. A server that is unable to establish a new stream identifier can send a [GOAWAY](#GOAWAY) frame so that the client is forced to open a new connection for new streams.[¶](#section-5.1.1-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
