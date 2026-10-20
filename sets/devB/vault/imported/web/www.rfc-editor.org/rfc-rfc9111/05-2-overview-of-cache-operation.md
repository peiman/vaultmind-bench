---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#05-2-overview-of-cache-operation.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-05-2-overview-of-cache-operation
type: reference
title: 'RFC 9111: HTTP Caching › 2. Overview of Cache Operation'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#05-2-overview-of-cache-operation
source_hash: 9d31967f857259fb21ea5cba2ce89a2c79706fd76430ab9181dab6e40953e5b2
---
Proper cache operation preserves the semantics of HTTP transfers while reducing the transmission of information already held in the cache. See [Section 3](https://www.rfc-editor.org/rfc/rfc9110#section-3) of \[[HTTP](#HTTP)] for the general terminology and core concepts of HTTP.[¶](#section-2-1)

Although caching is an entirely OPTIONAL feature of HTTP, it can be assumed that reusing a cached response is desirable and that such reuse is the default behavior when no requirement or local configuration prevents it. Therefore, HTTP cache requirements are focused on preventing a cache from either storing a non-reusable response or reusing a stored response inappropriately, rather than mandating that caches always store and reuse particular responses.[¶](#section-2-2)

The "cache key" is the information a cache uses to choose a response and is composed from, at a minimum, the request method and target URI used to retrieve the stored response; the method determines under which circumstances that response can be used to satisfy a subsequent request. However, many HTTP caches in common use today only cache GET responses and therefore only use the URI as the cache key.[¶](#section-2-3)

A cache might store multiple responses for a request target that is subject to content negotiation. Caches differentiate these responses by incorporating some of the original request's header fields into the cache key as well, using information in the Vary response header field, as per [Section 4.1](#caching.negotiated.responses).[¶](#section-2-4)

Caches might incorporate additional material into the cache key. For example, user agent caches might include the referring site's identity, thereby "double keying" the cache to avoid some privacy risks (see [Section 7.2](#security.timing)).[¶](#section-2-5)

Most commonly, caches store the successful result of a retrieval request: i.e., a 200 (OK) response to a GET request, which contains a representation of the target resource ([Section 9.3.1](https://www.rfc-editor.org/rfc/rfc9110#section-9.3.1) of \[[HTTP](#HTTP)]). However, it is also possible to store redirects, negative results (e.g., 404 (Not Found)), incomplete results (e.g., 206 (Partial Content)), and responses to methods other than GET if the method's definition allows such caching and defines something suitable for use as a cache key.[¶](#section-2-6)

A cache is "disconnected" when it cannot contact the origin server or otherwise find a forward path for a request. A disconnected cache can serve stale responses in some circumstances ([Section 4.2.4](#serving.stale.responses)).[¶](#section-2-7)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
