---
# Imported by `vaultmind import` from https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#06-preflighted-requests.
# The page is the source: re-run the import to refresh it.
id: imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-06-preflighted-requests
type: reference
title: Cross-Origin Resource Sharing (CORS) - HTTP | MDN › Examples of access control scenarios › Preflighted requests (2/2)
url: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
source: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS#06-preflighted-requests
source_hash: fb35c711ef318e6b7494f935403d29a3d7557dc9f981a24964039283e02a23cd
---
```
POST /doc HTTP/1.1
Host: bar.other
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Connection: keep-alive
X-PINGOTHER: pingpong
Content-Type: text/xml; charset=UTF-8
Referer: https://foo.example/examples/preflightInvocation.html
Content-Length: 55
Origin: https://foo.example
Pragma: no-cache
Cache-Control: no-cache

<person><name>Arun</name></person>

HTTP/1.1 200 OK
Date: Mon, 01 Dec 2008 01:15:40 GMT
Server: Apache/2
Access-Control-Allow-Origin: https://foo.example
Vary: Accept-Encoding, Origin
Content-Encoding: gzip
Content-Length: 235
Keep-Alive: timeout=2, max=99
Connection: Keep-Alive
Content-Type: text/plain

[Some XML content]
```

Part of [[imported/web/developer.mozilla.org/en-us-docs-web-http-guides-cors]].
