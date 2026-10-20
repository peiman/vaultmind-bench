---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#52-8-8-1-simple-request.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-52-8-8-1-simple-request
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.8. Examples › 8.8.1. Simple Request'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#52-8-8-1-simple-request
source_hash: f3da38aa917f0b5b8a45f57067c72642bda11626f8542c819a36981eb952fa5c
---
An HTTP GET request includes control data and a request header with no message content and is therefore transmitted as a single [HEADERS](#HEADERS) frame, followed by zero or more [CONTINUATION](#CONTINUATION) frames containing the serialized block of request header fields. The [HEADERS](#HEADERS) frame in the following has both the END\_HEADERS and END\_STREAM flags set; no [CONTINUATION](#CONTINUATION) frames are sent.[¶](#section-8.8.1-1)

```
  GET /resource HTTP/1.1           HEADERS
  Host: example.org          ==>     + END_STREAM
  Accept: image/jpeg                 + END_HEADERS
                                       :method = GET
                                       :scheme = https
                                       :authority = example.org
                                       :path = /resource
                                       host = example.org
                                       accept = image/jpeg
```

[¶](#section-8.8.1-2)

#### 8.8.2. Simple Response

Similarly, a response that includes only control data and a response header is transmitted as a [HEADERS](#HEADERS) frame (again, followed by zero or more [CONTINUATION](#CONTINUATION) frames) containing the serialized block of response header fields.[¶](#section-8.8.2-1)

```
  HTTP/1.1 304 Not Modified        HEADERS
  ETag: "xyzzy"              ==>     + END_STREAM
  Expires: Thu, 23 Jan ...           + END_HEADERS
                                       :status = 304
                                       etag = "xyzzy"
                                       expires = Thu, 23 Jan ...
```

[¶](#section-8.8.2-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
