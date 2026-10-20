---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#04-simple-requests.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-04-simple-requests
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Simple requests (2/2)
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#04-simple-requests
source_hash: 217212731ceb2f523cc3e0843d5d48e29db1a94318f7fc8ee12effa13650f9ec
---
This pattern of the [`Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin) and [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) headers is the simplest use of the access control protocol. If the resource owners at `https://bar.other` wished to restrict access to the resource to requests *only* from `https://foo.example` (i.e., no domain other than `https://foo.example` can access the resource in a cross-origin manner), they would send:

http

```
Access-Control-Allow-Origin: https://foo.example
```

**Note:** When responding to a [credentialed requests](#requests_with_credentials) request, the server **must** specify an origin in the value of the `Access-Control-Allow-Origin` header, instead of specifying the `*` wildcard.

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
