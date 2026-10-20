---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#25-5-4-1-connection-error-handling.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-25-5-4-1-connection-error-handling
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.4. Error Handling › 5.4.1. Connection Error Handling'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#25-5-4-1-connection-error-handling
source_hash: 71500064bcd6998e8de4d6328b60235c43f545f7270c925c6f33951b61f3447c
---
A connection error is any error that prevents further processing of the frame layer or corrupts any connection state.[¶](#section-5.4.1-1)

An endpoint that encounters a connection error SHOULD first send a [GOAWAY](#GOAWAY) frame ([Section 6.8](#GOAWAY)) with the stream identifier of the last stream that it successfully received from its peer. The [GOAWAY](#GOAWAY) frame includes an [error code](#ErrorCodes) ([Section 7](#ErrorCodes)) that indicates why the connection is terminating. After sending the [GOAWAY](#GOAWAY) frame for an error condition, the endpoint MUST close the TCP connection.[¶](#section-5.4.1-2)

It is possible that the [GOAWAY](#GOAWAY) will not be reliably received by the receiving endpoint. In the event of a connection error, [GOAWAY](#GOAWAY) only provides a best-effort attempt to communicate with the peer about why the connection is being terminated.[¶](#section-5.4.1-3)

An endpoint can end a connection at any time. In particular, an endpoint MAY choose to treat a stream error as a connection error. Endpoints SHOULD send a [GOAWAY](#GOAWAY) frame when ending a connection, providing that circumstances permit it.[¶](#section-5.4.1-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
