---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#02-functional-overview.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-02-functional-overview
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Functional overview
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#02-functional-overview
source_hash: 3faffb33bfe22d35f4608c77367e645626da720c4010f920ac2776d7ee142020
---
The Cross-Origin Resource Sharing standard works by adding new [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers) that let servers describe which origins are permitted to read that information from a web browser. Additionally, for HTTP request methods that can cause side-effects on server data (in particular, HTTP methods other than [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET), or [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST) with certain [MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types)), the specification mandates that browsers "preflight" the request, soliciting supported methods from the server with the HTTP [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/OPTIONS) request method, and then, upon "approval" from the server, sending the actual request. Servers can also inform clients whether "credentials" (such as [Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies) and [HTTP Authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Authentication)) should be sent with requests.

CORS failures result in errors but for security reasons, specifics about the error *are not available to JavaScript*. All the code knows is that an error occurred. The only way to determine what specifically went wrong is to look at the browser's console for details.

Subsequent sections discuss scenarios, as well as provide a breakdown of the HTTP headers used.

## Examples of access control scenarios

We present three scenarios that demonstrate how Cross-Origin Resource Sharing works. All these examples use [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch "fetch()"), which can make cross-origin requests in any supporting browser.

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
