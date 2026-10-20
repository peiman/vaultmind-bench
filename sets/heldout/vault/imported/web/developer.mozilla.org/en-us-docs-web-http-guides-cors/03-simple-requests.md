---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#03-simple-requests.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-03-simple-requests
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Simple requests (1/2)
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#03-simple-requests
source_hash: e7f8c5f67a20a9555211eb8bf36bf1a3ddd6f7441d697167e71a9b8b0e79b4d3
---
Some requests don't trigger a [CORS preflight](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request). Those are called *simple requests* from the obsolete [CORS spec](https://www.w3.org/TR/2014/REC-cors-20140116/#terminology "External link (opens in new tab)"), though the [Fetch spec](https://fetch.spec.whatwg.org/ "External link (opens in new tab)") (which now defines CORS) doesn't use that term.

The motivation is that the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form) element from HTML 4.0 (which predates cross-site [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch "fetch()") and [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest)) can submit simple requests to any origin, so anyone writing a server must already be protecting against [cross-site request forgery](https://developer.mozilla.org/en-US/docs/Glossary/CSRF) (CSRF). Under this assumption, the server doesn't have to opt-in (by responding to a preflight request) to receive any request that looks like a form submission, since the threat of CSRF is no worse than that of form submission. However, the server still must opt-in using [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) to *share* the response with the script.

A *simple request* is one that **meets all the following conditions**:

- One of the allowed methods:

- [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET)
  - [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/HEAD)
  - [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST)
- Apart from the headers automatically set by the user agent (for example, [`Connection`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Connection), [`User-Agent`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent), or the [forbidden request headers](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_request_header)), the only headers which are allowed to be manually set are the [CORS-safelisted request-headers](https://developer.mozilla.org/en-US/docs/Glossary/CORS-safelisted_request_header), which are:

- [`Accept`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept)
  - [`Accept-Language`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Language)
  - [`Content-Language`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Language)
  - [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) (please note the additional requirements below)
  - [`Range`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Range) (only with a [single range header value](https://fetch.spec.whatwg.org/#simple-range-header-value "External link (opens in new tab)"); e.g., `bytes=256-` or `bytes=127-255`)
- The only type/subtype combinations allowed for the [media type](https://developer.mozilla.org/en-US/docs/Glossary/MIME_type) specified in the [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) header are:

- `application/x-www-form-urlencoded`
  - `multipart/form-data`
  - `text/plain`
- If the request is made using an [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) object, no event listeners are registered on the object returned by the [`XMLHttpRequest.upload`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/upload) property used in the request; that is, given an [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) instance `xhr`, no code has called `xhr.upload.addEventListener()` to add an event listener to monitor the upload.
- No [`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream) object is used in the request.

For example, suppose web content at `https://foo.example` wishes to fetch JSON content from domain `https://bar.other`. Code of this sort might be used in JavaScript deployed on `foo.example`:

js

```
const fetchPromise = fetch("https://bar.other");

fetchPromise
  .then((response) => response.json())
  .then((data) => {
    console.log(data);
  });
```

This operation performs a simple exchange between the client and the server, using CORS headers to handle the privileges:

![Diagram of simple CORS GET request](https://mdn.github.io/shared-assets/images/diagrams/http/cors/simple-request.svg)

Let's look at what the browser will send to the server in this case:

http

```
GET /resources/public-data/ HTTP/1.1
Host: bar.other
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Connection: keep-alive
Origin: https://foo.example
```

The request header of note is [`Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Origin), which shows that the invocation is coming from `https://foo.example`.

Now let's see how the server responds:

http

```
HTTP/1.1 200 OK
Date: Mon, 01 Dec 2008 00:23:53 GMT
Server: Apache/2
Access-Control-Allow-Origin: *
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: application/xml

[…XML Data…]
```

In response, the server returns an [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) header with `Access-Control-Allow-Origin: *`, which means that the resource can be accessed by **any** origin.

http

```
Access-Control-Allow-Origin: *
```

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
