---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#58-10-4-cacheability-of-pushed-responses.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-58-10-4-cacheability-of-pushed-responses
type: reference
title: 'RFC 9113: HTTP/2 › 10. Security Considerations › 10.4. Cacheability of Pushed Responses'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#58-10-4-cacheability-of-pushed-responses
source_hash: 08a69d88014040716db9b829e9b1b5ec16678e165ebd30f0523bd3c0a8ea5056
---
Pushed responses do not have an explicit request from the client; the request is provided by the server in the [PUSH\_PROMISE](#PUSH_PROMISE) frame.[¶](#section-10.4-1)

Caching responses that are pushed is possible based on the guidance provided by the origin server in the Cache-Control header field. However, this can cause issues if a single server hosts more than one tenant. For example, a server might offer multiple users each a small portion of its URI space.[¶](#section-10.4-2)

Where multiple tenants share space on the same server, that server MUST ensure that tenants are not able to push representations of resources that they do not have authority over. Failure to enforce this would allow a tenant to provide a representation that would be served out of cache, overriding the actual representation that the authoritative tenant provides.[¶](#section-10.4-3)

Pushed responses for which an origin server is not authoritative (see [Section 10.1](#authority)) MUST NOT be used or cached.[¶](#section-10.4-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
