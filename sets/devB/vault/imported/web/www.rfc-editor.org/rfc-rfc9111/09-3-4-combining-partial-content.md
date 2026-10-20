---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#09-3-4-combining-partial-content.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-09-3-4-combining-partial-content
type: reference
title: 'RFC 9111: HTTP Caching › 3. Storing Responses in Caches › 3.4. Combining Partial Content'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#09-3-4-combining-partial-content
source_hash: 6af10686f7c9ac31222c97e183763423a25d48130ef176aff666c7fdb2ade8ee
---
A response might transfer only a partial representation if the connection closed prematurely or if the request used one or more Range specifiers ([Section 14.2](https://www.rfc-editor.org/rfc/rfc9110#section-14.2) of \[[HTTP](#HTTP)]). After several such transfers, a cache might have received several ranges of the same representation. A cache MAY combine these ranges into a single stored response, and reuse that response to satisfy later requests, if they all share the same strong validator and the cache complies with the client requirements in [Section 15.3.7.3](https://www.rfc-editor.org/rfc/rfc9110#section-15.3.7.3) of \[[HTTP](#HTTP)].[¶](#section-3.4-1)

When combining the new response with one or more stored responses, a cache MUST update the stored response header fields using the header fields provided in the new response, as per [Section 3.2](#update).[¶](#section-3.4-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
