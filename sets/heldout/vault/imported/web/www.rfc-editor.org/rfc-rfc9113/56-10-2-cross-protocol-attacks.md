---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#56-10-2-cross-protocol-attacks.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-56-10-2-cross-protocol-attacks
type: reference
title: 'RFC 9113: HTTP/2 › 10. Security Considerations › 10.2. Cross-Protocol Attacks'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#56-10-2-cross-protocol-attacks
source_hash: 956d488e5d0e917fb0c39ed238ef4314bdb8cedd0923f67d7c2f8efe5c293e1c
---
In a cross-protocol attack, an attacker causes a client to initiate a transaction in one protocol toward a server that understands a different protocol. An attacker might be able to cause the transaction to appear as a valid transaction in the second protocol. In combination with the capabilities of the web context, this can be used to interact with poorly protected servers in private networks.[¶](#section-10.2-1)

Completing a TLS handshake with an ALPN identifier for HTTP/2 can be considered sufficient protection against cross-protocol attacks. ALPN provides a positive indication that a server is willing to proceed with HTTP/2, which prevents attacks on other TLS-based protocols.[¶](#section-10.2-2)

The encryption in TLS makes it difficult for attackers to control the data that could be used in a cross-protocol attack on a cleartext protocol.[¶](#section-10.2-3)

The cleartext version of HTTP/2 has minimal protection against cross-protocol attacks. The [connection preface](#preface) ([Section 3.4](#preface)) contains a string that is designed to confuse HTTP/1.1 servers, but no special protection is offered for other protocols.[¶](#section-10.2-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
