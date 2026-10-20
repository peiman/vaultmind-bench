---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#14-4-2-1-calculating-freshness-lifetime.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-14-4-2-1-calculating-freshness-lifetime
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.2. Freshness › 4.2.1. Calculating Freshness Lifetime'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#14-4-2-1-calculating-freshness-lifetime
source_hash: e7b288ddd417fccb11d1ffb2726e7540e41dddf08bd8c2ac838355e776685ea7
---
A cache can calculate the freshness lifetime (denoted as freshness\_lifetime) of a response by evaluating the following rules and using the first match:[¶](#section-4.2.1-1)

- If the cache is shared and the s-maxage response directive ([Section 5.2.2.10](#cache-response-directive.s-maxage)) is present, use its value, or[¶](#section-4.2.1-2.1)
- If the max-age response directive ([Section 5.2.2.1](#cache-response-directive.max-age)) is present, use its value, or[¶](#section-4.2.1-2.2)
- If the [Expires](#field.expires) response header field ([Section 5.3](#field.expires)) is present, use its value minus the value of the Date response header field (using the time the message was received if it is not present, as per [Section 6.6.1](https://www.rfc-editor.org/rfc/rfc9110#section-6.6.1) of \[[HTTP](#HTTP)]), or[¶](#section-4.2.1-2.3)
- Otherwise, no explicit expiration time is present in the response. A heuristic freshness lifetime might be applicable; see [Section 4.2.2](#heuristic.freshness).[¶](#section-4.2.1-2.4)

Note that this calculation is intended to reduce clock skew by using the clock information provided by the origin server whenever possible.[¶](#section-4.2.1-3)

When there is more than one value present for a given directive (e.g., two [Expires](#field.expires) header field lines or multiple Cache-Control: max-age directives), either the first occurrence should be used or the response should be considered stale. If directives conflict (e.g., both max-age and no-cache are present), the most restrictive directive should be honored. Caches are encouraged to consider responses that have invalid freshness information (e.g., a max-age directive with non-integer content) to be stale.[¶](#section-4.2.1-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
