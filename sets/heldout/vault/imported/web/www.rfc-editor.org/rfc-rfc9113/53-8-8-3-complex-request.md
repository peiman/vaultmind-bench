---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#53-8-8-3-complex-request.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-53-8-8-3-complex-request
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.8. Examples › 8.8.3. Complex Request'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#53-8-8-3-complex-request
source_hash: d419ef116a789f9d6a1edaa038d5c16587a15b5ad792292859e8cf890be63bd7
---
An HTTP POST request that includes control data and a request header with message content is transmitted as one [HEADERS](#HEADERS) frame, followed by zero or more [CONTINUATION](#CONTINUATION) frames containing the request header, followed by one or more [DATA](#DATA) frames, with the last [CONTINUATION](#CONTINUATION) (or [HEADERS](#HEADERS)) frame having the END\_HEADERS flag set and the final [DATA](#DATA) frame having the END\_STREAM flag set:[¶](#section-8.8.3-1)

```
  POST /resource HTTP/1.1          HEADERS
  Host: example.org          ==>     - END_STREAM
  Content-Type: image/jpeg           - END_HEADERS
  Content-Length: 123                  :method = POST
                                       :authority = example.org
                                       :path = /resource
  {binary data}                        :scheme = https

                                   CONTINUATION
                                     + END_HEADERS
                                       content-type = image/jpeg
                                       host = example.org
                                       content-length = 123

                                   DATA
                                     + END_STREAM
                                   {binary data}
```

[¶](#section-8.8.3-2)

Note that data contributing to any given field line could be spread between field block fragments. The allocation of field lines to frames in this example is illustrative only.[¶](#section-8.8.3-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
