---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#19-4-3-2-handling-a-received-validation-request.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-19-4-3-2-handling-a-received-validation-request
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.3. Validation › 4.3.2. Handling a Received Validation Request'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#19-4-3-2-handling-a-received-validation-request
source_hash: 89ff30857e4b1288a975be0cd420f592016e3136ef9a05acff5a718b893762d2
---
Each client in the request chain may have its own cache, so it is common for a cache at an intermediary to receive conditional requests from other (outbound) caches. Likewise, some user agents make use of conditional requests to limit data transfers to recently modified representations or to complete the transfer of a partially retrieved representation.[¶](#section-4.3.2-1)

If a cache receives a request that can be satisfied by reusing a stored 200 (OK) or 206 (Partial Content) response, as per [Section 4](#constructing.responses.from.caches), the cache SHOULD evaluate any applicable conditional header field preconditions received in that request with respect to the corresponding validators contained within the stored response.[¶](#section-4.3.2-2)

A cache MUST NOT evaluate conditional header fields that only apply to an origin server, occur in a request with semantics that cannot be satisfied with a cached response, or occur in a request with a target resource for which it has no stored responses; such preconditions are likely intended for some other (inbound) server.[¶](#section-4.3.2-3)

The proper evaluation of conditional requests by a cache depends on the received precondition header fields and their precedence. In summary, the If-Match and If-Unmodified-Since conditional header fields are not applicable to a cache, and If-None-Match takes precedence over If-Modified-Since. See [Section 13.2.2](https://www.rfc-editor.org/rfc/rfc9110#section-13.2.2) of \[[HTTP](#HTTP)] for a complete specification of precondition precedence.[¶](#section-4.3.2-4)

A request containing an If-None-Match header field ([Section 13.1.2](https://www.rfc-editor.org/rfc/rfc9110#section-13.1.2) of \[[HTTP](#HTTP)]) indicates that the client wants to validate one or more of its own stored responses in comparison to the stored response chosen by the cache (as per [Section 4](#constructing.responses.from.caches)).[¶](#section-4.3.2-5)

If an If-None-Match header field is not present, a request containing an If-Modified-Since header field ([Section 13.1.3](https://www.rfc-editor.org/rfc/rfc9110#section-13.1.3) of \[[HTTP](#HTTP)]) indicates that the client wants to validate one or more of its own stored responses by modification date.[¶](#section-4.3.2-6)

If a request contains an If-Modified-Since header field and the Last-Modified header field is not present in a stored response, a cache SHOULD use the stored response's Date field value (or, if no Date field is present, the time that the stored response was received) to evaluate the conditional.[¶](#section-4.3.2-7)

A cache that implements partial responses to range requests, as defined in [Section 14.2](https://www.rfc-editor.org/rfc/rfc9110#section-14.2) of \[[HTTP](#HTTP)], also needs to evaluate a received If-Range header field ([Section 13.1.5](https://www.rfc-editor.org/rfc/rfc9110#section-13.1.5) of \[[HTTP](#HTTP)]) with respect to the cache's chosen response.[¶](#section-4.3.2-8)

When a cache decides to forward a request to revalidate its own stored responses for a request that contains an If-None-Match list of entity tags, the cache MAY combine the received list with a list of entity tags from its own stored set of responses (fresh or stale) and send the union of the two lists as a replacement If-None-Match header field value in the forwarded request. If a stored response contains only partial content, the cache MUST NOT include its entity tag in the union unless the request is for a range that would be fully satisfied by that partial stored response. If the response to the forwarded request is 304 (Not Modified) and has an ETag field value with an entity tag that is not in the client's list, the cache MUST generate a 200 (OK) response for the client by reusing its corresponding stored response, as updated by the 304 response metadata ([Section 4.3.4](#freshening.responses)).[¶](#section-4.3.2-9)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
