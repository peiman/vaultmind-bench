---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#61-10-6-use-of-compression.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-61-10-6-use-of-compression
type: reference
title: 'RFC 9113: HTTP/2 › 10. Security Considerations › 10.6. Use of Compression'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#61-10-6-use-of-compression
source_hash: a512bd608a3a204cf61145660dbf13f553045f25c28bfcba2f952a98686e16ec
---
Compression can allow an attacker to recover secret data when it is compressed in the same context as data under attacker control. HTTP/2 enables compression of field lines ([Section 4.3](#FieldBlock)); the following concerns also apply to the use of HTTP compressed content-codings ([Section 8.4.1](https://www.rfc-editor.org/rfc/rfc9110#section-8.4.1) of \[[HTTP](#RFC9110)]).[¶](#section-10.6-1)

There are demonstrable attacks on compression that exploit the characteristics of the Web (e.g., \[[BREACH](#BREACH)]). The attacker induces multiple requests containing varying plaintext, observing the length of the resulting ciphertext in each, which reveals a shorter length when a guess about the secret is correct.[¶](#section-10.6-2)

Implementations communicating on a secure channel MUST NOT compress content that includes both confidential and attacker-controlled data unless separate compression dictionaries are used for each source of data. Compression MUST NOT be used if the source of data cannot be reliably determined. Generic stream compression, such as that provided by TLS, MUST NOT be used with HTTP/2 (see [Section 9.2](#TLSUsage)).[¶](#section-10.6-3)

Further considerations regarding the compression of header fields are described in \[[COMPRESSION](#RFC7541)].[¶](#section-10.6-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
