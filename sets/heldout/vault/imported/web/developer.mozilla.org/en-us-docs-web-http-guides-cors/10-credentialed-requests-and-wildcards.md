---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#10-credentialed-requests-and-wildcards.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-10-credentialed-requests-and-wildcards
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Requests with credentials › Credentialed requests and wildcards
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#10-credentialed-requests-and-wildcards
source_hash: 619e206ce5f70d5fef34311e261575df7d935e3875fb04ed55feaadd74841fe3
---
When responding to a credentialed request:

- The server **must not** specify the `*` wildcard for the `Access-Control-Allow-Origin` response-header value, but must instead specify an explicit origin; for example: `Access-Control-Allow-Origin: https://example.com`
- The server **must not** specify the `*` wildcard for the `Access-Control-Allow-Headers` response-header value, but must instead specify an explicit list of header names; for example, `Access-Control-Allow-Headers: X-PINGOTHER, Content-Type`
- The server **must not** specify the `*` wildcard for the `Access-Control-Allow-Methods` response-header value, but must instead specify an explicit list of method names; for example, `Access-Control-Allow-Methods: POST, GET`
- The server **must not** specify the `*` wildcard for the `Access-Control-Expose-Headers` response-header value, but must instead specify an explicit list of header names; for example, `Access-Control-Expose-Headers: Content-Encoding, Kuma-Revision`

If a request includes a credential (most commonly a `Cookie` header) and the response includes an `Access-Control-Allow-Origin: *` header (that is, with the wildcard), the browser will block access to the response, and report a CORS error in the devtools console.

But if a request does include a credential (like the `Cookie` header) and the response includes an actual origin rather than the wildcard (like, for example, `Access-Control-Allow-Origin: https://example.com`), then the browser will allow access to the response from the specified origin.

Also note that any `Set-Cookie` response header in a response would not set a cookie if the `Access-Control-Allow-Origin` value in that response is the `*` wildcard rather an actual origin.

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
