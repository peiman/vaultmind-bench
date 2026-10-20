---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#23-4-4-invalidating-stored-responses.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-23-4-4-invalidating-stored-responses
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.4. Invalidating Stored Responses'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#23-4-4-invalidating-stored-responses
source_hash: a7a5ca21130add4d43b9c60163053130abca494317b1e88302a163e53d6c78ed
---
Because unsafe request methods ([Section 9.2.1](https://www.rfc-editor.org/rfc/rfc9110#section-9.2.1) of \[[HTTP](#HTTP)]) such as PUT, POST, or DELETE have the potential for changing state on the origin server, intervening caches are required to invalidate stored responses to keep their contents up to date.[¶](#section-4.4-1)

A cache MUST invalidate the target URI ([Section 7.1](https://www.rfc-editor.org/rfc/rfc9110#section-7.1) of \[[HTTP](#HTTP)]) when it receives a non-error status code in response to an unsafe request method (including methods whose safety is unknown).[¶](#section-4.4-2)

A cache MAY invalidate other URIs when it receives a non-error status code in response to an unsafe request method (including methods whose safety is unknown). In particular, the URI(s) in the Location and Content-Location response header fields (if present) are candidates for invalidation; other URIs might be discovered through mechanisms not specified in this document. However, a cache MUST NOT trigger an invalidation under these conditions if the origin ([Section 4.3.1](https://www.rfc-editor.org/rfc/rfc9110#section-4.3.1) of \[[HTTP](#HTTP)]) of the URI to be invalidated differs from that of the target URI ([Section 7.1](https://www.rfc-editor.org/rfc/rfc9110#section-7.1) of \[[HTTP](#HTTP)]). This helps prevent denial-of-service attacks.[¶](#section-4.4-3)

"Invalidate" means that the cache will either remove all stored responses whose target URI matches the given URI or mark them as "invalid" and in need of a mandatory validation before they can be sent in response to a subsequent request.[¶](#section-4.4-4)

A "non-error response" is one with a 2xx (Successful) or 3xx (Redirection) status code.[¶](#section-4.4-5)

Note that this does not guarantee that all appropriate responses are invalidated globally; a state-changing request would only invalidate responses in the caches it travels through.[¶](#section-4.4-6)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
