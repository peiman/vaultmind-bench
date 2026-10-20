---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#30-6-4-rst-stream.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-30-6-4-rst-stream
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.4. RST\_STREAM'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#30-6-4-rst-stream
source_hash: 6b8ee2d8ec720981419f4c2afe1027c59327c0240fac1e970427365829ec6b27
---
The RST\_STREAM frame (type=0x03) allows for immediate termination of a stream. RST\_STREAM is sent to request cancellation of a stream or to indicate that an error condition has occurred.[¶](#section-6.4-1)

```
RST_STREAM Frame {
  Length (24) = 0x04,
  Type (8) = 0x03,

  Unused Flags (8),

  Reserved (1),
  Stream Identifier (31),

  Error Code (32),
}
```

[Figure 6](#figure-6): [RST\_STREAM Frame Format](#name-rst_stream-frame-format)

The Length, Type, Unused Flag(s), Reserved, and Stream Identifier fields are described in [Section 4](#FramingLayer). Additionally, the RST\_STREAM frame contains a single unsigned, 32-bit integer identifying the [error code](#ErrorCodes) ([Section 7](#ErrorCodes)). The error code indicates why the stream is being terminated.[¶](#section-6.4-3)

The RST\_STREAM frame does not define any flags.[¶](#section-6.4-4)

The RST\_STREAM frame fully terminates the referenced stream and causes it to enter the "closed" state. After receiving a RST\_STREAM on a stream, the receiver MUST NOT send additional frames for that stream, except for [PRIORITY](#PRIORITY). However, after sending the RST\_STREAM, the sending endpoint MUST be prepared to receive and process additional frames sent on the stream that might have been sent by the peer prior to the arrival of the RST\_STREAM.[¶](#section-6.4-5)

RST\_STREAM frames MUST be associated with a stream. If a RST\_STREAM frame is received with a stream identifier of 0x00, the recipient MUST treat this as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.4-6)

RST\_STREAM frames MUST NOT be sent for a stream in the "idle" state. If a RST\_STREAM frame identifying an idle stream is received, the recipient MUST treat this as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.4-7)

A RST\_STREAM frame with a length other than 4 octets MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [FRAME\_SIZE\_ERROR](#FRAME_SIZE_ERROR).[¶](#section-6.4-8)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
