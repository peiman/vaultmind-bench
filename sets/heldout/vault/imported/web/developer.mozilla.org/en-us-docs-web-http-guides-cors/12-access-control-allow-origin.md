---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#12-access-control-allow-origin.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-12-access-control-allow-origin
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › The HTTP response headers › Access-Control-Allow-Origin
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#12-access-control-allow-origin
source_hash: 8135e41576bada8b5cfc0bf7802f98638647c3ef926ddd231784c4990e38c512
---
A returned resource may have one [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) header with the following syntax:

http

```
Access-Control-Allow-Origin: <origin> | *
```

`Access-Control-Allow-Origin` specifies either a single origin which tells browsers to allow that origin to access the resource; or else — for requests **without** credentials — the `*` wildcard tells browsers to allow any origin to access the resource.

For example, to allow code from the origin `https://mozilla.org` to access the resource, you can specify:

http

```
Access-Control-Allow-Origin: https://mozilla.org
Vary: Origin
```

If the server specifies a single origin (that may dynamically change based on the requesting origin as part of an allowlist) rather than the `*` wildcard, then the server should also include `Origin` in the [`Vary`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary) response header to indicate to clients that server responses will differ based on the value of the [`Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin) request header.

### Access-Control-Expose-Headers

The [`Access-Control-Expose-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers) header adds the specified headers to the allowlist that JavaScript (such as [`Response.headers`](https://developer.mozilla.org/en-US/docs/Web/API/Response/headers)) in browsers is allowed to access.

http

```
Access-Control-Expose-Headers: <header-name>[, <header-name>]*
```

For example, the following would allow the `X-My-Custom-Header` and `X-Another-Custom-Header` headers to be exposed to the browser:

http

```
Access-Control-Expose-Headers: X-My-Custom-Header, X-Another-Custom-Header
```

### Access-Control-Max-Age

The [`Access-Control-Max-Age`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Max-Age) header indicates how long the results of a preflight request can be cached. For an example of a preflight request, see the above examples.

http

```
Access-Control-Max-Age: <delta-seconds>
```

The `delta-seconds` parameter indicates the number of seconds the results can be cached.

### Access-Control-Allow-Credentials

The [`Access-Control-Allow-Credentials`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Credentials) header indicates whether or not the response to the request can be exposed when the `credentials` flag is true. When used as part of a response to a preflight request, this indicates whether or not the actual request can be made using credentials. Note that simple `GET` requests are not preflighted, and so if a request is made for a resource with credentials, if this header is not returned with the resource, the response is ignored by the browser and not returned to web content.

http

```
Access-Control-Allow-Credentials: true
```

[Credentialed requests](#requests_with_credentials) are discussed above.

### Access-Control-Allow-Methods

The [`Access-Control-Allow-Methods`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Methods) header specifies the method or methods allowed when accessing the resource. This is used in response to a preflight request. The conditions under which a request is preflighted are discussed above.

http

```
Access-Control-Allow-Methods: <method>[, <method>]*
```

An example of a [preflight request](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request) is given above, including an example which sends this header to the browser.

### Access-Control-Allow-Headers

The [`Access-Control-Allow-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Headers) header is used in response to a [preflight request](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request) to indicate which HTTP headers can be used when making the actual request. This header is the server side response to the browser's [`Access-Control-Request-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Request-Headers) header.

http

```
Access-Control-Allow-Headers: <header-name>[, <header-name>]*
```

## The HTTP request headers

This section lists headers that clients may use when issuing HTTP requests in order to make use of the cross-origin sharing feature. Note that these headers are set for you when making invocations to servers. Developers making cross-origin requests do not have to set any cross-origin sharing request headers programmatically.

### Origin

The [`Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin) header indicates the origin of the cross-origin access request or preflight request.

http

```
Origin: <origin>
```

The origin is a URL indicating the server from which the request is initiated. It does not include any path information, only the server name.

**Note:** The `origin` value can be `null`.

Note that in any access control request, the [`Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin) header is **always** sent.

### Access-Control-Request-Method

The [`Access-Control-Request-Method`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Request-Method) is used when issuing a preflight request to let the server know what HTTP method will be used when the actual request is made.

http

```
Access-Control-Request-Method: <method>
```

Examples of this usage can be [found above.](#preflighted_requests)

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
