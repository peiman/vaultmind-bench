---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#26-5-4-2-stream-error-handling.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-26-5-4-2-stream-error-handling
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.4. Error Handling › 5.4.2. Stream Error Handling'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#26-5-4-2-stream-error-handling
source_hash: 1f79bf22b3f34a2801d7a19a13f172a40a5ed936d7b016180493ff0e99b2b7ce
---
A stream error is an error related to a specific stream that does not affect processing of other streams.[¶](#section-5.4.2-1)

An endpoint that detects a stream error sends a [RST\_STREAM](#RST_STREAM) frame ([Section 6.4](#RST_STREAM)) that contains the stream identifier of the stream where the error occurred. The [RST\_STREAM](#RST_STREAM) frame includes an error code that indicates the type of error.[¶](#section-5.4.2-2)

A [RST\_STREAM](#RST_STREAM) is the last frame that an endpoint can send on a stream. The peer that sends the [RST\_STREAM](#RST_STREAM) frame MUST be prepared to receive any frames that were sent or enqueued for sending by the remote peer. These frames can be ignored, except where they modify connection state (such as the state maintained for [field section compression](#FieldBlock) ([Section 4.3](#FieldBlock)) or flow control).[¶](#section-5.4.2-3)

Normally, an endpoint SHOULD NOT send more than one [RST\_STREAM](#RST_STREAM) frame for any stream. However, an endpoint MAY send additional [RST\_STREAM](#RST_STREAM) frames if it receives frames on a closed stream after more than a round-trip time. This behavior is permitted to deal with misbehaving implementations.[¶](#section-5.4.2-4)

To avoid looping, an endpoint MUST NOT send a [RST\_STREAM](#RST_STREAM) in response to a [RST\_STREAM](#RST_STREAM) frame.[¶](#section-5.4.2-5)

#### 5.4.3. Connection Termination

If the TCP connection is closed or reset while streams remain in the "open" or "half-closed" states, then the affected streams cannot be automatically retried (see [Section 8.7](#Reliability) for details).[¶](#section-5.4.3-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
