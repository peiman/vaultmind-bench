---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#16-5-1-stream-states.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-16-5-1-stream-states
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.1. Stream States (1/3)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#16-5-1-stream-states
source_hash: 0c08e5d83670cfaff77d048cda90063e224921b37450527c71a025d86bfc796b
---
The lifecycle of a stream is shown in [Figure 2](#StreamStatesFigure).[¶](#section-5.1-1)

send PP recv PP idle send H / reserved recv H reserved (local) (remote) recv ES send ES send H open recv H half- half- closed send R / closed (remote) recv R (local) send ES / recv ES / send R / send R / recv R recv R send R / send R / recv R closed recv R [¶](#section-5.1-2.1.1)

[Figure 2](#figure-2): [Stream States](#name-stream-states-2)

`send`:

endpoint sends this frame[¶](#section-5.1-3.2)

`recv`:

endpoint receives this frame[¶](#section-5.1-3.4)

`H`:

[HEADERS](#HEADERS) frame (with implied [CONTINUATION](#CONTINUATION) frames)[¶](#section-5.1-3.6)

`ES`:

END\_STREAM flag[¶](#section-5.1-3.8)

`R`:

[RST\_STREAM](#RST_STREAM) frame[¶](#section-5.1-3.10)

`PP`:

[PUSH\_PROMISE](#PUSH_PROMISE) frame (with implied [CONTINUATION](#CONTINUATION) frames); state transitions are for the promised stream[¶](#section-5.1-3.12)

Note that this diagram shows stream state transitions and the frames and flags that affect those transitions only. In this regard, [CONTINUATION](#CONTINUATION) frames do not result in state transitions; they are effectively part of the [HEADERS](#HEADERS) or [PUSH\_PROMISE](#PUSH_PROMISE) that they follow. For the purpose of state transitions, the END\_STREAM flag is processed as a separate event to the frame that bears it; a [HEADERS](#HEADERS) frame with the END\_STREAM flag set can cause two state transitions.[¶](#section-5.1-4)

Both endpoints have a subjective view of the state of a stream that could be different when frames are in transit. Endpoints do not coordinate the creation of streams; they are created unilaterally by either endpoint. The negative consequences of a mismatch in states are limited to the "closed" state after sending [RST\_STREAM](#RST_STREAM), where frames might be received for some time after closing.[¶](#section-5.1-5)

Streams have the following states:[¶](#section-5.1-6)

idle:

All streams start in the "idle" state.[¶](#section-5.1-7.2.1)

The following transitions are valid from this state:[¶](#section-5.1-7.2.2)

- Sending a [HEADERS](#HEADERS) frame as a client, or receiving a HEADERS frame as a server, causes the stream to become "open". The stream identifier is selected as described in [Section 5.1.1](#StreamIdentifiers). The same [HEADERS](#HEADERS) frame can also cause a stream to immediately become "half-closed".[¶](#section-5.1-7.2.3.1)
- Sending a [PUSH\_PROMISE](#PUSH_PROMISE) frame on another stream reserves the idle stream that is identified for later use. The stream state for the reserved stream transitions to "reserved (local)". Only a server may send [PUSH\_PROMISE](#PUSH_PROMISE) frames.[¶](#section-5.1-7.2.3.2)
- Receiving a [PUSH\_PROMISE](#PUSH_PROMISE) frame on another stream reserves an idle stream that is identified for later use. The stream state for the reserved stream transitions to "reserved (remote)". Only a client may receive [PUSH\_PROMISE](#PUSH_PROMISE) frames.[¶](#section-5.1-7.2.3.3)
- Note that the [PUSH\_PROMISE](#PUSH_PROMISE) frame is not sent on the idle stream but references the newly reserved stream in the Promised Stream ID field.[¶](#section-5.1-7.2.3.4)
- Opening a stream with a higher-valued stream identifier causes the stream to transition immediately to a "closed" state; note that this transition is not shown in the diagram.[¶](#section-5.1-7.2.3.5)

Receiving any frame other than [HEADERS](#HEADERS) or [PRIORITY](#PRIORITY) on a stream in this state MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR). If this stream is initiated by the server, as described in [Section 5.1.1](#StreamIdentifiers), then receiving a [HEADERS](#HEADERS) frame MUST also be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-5.1-7.2.4)

reserved (local):

A stream in the "reserved (local)" state is one that has been promised by sending a [PUSH\_PROMISE](#PUSH_PROMISE) frame. A [PUSH\_PROMISE](#PUSH_PROMISE) frame reserves an idle stream by associating the stream with an open stream that was initiated by the remote peer (see [Section 8.4](#PushResources)).[¶](#section-5.1-7.4.1)

In this state, only the following transitions are possible:[¶](#section-5.1-7.4.2)

- The endpoint can send a [HEADERS](#HEADERS) frame. This causes the stream to open in a "half-closed (remote)" state.[¶](#section-5.1-7.4.3.1)
- Either endpoint can send a [RST\_STREAM](#RST_STREAM) frame to cause the stream to become "closed". This releases the stream reservation.[¶](#section-5.1-7.4.3.2)

An endpoint MUST NOT send any type of frame other than [HEADERS](#HEADERS), [RST\_STREAM](#RST_STREAM), or [PRIORITY](#PRIORITY) in this state.[¶](#section-5.1-7.4.4)

A [PRIORITY](#PRIORITY) or [WINDOW\_UPDATE](#WINDOW_UPDATE) frame MAY be received in this state. Receiving any type of frame other than [RST\_STREAM](#RST_STREAM), [PRIORITY](#PRIORITY), or [WINDOW\_UPDATE](#WINDOW_UPDATE) on a stream in this state MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-5.1-7.4.5)

reserved (remote):

A stream in the "reserved (remote)" state has been reserved by a remote peer.[¶](#section-5.1-7.6.1)

In this state, only the following transitions are possible:[¶](#section-5.1-7.6.2)

- Receiving a [HEADERS](#HEADERS) frame causes the stream to transition to "half-closed (local)".[¶](#section-5.1-7.6.3.1)
- Either endpoint can send a [RST\_STREAM](#RST_STREAM) frame to cause the stream to become "closed". This releases the stream reservation.[¶](#section-5.1-7.6.3.2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
