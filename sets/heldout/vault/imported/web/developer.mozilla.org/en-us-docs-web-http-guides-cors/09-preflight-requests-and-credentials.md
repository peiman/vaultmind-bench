---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#09-preflight-requests-and-credentials.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-09-preflight-requests-and-credentials
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Requests with credentials › Preflight requests and credentials
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#09-preflight-requests-and-credentials
source_hash: 6a04d55a1c6dabad08a15fd9833e56f82a69832dee4d29b621a0bffbdbdfd64d
---
CORS-preflight requests must never include credentials. The *response* to a preflight request must specify `Access-Control-Allow-Credentials: true` to indicate that the actual request can be made with credentials.

**Note:** Some enterprise authentication services require that TLS client certificates be sent in preflight requests, in contravention of the [Fetch](https://fetch.spec.whatwg.org/#cors-protocol-and-credentials "External link (opens in new tab)") specification.

Firefox 87 allows this non-compliant behavior to be enabled by setting the preference: `network.cors_preflight.allow_client_cert` to `true` ([Firefox bug 1511151](https://bugzil.la/1511151 "External link (opens in new tab)")). Chromium-based browsers currently always send TLS client certificates in CORS preflight requests ([Chrome bug 775438](https://crbug.com/775438 "External link (opens in new tab)")).

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
