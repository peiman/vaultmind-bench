---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#13-access-control-request-headers.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-13-access-control-request-headers
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › The HTTP request headers › Access-Control-Request-Headers
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#13-access-control-request-headers
source_hash: a66f1f7b8212be13d8c49ce5c59ec19340e1cf2c88efc8c0511cb7b6354c02e3
---
The [`Access-Control-Request-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Request-Headers) header is used when issuing a preflight request to let the server know what HTTP headers will be used when the actual request is made (for example, by passing them as the [`headers`](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#headers) option). This browser-side header will be answered by the complementary server-side header of [`Access-Control-Allow-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Headers).

http

```
Access-Control-Request-Headers: <field-name>[,<field-name>]*
```

Examples of this usage can be [found above](#preflighted_requests).

## Specifications

Specification [Fetch  
\# http-access-control-allow-origin](https://fetch.spec.whatwg.org/#http-access-control-allow-origin)

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
