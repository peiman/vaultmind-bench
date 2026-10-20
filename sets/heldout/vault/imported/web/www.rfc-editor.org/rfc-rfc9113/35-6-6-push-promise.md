---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#35-6-6-push-promise.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-35-6-6-push-promise
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.6. PUSH\_PROMISE (1/2)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#35-6-6-push-promise
source_hash: 160751d4d9b33be751521755589b21bc3cab0ad86fafbe6805009e342bc5cf8f
---
The PUSH\_PROMISE frame (type=0x05) is used to notify the peer endpoint in advance of streams the sender intends to initiate. The PUSH\_PROMISE frame includes the unsigned 31-bit identifier of the stream the endpoint plans to create along with a field section that provides additional context for the stream. [Section 8.4](#PushResources) contains a thorough description of the use of PUSH\_PROMISE frames.[¶](#section-6.6-1)

```
PUSH_PROMISE Frame {
  Length (24),
  Type (8) = 0x05,

Unused Flags (4),
  PADDED Flag (1),
  END_HEADERS Flag (1),
  Unused Flags (2),

Reserved (1),
  Stream Identifier (31),

[Pad Length (8)],
  Reserved (1),
  Promised Stream ID (31),
  Field Block Fragment (..),
  Padding (..2040),
}
```

[Figure 8](#figure-8): [PUSH\_PROMISE Frame Format](#name-push_promise-frame-format)

The Length, Type, Unused Flag(s), Reserved, and Stream Identifier fields are described in [Section 4](#FramingLayer). The PUSH\_PROMISE frame payload has the following additional fields:[¶](#section-6.6-3)

Pad Length:

An 8-bit field containing the length of the frame padding in units of octets. This field is only present if the PADDED flag is set.[¶](#section-6.6-4.2)

Promised Stream ID:

An unsigned 31-bit integer that identifies the stream that is reserved by the PUSH\_PROMISE. The promised stream identifier MUST be a valid choice for the next stream sent by the sender (see "new stream identifier" in [Section 5.1.1](#StreamIdentifiers)).[¶](#section-6.6-4.4)

Field Block Fragment:

A [field block fragment](#FieldBlock) ([Section 4.3](#FieldBlock)) containing the request control data and a header section.[¶](#section-6.6-4.6)

Padding:

Padding octets that contain no application semantic value. Padding octets MUST be set to zero when sending. A receiver is not obligated to verify padding but MAY treat non-zero padding as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.6-4.8)

The PUSH\_PROMISE frame defines the following flags:[¶](#section-6.6-5)

PADDED (0x08):

When set, the PADDED flag indicates that the Pad Length field and any padding that it describes are present.[¶](#section-6.6-6.2.1)

END\_HEADERS (0x04):

When set, the END\_HEADERS flag indicates that this frame contains an entire [field block](#FieldBlock) ([Section 4.3](#FieldBlock)) and is not followed by any [CONTINUATION](#CONTINUATION) frames.[¶](#section-6.6-6.4.1)

A PUSH\_PROMISE frame without the END\_HEADERS flag set MUST be followed by a CONTINUATION frame for the same stream. A receiver MUST treat the receipt of any other type of frame or a frame on a different stream as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.6-6.4.2)

PUSH\_PROMISE frames MUST only be sent on a peer-initiated stream that is in either the "open" or "half-closed (remote)" state. The stream identifier of a PUSH\_PROMISE frame indicates the stream it is associated with. If the Stream Identifier field specifies the value 0x00, a recipient MUST respond with a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.6-7)

Promised streams are not required to be used in the order they are promised. The PUSH\_PROMISE only reserves stream identifiers for later use.[¶](#section-6.6-8)

PUSH\_PROMISE MUST NOT be sent if the [SETTINGS\_ENABLE\_PUSH](#SETTINGS_ENABLE_PUSH) setting of the peer endpoint is set to 0. An endpoint that has set this setting and has received acknowledgment MUST treat the receipt of a PUSH\_PROMISE frame as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.6-9)

Recipients of PUSH\_PROMISE frames can choose to reject promised streams by returning a [RST\_STREAM](#RST_STREAM) referencing the promised stream identifier back to the sender of the PUSH\_PROMISE.[¶](#section-6.6-10)

A PUSH\_PROMISE frame modifies the connection state in two ways. First, the inclusion of a [field block](#FieldBlock) ([Section 4.3](#FieldBlock)) potentially modifies the state maintained for field section compression. Second, PUSH\_PROMISE also reserves a stream for later use, causing the promised stream to enter the "reserved (local)" or "reserved (remote)" state. A sender MUST NOT send a PUSH\_PROMISE on a stream unless that stream is either "open" or "half-closed (remote)"; the sender MUST ensure that the promised stream is a valid choice for a [new stream identifier](#StreamIdentifiers) ([Section 5.1.1](#StreamIdentifiers)) (that is, the promised stream MUST be in the "idle" state).[¶](#section-6.6-11)

Since PUSH\_PROMISE reserves a stream, ignoring a PUSH\_PROMISE frame causes the stream state to become indeterminate. A receiver MUST treat the receipt of a PUSH\_PROMISE on a stream that is neither "open" nor "half-closed (local)" as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR). However, an endpoint that has sent [RST\_STREAM](#RST_STREAM) on the associated stream MUST handle PUSH\_PROMISE frames that might have been created before the [RST\_STREAM](#RST_STREAM) frame is received and processed.[¶](#section-6.6-12)

A receiver MUST treat the receipt of a PUSH\_PROMISE that promises an [illegal stream identifier](#StreamIdentifiers) ([Section 5.1.1](#StreamIdentifiers)) as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR). Note that an illegal stream identifier is an identifier for a stream that is not currently in the "idle" state.[¶](#section-6.6-13)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
