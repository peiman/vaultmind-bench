---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#38-6-8-goaway.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-38-6-8-goaway
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.8. GOAWAY (2/2)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#38-6-8-goaway
source_hash: 6ca8cf430869009050d2ca33027216e5e45b46b7236048883916aa32cf126912
---
After sending a GOAWAY frame, the sender can discard frames for streams initiated by the receiver with identifiers higher than the identified last stream. However, any frames that alter connection state cannot be completely ignored. For instance, [HEADERS](#HEADERS), [PUSH\_PROMISE](#PUSH_PROMISE), and [CONTINUATION](#CONTINUATION) frames MUST be minimally processed to ensure that the state maintained for field section compression is consistent (see [Section 4.3](#FieldBlock)); similarly, DATA frames MUST be counted toward the connection flow-control window. Failure to process these frames can cause flow control or field section compression state to become unsynchronized.[¶](#section-6.8-19)

The GOAWAY frame also contains a 32-bit [error code](#ErrorCodes) ([Section 7](#ErrorCodes)) that contains the reason for closing the connection.[¶](#section-6.8-20)

Endpoints MAY append opaque data to the frame payload of any GOAWAY frame. Additional debug data is intended for diagnostic purposes only and carries no semantic value. Debug information could contain security- or privacy-sensitive data. Logged or otherwise persistently stored debug data MUST have adequate safeguards to prevent unauthorized access.[¶](#section-6.8-21)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
