---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#15-4-2-2-calculating-heuristic-freshness.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-15-4-2-2-calculating-heuristic-freshness
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.2. Freshness › 4.2.2. Calculating Heuristic Freshness'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#15-4-2-2-calculating-heuristic-freshness
source_hash: 2140862f1f1713ad803bf044b4642fbba083dd078867cb38994a68f43f247eeb
---
Since origin servers do not always provide explicit expiration times, a cache MAY assign a heuristic expiration time when an explicit time is not specified, employing algorithms that use other field values (such as the Last-Modified time) to estimate a plausible expiration time. This specification does not provide specific algorithms, but it does impose worst-case constraints on their results.[¶](#section-4.2.2-1)

A cache MUST NOT use heuristics to determine freshness when an explicit expiration time is present in the stored response. Because of the requirements in [Section 3](#response.cacheability), heuristics can only be used on responses without explicit freshness whose status codes are defined as "heuristically cacheable" (e.g., see [Section 15.1](https://www.rfc-editor.org/rfc/rfc9110#section-15.1) of \[[HTTP](#HTTP)]) and on responses without explicit freshness that have been marked as explicitly cacheable (e.g., with a public response directive).[¶](#section-4.2.2-2)

Note that in previous specifications, heuristically cacheable response status codes were called "cacheable by default".[¶](#section-4.2.2-3)

If the response has a Last-Modified header field ([Section 8.8.2](https://www.rfc-editor.org/rfc/rfc9110#section-8.8.2) of \[[HTTP](#HTTP)]), caches are encouraged to use a heuristic expiration value that is no more than some fraction of the interval since that time. A typical setting of this fraction might be 10%.[¶](#section-4.2.2-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
