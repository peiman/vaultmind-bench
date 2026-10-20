---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#09-3-1-http-2-version-identification.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-09-3-1-http-2-version-identification
type: reference
title: 'RFC 9113: HTTP/2 › 3. Starting HTTP/2 › 3.1. HTTP/2 Version Identification'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#09-3-1-http-2-version-identification
source_hash: aea6d9821a33806c8223b765285716e7ee74adc66b79c7140ba1aa7e27ff0306
---
The protocol defined in this document has two identifiers. Creating a connection based on either implies the use of the transport, framing, and message semantics described in this document.[¶](#section-3.1-1)

- The string "h2" identifies the protocol where HTTP/2 uses Transport Layer Security (TLS); see [Section 9.2](#TLSUsage). This identifier is used in the [TLS Application-Layer Protocol Negotiation (ALPN) extension](#RFC7301) \[[TLS-ALPN](#RFC7301)] field and in any place where HTTP/2 over TLS is identified.[¶](#section-3.1-2.1.1)
  
  The "h2" string is serialized into an ALPN protocol identifier as the two-octet sequence: 0x68, 0x32.[¶](#section-3.1-2.1.2)
- The "h2c" string was previously used as a token for use in the HTTP Upgrade mechanism's Upgrade header field ([Section 7.8](https://www.rfc-editor.org/rfc/rfc9110#section-7.8) of \[[HTTP](#RFC9110)]). This usage was never widely deployed and is deprecated by this document. The same applies to the HTTP2-Settings header field, which was used with the upgrade to "h2c".[¶](#section-3.1-2.2.1)

### 3.2. Starting HTTP/2 for "`https`" URIs

A client that makes a request to an "`https`" URI uses [TLS](#RFC8446) \[[TLS13](#RFC8446)] with the [ALPN extension](#RFC7301) \[[TLS-ALPN](#RFC7301)].[¶](#section-3.2-1)

HTTP/2 over TLS uses the "h2" protocol identifier. The "h2c" protocol identifier MUST NOT be sent by a client or selected by a server; the "h2c" protocol identifier describes a protocol that does not use TLS.[¶](#section-3.2-2)

Once TLS negotiation is complete, both the client and the server MUST send a [connection preface](#preface) ([Section 3.4](#preface)).[¶](#section-3.2-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
