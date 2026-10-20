---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#07-2-2-conventions-and-terminology.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-07-2-2-conventions-and-terminology
type: reference
title: 'RFC 9113: HTTP/2 › 2. HTTP/2 Protocol Overview › 2.2. Conventions and Terminology'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#07-2-2-conventions-and-terminology
source_hash: cc3887d7ae6402bf5f2e91fdb97e6f6b36470355ed566814b4194e827ff71140
---
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 \[[RFC2119](#RFC2119)] \[[RFC8174](#RFC8174)] when, and only when, they appear in all capitals, as shown here.[¶](#section-2.2-1)

All numeric values are in network byte order. Values are unsigned unless otherwise indicated. Literal values are provided in decimal or hexadecimal as appropriate. Hexadecimal literals are prefixed with "`0x`" to distinguish them from decimal literals.[¶](#section-2.2-2)

This specification describes binary formats using the conventions described in [Section 1.3](https://www.rfc-editor.org/rfc/rfc9000#section-1.3) of RFC 9000 \[[QUIC](#RFC9000)]. Note that this format uses network byte order and that high-valued bits are listed before low-valued bits.[¶](#section-2.2-3)

The following terms are used:[¶](#section-2.2-4)

client:

The endpoint that initiates an HTTP/2 connection. Clients send HTTP requests and receive HTTP responses.[¶](#section-2.2-5.2)

connection:

A transport-layer connection between two endpoints.[¶](#section-2.2-5.4)

connection error:

An error that affects the entire HTTP/2 connection.[¶](#section-2.2-5.6)

endpoint:

Either the client or server of the connection.[¶](#section-2.2-5.8)

frame:

The smallest unit of communication within an HTTP/2 connection, consisting of a header and a variable-length sequence of octets structured according to the frame type.[¶](#section-2.2-5.10)

peer:

An endpoint. When discussing a particular endpoint, "peer" refers to the endpoint that is remote to the primary subject of discussion.[¶](#section-2.2-5.12)

receiver:

An endpoint that is receiving frames.[¶](#section-2.2-5.14)

sender:

An endpoint that is transmitting frames.[¶](#section-2.2-5.16)

server:

The endpoint that accepts an HTTP/2 connection. Servers receive HTTP requests and send HTTP responses.[¶](#section-2.2-5.18)

stream:

A bidirectional flow of frames within the HTTP/2 connection.[¶](#section-2.2-5.20)

stream error:

An error on the individual HTTP/2 stream.[¶](#section-2.2-5.22)

Finally, the terms "gateway", "intermediary", "proxy", and "tunnel" are defined in [Section 3.7](https://www.rfc-editor.org/rfc/rfc9110#section-3.7) of \[[HTTP](#RFC9110)]. Intermediaries act as both client and server at different times.[¶](#section-2.2-6)

The term "content" as it applies to message bodies is defined in [Section 6.4](https://www.rfc-editor.org/rfc/rfc9110#section-6.4) of \[[HTTP](#RFC9110)].[¶](#section-2.2-7)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
