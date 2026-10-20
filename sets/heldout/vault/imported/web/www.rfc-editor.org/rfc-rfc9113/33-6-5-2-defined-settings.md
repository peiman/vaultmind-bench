---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#33-6-5-2-defined-settings.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-33-6-5-2-defined-settings
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.5. SETTINGS › 6.5.2. Defined Settings'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#33-6-5-2-defined-settings
source_hash: 555c5340f81d605e85b4712c4ec44e1fd9e4d326fab62209aabff422b7cc397f
---
The following settings are defined:[¶](#section-6.5.2-1)

This setting allows the sender to inform the remote endpoint of the maximum size of the compression table used to decode field blocks, in units of octets. The encoder can select any size equal to or less than this value by using signaling specific to the compression format inside a field block (see \[[COMPRESSION](#RFC7541)]). The initial value is 4,096 octets.[¶](#section-6.5.2-2.2.1)

SETTINGS\_ENABLE\_PUSH (0x02):

This setting can be used to enable or disable server push. A server MUST NOT send a [PUSH\_PROMISE](#PUSH_PROMISE) frame if it receives this parameter set to a value of 0; see [Section 8.4](#PushResources). A client that has both set this parameter to 0 and had it acknowledged MUST treat the receipt of a [PUSH\_PROMISE](#PUSH_PROMISE) frame as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.5.2-2.4.1)

The initial value of SETTINGS\_ENABLE\_PUSH is 1. For a client, this value indicates that it is willing to receive PUSH\_PROMISE frames. For a server, this initial value has no effect, and is equivalent to the value 0. Any value other than 0 or 1 MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.5.2-2.4.2)

A server MUST NOT explicitly set this value to 1. A server MAY choose to omit this setting when it sends a SETTINGS frame, but if a server does include a value, it MUST be 0. A client MUST treat receipt of a SETTINGS frame with SETTINGS\_ENABLE\_PUSH set to 1 as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.5.2-2.4.3)

SETTINGS\_MAX\_CONCURRENT\_STREAMS (0x03):

This setting indicates the maximum number of concurrent streams that the sender will allow. This limit is directional: it applies to the number of streams that the sender permits the receiver to create. Initially, there is no limit to this value. It is recommended that this value be no smaller than 100, so as to not unnecessarily limit parallelism.[¶](#section-6.5.2-2.6.1)

A value of 0 for SETTINGS\_MAX\_CONCURRENT\_STREAMS SHOULD NOT be treated as special by endpoints. A zero value does prevent the creation of new streams; however, this can also happen for any limit that is exhausted with active streams. Servers SHOULD only set a zero value for short durations; if a server does not wish to accept requests, closing the connection is more appropriate.[¶](#section-6.5.2-2.6.2)

SETTINGS\_INITIAL\_WINDOW\_SIZE (0x04):

This setting indicates the sender's initial window size (in units of octets) for stream-level flow control. The initial value is 216-1 (65,535) octets.[¶](#section-6.5.2-2.8.1)

This setting affects the window size of all streams (see [Section 6.9.2](#InitialWindowSize)).[¶](#section-6.5.2-2.8.2)

Values above the maximum flow-control window size of 231-1 MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [FLOW\_CONTROL\_ERROR](#FLOW_CONTROL_ERROR).[¶](#section-6.5.2-2.8.3)

SETTINGS\_MAX\_FRAME\_SIZE (0x05):

This setting indicates the size of the largest frame payload that the sender is willing to receive, in units of octets.[¶](#section-6.5.2-2.10.1)

The initial value is 214 (16,384) octets. The value advertised by an endpoint MUST be between this initial value and the maximum allowed frame size (224-1 or 16,777,215 octets), inclusive. Values outside this range MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.5.2-2.10.2)

This advisory setting informs a peer of the maximum field section size that the sender is prepared to accept, in units of octets. The value is based on the uncompressed size of field lines, including the length of the name and value in units of octets plus an overhead of 32 octets for each field line.[¶](#section-6.5.2-2.12.1)

For any given request, a lower limit than what is advertised MAY be enforced. The initial value of this setting is unlimited.[¶](#section-6.5.2-2.12.2)

An endpoint that receives a SETTINGS frame with any unknown or unsupported identifier MUST ignore that setting.[¶](#section-6.5.2-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
