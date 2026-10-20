---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#13-4-3-field-section-compression-and-decompression.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-13-4-3-field-section-compression-and-decompression
type: reference
title: 'RFC 9113: HTTP/2 › 4. HTTP Frames › 4.3. Field Section Compression and Decompression'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#13-4-3-field-section-compression-and-decompression
source_hash: 3aca46750b54ff0b38dce14194951e69e8be1a58cd4e078df2bb3f9b16e4fd51
---
Field section compression is the process of compressing a set of field lines ([Section 5.2](https://www.rfc-editor.org/rfc/rfc9110#section-5.2) of \[[HTTP](#RFC9110)]) to form a field block. Field section decompression is the process of decoding a field block into a set of field lines. Details of HTTP/2 field section compression and decompression are defined in \[[COMPRESSION](#RFC7541)], which, for historical reasons, refers to these processes as header compression and decompression.[¶](#section-4.3-1)

Each field block carries all of the compressed field lines of a single field section. Header sections also include control data associated with the message in the form of [pseudo-header fields](#PseudoHeaderFields) ([Section 8.3](#PseudoHeaderFields)) that use the same format as a field line.[¶](#section-4.3-2)

Field blocks carry control data and header sections for requests, responses, promised requests, and pushed responses (see [Section 8.4](#PushResources)). All these messages, except for interim responses and requests contained in [PUSH\_PROMISE](#PUSH_PROMISE) ([Section 6.6](#PUSH_PROMISE)) frames, can optionally include a field block that carries a trailer section.[¶](#section-4.3-4)

A field section is a collection of field lines. Each of the field lines in a field block carries a single value. The serialized field block is then divided into one or more octet sequences, called field block fragments. The first field block fragment is transmitted within the frame payload of [HEADERS](#HEADERS) ([Section 6.2](#HEADERS)) or [PUSH\_PROMISE](#PUSH_PROMISE) ([Section 6.6](#PUSH_PROMISE)), each of which could be followed by [CONTINUATION](#CONTINUATION) ([Section 6.10](#CONTINUATION)) frames to carry subsequent field block fragments.[¶](#section-4.3-5)

The [Cookie header field](#RFC6265) \[[COOKIE](#RFC6265)] is treated specially by the HTTP mapping (see [Section 8.2.3](#CompressCookie)).[¶](#section-4.3-6)

A receiving endpoint reassembles the field block by concatenating its fragments and then decompresses the block to reconstruct the field section.[¶](#section-4.3-7)

A complete field section consists of either:[¶](#section-4.3-8)

- a single [HEADERS](#HEADERS) or [PUSH\_PROMISE](#PUSH_PROMISE) frame, with the END\_HEADERS flag set, or[¶](#section-4.3-9.1)
- a [HEADERS](#HEADERS) or [PUSH\_PROMISE](#PUSH_PROMISE) frame with the END\_HEADERS flag unset and one or more [CONTINUATION](#CONTINUATION) frames, where the last [CONTINUATION](#CONTINUATION) frame has the END\_HEADERS flag set.[¶](#section-4.3-9.2)

Each field block is processed as a discrete unit. Field blocks MUST be transmitted as a contiguous sequence of frames, with no interleaved frames of any other type or from any other stream. The last frame in a sequence of [HEADERS](#HEADERS) or [CONTINUATION](#CONTINUATION) frames has the END\_HEADERS flag set. The last frame in a sequence of [PUSH\_PROMISE](#PUSH_PROMISE) or [CONTINUATION](#CONTINUATION) frames has the END\_HEADERS flag set. This allows a field block to be logically equivalent to a single frame.[¶](#section-4.3-10)

Field block fragments can only be sent as the frame payload of [HEADERS](#HEADERS), [PUSH\_PROMISE](#PUSH_PROMISE), or [CONTINUATION](#CONTINUATION) frames because these frames carry data that can modify the compression context maintained by a receiver. An endpoint receiving [HEADERS](#HEADERS), [PUSH\_PROMISE](#PUSH_PROMISE), or [CONTINUATION](#CONTINUATION) frames needs to reassemble field blocks and perform decompression even if the frames are to be discarded. A receiver MUST terminate the connection with a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [COMPRESSION\_ERROR](#COMPRESSION_ERROR) if it does not decompress a field block.[¶](#section-4.3-11)

A decoding error in a field block MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [COMPRESSION\_ERROR](#COMPRESSION_ERROR).[¶](#section-4.3-12)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
