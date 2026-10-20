---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#07-3-1-storing-header-and-trailer-fields.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-07-3-1-storing-header-and-trailer-fields
type: reference
title: 'RFC 9111: HTTP Caching › 3. Storing Responses in Caches › 3.1. Storing Header and Trailer Fields'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#07-3-1-storing-header-and-trailer-fields
source_hash: fb4991e47a96317eca502267ecdd824a790fc984a6901793e3d3ad3b09fde476
---
Caches MUST include all received response header fields -- including unrecognized ones -- when storing a response; this assures that new HTTP header fields can be successfully deployed. However, the following exceptions are made:[¶](#section-3.1-1)

- The Connection header field and fields whose names are listed in it are required by [Section 7.6.1](https://www.rfc-editor.org/rfc/rfc9110#section-7.6.1) of \[[HTTP](#HTTP)] to be removed before forwarding the message. This MAY be implemented by doing so before storage.[¶](#section-3.1-2.1)
- Likewise, some fields' semantics require them to be removed before forwarding the message, and this MAY be implemented by doing so before storage; see [Section 7.6.1](https://www.rfc-editor.org/rfc/rfc9110#section-7.6.1) of \[[HTTP](#HTTP)] for some examples.[¶](#section-3.1-2.2)
- The no-cache ([Section 5.2.2.4](#cache-response-directive.no-cache)) and private ([Section 5.2.2.7](#cache-response-directive.private)) cache directives can have arguments that prevent storage of header fields by all caches and shared caches, respectively.[¶](#section-3.1-2.3)
- Header fields that are specific to the proxy that a cache uses when forwarding a request MUST NOT be stored, unless the cache incorporates the identity of the proxy into the cache key. Effectively, this is limited to Proxy-Authenticate ([Section 11.7.1](https://www.rfc-editor.org/rfc/rfc9110#section-11.7.1) of \[[HTTP](#HTTP)]), Proxy-Authentication-Info ([Section 11.7.3](https://www.rfc-editor.org/rfc/rfc9110#section-11.7.3) of \[[HTTP](#HTTP)]), and Proxy-Authorization ([Section 11.7.2](https://www.rfc-editor.org/rfc/rfc9110#section-11.7.2) of \[[HTTP](#HTTP)]).[¶](#section-3.1-2.4)

Caches MAY either store trailer fields separate from header fields or discard them. Caches MUST NOT combine trailer fields with header fields.[¶](#section-3.1-3)

Caches are required to update a stored response's header fields from another (typically newer) response in several situations; for example, see Sections [3.4](#combining.responses), [4.3.4](#freshening.responses), and [4.3.5](#head.effects).[¶](#section-3.2-1)

When doing so, the cache MUST add each header field in the provided response to the stored response, replacing field values that are already present, with the following exceptions:[¶](#section-3.2-2)

- Header fields excepted from storage in [Section 3.1](#storing.fields),[¶](#section-3.2-3.1)
- Header fields that the cache's stored response depends upon, as described below,[¶](#section-3.2-3.2)
- Header fields that are automatically processed and removed by the recipient, as described below, and[¶](#section-3.2-3.3)
- The Content-Length header field.[¶](#section-3.2-3.4)

In some cases, caches (especially in user agents) store the results of processing the received response, rather than the response itself, and updating header fields that affect that processing can result in inconsistent behavior and security issues. Caches in this situation MAY omit these header fields from updating stored responses on an exceptional basis but SHOULD limit such omission to those fields necessary to assure integrity of the stored response.[¶](#section-3.2-4)

For example, a browser might decode the content coding of a response while it is being received, creating a disconnect between the data it has stored and the response's original metadata. Updating that stored metadata with a different Content-Encoding header field would be problematic. Likewise, a browser might store a post-parse HTML tree rather than the content received in the response; updating the Content-Type header field would not be workable in this case because any assumptions about the format made in parsing would now be invalid.[¶](#section-3.2-5)

Furthermore, some fields are automatically processed and removed by the HTTP implementation, such as the Content-Range header field. Implementations MAY automatically omit such header fields from updates, even when the processing does not actually occur.[¶](#section-3.2-6)

Note that the Content-* prefix is not a signal that a header field is omitted from update; it is a convention for MIME header fields, not HTTP.[¶](#section-3.2-7)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
