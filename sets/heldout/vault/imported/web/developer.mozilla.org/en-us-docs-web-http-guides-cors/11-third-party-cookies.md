---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#11-third-party-cookies.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-11-third-party-cookies
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Requests with credentials › Third-party cookies
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#11-third-party-cookies
source_hash: 921ab19a1896af8065ef345284a042ff0c2e01b8f9259a77f86ab45136fbfd50
---
Note that cookies set in CORS responses are subject to normal third-party cookie policies. In the example above, the page is loaded from `foo.example` but the `Set-Cookie` header in the response is sent by `bar.other`, and would thus not be saved if the user's browser is configured to reject all third-party cookies.

Cookies set in CORS requests and responses are subject to normal third-party cookie policies.

Third-party cookie policies may prevent third-party cookies being sent in requests, effectively stopping a site from making credentialed requests even if permitted by the third-party server (using `Access-Control-Allow-Credentials`). The default policy differs between browsers, but may be set using the [SameSite](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie#samesitesamesite-value) attribute.

Even if credentialed requests are allowed, a browser may be configured to reject all third-party cookies in responses.

## The HTTP response headers

This section lists the HTTP response headers that servers return for access control requests as defined by the Cross-Origin Resource Sharing specification. The previous section gives an overview of these in action.

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
