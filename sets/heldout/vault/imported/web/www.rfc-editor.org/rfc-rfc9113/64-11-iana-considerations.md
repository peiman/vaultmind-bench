---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#64-11-iana-considerations.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-64-11-iana-considerations
type: reference
title: 'RFC 9113: HTTP/2 › 11. IANA Considerations'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#64-11-iana-considerations
source_hash: 4af38bb161965a92cb700f77f7b02ca5061e40e6f2a6d3d374f7039ecf4f9c55
---
This revision of HTTP/2 marks the `HTTP2-Settings` header field and the `h2c` upgrade token, both defined in \[[RFC7540](#RFC7540)], as obsolete.[¶](#section-11-1)

[Section 11](https://www.rfc-editor.org/rfc/rfc7540#section-11) of \[[RFC7540](#RFC7540)] registered the `h2` and `h2c` ALPN identifiers along with the `PRI` HTTP method. RFC 7540 also established a registry for frame types, settings, and error codes. These registrations and registries apply to HTTP/2, but are not redefined in this document.[¶](#section-11-2)

IANA has updated references to RFC 7540 in the following registries to refer to this document: "TLS Application-Layer Protocol Negotiation (ALPN) Protocol IDs", "HTTP/2 Frame Type", "HTTP/2 Settings", "HTTP/2 Error Code", and "HTTP Method Registry". The registration of the `PRI` method has been updated to refer to [Section 3.4](#preface); all other section numbers have not changed.[¶](#section-11-3)

IANA has changed the policy on those portions of the "HTTP/2 Frame Type" and "HTTP/2 Settings" registries that were reserved for Experimental Use in RFC 7540. These portions of the registries shall operate on the same policy as the remainder of each registry.[¶](#section-11-4)

This section marks the `HTTP2-Settings` header field registered by [Section 11.5](https://www.rfc-editor.org/rfc/rfc7540#section-11.5) of \[[RFC7540](#RFC7540)] in the "Hypertext Transfer Protocol (HTTP) Field Name Registry" as obsolete. This capability has been removed: see [Section 3.1](#versioning). The registration is updated to include the details as required by [Section 18.4](https://www.rfc-editor.org/rfc/rfc9110#section-18.4) of \[[HTTP](#RFC9110)]:[¶](#section-11.1-1)

Field Name:

HTTP2-Settings[¶](#section-11.1-2.2)

Status:

obsoleted[¶](#section-11.1-2.4)

Reference:

[Section 3.2.1](https://www.rfc-editor.org/rfc/rfc7540#section-3.2.1) of \[[RFC7540](#RFC7540)][¶](#section-11.1-2.6)

Comments:

Obsolete; see [Section 11.1](#HTTP2-Settings) of this document.[¶](#section-11.1-2.8)

### 11.2. The h2c Upgrade Token

This section records the `h2c` upgrade token registered by [Section 11.8](https://www.rfc-editor.org/rfc/rfc7540#section-11.8) of \[[RFC7540](#RFC7540)] in the "Hypertext Transfer Protocol (HTTP) Upgrade Token Registry" as obsolete. This capability has been removed: see [Section 3.1](#versioning). The registration is updated as follows:[¶](#section-11.2-1)

Value:

h2c[¶](#section-11.2-2.2)

Description:

(OBSOLETE) Hypertext Transfer Protocol version 2 (HTTP/2)[¶](#section-11.2-2.4)

Expected Version Tokens:

None[¶](#section-11.2-2.6)

Reference:

[Section 3.1](#versioning) of this document[¶](#section-11.2-2.8)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
