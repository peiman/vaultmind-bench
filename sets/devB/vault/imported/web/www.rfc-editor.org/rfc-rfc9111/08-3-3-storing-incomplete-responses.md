---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#08-3-3-storing-incomplete-responses.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-08-3-3-storing-incomplete-responses
type: reference
title: 'RFC 9111: HTTP Caching › 3. Storing Responses in Caches › 3.3. Storing Incomplete Responses'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#08-3-3-storing-incomplete-responses
source_hash: a9c4a5ad0ffa3efdff371c0a8286f9ec758a9c5165ca1f76b943aea218abd91a
---
If the request method is GET, the response status code is 200 (OK), and the entire response header section has been received, a cache MAY store a response that is not complete ([Section 6.1](https://www.rfc-editor.org/rfc/rfc9110#section-6.1) of \[[HTTP](#HTTP)]) provided that the stored response is recorded as being incomplete. Likewise, a 206 (Partial Content) response MAY be stored as if it were an incomplete 200 (OK) response. However, a cache MUST NOT store incomplete or partial-content responses if it does not support the Range and Content-Range header fields or if it does not understand the range units used in those fields.[¶](#section-3.3-1)

A cache MAY complete a stored incomplete response by making a subsequent range request ([Section 14.2](https://www.rfc-editor.org/rfc/rfc9110#section-14.2) of \[[HTTP](#HTTP)]) and combining the successful response with the stored response, as defined in [Section 3.4](#combining.responses). A cache MUST NOT use an incomplete response to answer requests unless the response has been made complete, or the request is partial and specifies a range wholly within the incomplete response. A cache MUST NOT send a partial response to a client without explicitly marking it using the 206 (Partial Content) status code.[¶](#section-3.3-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
