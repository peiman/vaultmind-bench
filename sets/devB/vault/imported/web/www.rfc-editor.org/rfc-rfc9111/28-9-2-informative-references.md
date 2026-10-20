---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#28-9-2-informative-references.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-28-9-2-informative-references
type: reference
title: 'RFC 9111: HTTP Caching › 9. References › 9.2. Informative References'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#28-9-2-informative-references
source_hash: 0389c03f11c19d7ff65a6df330f329f3bd3c14c7bb3fab04f4cdcc4dcc4b36a7
---
\[COOKIE]

Barth, A., "HTTP State Management Mechanism", RFC 6265, DOI 10.17487/RFC6265, April 2011, &lt;[https://www.rfc-editor.org/info/rfc6265](https://www.rfc-editor.org/info/rfc6265)&gt;.

\[HTTP/1.1]

Fielding, R., Ed., Nottingham, M., Ed., and J. Reschke, Ed., "HTTP/1.1", STD 99, RFC 9112, DOI 10.17487/RFC9112, June 2022, &lt;[https://www.rfc-editor.org/info/rfc9112](https://www.rfc-editor.org/info/rfc9112)&gt;.

\[RFC2616]

Fielding, R., Gettys, J., Mogul, J., Frystyk, H., Masinter, L., Leach, P., and T. Berners-Lee, "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, DOI 10.17487/RFC2616, June 1999, &lt;[https://www.rfc-editor.org/info/rfc2616](https://www.rfc-editor.org/info/rfc2616)&gt;.

\[RFC5861]

Nottingham, M., "HTTP Cache-Control Extensions for Stale Content", RFC 5861, DOI 10.17487/RFC5861, May 2010, &lt;[https://www.rfc-editor.org/info/rfc5861](https://www.rfc-editor.org/info/rfc5861)&gt;.

\[RFC7234]

Fielding, R., Ed., Nottingham, M., Ed., and J. Reschke, Ed., "Hypertext Transfer Protocol (HTTP/1.1): Caching", RFC 7234, DOI 10.17487/RFC7234, June 2014, &lt;[https://www.rfc-editor.org/info/rfc7234](https://www.rfc-editor.org/info/rfc7234)&gt;.

\[RFC8126]

Cotton, M., Leiba, B., and T. Narten, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 8126, DOI 10.17487/RFC8126, June 2017, &lt;[https://www.rfc-editor.org/info/rfc8126](https://www.rfc-editor.org/info/rfc8126)&gt;.

## Appendix A. Collected ABNF

In the collected ABNF below, list rules are expanded per [Section 5.6.1](https://www.rfc-editor.org/rfc/rfc9110#section-5.6.1) of \[[HTTP](#HTTP)].[¶](#appendix-A-1)

```
Age = delta-seconds

Cache-Control = [ cache-directive *( OWS "," OWS cache-directive ) ]

Expires = HTTP-date

HTTP-date = <HTTP-date, see [HTTP], Section 5.6.7>

OWS = <OWS, see [HTTP], Section 5.6.3>

cache-directive = token [ "=" ( token / quoted-string ) ]

delta-seconds = 1*DIGIT

field-name = <field-name, see [HTTP], Section 5.1>

quoted-string = <quoted-string, see [HTTP], Section 5.6.4>

token = <token, see [HTTP], Section 5.6.2>
```

[¶](#appendix-A-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
