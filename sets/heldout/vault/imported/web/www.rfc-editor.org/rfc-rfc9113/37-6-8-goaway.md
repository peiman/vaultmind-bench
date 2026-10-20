---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#37-6-8-goaway.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-37-6-8-goaway
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.8. GOAWAY (1/2)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#37-6-8-goaway
source_hash: 06f2f24caeaf50ab22616ad62c2470d9949749c283dedecc14ab5decd5fbf780
---
The GOAWAY frame (type=0x07) is used to initiate shutdown of a connection or to signal serious error conditions. GOAWAY allows an endpoint to gracefully stop accepting new streams while still finishing processing of previously established streams. This enables administrative actions, like server maintenance.[¶](#section-6.8-1)

There is an inherent race condition between an endpoint starting new streams and the remote peer sending a GOAWAY frame. To deal with this case, the GOAWAY contains the stream identifier of the last peer-initiated stream that was or might be processed on the sending endpoint in this connection. For instance, if the server sends a GOAWAY frame, the identified stream is the highest-numbered stream initiated by the client.[¶](#section-6.8-2)

Once the GOAWAY is sent, the sender will ignore frames sent on streams initiated by the receiver if the stream has an identifier higher than the included last stream identifier. Receivers of a GOAWAY frame MUST NOT open additional streams on the connection, although a new connection can be established for new streams.[¶](#section-6.8-3)

If the receiver of the GOAWAY has sent data on streams with a higher stream identifier than what is indicated in the GOAWAY frame, those streams are not or will not be processed. The receiver of the GOAWAY frame can treat the streams as though they had never been created at all, thereby allowing those streams to be retried later on a new connection.[¶](#section-6.8-4)

Endpoints SHOULD always send a GOAWAY frame before closing a connection so that the remote peer can know whether a stream has been partially processed or not. For example, if an HTTP client sends a POST at the same time that a server closes a connection, the client cannot know if the server started to process that POST request if the server does not send a GOAWAY frame to indicate what streams it might have acted on.[¶](#section-6.8-5)

An endpoint might choose to close a connection without sending a GOAWAY for misbehaving peers.[¶](#section-6.8-6)

A GOAWAY frame might not immediately precede closing of the connection; a receiver of a GOAWAY that has no more use for the connection SHOULD still send a GOAWAY frame before terminating the connection.[¶](#section-6.8-7)

```
GOAWAY Frame {
  Length (24),
  Type (8) = 0x07,

Unused Flags (8),

Reserved (1),
  Stream Identifier (31) = 0,

Reserved (1),
  Last-Stream-ID (31),
  Error Code (32),
  Additional Debug Data (..),
}
```

[Figure 10](#figure-10): [GOAWAY Frame Format](#name-goaway-frame-format)

The Length, Type, Unused Flag(s), Reserved, and Stream Identifier fields are described in [Section 4](#FramingLayer).[¶](#section-6.8-9)

The GOAWAY frame does not define any flags.[¶](#section-6.8-10)

The GOAWAY frame applies to the connection, not a specific stream. An endpoint MUST treat a [GOAWAY](#GOAWAY) frame with a stream identifier other than 0x00 as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.8-11)

The last stream identifier in the GOAWAY frame contains the highest-numbered stream identifier for which the sender of the GOAWAY frame might have taken some action on or might yet take action on. All streams up to and including the identified stream might have been processed in some way. The last stream identifier can be set to 0 if no streams were processed.[¶](#section-6.8-12)

If a connection terminates without a GOAWAY frame, the last stream identifier is effectively the highest possible stream identifier.[¶](#section-6.8-14)

On streams with lower- or equal-numbered identifiers that were not closed completely prior to the connection being closed, reattempting requests, transactions, or any protocol activity is not possible, except for idempotent actions like HTTP GET, PUT, or DELETE. Any protocol activity that uses higher-numbered streams can be safely retried using a new connection.[¶](#section-6.8-15)

Activity on streams numbered lower than or equal to the last stream identifier might still complete successfully. The sender of a GOAWAY frame might gracefully shut down a connection by sending a GOAWAY frame, maintaining the connection in an "open" state until all in-progress streams complete.[¶](#section-6.8-16)

An endpoint MAY send multiple GOAWAY frames if circumstances change. For instance, an endpoint that sends GOAWAY with [NO\_ERROR](#NO_ERROR) during graceful shutdown could subsequently encounter a condition that requires immediate termination of the connection. The last stream identifier from the last GOAWAY frame received indicates which streams could have been acted upon. Endpoints MUST NOT increase the value they send in the last stream identifier, since the peers might already have retried unprocessed requests on another connection.[¶](#section-6.8-17)

A client that is unable to retry requests loses all requests that are in flight when the server closes the connection. This is especially true for intermediaries that might not be serving clients using HTTP/2. A server that is attempting to gracefully shut down a connection SHOULD send an initial GOAWAY frame with the last stream identifier set to 231-1 and a [NO\_ERROR](#NO_ERROR) code. This signals to the client that a shutdown is imminent and that initiating further requests is prohibited. After allowing time for any in-flight stream creation (at least one round-trip time), the server MAY send another GOAWAY frame with an updated last stream identifier. This ensures that a connection can be cleanly shut down without losing requests.[¶](#section-6.8-18)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
