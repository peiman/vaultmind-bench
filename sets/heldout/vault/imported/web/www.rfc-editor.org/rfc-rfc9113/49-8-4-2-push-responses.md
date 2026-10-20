---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#49-8-4-2-push-responses.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-49-8-4-2-push-responses
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.4. Server Push › 8.4.2. Push Responses'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#49-8-4-2-push-responses
source_hash: e32b54f5020bbbe5fa8ecaad47a398b4eb39bf2318f5688aab4a725aeb075ae8
---
After sending the [PUSH\_PROMISE](#PUSH_PROMISE) frame, the server can begin delivering the pushed response as a [response](#HttpResponse) ([Section 8.3.2](#HttpResponse)) on a server-initiated stream that uses the promised stream identifier. The server uses this stream to transmit an HTTP response, using the same sequence of frames as that defined in [Section 8.1](#HttpFraming). This stream becomes ["half-closed" to the client](#StreamStates) ([Section 5.1](#StreamStates)) after the initial [HEADERS](#HEADERS) frame is sent.[¶](#section-8.4.2-1)

Once a client receives a [PUSH\_PROMISE](#PUSH_PROMISE) frame and chooses to accept the pushed response, the client SHOULD NOT issue any requests for the promised response until after the promised stream has closed.[¶](#section-8.4.2-2)

If the client determines, for any reason, that it does not wish to receive the pushed response from the server or if the server takes too long to begin sending the promised response, the client can send a [RST\_STREAM](#RST_STREAM) frame, using either the [CANCEL](#CANCEL) or [REFUSED\_STREAM](#REFUSED_STREAM) code and referencing the pushed stream's identifier.[¶](#section-8.4.2-3)

A client can use the [SETTINGS\_MAX\_CONCURRENT\_STREAMS](#SETTINGS_MAX_CONCURRENT_STREAMS) setting to limit the number of responses that can be concurrently pushed by a server. Advertising a [SETTINGS\_MAX\_CONCURRENT\_STREAMS](#SETTINGS_MAX_CONCURRENT_STREAMS) value of zero prevents the server from opening the streams necessary to push responses. However, this does not prevent the server from reserving streams using [PUSH\_PROMISE](#PUSH_PROMISE) frames, because reserved streams do not count toward the concurrent stream limit. Clients that do not wish to receive pushed resources need to reset any unwanted reserved streams or set [SETTINGS\_ENABLE\_PUSH](#SETTINGS_ENABLE_PUSH) to 0.[¶](#section-8.4.2-4)

Clients receiving a pushed response MUST validate that either the server is authoritative (see [Section 10.1](#authority)) or the proxy that provided the pushed response is configured for the corresponding request. For example, a server that offers a certificate for only the `example.com` DNS-ID (see \[[RFC6125](#RFC6125)]) is not permitted to push a response for &lt;`https://www.example.org/doc`&gt;.[¶](#section-8.4.2-5)

The response for a [PUSH\_PROMISE](#PUSH_PROMISE) stream begins with a [HEADERS](#HEADERS) frame, which immediately puts the stream into the "half-closed (remote)" state for the server and "half-closed (local)" state for the client, and ends with a frame with the END\_STREAM flag set, which places the stream in the "closed" state.[¶](#section-8.4.2-6)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
