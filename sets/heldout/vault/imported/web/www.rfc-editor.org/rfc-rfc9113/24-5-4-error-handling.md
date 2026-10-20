---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#24-5-4-error-handling.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-24-5-4-error-handling
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.4. Error Handling'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#24-5-4-error-handling
source_hash: 7ae3e4037a8dc6801638b05b938e00f3fed85a718bf5517742c8ac0313373de8
---
HTTP/2 framing permits two classes of errors:[¶](#section-5.4-1)

- An error condition that renders the entire connection unusable is a connection error.[¶](#section-5.4-2.1)
- An error in an individual stream is a stream error.[¶](#section-5.4-2.2)

A list of error codes is included in [Section 7](#ErrorCodes).[¶](#section-5.4-3)

It is possible that an endpoint will encounter frames that would cause multiple errors. Implementations MAY discover multiple errors during processing, but they SHOULD report at most one stream and one connection error as a result.[¶](#section-5.4-4)

The first stream error reported for a given stream prevents any other errors on that stream from being reported. In comparison, the protocol permits multiple [GOAWAY](#GOAWAY) frames, though an endpoint SHOULD report just one type of connection error unless an error is encountered during graceful shutdown. If this occurs, an endpoint MAY send an additional GOAWAY frame with the new error code, in addition to any prior GOAWAY that contained [NO\_ERROR](#NO_ERROR).[¶](#section-5.4-5)

If an endpoint detects multiple different errors, it MAY choose to report any one of those errors. If a frame causes a connection error, that error MUST be reported. Additionally, an endpoint MAY use any applicable error code when it detects an error condition; a generic error code (such as [PROTOCOL\_ERROR](#PROTOCOL_ERROR) or [INTERNAL\_ERROR](#INTERNAL_ERROR)) can always be used in place of more specific error codes.[¶](#section-5.4-6)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
