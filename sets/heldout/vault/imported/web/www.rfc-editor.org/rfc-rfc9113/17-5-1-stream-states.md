---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#17-5-1-stream-states.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-17-5-1-stream-states
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.1. Stream States (2/3)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#17-5-1-stream-states
source_hash: 41727e147d401678b31db7a903dda500ea9328d469477f1bfbc3302bf0b5dbb1
---
An endpoint MUST NOT send any type of frame other than [RST\_STREAM](#RST_STREAM), [WINDOW\_UPDATE](#WINDOW_UPDATE), or [PRIORITY](#PRIORITY) in this state.[¶](#section-5.1-7.6.4)

Receiving any type of frame other than [HEADERS](#HEADERS), [RST\_STREAM](#RST_STREAM), or [PRIORITY](#PRIORITY) on a stream in this state MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-5.1-7.6.5)

open:

A stream in the "open" state may be used by both peers to send frames of any type. In this state, sending peers observe advertised [stream-level flow-control limits](#FlowControl) ([Section 5.2](#FlowControl)).[¶](#section-5.1-7.8.1)

From this state, either endpoint can send a frame with an END\_STREAM flag set, which causes the stream to transition into one of the "half-closed" states. An endpoint sending an END\_STREAM flag causes the stream state to become "half-closed (local)"; an endpoint receiving an END\_STREAM flag causes the stream state to become "half-closed (remote)".[¶](#section-5.1-7.8.2)

Either endpoint can send a [RST\_STREAM](#RST_STREAM) frame from this state, causing it to transition immediately to "closed".[¶](#section-5.1-7.8.3)

half-closed (local):

A stream that is in the "half-closed (local)" state cannot be used for sending frames other than [WINDOW\_UPDATE](#WINDOW_UPDATE), [PRIORITY](#PRIORITY), and [RST\_STREAM](#RST_STREAM).[¶](#section-5.1-7.10.1)

A stream transitions from this state to "closed" when a frame is received with the END\_STREAM flag set or when either peer sends a [RST\_STREAM](#RST_STREAM) frame.[¶](#section-5.1-7.10.2)

An endpoint can receive any type of frame in this state. Providing flow-control credit using [WINDOW\_UPDATE](#WINDOW_UPDATE) frames is necessary to continue receiving flow-controlled frames. In this state, a receiver can ignore [WINDOW\_UPDATE](#WINDOW_UPDATE) frames, which might arrive for a short period after a frame with the END\_STREAM flag set is sent.[¶](#section-5.1-7.10.3)

[PRIORITY](#PRIORITY) frames can be received in this state.[¶](#section-5.1-7.10.4)

half-closed (remote):

A stream that is "half-closed (remote)" is no longer being used by the peer to send frames. In this state, an endpoint is no longer obligated to maintain a receiver flow-control window.[¶](#section-5.1-7.12.1)

If an endpoint receives additional frames, other than [WINDOW\_UPDATE](#WINDOW_UPDATE), [PRIORITY](#PRIORITY), or [RST\_STREAM](#RST_STREAM), for a stream that is in this state, it MUST respond with a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [STREAM\_CLOSED](#STREAM_CLOSED).[¶](#section-5.1-7.12.2)

A stream that is "half-closed (remote)" can be used by the endpoint to send frames of any type. In this state, the endpoint continues to observe advertised [stream-level flow-control limits](#FlowControl) ([Section 5.2](#FlowControl)).[¶](#section-5.1-7.12.3)

A stream can transition from this state to "closed" by sending a frame with the END\_STREAM flag set or when either peer sends a [RST\_STREAM](#RST_STREAM) frame.[¶](#section-5.1-7.12.4)

closed:

The "closed" state is the terminal state.[¶](#section-5.1-7.14.1)

A stream enters the "closed" state after an endpoint both sends and receives a frame with an END\_STREAM flag set. A stream also enters the "closed" state after an endpoint either sends or receives a [RST\_STREAM](#RST_STREAM) frame.[¶](#section-5.1-7.14.2)

An endpoint MUST NOT send frames other than [PRIORITY](#PRIORITY) on a closed stream. An endpoint MAY treat receipt of any other type of frame on a closed stream as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [STREAM\_CLOSED](#STREAM_CLOSED), except as noted below.[¶](#section-5.1-7.14.3)

An endpoint that sends a frame with the END\_STREAM flag set or a [RST\_STREAM](#RST_STREAM) frame might receive a [WINDOW\_UPDATE](#WINDOW_UPDATE) or [RST\_STREAM](#RST_STREAM) frame from its peer in the time before the peer receives and processes the frame that closes the stream.[¶](#section-5.1-7.14.4)

An endpoint that sends a [RST\_STREAM](#RST_STREAM) frame on a stream that is in the "open" or "half-closed (local)" state could receive any type of frame. The peer might have sent or enqueued for sending these frames before processing the [RST\_STREAM](#RST_STREAM) frame. An endpoint MUST minimally process and then discard any frames it receives in this state. This means updating header compression state for [HEADERS](#HEADERS) and [PUSH\_PROMISE](#PUSH_PROMISE) frames. Receiving a [PUSH\_PROMISE](#PUSH_PROMISE) frame also causes the promised stream to become "reserved (remote)", even when the [PUSH\_PROMISE](#PUSH_PROMISE) frame is received on a closed stream. Additionally, the content of [DATA](#DATA) frames counts toward the connection flow-control window.[¶](#section-5.1-7.14.5)

An endpoint can perform this minimal processing for all streams that are in the "closed" state. Endpoints MAY use other signals to detect that a peer has received the frames that caused the stream to enter the "closed" state and treat receipt of any frame other than [PRIORITY](#PRIORITY) as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR). Endpoints can use frames that indicate that the peer has received the closing signal to drive this. Endpoints SHOULD NOT use timers for this purpose. For example, an endpoint that sends a [SETTINGS](#SETTINGS) frame after closing a stream can safely treat receipt of a [DATA](#DATA) frame on that stream as an error after receiving an acknowledgment of the settings. Other things that might be used are [PING](#PING) frames, receiving data on streams that were created after closing the stream, or responses to requests created after closing the stream.[¶](#section-5.1-7.14.6)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
