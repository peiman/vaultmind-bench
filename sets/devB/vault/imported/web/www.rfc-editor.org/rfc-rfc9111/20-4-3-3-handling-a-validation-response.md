---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#20-4-3-3-handling-a-validation-response.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-20-4-3-3-handling-a-validation-response
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.3. Validation › 4.3.3. Handling a Validation Response'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#20-4-3-3-handling-a-validation-response
source_hash: f18a7e56656fe1dbeb8f5741bdfb13305d53704094f5a451e3e398ab8806d143
---
Cache handling of a response to a conditional request depends upon its status code:[¶](#section-4.3.3-1)

- A 304 (Not Modified) response status code indicates that the stored response can be updated and reused; see [Section 4.3.4](#freshening.responses).[¶](#section-4.3.3-2.1)
- A full response (i.e., one containing content) indicates that none of the stored responses nominated in the conditional request are suitable. Instead, the cache MUST use the full response to satisfy the request. The cache MAY store such a full response, subject to its constraints (see [Section 3](#response.cacheability)).[¶](#section-4.3.3-2.2)
- However, if a cache receives a 5xx (Server Error) response while attempting to validate a response, it can either forward this response to the requesting client or act as if the server failed to respond. In the latter case, the cache can send a previously stored response, subject to its constraints on doing so (see [Section 4.2.4](#serving.stale.responses)), or retry the validation request.[¶](#section-4.3.3-2.3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
