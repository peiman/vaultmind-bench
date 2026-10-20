---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#29-appendix-b-changes-from-rfc-7234.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-29-appendix-b-changes-from-rfc-7234
type: reference
title: 'RFC 9111: HTTP Caching › Appendix B. Changes from RFC 7234'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#29-appendix-b-changes-from-rfc-7234
source_hash: a8d7c42855568d1d0f218ebfa7339a054ce497ca5a68c02f8bb07d2714e3b936
---
Handling of duplicate and conflicting cache directives has been clarified. ([Section 4.2.1](#calculating.freshness.lifetime))[¶](#appendix-B-1)

Cache invalidation of the URIs in the Location and Content-Location header fields is no longer required but is still allowed. ([Section 4.4](#invalidation))[¶](#appendix-B-2)

Cache invalidation of the URIs in the Location and Content-Location header fields is disallowed when the origin is different; previously, it was the host. ([Section 4.4](#invalidation))[¶](#appendix-B-3)

Handling invalid and multiple Age header field values has been clarified. ([Section 5.1](#field.age))[¶](#appendix-B-4)

Some cache directives defined by this specification now have stronger prohibitions against generating the quoted form of their values, since this has been found to create interoperability problems. Consumers of extension cache directives are no longer required to accept both token and quoted-string forms, but they still need to parse them properly for unknown extensions. ([Section 5.2](#field.cache-control))[¶](#appendix-B-5)

The public and private cache directives were clarified, so that they do not make responses reusable under any condition. ([Section 5.2.2](#cache-response-directive))[¶](#appendix-B-6)

The must-understand cache directive was introduced; caches are no longer required to understand the semantics of new response status codes unless it is present. ([Section 5.2.2.3](#cache-response-directive.must-understand))[¶](#appendix-B-7)

The Warning response header was obsoleted. Much of the information supported by Warning could be gleaned by examining the response, and the remaining information -- although potentially useful -- was entirely advisory. In practice, Warning was not added by caches or intermediaries. ([Section 5.5](#field.warning))[¶](#appendix-B-8)

## Acknowledgements

See Appendix "Acknowledgements" of \[[HTTP](#HTTP)], which applies to this document as well.[¶](#appendix-C-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
