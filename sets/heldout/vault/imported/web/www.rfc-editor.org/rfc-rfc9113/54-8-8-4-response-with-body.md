---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#54-8-8-4-response-with-body.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-54-8-8-4-response-with-body
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.8. Examples › 8.8.4. Response with Body'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#54-8-8-4-response-with-body
source_hash: c22777262afe37649f1523d047ba8c192cc45012d1378d2553bb2d0de7da373a
---
A response that includes control data and a response header with message content is transmitted as a [HEADERS](#HEADERS) frame, followed by zero or more [CONTINUATION](#CONTINUATION) frames, followed by one or more [DATA](#DATA) frames, with the last [DATA](#DATA) frame in the sequence having the END\_STREAM flag set:[¶](#section-8.8.4-1)

```
  HTTP/1.1 200 OK                  HEADERS
  Content-Type: image/jpeg   ==>     - END_STREAM
  Content-Length: 123                + END_HEADERS
                                       :status = 200
  {binary data}                        content-type = image/jpeg
                                       content-length = 123

                                   DATA
                                     + END_STREAM
                                   {binary data}
```

[¶](#section-8.8.4-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
