---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#66-12-2-informative-references.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-66-12-2-informative-references
type: reference
title: 'RFC 9113: HTTP/2 › 12. References › 12.2. Informative References'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#66-12-2-informative-references
source_hash: e7914f9cd94c8bb54caee979d322e5cf0548e750cb0363e2fde0ae7fb3a11c0d
---
\[ALT-SVC]

Nottingham, M., McManus, P., and J. Reschke, "HTTP Alternative Services", RFC 7838, DOI 10.17487/RFC7838, April 2016, &lt;[https://www.rfc-editor.org/info/rfc7838](https://www.rfc-editor.org/info/rfc7838)&gt;.

\[BREACH]

Gluck, Y., Harris, N., and A. Prado, "BREACH: Reviving the CRIME Attack", 12 July 2013, &lt;[https://breachattack.com/resources/BREACH%20-%20SSL,%20gone%20in%2030%20seconds.pdf](https://breachattack.com/resources/BREACH%20-%20SSL,%20gone%20in%2030%20seconds.pdf)&gt;.

\[DNS-TERMS]

Hoffman, P., Sullivan, A., and K. Fujiwara, "DNS Terminology", BCP 219, RFC 8499, DOI 10.17487/RFC8499, January 2019, &lt;[https://www.rfc-editor.org/info/rfc8499](https://www.rfc-editor.org/info/rfc8499)&gt;.

\[HTTP-PRIORITY]

Oku, K. and L. Pardue, "Extensible Prioritization Scheme for HTTP", RFC 9218, DOI 10.17487/RFC9218, June 2022, &lt;[https://www.rfc-editor.org/info/rfc9218](https://www.rfc-editor.org/info/rfc9218)&gt;.

\[HTTP/1.1]

Fielding, R., Ed., Nottingham, M., Ed., and J. Reschke, Ed., "HTTP/1.1", STD 99, RFC 9112, DOI 10.17487/RFC9112, June 2022, &lt;[https://www.rfc-editor.org/info/rfc9112](https://www.rfc-editor.org/info/rfc9112)&gt;.

\[NFLX-2019-002]

Netflix, "HTTP/2 Denial of Service Advisory", 13 August 2019, &lt;[https://github.com/Netflix/security-bulletins/blob/master/advisories/third-party/2019-002.md](https://github.com/Netflix/security-bulletins/blob/master/advisories/third-party/2019-002.md)&gt;.

\[PRIVACY]

Cooper, A., Tschofenig, H., Aboba, B., Peterson, J., Morris, J., Hansen, M., and R. Smith, "Privacy Considerations for Internet Protocols", RFC 6973, DOI 10.17487/RFC6973, July 2013, &lt;[https://www.rfc-editor.org/info/rfc6973](https://www.rfc-editor.org/info/rfc6973)&gt;.

\[RFC1122]

Braden, R., Ed., "Requirements for Internet Hosts - Communication Layers", STD 3, RFC 1122, DOI 10.17487/RFC1122, October 1989, &lt;[https://www.rfc-editor.org/info/rfc1122](https://www.rfc-editor.org/info/rfc1122)&gt;.

\[RFC3749]

Hollenbeck, S., "Transport Layer Security Protocol Compression Methods", RFC 3749, DOI 10.17487/RFC3749, May 2004, &lt;[https://www.rfc-editor.org/info/rfc3749](https://www.rfc-editor.org/info/rfc3749)&gt;.

\[RFC6125]

Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125, DOI 10.17487/RFC6125, March 2011, &lt;[https://www.rfc-editor.org/info/rfc6125](https://www.rfc-editor.org/info/rfc6125)&gt;.

\[RFC6585]

Nottingham, M. and R. Fielding, "Additional HTTP Status Codes", RFC 6585, DOI 10.17487/RFC6585, April 2012, &lt;[https://www.rfc-editor.org/info/rfc6585](https://www.rfc-editor.org/info/rfc6585)&gt;.

\[RFC7323]

Borman, D., Braden, B., Jacobson, V., and R. Scheffenegger, Ed., "TCP Extensions for High Performance", RFC 7323, DOI 10.17487/RFC7323, September 2014, &lt;[https://www.rfc-editor.org/info/rfc7323](https://www.rfc-editor.org/info/rfc7323)&gt;.

\[RFC7540]

Belshe, M., Peon, R., and M. Thomson, Ed., "Hypertext Transfer Protocol Version 2 (HTTP/2)", RFC 7540, DOI 10.17487/RFC7540, May 2015, &lt;[https://www.rfc-editor.org/info/rfc7540](https://www.rfc-editor.org/info/rfc7540)&gt;.

\[RFC8441]

McManus, P., "Bootstrapping WebSockets with HTTP/2", RFC 8441, DOI 10.17487/RFC8441, September 2018, &lt;[https://www.rfc-editor.org/info/rfc8441](https://www.rfc-editor.org/info/rfc8441)&gt;.

\[RFC8740]

Benjamin, D., "Using TLS 1.3 with HTTP/2", RFC 8740, DOI 10.17487/RFC8740, February 2020, &lt;[https://www.rfc-editor.org/info/rfc8740](https://www.rfc-editor.org/info/rfc8740)&gt;.

\[TALKING]

Huang, L., Chen, E., Barth, A., Rescorla, E., and C. Jackson, "Talking to Yourself for Fun and Profit", 2011, &lt;[https://www.adambarth.com/papers/2011/huang-chen-barth-rescorla-jackson.pdf](https://www.adambarth.com/papers/2011/huang-chen-barth-rescorla-jackson.pdf)&gt;.

## Appendix A. Prohibited TLS 1.2 Cipher Suites

An HTTP/2 implementation MAY treat the negotiation of any of the following cipher suites with TLS 1.2 as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [INADEQUATE\_SECURITY](#INADEQUATE_SECURITY):[¶](#appendix-A-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
