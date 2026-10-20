---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#12-4-1-calculating-cache-keys-with-the-vary-header-fi.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-12-4-1-calculating-cache-keys-with-the-vary-header-fi
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.1. Calculating Cache Keys with the Vary Header Field'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#12-4-1-calculating-cache-keys-with-the-vary-header-fi
source_hash: aa370324b28f2c6be694f8328422dfe0d160914acf4abfcec705ca54a8612d2d
---
When a cache receives a request that can be satisfied by a stored response and that stored response contains a Vary header field ([Section 12.5.5](https://www.rfc-editor.org/rfc/rfc9110#section-12.5.5) of \[[HTTP](#HTTP)]), the cache MUST NOT use that stored response without revalidation unless all the presented request header fields nominated by that Vary field value match those fields in the original request (i.e., the request that caused the cached response to be stored).[¶](#section-4.1-1)

The header fields from two requests are defined to match if and only if those in the first request can be transformed to those in the second request by applying any of the following:[¶](#section-4.1-2)

- adding or removing whitespace, where allowed in the header field's syntax[¶](#section-4.1-3.1)
- combining multiple header field lines with the same field name (see [Section 5.2](https://www.rfc-editor.org/rfc/rfc9110#section-5.2) of \[[HTTP](#HTTP)])[¶](#section-4.1-3.2)
- normalizing both header field values in a way that is known to have identical semantics, according to the header field's specification (e.g., reordering field values when order is not significant; case-normalization, where values are defined to be case-insensitive)[¶](#section-4.1-3.3)

If (after any normalization that might take place) a header field is absent from a request, it can only match another request if it is also absent there.[¶](#section-4.1-4)

A stored response with a Vary header field value containing a member "\*" always fails to match.[¶](#section-4.1-5)

If multiple stored responses match, the cache will need to choose one to use. When a nominated request header field has a known mechanism for ranking preference (e.g., qvalues on Accept and similar request header fields), that mechanism MAY be used to choose a preferred response. If such a mechanism is not available, or leads to equally preferred responses, the most recent response (as determined by the Date header field) is chosen, as per [Section 4](#constructing.responses.from.caches).[¶](#section-4.1-6)

Some resources mistakenly omit the Vary header field from their default response (i.e., the one sent when the request does not express any preferences), with the effect of choosing it for subsequent requests to that resource even when more preferable responses are available. When a cache has multiple stored responses for a target URI and one or more omits the Vary header field, the cache SHOULD choose the most recent (see [Section 4.2.3](#age.calculations)) stored response with a valid Vary field value.[¶](#section-4.1-7)

If no stored response matches, the cache cannot satisfy the presented request. Typically, the request is forwarded to the origin server, potentially with preconditions added to describe what responses the cache has already stored ([Section 4.3](#validation.model)).[¶](#section-4.1-8)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
