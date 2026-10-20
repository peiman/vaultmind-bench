---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#07-preflighted-requests-and-redirects.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-07-preflighted-requests-and-redirects
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Preflighted requests › Preflighted requests and redirects
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#07-preflighted-requests-and-redirects
source_hash: af2e37eda2049e05b06906536306a33645688ed197b81ca4ea8d88058c079eab
---
Not all browsers currently support following redirects after a preflighted request. If a redirect occurs after such a request, some browsers currently will report an error message such as the following:

> The request was redirected to `https://example.com/foo`, which is disallowed for cross-origin requests that require preflight. Request requires preflight, which is disallowed to follow cross-origin redirects.

The CORS protocol originally required that behavior but [was subsequently changed to no longer require it](https://github.com/whatwg/fetch/commit/0d9a4db8bc02251cc9e391543bb3c1322fb882f2 "External link (opens in new tab)"). However, not all browsers have implemented the change, and thus still exhibit the originally required behavior.

Until browsers catch up with the spec, you may be able to work around this limitation by doing one or both of the following:

- Change the server-side behavior to avoid the preflight and/or to avoid the redirect
- Change the request such that it is a [simple request](#simple_requests) that doesn't cause a preflight

If that's not possible, then another way is to:

1. Make a [simple request](#simple_requests) (using [`Response.url`](https://developer.mozilla.org/en-US/docs/Web/API/Response/url) for the Fetch API, or [`XMLHttpRequest.responseURL`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseURL)) to determine what URL the real preflighted request would end up at.
2. Make another request (the *real* request) using the URL you obtained from `Response.url` or `XMLHttpRequest.responseURL` in the first step.

However, if the request is one that triggers a preflight due to the presence of the `Authorization` header in the request, you won't be able to work around the limitation using the steps above. And you won't be able to work around it at all unless you have control over the server the request is being made to.

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
