---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#55-8-8-5-informational-responses.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-55-8-8-5-informational-responses
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.8. Examples › 8.8.5. Informational Responses'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#55-8-8-5-informational-responses
source_hash: ac9a58c645f0c2783cd7bc9e00471a0b9b0b3ecfce35079040c8580e1bcb2f08
---
An informational response using a 1xx status code other than 101 is transmitted as a [HEADERS](#HEADERS) frame, followed by zero or more [CONTINUATION](#CONTINUATION) frames.[¶](#section-8.8.5-1)

A trailer section is sent as a field block after both the request or response field block and all the [DATA](#DATA) frames have been sent. The [HEADERS](#HEADERS) frame starting the field block that comprises the trailer section has the END\_STREAM flag set.[¶](#section-8.8.5-2)

The following example includes both a 100 (Continue) status code, which is sent in response to a request containing a "100-continue" token in the Expect header field, and a trailer section:[¶](#section-8.8.5-3)

```
  HTTP/1.1 100 Continue            HEADERS
  Extension-Field: bar       ==>     - END_STREAM
                                     + END_HEADERS
                                       :status = 100
                                       extension-field = bar

  HTTP/1.1 200 OK                  HEADERS
  Content-Type: image/jpeg   ==>     - END_STREAM
  Transfer-Encoding: chunked         + END_HEADERS
  Trailer: Foo                         :status = 200
                                       content-type = image/jpeg
  123                                  trailer = Foo
  {binary data}
  0                                DATA
  Foo: bar                           - END_STREAM
                                   {binary data}

                                   HEADERS
                                     + END_STREAM
                                     + END_HEADERS
                                       foo = bar
```

[¶](#section-8.8.5-4)

## 10. Security Considerations

The use of TLS is necessary to provide many of the security properties of this protocol. Many of the claims in this section do not hold unless TLS is used as described in [Section 9.2](#TLSUsage).[¶](#section-10-1)

### 10.1. Server Authority

HTTP/2 relies on the HTTP definition of authority for determining whether a server is authoritative in providing a given response (see [Section 4.3](https://www.rfc-editor.org/rfc/rfc9110#section-4.3) of \[[HTTP](#RFC9110)]). This relies on local name resolution for the "`http`" URI scheme and the authenticated server identity for the "`https`" scheme.[¶](#section-10.1-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
