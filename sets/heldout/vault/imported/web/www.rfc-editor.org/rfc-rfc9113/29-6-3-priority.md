---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#29-6-3-priority.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-29-6-3-priority
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.3. PRIORITY'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#29-6-3-priority
source_hash: 1a81f7a6b328b4ec397f3c3239c800da76a3e90c29b4600dd4d7ac16dacdbc94
---
The PRIORITY frame (type=0x02) is deprecated; see [Section 5.3.2](#PriorityHere). A PRIORITY frame can be sent in any stream state, including idle or closed streams.[¶](#section-6.3-1)

```
PRIORITY Frame {
  Length (24) = 0x05,
  Type (8) = 0x02,

  Unused Flags (8),

  Reserved (1),
  Stream Identifier (31),

  Exclusive (1),
  Stream Dependency (31),
  Weight (8),
}
```

[Figure 5](#figure-5): [PRIORITY Frame Format](#name-priority-frame-format)

The Length, Type, Unused Flag(s), Reserved, and Stream Identifier fields are described in [Section 4](#FramingLayer). The frame payload of a PRIORITY frame contains the following additional fields:[¶](#section-6.3-3)

Exclusive:

A single-bit flag.[¶](#section-6.3-4.2)

Stream Dependency:

A 31-bit stream identifier.[¶](#section-6.3-4.4)

Weight:

An unsigned 8-bit integer.[¶](#section-6.3-4.6)

The PRIORITY frame does not define any flags.[¶](#section-6.3-5)

The PRIORITY frame always identifies a stream. If a PRIORITY frame is received with a stream identifier of 0x00, the recipient MUST respond with a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.3-6)

Sending or receiving a PRIORITY frame does not affect the state of any stream ([Section 5.1](#StreamStates)). The PRIORITY frame can be sent on a stream in any state, including "idle" or "closed". A PRIORITY frame cannot be sent between consecutive frames that comprise a single [field block](#FieldBlock) ([Section 4.3](#FieldBlock)).[¶](#section-6.3-7)

A PRIORITY frame with a length other than 5 octets MUST be treated as a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [FRAME\_SIZE\_ERROR](#FRAME_SIZE_ERROR).[¶](#section-6.3-8)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
