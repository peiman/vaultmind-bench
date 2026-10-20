---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#62-10-7-use-of-padding.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-62-10-7-use-of-padding
type: reference
title: 'RFC 9113: HTTP/2 › 10. Security Considerations › 10.7. Use of Padding'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#62-10-7-use-of-padding
source_hash: 26cad03e3b7e7f883f6a6cced2528b414905cb2bf4c0b03833050c730b100cce
---
Padding within HTTP/2 is not intended as a replacement for general purpose padding, such as that provided by [TLS](#RFC8446) \[[TLS13](#RFC8446)]. Redundant padding could even be counterproductive. Correct application can depend on having specific knowledge of the data that is being padded.[¶](#section-10.7-1)

To mitigate attacks that rely on compression, disabling or limiting compression might be preferable to padding as a countermeasure.[¶](#section-10.7-2)

Padding can be used to obscure the exact size of frame content and is provided to mitigate specific attacks within HTTP -- for example, attacks where compressed content includes both attacker-controlled plaintext and secret data (e.g., \[[BREACH](#BREACH)]).[¶](#section-10.7-3)

Use of padding can result in less protection than might seem immediately obvious. At best, padding only makes it more difficult for an attacker to infer length information by increasing the number of frames an attacker has to observe. Incorrectly implemented padding schemes can be easily defeated. In particular, randomized padding with a predictable distribution provides very little protection; similarly, padding frame payloads to a fixed size exposes information as frame payload sizes cross the fixed-sized boundary, which could be possible if an attacker can control plaintext.[¶](#section-10.7-4)

Intermediaries SHOULD retain padding for [DATA](#DATA) frames but MAY drop padding for [HEADERS](#HEADERS) and [PUSH\_PROMISE](#PUSH_PROMISE) frames. A valid reason for an intermediary to change the amount of padding of frames is to improve the protections that padding provides.[¶](#section-10.7-5)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
