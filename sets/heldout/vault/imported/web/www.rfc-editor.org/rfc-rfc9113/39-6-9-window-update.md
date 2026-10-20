---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#39-6-9-window-update.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-39-6-9-window-update
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.9. WINDOW\_UPDATE'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#39-6-9-window-update
source_hash: 8406b1d6da8b1eb65f650882e91a2e83f88488f0f5df3e89f10a5a8ee97e5591
---
The WINDOW\_UPDATE frame (type=0x08) is used to implement flow control; see [Section 5.2](#FlowControl) for an overview.[¶](#section-6.9-1)

Flow control operates at two levels: on each individual stream and on the entire connection.[¶](#section-6.9-2)

Both types of flow control are hop by hop, that is, only between the two endpoints. Intermediaries do not forward WINDOW\_UPDATE frames between dependent connections. However, throttling of data transfer by any receiver can indirectly cause the propagation of flow-control information toward the original sender.[¶](#section-6.9-3)

Flow control only applies to frames that are identified as being subject to flow control. Of the frame types defined in this document, this includes only [DATA](#DATA) frames. Frames that are exempt from flow control MUST be accepted and processed, unless the receiver is unable to assign resources to handling the frame. A receiver MAY respond with a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) or [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [FLOW\_CONTROL\_ERROR](#FLOW_CONTROL_ERROR) if it is unable to accept a frame.[¶](#section-6.9-4)

```
WINDOW_UPDATE Frame {
  Length (24) = 0x04,
  Type (8) = 0x08,

  Unused Flags (8),

  Reserved (1),
  Stream Identifier (31),

  Reserved (1),
  Window Size Increment (31),
}
```

[Figure 11](#figure-11): [WINDOW\_UPDATE Frame Format](#name-window_update-frame-format)

The Length, Type, Unused Flag(s), Reserved, and Stream Identifier fields are described in [Section 4](#FramingLayer). The frame payload of a WINDOW\_UPDATE frame is one reserved bit plus an unsigned 31-bit integer indicating the number of octets that the sender can transmit in addition to the existing flow-control window. The legal range for the increment to the flow-control window is 1 to 231-1 (2,147,483,647) octets.[¶](#section-6.9-6)

The WINDOW\_UPDATE frame does not define any flags.[¶](#section-6.9-7)

The WINDOW\_UPDATE frame can be specific to a stream or to the entire connection. In the former case, the frame's stream identifier indicates the affected stream; in the latter, the value "0" indicates that the entire connection is the subject of the frame.[¶](#section-6.9-8)

A receiver MUST treat the receipt of a WINDOW\_UPDATE frame with a flow-control window increment of 0 as a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR); errors on the connection flow-control window MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)).[¶](#section-6.9-9)

WINDOW\_UPDATE can be sent by a peer that has sent a frame with the END\_STREAM flag set. This means that a receiver could receive a WINDOW\_UPDATE frame on a stream in a "half-closed (remote)" or "closed" state. A receiver MUST NOT treat this as an error (see [Section 5.1](#StreamStates)).[¶](#section-6.9-10)

A receiver that receives a flow-controlled frame MUST always account for its contribution against the connection flow-control window, unless the receiver treats this as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)). This is necessary even if the frame is in error. The sender counts the frame toward the flow-control window, but if the receiver does not, the flow-control window at the sender and receiver can become different.[¶](#section-6.9-11)

A WINDOW\_UPDATE frame with a length other than 4 octets MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [FRAME\_SIZE\_ERROR](#FRAME_SIZE_ERROR).[¶](#section-6.9-12)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
