---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#21-5-2-1-flow-control-principles.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-21-5-2-1-flow-control-principles
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.2. Flow Control › 5.2.1. Flow-Control Principles'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#21-5-2-1-flow-control-principles
source_hash: 9df288bfbe38168f8d23929513e3bbb8e7737c631ebcc40ed6837268407ff2d2
---
HTTP/2 stream flow control aims to allow a variety of flow-control algorithms to be used without requiring protocol changes. Flow control in HTTP/2 has the following characteristics:[¶](#section-5.2.1-1)

1. Flow control is specific to a connection. HTTP/2 flow control operates between the endpoints of a single hop and not over the entire end-to-end path.[¶](#section-5.2.1-2.1)
2. Flow control is based on [WINDOW\_UPDATE](#WINDOW_UPDATE) frames. Receivers advertise how many octets they are prepared to receive on a stream and for the entire connection. This is a credit-based scheme.[¶](#section-5.2.1-2.2)
3. Flow control is directional with overall control provided by the receiver. A receiver MAY choose to set any window size that it desires for each stream and for the entire connection. A sender MUST respect flow-control limits imposed by a receiver. Clients, servers, and intermediaries all independently advertise their flow-control window as a receiver and abide by the flow-control limits set by their peer when sending.[¶](#section-5.2.1-2.3)
4. The initial value for the flow-control window is 65,535 octets for both new streams and the overall connection.[¶](#section-5.2.1-2.4)
5. The frame type determines whether flow control applies to a frame. Of the frames specified in this document, only [DATA](#DATA) frames are subject to flow control; all other frame types do not consume space in the advertised flow-control window. This ensures that important control frames are not blocked by flow control.[¶](#section-5.2.1-2.5)
6. An endpoint can choose to disable its own flow control, but an endpoint cannot ignore flow-control signals from its peer.[¶](#section-5.2.1-2.6)
7. HTTP/2 defines only the format and semantics of the [WINDOW\_UPDATE](#WINDOW_UPDATE) frame ([Section 6.9](#WINDOW_UPDATE)). This document does not stipulate how a receiver decides when to send this frame or the value that it sends, nor does it specify how a sender chooses to send packets. Implementations are able to select any algorithm that suits their needs.[¶](#section-5.2.1-2.7)

Implementations are also responsible for prioritizing the sending of requests and responses, choosing how to avoid head-of-line blocking for requests, and managing the creation of new streams. Algorithm choices for these could interact with any flow-control algorithm.[¶](#section-5.2.1-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
