---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#18-5-1-stream-states.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-18-5-1-stream-states
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.1. Stream States (3/3)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#18-5-1-stream-states
source_hash: d6f09ab71efa11d852c4245a78eb628f4759ace1715d3f279fa05ca6d360bee7
---
In the absence of more specific rules, implementations SHOULD treat the receipt of a frame that is not expressly permitted in the description of a state as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR). Note that [PRIORITY](#PRIORITY) can be sent and received in any stream state.[¶](#section-5.1-8)

The rules in this section only apply to frames defined in this document. Receipt of frames for which the semantics are unknown cannot be treated as an error, as the conditions for sending and receiving those frames are also unknown; see [Section 5.5](#extensibility).[¶](#section-5.1-9)

An example of the state transitions for an HTTP request/response exchange can be found in [Section 8.8](#HttpExamples). An example of the state transitions for server push can be found in Sections [8.4.1](#PushRequests) and [8.4.2](#PushResponses).[¶](#section-5.1-10)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
