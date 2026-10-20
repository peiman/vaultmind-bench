---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#43-6-10-continuation.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-43-6-10-continuation
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.10. CONTINUATION'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#43-6-10-continuation
source_hash: f5faf06b2d73243c79d3c27343fc1376d30e7f46c129f0dcfb8bdbe9695ef984
---
The CONTINUATION frame (type=0x09) is used to continue a sequence of [field block fragments](#FieldBlock) ([Section 4.3](#FieldBlock)). Any number of CONTINUATION frames can be sent, as long as the preceding frame is on the same stream and is a [HEADERS](#HEADERS), [PUSH\_PROMISE](#PUSH_PROMISE), or CONTINUATION frame without the END\_HEADERS flag set.[¶](#section-6.10-1)

```
CONTINUATION Frame {
  Length (24),
  Type (8) = 0x09,

  Unused Flags (5),
  END_HEADERS Flag (1),
  Unused Flags (2),

  Reserved (1),
  Stream Identifier (31),

  Field Block Fragment (..),
}
```

[Figure 12](#figure-12): [CONTINUATION Frame Format](#name-continuation-frame-format)

The Length, Type, Unused Flag(s), Reserved, and Stream Identifier fields are described in [Section 4](#FramingLayer). The CONTINUATION frame payload contains a [field block fragment](#FieldBlock) ([Section 4.3](#FieldBlock)).[¶](#section-6.10-3)

The CONTINUATION frame defines the following flag:[¶](#section-6.10-4)

END\_HEADERS (0x04):

When set, the END\_HEADERS flag indicates that this frame ends a [field block](#FieldBlock) ([Section 4.3](#FieldBlock)).[¶](#section-6.10-5.2.1)

If the END\_HEADERS flag is not set, this frame MUST be followed by another CONTINUATION frame. A receiver MUST treat the receipt of any other type of frame or a frame on a different stream as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.10-5.2.2)

The CONTINUATION frame changes the connection state as defined in [Section 4.3](#FieldBlock).[¶](#section-6.10-6)

CONTINUATION frames MUST be associated with a stream. If a CONTINUATION frame is received with a Stream Identifier field of 0x00, the recipient MUST respond with a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type PROTOCOL\_ERROR.[¶](#section-6.10-7)

A CONTINUATION frame MUST be preceded by a [HEADERS](#HEADERS), [PUSH\_PROMISE](#PUSH_PROMISE) or CONTINUATION frame without the END\_HEADERS flag set. A recipient that observes violation of this rule MUST respond with a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.10-8)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
