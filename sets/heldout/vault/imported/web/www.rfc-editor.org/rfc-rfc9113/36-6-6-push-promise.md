---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#36-6-6-push-promise.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-36-6-6-push-promise
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.6. PUSH\_PROMISE (2/2)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#36-6-6-push-promise
source_hash: b122b99a686888634122bfb99962c1631d7b8b46bbbe13c548e86746e2f192e5
---
The total number of padding octets is determined by the value of the Pad Length field. If the length of the padding is the length of the frame payload or greater, the recipient MUST treat this as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.6-14)

### 6.7. PING

The PING frame (type=0x06) is a mechanism for measuring a minimal round-trip time from the sender, as well as determining whether an idle connection is still functional. PING frames can be sent from any endpoint.[¶](#section-6.7-1)

```
PING Frame {
  Length (24) = 0x08,
  Type (8) = 0x06,

  Unused Flags (7),
  ACK Flag (1),

  Reserved (1),
  Stream Identifier (31) = 0,

  Opaque Data (64),
}
```

[Figure 9](#figure-9): [PING Frame Format](#name-ping-frame-format)

The Length, Type, Unused Flag(s), Reserved, and Stream Identifier fields are described in [Section 4](#FramingLayer).[¶](#section-6.7-3)

In addition to the frame header, PING frames MUST contain 8 octets of opaque data in the frame payload. A sender can include any value it chooses and use those octets in any fashion.[¶](#section-6.7-4)

Receivers of a PING frame that does not include an ACK flag MUST send a PING frame with the ACK flag set in response, with an identical frame payload. PING responses SHOULD be given higher priority than any other frame.[¶](#section-6.7-5)

The PING frame defines the following flags:[¶](#section-6.7-6)

ACK (0x01):

When set, the ACK flag indicates that this PING frame is a PING response. An endpoint MUST set this flag in PING responses. An endpoint MUST NOT respond to PING frames containing this flag.[¶](#section-6.7-7.2)

PING frames are not associated with any individual stream. If a PING frame is received with a Stream Identifier field value other than 0x00, the recipient MUST respond with a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.7-8)

Receipt of a PING frame with a length field value other than 8 MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [FRAME\_SIZE\_ERROR](#FRAME_SIZE_ERROR).[¶](#section-6.7-9)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
