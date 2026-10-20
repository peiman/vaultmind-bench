---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#40-6-9-1-the-flow-control-window.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-40-6-9-1-the-flow-control-window
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.9. WINDOW\_UPDATE › 6.9.1. The Flow-Control Window'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#40-6-9-1-the-flow-control-window
source_hash: 38774766fcb3e9acb33cfee5077732b3eab6317e0510be635cebb0b39a6f5bf1
---
Flow control in HTTP/2 is implemented using a window kept by each sender on every stream. The flow-control window is a simple integer value that indicates how many octets of data the sender is permitted to transmit; as such, its size is a measure of the buffering capacity of the receiver.[¶](#section-6.9.1-1)

Two flow-control windows are applicable: the stream flow-control window and the connection flow-control window. The sender MUST NOT send a flow-controlled frame with a length that exceeds the space available in either of the flow-control windows advertised by the receiver. Frames with zero length with the END\_STREAM flag set (that is, an empty [DATA](#DATA) frame) MAY be sent if there is no available space in either flow-control window.[¶](#section-6.9.1-2)

For flow-control calculations, the 9-octet frame header is not counted.[¶](#section-6.9.1-3)

After sending a flow-controlled frame, the sender reduces the space available in both windows by the length of the transmitted frame.[¶](#section-6.9.1-4)

The receiver of a frame sends a WINDOW\_UPDATE frame as it consumes data and frees up space in flow-control windows. Separate WINDOW\_UPDATE frames are sent for the stream- and connection-level flow-control windows. Receivers are advised to have mechanisms in place to avoid sending WINDOW\_UPDATE frames with very small increments; see [Section 4.2.3.3](https://www.rfc-editor.org/rfc/rfc1122#section-4.2.3.3) of \[[RFC1122](#RFC1122)].[¶](#section-6.9.1-5)

A sender that receives a WINDOW\_UPDATE frame updates the corresponding window by the amount specified in the frame.[¶](#section-6.9.1-6)

A sender MUST NOT allow a flow-control window to exceed 231-1 octets. If a sender receives a WINDOW\_UPDATE that causes a flow-control window to exceed this maximum, it MUST terminate either the stream or the connection, as appropriate. For streams, the sender sends a [RST\_STREAM](#RST_STREAM) with an error code of [FLOW\_CONTROL\_ERROR](#FLOW_CONTROL_ERROR); for the connection, a [GOAWAY](#GOAWAY) frame with an error code of [FLOW\_CONTROL\_ERROR](#FLOW_CONTROL_ERROR) is sent.[¶](#section-6.9.1-7)

Flow-controlled frames from the sender and WINDOW\_UPDATE frames from the receiver are completely asynchronous with respect to each other. This property allows a receiver to aggressively update the window size kept by the sender to prevent streams from stalling.[¶](#section-6.9.1-8)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
