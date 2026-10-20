---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#05-preflighted-requests.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-05-preflighted-requests
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Preflighted requests (1/2)
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#05-preflighted-requests
source_hash: 8d83b18509dbc11bbb0f2f5c9f2b75e9fc1e0189bc506c9b06385616e18d97fe
---
Unlike [*simple requests*](#simple_requests), for "preflighted" requests the browser first sends an HTTP request using the [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/OPTIONS) method to the resource on the other origin, in order to determine if the actual request is safe to send. Such cross-origin requests are preflighted since they may have implications for user data.

The following is an example of a request that will be preflighted:

js

```
const fetchPromise = fetch("https://bar.other/doc", {
  method: "POST",
  mode: "cors",
  headers: {
    "Content-Type": "text/xml",
    "X-PINGOTHER": "pingpong",
  },
  body: "<person><name>Arun</name></person>",
});

fetchPromise.then((response) => {
  console.log(response.status);
});
```

The example above creates an XML body to send with the `POST` request. Also, a non-standard HTTP `X-PINGOTHER` request header is set. Such headers are not part of HTTP/1.1, but are generally useful to web applications. Since the request uses a `Content-Type` of `text/xml`, and since a custom header is set, this request is preflighted.

![Diagram of a request that is preflighted](https://mdn.github.io/shared-assets/images/diagrams/http/cors/preflight-correct.svg)

**Note:** As described below, the actual `POST` request does not include the `Access-Control-Request-*` headers; they are needed only for the `OPTIONS` request.

Let's look at the full exchange between client and server. The first exchange is the *preflight request/response*:

http

```
OPTIONS /doc HTTP/1.1
Host: bar.other
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Connection: keep-alive
Origin: https://foo.example
Access-Control-Request-Method: POST
Access-Control-Request-Headers: content-type,x-pingother

HTTP/1.1 204 No Content
Date: Mon, 01 Dec 2008 01:15:39 GMT
Server: Apache/2
Access-Control-Allow-Origin: https://foo.example
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: X-PINGOTHER, Content-Type
Access-Control-Max-Age: 86400
Vary: Accept-Encoding, Origin
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
```

The first block above represents the preflight request with the [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/OPTIONS) method. The browser determines that it needs to send this based on the request parameters that the JavaScript code snippet above was using, so that the server can respond whether it is acceptable to send the request with the actual request parameters. OPTIONS is an HTTP/1.1 method that is used to determine further information from servers, and is a [safe](https://developer.mozilla.org/en-US/docs/Glossary/Safe/HTTP) method, meaning that it can't be used to change the resource. Note that along with the OPTIONS request, two other request headers are sent:

http

```
Access-Control-Request-Method: POST
Access-Control-Request-Headers: content-type,x-pingother
```

The [`Access-Control-Request-Method`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Request-Method) header notifies the server as part of a preflight request that when the actual request is sent, it will do so with a `POST` request method. The [`Access-Control-Request-Headers`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Request-Headers) header notifies the server that when the actual request is sent, it will do so with `X-PINGOTHER` and `Content-Type` custom headers. Now the server has an opportunity to determine whether it can accept a request under these conditions.

The second block above is the response that the server returns, which indicate that the request method (`POST`) and request headers (`X-PINGOTHER`) are acceptable. Let's have a closer look at the following lines:

http

```
Access-Control-Allow-Origin: https://foo.example
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: X-PINGOTHER, Content-Type
Access-Control-Max-Age: 86400
```

The server responds with `Access-Control-Allow-Origin: https://foo.example`, restricting access to the requesting origin domain only. It also responds with `Access-Control-Allow-Methods`, which says that `POST` and `GET` are valid methods to query the resource in question (this header is similar to the [`Allow`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Allow) response header, but used strictly within the context of access control).

The server also sends `Access-Control-Allow-Headers` with a value of `X-PINGOTHER, Content-Type`, confirming that these are permitted headers to be used with the actual request. Like `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers` is a comma-separated list of acceptable headers.

Finally, [`Access-Control-Max-Age`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Max-Age) gives the value in seconds for how long the response to the preflight request can be cached without sending another preflight request. The default value is 5 seconds. In the present case, the max age is 86400 seconds (= 24 hours). Note that each browser has a [maximum internal value](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Max-Age) that takes precedence when the `Access-Control-Max-Age` exceeds it.

Once the preflight request is complete, the real request is sent:

http

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
