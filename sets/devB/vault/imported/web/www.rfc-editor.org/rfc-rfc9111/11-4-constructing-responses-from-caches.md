---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#11-4-constructing-responses-from-caches.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-11-4-constructing-responses-from-caches
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#11-4-constructing-responses-from-caches
source_hash: 7ef00ed5165f013c6b12149a3eb1e6774a3715d5f8fc3189de615d066026a08c
---
When presented with a request, a cache MUST NOT reuse a stored response unless:[¶](#section-4-1)

- the presented target URI ([Section 7.1](https://www.rfc-editor.org/rfc/rfc9110#section-7.1) of \[[HTTP](#HTTP)]) and that of the stored response match, and[¶](#section-4-2.1.1)
- the request method associated with the stored response allows it to be used for the presented request, and[¶](#section-4-2.2.1)
- request header fields nominated by the stored response (if any) match those presented (see [Section 4.1](#caching.negotiated.responses)), and[¶](#section-4-2.3.1)
- the stored response does not contain the no-cache directive ([Section 5.2.2.4](#cache-response-directive.no-cache)), unless it is successfully validated ([Section 4.3](#validation.model)), and[¶](#section-4-2.4.1)
- the stored response is one of the following:[¶](#section-4-2.5.1)
  
  - fresh (see [Section 4.2](#expiration.model)), or[¶](#section-4-2.5.2.1)
  - allowed to be served stale (see [Section 4.2.4](#serving.stale.responses)), or[¶](#section-4-2.5.2.2)
  - successfully validated (see [Section 4.3](#validation.model)).[¶](#section-4-2.5.2.3)

Note that a cache extension can override any of the requirements listed; see [Section 5.2.3](#cache.control.extensions).[¶](#section-4-3)

When a stored response is used to satisfy a request without validation, a cache MUST generate an [Age](#field.age) header field ([Section 5.1](#field.age)), replacing any present in the response with a value equal to the stored response's current\_age; see [Section 4.2.3](#age.calculations).[¶](#section-4-4)

A cache MUST write through requests with methods that are unsafe ([Section 9.2.1](https://www.rfc-editor.org/rfc/rfc9110#section-9.2.1) of \[[HTTP](#HTTP)]) to the origin server; i.e., a cache is not allowed to generate a reply to such a request before having forwarded the request and having received a corresponding response.[¶](#section-4-5)

Also, note that unsafe requests might invalidate already-stored responses; see [Section 4.4](#invalidation).[¶](#section-4-6)

A cache can use a response that is stored or storable to satisfy multiple requests, provided that it is allowed to reuse that response for the requests in question. This enables a cache to "collapse requests" -- or combine multiple incoming requests into a single forward request upon a cache miss -- thereby reducing load on the origin server and network. Note, however, that if the cache cannot use the returned response for some or all of the collapsed requests, it will need to forward the requests in order to satisfy them, potentially introducing additional latency.[¶](#section-4-7)

When more than one suitable response is stored, a cache MUST use the most recent one (as determined by the Date header field). It can also forward the request with "Cache-Control: max-age=0" or "Cache-Control: no-cache" to disambiguate which response to use.[¶](#section-4-8)

A cache without a clock ([Section 5.6.7](https://www.rfc-editor.org/rfc/rfc9110#section-5.6.7) of \[[HTTP](#HTTP)]) MUST revalidate stored responses upon every use.[¶](#section-4-9)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
