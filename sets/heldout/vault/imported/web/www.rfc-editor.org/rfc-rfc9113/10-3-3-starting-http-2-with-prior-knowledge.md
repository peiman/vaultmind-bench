---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#10-3-3-starting-http-2-with-prior-knowledge.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-10-3-3-starting-http-2-with-prior-knowledge
type: reference
title: 'RFC 9113: HTTP/2 › 3. Starting HTTP/2 › 3.3. Starting HTTP/2 with Prior Knowledge'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#10-3-3-starting-http-2-with-prior-knowledge
source_hash: d70ad671ef072c648d34d58b0aef0d7753c4f54df0991a984570ec809e35c234
---
A client can learn that a particular server supports HTTP/2 by other means. For example, a client could be configured with knowledge that a server supports HTTP/2.[¶](#section-3.3-1)

A client that knows that a server supports HTTP/2 can establish a TCP connection and send the [connection preface](#preface) ([Section 3.4](#preface)) followed by HTTP/2 frames. Servers can identify these connections by the presence of the connection preface. This only affects the establishment of HTTP/2 connections over cleartext TCP; HTTP/2 connections over TLS MUST use [protocol negotiation in TLS](#RFC7301) \[[TLS-ALPN](#RFC7301)].[¶](#section-3.3-2)

Likewise, the server MUST send a [connection preface](#preface) ([Section 3.4](#preface)).[¶](#section-3.3-3)

Without additional information, prior support for HTTP/2 is not a strong signal that a given server will support HTTP/2 for future connections. For example, it is possible for server configurations to change, for configurations to differ between instances in clustered servers, or for network conditions to change.[¶](#section-3.3-4)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
