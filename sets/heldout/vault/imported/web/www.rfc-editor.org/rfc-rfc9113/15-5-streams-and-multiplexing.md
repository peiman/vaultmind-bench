---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#15-5-streams-and-multiplexing.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-15-5-streams-and-multiplexing
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#15-5-streams-and-multiplexing
source_hash: aa6d2f33867a267b894108a12836d0eff48af5d642e11348be9d1e4991c76249
---
A "stream" is an independent, bidirectional sequence of frames exchanged between the client and server within an HTTP/2 connection. Streams have several important characteristics:[¶](#section-5-1)

- A single HTTP/2 connection can contain multiple concurrently open streams, with either endpoint interleaving frames from multiple streams.[¶](#section-5-2.1)
- Streams can be established and used unilaterally or shared by either endpoint.[¶](#section-5-2.2)
- Streams can be closed by either endpoint.[¶](#section-5-2.3)
- The order in which frames are sent is significant. Recipients process frames in the order they are received. In particular, the order of [HEADERS](#HEADERS) and [DATA](#DATA) frames is semantically significant.[¶](#section-5-2.4)
- Streams are identified by an integer. Stream identifiers are assigned to streams by the endpoint initiating the stream.[¶](#section-5-2.5)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
