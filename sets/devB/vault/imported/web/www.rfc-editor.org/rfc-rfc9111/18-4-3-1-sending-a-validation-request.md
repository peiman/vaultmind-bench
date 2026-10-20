---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#18-4-3-1-sending-a-validation-request.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-18-4-3-1-sending-a-validation-request
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.3. Validation › 4.3.1. Sending a Validation Request'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#18-4-3-1-sending-a-validation-request
source_hash: a9779c33ce6d882d8f4ca063f4da60c546c9931fe10a9e508227ba13d5469918
---
When generating a conditional request for validation, a cache either starts with a request it is attempting to satisfy or -- if it is initiating the request independently -- synthesizes a request using a stored response by copying the method, target URI, and request header fields identified by the Vary header field ([Section 4.1](#caching.negotiated.responses)).[¶](#section-4.3.1-1)

It then updates that request with one or more precondition header fields. These contain validator metadata sourced from a stored response(s) that has the same URI. Typically, this will include only the stored response(s) that has the same cache key, although a cache is allowed to validate a response that it cannot choose with the request header fields it is sending (see [Section 4.1](#caching.negotiated.responses)).[¶](#section-4.3.1-2)

The precondition header fields are then compared by recipients to determine whether any stored response is equivalent to a current representation of the resource.[¶](#section-4.3.1-3)

One such validator is the timestamp given in a Last-Modified header field ([Section 8.8.2](https://www.rfc-editor.org/rfc/rfc9110#section-8.8.2) of \[[HTTP](#HTTP)]), which can be used in an If-Modified-Since header field for response validation, or in an If-Unmodified-Since or If-Range header field for representation selection (i.e., the client is referring specifically to a previously obtained representation with that timestamp).[¶](#section-4.3.1-4)

Another validator is the entity tag given in an ETag field ([Section 8.8.3](https://www.rfc-editor.org/rfc/rfc9110#section-8.8.3) of \[[HTTP](#HTTP)]). One or more entity tags, indicating one or more stored responses, can be used in an If-None-Match header field for response validation, or in an If-Match or If-Range header field for representation selection (i.e., the client is referring specifically to one or more previously obtained representations with the listed entity tags).[¶](#section-4.3.1-5)

When generating a conditional request for validation, a cache:[¶](#section-4.3.1-6)

- MUST send the relevant entity tags (using If-Match, If-None-Match, or If-Range) if the entity tags were provided in the stored response(s) being validated.[¶](#section-4.3.1-7.1)
- SHOULD send the Last-Modified value (using If-Modified-Since) if the request is not for a subrange, a single stored response is being validated, and that response contains a Last-Modified value.[¶](#section-4.3.1-7.2)
- MAY send the Last-Modified value (using If-Unmodified-Since or If-Range) if the request is for a subrange, a single stored response is being validated, and that response contains only a Last-Modified value (not an entity tag).[¶](#section-4.3.1-7.3)

In most cases, both validators are generated in cache validation requests, even when entity tags are clearly superior, to allow old intermediaries that do not understand entity tag preconditions to respond appropriately.[¶](#section-4.3.1-8)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
