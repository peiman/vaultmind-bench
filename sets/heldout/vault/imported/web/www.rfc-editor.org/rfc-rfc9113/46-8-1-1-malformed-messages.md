---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#46-8-1-1-malformed-messages.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-46-8-1-1-malformed-messages
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.1. HTTP Message Framing › 8.1.1. Malformed Messages'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#46-8-1-1-malformed-messages
source_hash: 440a865ab86e65175bdfd97c84b34be4fb20d8b78239e70692ff93aad854b0a9
---
A malformed request or response is one that is an otherwise valid sequence of HTTP/2 frames but is invalid due to the presence of extraneous frames, prohibited fields or pseudo-header fields, the absence of mandatory pseudo-header fields, the inclusion of uppercase field names, or invalid field names and/or values (in certain circumstances; see [Section 8.2](#HttpHeaders)).[¶](#section-8.1.1-1)

A request or response that includes message content can include a `content-length` header field. A request or response is also malformed if the value of a `content-length` header field does not equal the sum of the [DATA](#DATA) frame payload lengths that form the content, unless the message is defined as having no content. For example, 204 or 304 responses contain no content, as does the response to a HEAD request. A response that is defined to have no content, as described in [Section 6.4.1](https://www.rfc-editor.org/rfc/rfc9110#section-6.4.1) of \[[HTTP](#RFC9110)], MAY have a non-zero `content-length` header field, even though no content is included in [DATA](#DATA) frames.[¶](#section-8.1.1-2)

Intermediaries that process HTTP requests or responses (i.e., any intermediary not acting as a tunnel) MUST NOT forward a malformed request or response. Malformed requests or responses that are detected MUST be treated as a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-8.1.1-3)

For malformed requests, a server MAY send an HTTP response prior to closing or resetting the stream. Clients MUST NOT accept a malformed response.[¶](#section-8.1.1-4)

Endpoints that progressively process messages might have performed some processing before identifying a request or response as malformed. For instance, it might be possible to generate an informational or 404 status code without having received a complete request. Similarly, intermediaries might forward incomplete messages before detecting errors. A server MAY generate a final response before receiving an entire request when the response does not depend on the remainder of the request being correct.[¶](#section-8.1.1-5)

These requirements are intended to protect against several types of common attacks against HTTP; they are deliberately strict because being permissive can expose implementations to these vulnerabilities.[¶](#section-8.1.1-6)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
