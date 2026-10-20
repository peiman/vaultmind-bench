---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#31-6-5-settings.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-31-6-5-settings
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.5. SETTINGS'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#31-6-5-settings
source_hash: e9ddc8c39d095282dc571a1e17ae7dd60bfabd4bd2f50c19d22da109872ff836
---
The SETTINGS frame (type=0x04) conveys configuration parameters that affect how endpoints communicate, such as preferences and constraints on peer behavior. The SETTINGS frame is also used to acknowledge the receipt of those settings. Individually, a configuration parameter from a SETTINGS frame is referred to as a "setting".[¶](#section-6.5-1)

Settings are not negotiated; they describe characteristics of the sending peer, which are used by the receiving peer. Different values for the same setting can be advertised by each peer. For example, a client might set a high initial flow-control window, whereas a server might set a lower value to conserve resources.[¶](#section-6.5-2)

A SETTINGS frame MUST be sent by both endpoints at the start of a connection and MAY be sent at any other time by either endpoint over the lifetime of the connection. Implementations MUST support all of the settings defined by this specification.[¶](#section-6.5-3)

Each parameter in a SETTINGS frame replaces any existing value for that parameter. Settings are processed in the order in which they appear, and a receiver of a SETTINGS frame does not need to maintain any state other than the current value of each setting. Therefore, the value of a SETTINGS parameter is the last value that is seen by a receiver.[¶](#section-6.5-4)

SETTINGS frames are acknowledged by the receiving peer. To enable this, the SETTINGS frame defines the ACK flag:[¶](#section-6.5-5)

ACK (0x01):

When set, the ACK flag indicates that this frame acknowledges receipt and application of the peer's SETTINGS frame. When this bit is set, the frame payload of the SETTINGS frame MUST be empty. Receipt of a SETTINGS frame with the ACK flag set and a length field value other than 0 MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [FRAME\_SIZE\_ERROR](#FRAME_SIZE_ERROR). For more information, see [Section 6.5.3](#SettingsSync) ("[Settings Synchronization](#SettingsSync)").[¶](#section-6.5-6.2)

SETTINGS frames always apply to a connection, never a single stream. The stream identifier for a SETTINGS frame MUST be zero (0x00). If an endpoint receives a SETTINGS frame whose Stream Identifier field is anything other than 0x00, the endpoint MUST respond with a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.5-7)

The SETTINGS frame affects connection state. A badly formed or incomplete SETTINGS frame MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-6.5-8)

A SETTINGS frame with a length other than a multiple of 6 octets MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [FRAME\_SIZE\_ERROR](#FRAME_SIZE_ERROR).[¶](#section-6.5-9)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
