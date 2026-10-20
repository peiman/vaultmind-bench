---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#17-4-2-4-serving-stale-responses.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-17-4-2-4-serving-stale-responses
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.2. Freshness › 4.2.4. Serving Stale Responses'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#17-4-2-4-serving-stale-responses
source_hash: 063d54eea1d6151d2feffc1bb587b8cca05fad5cf8e8a100edf1c0683cf56b25
---
A "stale" response is one that either has explicit expiry information or is allowed to have heuristic expiry calculated, but is not fresh according to the calculations in [Section 4.2](#expiration.model).[¶](#section-4.2.4-1)

A cache MUST NOT generate a stale response if it is prohibited by an explicit in-protocol directive (e.g., by a no-cache response directive, a must-revalidate response directive, or an applicable s-maxage or proxy-revalidate response directive; see [Section 5.2.2](#cache-response-directive)).[¶](#section-4.2.4-2)

A cache MUST NOT generate a stale response unless it is disconnected or doing so is explicitly permitted by the client or origin server (e.g., by the max-stale request directive in [Section 5.2.1](#cache-request-directive), extension directives such as those defined in \[[RFC5861](#RFC5861)], or configuration in accordance with an out-of-band contract).[¶](#section-4.2.4-3)

### 4.3. Validation

When a cache has one or more stored responses for a requested URI, but cannot serve any of them (e.g., because they are not fresh, or one cannot be chosen; see [Section 4.1](#caching.negotiated.responses)), it can use the conditional request mechanism ([Section 13](https://www.rfc-editor.org/rfc/rfc9110#section-13) of \[[HTTP](#HTTP)]) in the forwarded request to give the next inbound server an opportunity to choose a valid stored response to use, updating the stored metadata in the process, or to replace the stored response(s) with a new response. This process is known as "validating" or "revalidating" the stored response.[¶](#section-4.3-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
