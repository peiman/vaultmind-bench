---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#14-4-3-1-compression-state.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-14-4-3-1-compression-state
type: reference
title: 'RFC 9113: HTTP/2 › 4. HTTP Frames › 4.3. Field Section Compression and Decompression › 4.3.1. Compression State'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#14-4-3-1-compression-state
source_hash: 87dc7b7345c4ebaffbfc80d6f2d874351abf39aaf950105bc9dd274379549a38
---
Field compression is stateful. Each endpoint has an HPACK encoder context and an HPACK decoder context that are used for encoding and decoding all field blocks on a connection. [Section 4](https://www.rfc-editor.org/rfc/rfc7541#section-4) of \[[COMPRESSION](#RFC7541)] defines the dynamic table, which is the primary state for each context.[¶](#section-4.3.1-1)

The dynamic table has a maximum size that is set by an HPACK decoder. An endpoint communicates the size chosen by its HPACK decoder context using the SETTINGS\_HEADER\_TABLE\_SIZE setting; see [Section 6.5.2](#SettingValues). When a connection is established, the dynamic table size for the HPACK decoder and encoder at both endpoints starts at 4,096 bytes, the initial value of the SETTINGS\_HEADER\_TABLE\_SIZE setting.[¶](#section-4.3.1-2)

Any change to the maximum value set using SETTINGS\_HEADER\_TABLE\_SIZE takes effect when the endpoint [acknowledges settings](#SettingsSync) ([Section 6.5.3](#SettingsSync)). The HPACK encoder at that endpoint can set the dynamic table to any size up to the maximum value set by the decoder. An HPACK encoder declares the size of the dynamic table with a Dynamic Table Size Update instruction ([Section 6.3](https://www.rfc-editor.org/rfc/rfc7541#section-6.3) of \[[COMPRESSION](#RFC7541)]).[¶](#section-4.3.1-3)

Once an endpoint acknowledges a change to SETTINGS\_HEADER\_TABLE\_SIZE that reduces the maximum below the current size of the dynamic table, its HPACK encoder MUST start the next field block with a Dynamic Table Size Update instruction that sets the dynamic table to a size that is less than or equal to the reduced maximum; see [Section 4.2](https://www.rfc-editor.org/rfc/rfc7541#section-4.2) of \[[COMPRESSION](#RFC7541)]. An endpoint MUST treat a field block that follows an acknowledgment of the reduction to the maximum dynamic table size as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [COMPRESSION\_ERROR](#COMPRESSION_ERROR) if it does not start with a conformant Dynamic Table Size Update instruction.[¶](#section-4.3.1-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
