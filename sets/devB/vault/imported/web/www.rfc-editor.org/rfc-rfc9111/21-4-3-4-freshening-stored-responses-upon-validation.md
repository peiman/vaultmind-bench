---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#21-4-3-4-freshening-stored-responses-upon-validation.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-21-4-3-4-freshening-stored-responses-upon-validation
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.3. Validation › 4.3.4. Freshening Stored Responses upon Validation'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#21-4-3-4-freshening-stored-responses-upon-validation
source_hash: 4bd13e8e58269942f65c0484001dddd555d453dc2099efa11a3887945f0917ef
---
When a cache receives a 304 (Not Modified) response, it needs to identify stored responses that are suitable for updating with the new information provided, and then do so.[¶](#section-4.3.4-1)

The initial set of stored responses to update are those that could have been chosen for that request -- i.e., those that meet the requirements in [Section 4](#constructing.responses.from.caches), except the last requirement to be fresh, able to be served stale, or just validated.[¶](#section-4.3.4-2)

Then, that initial set of stored responses is further filtered by the first match of:[¶](#section-4.3.4-3)

- If the new response contains one or more "strong validators" (see [Section 8.8.1](https://www.rfc-editor.org/rfc/rfc9110#section-8.8.1) of \[[HTTP](#HTTP)]), then each of those strong validators identifies a selected representation for update. All the stored responses in the initial set with one of those same strong validators are identified for update. If none of the initial set contains at least one of the same strong validators, then the cache MUST NOT use the new response to update any stored responses.[¶](#section-4.3.4-4.1)
- If the new response contains no strong validators but does contain one or more "weak validators", and those validators correspond to one of the initial set's stored responses, then the most recent of those matching stored responses is identified for update.[¶](#section-4.3.4-4.2)
- If the new response does not include any form of validator (such as where a client generates an If-Modified-Since request from a source other than the Last-Modified response header field), and there is only one stored response in the initial set, and that stored response also lacks a validator, then that stored response is identified for update.[¶](#section-4.3.4-4.3)

For each stored response identified, the cache MUST update its header fields with the header fields provided in the 304 (Not Modified) response, as per [Section 3.2](#update).[¶](#section-4.3.4-5)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
