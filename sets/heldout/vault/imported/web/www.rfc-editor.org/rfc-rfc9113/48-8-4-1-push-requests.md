---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#48-8-4-1-push-requests.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-48-8-4-1-push-requests
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.4. Server Push › 8.4.1. Push Requests'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#48-8-4-1-push-requests
source_hash: 62a036e7244465f64b789b666a76f2bfc44f2b90f127276ab28da185d3f8252d
---
Server push is semantically equivalent to a server responding to a request; however, in this case, that request is also sent by the server, as a [PUSH\_PROMISE](#PUSH_PROMISE) frame.[¶](#section-8.4.1-1)

The [PUSH\_PROMISE](#PUSH_PROMISE) frame includes a field block that contains control data and a complete set of request header fields that the server attributes to the request. It is not possible to push a response to a request that includes message content.[¶](#section-8.4.1-2)

Promised requests are always associated with an explicit request from the client. The [PUSH\_PROMISE](#PUSH_PROMISE) frames sent by the server are sent on that explicit request's stream. The [PUSH\_PROMISE](#PUSH_PROMISE) frame also includes a promised stream identifier, chosen from the stream identifiers available to the server (see [Section 5.1.1](#StreamIdentifiers)).[¶](#section-8.4.1-3)

The header fields in [PUSH\_PROMISE](#PUSH_PROMISE) and any subsequent [CONTINUATION](#CONTINUATION) frames MUST be a valid and complete set of [request header fields](#HttpRequest) ([Section 8.3.1](#HttpRequest)). The server MUST include a method in the "`:method`" pseudo-header field that is safe and cacheable. If a client receives a [PUSH\_PROMISE](#PUSH_PROMISE) that does not include a complete and valid set of header fields or the "`:method`" pseudo-header field identifies a method that is not safe, it MUST respond on the promised stream with a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-8.4.1-4)

The server SHOULD send [PUSH\_PROMISE](#PUSH_PROMISE) ([Section 6.6](#PUSH_PROMISE)) frames prior to sending any frames that reference the promised responses. This avoids a race where clients issue requests prior to receiving any [PUSH\_PROMISE](#PUSH_PROMISE) frames.[¶](#section-8.4.1-5)

For example, if the server receives a request for a document containing embedded links to multiple image files and the server chooses to push those additional images to the client, sending [PUSH\_PROMISE](#PUSH_PROMISE) frames before the [DATA](#DATA) frames that contain the image links ensures that the client is able to see that a resource will be pushed before discovering embedded links. Similarly, if the server pushes resources referenced by the field block (for instance, in Link header fields), sending a [PUSH\_PROMISE](#PUSH_PROMISE) before sending the header ensures that clients do not request those resources.[¶](#section-8.4.1-6)

[PUSH\_PROMISE](#PUSH_PROMISE) frames MUST NOT be sent by the client.[¶](#section-8.4.1-7)

[PUSH\_PROMISE](#PUSH_PROMISE) frames can be sent by the server on any client-initiated stream, but the stream MUST be in either the "open" or "half-closed (remote)" state with respect to the server. [PUSH\_PROMISE](#PUSH_PROMISE) frames are interspersed with the frames that comprise a response, though they cannot be interspersed with [HEADERS](#HEADERS) and [CONTINUATION](#CONTINUATION) frames that comprise a single field block.[¶](#section-8.4.1-8)

Sending a [PUSH\_PROMISE](#PUSH_PROMISE) frame creates a new stream and puts the stream into the "reserved (local)" state for the server and the "reserved (remote)" state for the client.[¶](#section-8.4.1-9)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
