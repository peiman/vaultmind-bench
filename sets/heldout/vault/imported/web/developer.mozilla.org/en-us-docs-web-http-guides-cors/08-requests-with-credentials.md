---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#08-requests-with-credentials.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-08-requests-with-credentials
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Requests with credentials
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#08-requests-with-credentials
source_hash: ec69c137a05d48d82187b453a9677e6e3af904ab60be11a469388f34efd0b0b8
---
**Note:** When making credentialed requests to a different domain, third-party cookie policies will still apply. The policy is always enforced regardless of any setup on the server and the client as described in this chapter.

The most interesting capability exposed by both [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch "fetch()") or [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) and CORS is the ability to make "credentialed" requests that are aware of [HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Cookies) and HTTP Authentication information. By default, in cross-origin `fetch()` or `XMLHttpRequest` calls, browsers will *not* send credentials.

To ask for a `fetch()` request to include credentials, set the [`credentials`](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#credentials) option to `"include"`.

To ask for an `XMLHttpRequest` request to include credentials, set the [`XMLHttpRequest.withCredentials`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials) property to `true`.

In this example, content originally loaded from `https://foo.example` makes a GET request to a resource on `https://bar.other` which sets Cookies. Content on foo.example might contain JavaScript like this:

js

```
const url = "https://bar.other/resources/credentialed-content/";

const request = new Request(url, { credentials: "include" });

const fetchPromise = fetch(request);
fetchPromise.then((response) => console.log(response));
```

This code creates a [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object, setting the `credentials` option to `"include"` in the constructor, then passes this request into `fetch()`. Since this is a simple `GET` request, it is not preflighted but the browser will **reject** any response that does not have the [`Access-Control-Allow-Credentials`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Credentials) header set to `true`, and **not** make the response available to the invoking web content.

![Diagram of a GET request with Access-Control-Allow-Credentials](https://mdn.github.io/shared-assets/images/diagrams/http/cors/include-credentials.svg)

Here is a sample exchange between client and server:

http

```
GET /resources/credentialed-content/ HTTP/1.1
Host: bar.other
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Connection: keep-alive
Referer: https://foo.example/examples/credential.html
Origin: https://foo.example
Cookie: pageAccess=2

HTTP/1.1 200 OK
Date: Mon, 01 Dec 2008 01:34:52 GMT
Server: Apache/2
Access-Control-Allow-Origin: https://foo.example
Access-Control-Allow-Credentials: true
Cache-Control: no-cache
Pragma: no-cache
Set-Cookie: pageAccess=3; expires=Wed, 31-Dec-2008 01:34:53 GMT
Vary: Accept-Encoding, Origin
Content-Encoding: gzip
Content-Length: 106
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
Content-Type: text/plain

[text/plain content]
```

Although the request's `Cookie` header contains the cookie destined for the content on `https://bar.other`, if bar.other did not respond with an [`Access-Control-Allow-Credentials`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Credentials) with value `true`, as demonstrated in this example, the response would be ignored and not made available to the web content.

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
