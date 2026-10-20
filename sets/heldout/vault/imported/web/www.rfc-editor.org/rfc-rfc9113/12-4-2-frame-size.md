---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#12-4-2-frame-size.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-12-4-2-frame-size
type: reference
title: 'RFC 9113: HTTP/2 › 4. HTTP Frames › 4.2. Frame Size'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#12-4-2-frame-size
source_hash: 2e5647f15b06350c349b2e407fd8a1d572217f177752df1898d16fe2001a4466
---
The size of a frame payload is limited by the maximum size that a receiver advertises in the [SETTINGS\_MAX\_FRAME\_SIZE](#SETTINGS_MAX_FRAME_SIZE) setting. This setting can have any value between 214 (16,384) and 224-1 (16,777,215) octets, inclusive.[¶](#section-4.2-1)

All implementations MUST be capable of receiving and minimally processing frames up to 214 octets in length, plus the 9-octet [frame header](#FrameHeader) ([Section 4.1](#FrameHeader)). The size of the frame header is not included when describing frame sizes.[¶](#section-4.2-2)

An endpoint MUST send an error code of [FRAME\_SIZE\_ERROR](#FRAME_SIZE_ERROR) if a frame exceeds the size defined in [SETTINGS\_MAX\_FRAME\_SIZE](#SETTINGS_MAX_FRAME_SIZE), exceeds any limit defined for the frame type, or is too small to contain mandatory frame data. A frame size error in a frame that could alter the state of the entire connection MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)); this includes any frame carrying a [field block](#FieldBlock) ([Section 4.3](#FieldBlock)) (that is, [HEADERS](#HEADERS), [PUSH\_PROMISE](#PUSH_PROMISE), and [CONTINUATION](#CONTINUATION)), a [SETTINGS](#SETTINGS) frame, and any frame with a stream identifier of 0.[¶](#section-4.2-4)

Endpoints are not obligated to use all available space in a frame. Responsiveness can be improved by using frames that are smaller than the permitted maximum size. Sending large frames can result in delays in sending time-sensitive frames (such as [RST\_STREAM](#RST_STREAM), [WINDOW\_UPDATE](#WINDOW_UPDATE), or [PRIORITY](#PRIORITY)), which, if blocked by the transmission of a large frame, could affect performance.[¶](#section-4.2-5)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
