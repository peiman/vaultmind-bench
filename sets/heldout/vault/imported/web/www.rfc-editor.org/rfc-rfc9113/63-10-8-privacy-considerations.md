---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#63-10-8-privacy-considerations.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-63-10-8-privacy-considerations
type: reference
title: 'RFC 9113: HTTP/2 › 10. Security Considerations › 10.8. Privacy Considerations'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#63-10-8-privacy-considerations
source_hash: 32908dd177578aceb9444052d613091d51a67a6fdfde7f81acbe0371df6a6b5b
---
Several characteristics of HTTP/2 provide an observer an opportunity to correlate actions of a single client or server over time. These include the values of settings, the manner in which flow-control windows are managed, the way priorities are allocated to streams, the timing of reactions to stimulus, and the handling of any features that are controlled by settings.[¶](#section-10.8-1)

As far as these create observable differences in behavior, they could be used as a basis for fingerprinting a specific client, as defined in [Section 3.2](https://www.rfc-editor.org/rfc/rfc6973#section-3.2) of \[[PRIVACY](#RFC6973)].[¶](#section-10.8-2)

HTTP/2's preference for using a single TCP connection allows correlation of a user's activity on a site. Reusing connections for different origins allows tracking across those origins.[¶](#section-10.8-3)

Because the PING and SETTINGS frames solicit immediate responses, they can be used by an endpoint to measure latency to their peer. This might have privacy implications in certain scenarios.[¶](#section-10.8-4)

### 10.9. Remote Timing Attacks

Remote timing attacks extract secrets from servers by observing variations in the time that servers take when processing requests that use secrets. HTTP/2 enables concurrent request creation and processing, which can give attackers better control over when request processing commences. Multiple HTTP/2 requests can be included in the same IP packet or TLS record. HTTP/2 can therefore make remote timing attacks more efficient by eliminating variability in request delivery, leaving only request order and the delivery of responses as sources of timing variability.[¶](#section-10.9-1)

Ensuring that processing time is not dependent on the value of a secret is the best defense against any form of timing attack.[¶](#section-10.9-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
