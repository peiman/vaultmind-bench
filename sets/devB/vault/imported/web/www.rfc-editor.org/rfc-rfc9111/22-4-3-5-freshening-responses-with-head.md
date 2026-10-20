---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#22-4-3-5-freshening-responses-with-head.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-22-4-3-5-freshening-responses-with-head
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.3. Validation › 4.3.5. Freshening Responses with HEAD'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#22-4-3-5-freshening-responses-with-head
source_hash: 4ff632d087eb7efa01df2136ee59dbd99534f34a5249dfae981c23ce31509385
---
A response to the HEAD method is identical to what an equivalent request made with a GET would have been, without sending the content. This property of HEAD responses can be used to invalidate or update a cached GET response if the more efficient conditional GET request mechanism is not available (due to no validators being present in the stored response) or if transmission of the content is not desired even if it has changed.[¶](#section-4.3.5-1)

When a cache makes an inbound HEAD request for a target URI and receives a 200 (OK) response, the cache SHOULD update or invalidate each of its stored GET responses that could have been chosen for that request (see [Section 4.1](#caching.negotiated.responses)).[¶](#section-4.3.5-2)

For each of the stored responses that could have been chosen, if the stored response and HEAD response have matching values for any received validator fields (ETag and Last-Modified) and, if the HEAD response has a Content-Length header field, the value of Content-Length matches that of the stored response, the cache SHOULD update the stored response as described below; otherwise, the cache SHOULD consider the stored response to be stale.[¶](#section-4.3.5-3)

If a cache updates a stored response with the metadata provided in a HEAD response, the cache MUST use the header fields provided in the HEAD response to update the stored response (see [Section 3.2](#update)).[¶](#section-4.3.5-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
