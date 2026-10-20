---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#44-7-error-codes.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-44-7-error-codes
type: reference
title: 'RFC 9113: HTTP/2 › 7. Error Codes'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#44-7-error-codes
source_hash: ad05d5c5de87e5f08e838ec185813c523ce5436d52e8d6a2c13cf7d06e91ecc9
---
Error codes are 32-bit fields that are used in [RST\_STREAM](#RST_STREAM) and [GOAWAY](#GOAWAY) frames to convey the reasons for the stream or connection error.[¶](#section-7-1)

Error codes share a common code space. Some error codes apply only to either streams or the entire connection and have no defined semantics in the other context.[¶](#section-7-2)

The following error codes are defined:[¶](#section-7-3)

NO\_ERROR (0x00):

The associated condition is not a result of an error. For example, a [GOAWAY](#GOAWAY) might include this code to indicate graceful shutdown of a connection.[¶](#NO_ERROR)

PROTOCOL\_ERROR (0x01):

The endpoint detected an unspecific protocol error. This error is for use when a more specific error code is not available.[¶](#PROTOCOL_ERROR)

INTERNAL\_ERROR (0x02):

The endpoint encountered an unexpected internal error.[¶](#INTERNAL_ERROR)

FLOW\_CONTROL\_ERROR (0x03):

The endpoint detected that its peer violated the flow-control protocol.[¶](#FLOW_CONTROL_ERROR)

SETTINGS\_TIMEOUT (0x04):

The endpoint sent a [SETTINGS](#SETTINGS) frame but did not receive a response in a timely manner. See [Section 6.5.3](#SettingsSync) ("Settings Synchronization").[¶](#SETTINGS_TIMEOUT)

STREAM\_CLOSED (0x05):

The endpoint received a frame after a stream was half-closed.[¶](#STREAM_CLOSED)

FRAME\_SIZE\_ERROR (0x06):

The endpoint received a frame with an invalid size.[¶](#FRAME_SIZE_ERROR)

REFUSED\_STREAM (0x07):

The endpoint refused the stream prior to performing any application processing (see [Section 8.7](#Reliability) for details).[¶](#REFUSED_STREAM)

CANCEL (0x08):

The endpoint uses this error code to indicate that the stream is no longer needed.[¶](#CANCEL)

COMPRESSION\_ERROR (0x09):

The endpoint is unable to maintain the field section compression context for the connection.[¶](#COMPRESSION_ERROR)

CONNECT\_ERROR (0x0a):

The connection established in response to a [CONNECT request](#CONNECT) ([Section 8.5](#CONNECT)) was reset or abnormally closed.[¶](#CONNECT_ERROR)

ENHANCE\_YOUR\_CALM (0x0b):

The endpoint detected that its peer is exhibiting a behavior that might be generating excessive load.[¶](#ENHANCE_YOUR_CALM)

INADEQUATE\_SECURITY (0x0c):

The underlying transport has properties that do not meet minimum security requirements (see [Section 9.2](#TLSUsage)).[¶](#INADEQUATE_SECURITY)

HTTP\_1\_1\_REQUIRED (0x0d):

The endpoint requires that HTTP/1.1 be used instead of HTTP/2.[¶](#HTTP_1_1_REQUIRED)

Unknown or unsupported error codes MUST NOT trigger any special behavior. These MAY be treated by an implementation as being equivalent to [INTERNAL\_ERROR](#INTERNAL_ERROR).[¶](#section-7-5)

## 8. Expressing HTTP Semantics in HTTP/2

HTTP/2 is an instantiation of the HTTP message abstraction ([Section 6](https://www.rfc-editor.org/rfc/rfc9110#section-6) of \[[HTTP](#RFC9110)]).[¶](#section-8-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
