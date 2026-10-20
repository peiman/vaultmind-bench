---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#06-3-storing-responses-in-caches.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-06-3-storing-responses-in-caches
type: reference
title: 'RFC 9111: HTTP Caching › 3. Storing Responses in Caches'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#06-3-storing-responses-in-caches
source_hash: 98ad26f161f317fed9d0de456eeffc911ec095dc38fefb93ab5ed3adb770fe67
---
A cache MUST NOT store a response to a request unless:[¶](#section-3-1)

- the request method is understood by the cache;[¶](#section-3-2.1.1)
- the response status code is final (see [Section 15](https://www.rfc-editor.org/rfc/rfc9110#section-15) of \[[HTTP](#HTTP)]);[¶](#section-3-2.2.1)
- if the response status code is 206 or 304, or the must-understand cache directive (see [Section 5.2.2.3](#cache-response-directive.must-understand)) is present: the cache understands the response status code;[¶](#section-3-2.3.1)
- the no-store cache directive is not present in the response (see [Section 5.2.2.5](#cache-response-directive.no-store));[¶](#section-3-2.4.1)
- if the cache is shared: the private response directive is either not present or allows a shared cache to store a modified response; see [Section 5.2.2.7](#cache-response-directive.private));[¶](#section-3-2.5.1)
- if the cache is shared: the Authorization header field is not present in the request (see [Section 11.6.2](https://www.rfc-editor.org/rfc/rfc9110#section-11.6.2) of \[[HTTP](#HTTP)]) or a response directive is present that explicitly allows shared caching (see [Section 3.5](#caching.authenticated.responses)); and[¶](#section-3-2.6.1)
- the response contains at least one of the following:[¶](#section-3-2.7.1)
  
  - a public response directive (see [Section 5.2.2.9](#cache-response-directive.public));[¶](#section-3-2.7.2.1)
  - a private response directive, if the cache is not shared (see [Section 5.2.2.7](#cache-response-directive.private));[¶](#section-3-2.7.2.2)
  - an [Expires](#field.expires) header field (see [Section 5.3](#field.expires));[¶](#section-3-2.7.2.3)
  - a max-age response directive (see [Section 5.2.2.1](#cache-response-directive.max-age));[¶](#section-3-2.7.2.4)
  - if the cache is shared: an s-maxage response directive (see [Section 5.2.2.10](#cache-response-directive.s-maxage));[¶](#section-3-2.7.2.5)
  - a cache extension that allows it to be cached (see [Section 5.2.3](#cache.control.extensions)); or[¶](#section-3-2.7.2.6)
  - a status code that is defined as heuristically cacheable (see [Section 4.2.2](#heuristic.freshness)).[¶](#section-3-2.7.2.7)

Note that a cache extension can override any of the requirements listed; see [Section 5.2.3](#cache.control.extensions).[¶](#section-3-3)

In this context, a cache has "understood" a request method or a response status code if it recognizes it and implements all specified caching-related behavior.[¶](#section-3-4)

Note that, in normal operation, some caches will not store a response that has neither a cache validator nor an explicit expiration time, as such responses are not usually useful to store. However, caches are not prohibited from storing such responses.[¶](#section-3-5)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
