---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#22-5-2-2-appropriate-use-of-flow-control.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-22-5-2-2-appropriate-use-of-flow-control
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.2. Flow Control › 5.2.2. Appropriate Use of Flow Control'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#22-5-2-2-appropriate-use-of-flow-control
source_hash: fac27d0e9557d28636f2d6784ab6d65698f5a0c8158ebed9347d0c34dd3e74e7
---
Flow control is defined to protect endpoints that are operating under resource constraints. For example, a proxy needs to share memory between many connections and also might have a slow upstream connection and a fast downstream one. Flow control addresses cases where the receiver is unable to process data on one stream yet wants to continue to process other streams in the same connection.[¶](#section-5.2.2-1)

Deployments that do not require this capability can advertise a flow-control window of the maximum size (231-1) and can maintain this window by sending a [WINDOW\_UPDATE](#WINDOW_UPDATE) frame when any data is received. This effectively disables flow control for that receiver. Conversely, a sender is always subject to the flow-control window advertised by the receiver.[¶](#section-5.2.2-2)

Deployments with constrained resources (for example, memory) can employ flow control to limit the amount of memory a peer can consume. Note, however, that this can lead to suboptimal use of available network resources if flow control is enabled without knowledge of the bandwidth * delay product (see \[[RFC7323](#RFC7323)]).[¶](#section-5.2.2-3)

Even with full awareness of the current bandwidth * delay product, implementation of flow control can be difficult. Endpoints MUST read and process HTTP/2 frames from the TCP receive buffer as soon as data is available. Failure to read promptly could lead to a deadlock when critical frames, such as [WINDOW\_UPDATE](#WINDOW_UPDATE), are not read and acted upon. Reading frames promptly does not expose endpoints to resource exhaustion attacks, as HTTP/2 flow control limits resource commitments.[¶](#section-5.2.2-4)

#### 5.2.3. Flow-Control Performance

If an endpoint cannot ensure that its peer always has available flow-control window space that is greater than the peer's bandwidth * delay product on this connection, its receive throughput will be limited by HTTP/2 flow control. This will result in degraded performance.[¶](#section-5.2.3-1)

Sending timely [WINDOW\_UPDATE](#WINDOW_UPDATE) frames can improve performance. Endpoints will want to balance the need to improve receive throughput with the need to manage resource exhaustion risks and should take careful note of [Section 10.5](#dos) in defining their strategy to manage window sizes.[¶](#section-5.2.3-2)

### 5.3. Prioritization

In a multiplexed protocol like HTTP/2, prioritizing allocation of bandwidth and computation resources to streams can be critical to attaining good performance. A poor prioritization scheme can result in HTTP/2 providing poor performance. With no parallelism at the TCP layer, performance could be significantly worse than HTTP/1.1.[¶](#section-5.3-1)

A good prioritization scheme benefits from the application of contextual knowledge such as the content of resources, how resources are interrelated, and how those resources will be used by a peer. In particular, clients can possess knowledge about the priority of requests that is relevant to server prioritization. In those cases, having clients provide priority information can improve performance.[¶](#section-5.3-2)

#### 5.3.1. Background on Priority in RFC 7540

RFC 7540 defined a rich system for signaling priority of requests. However, this system proved to be complex, and it was not uniformly implemented.[¶](#section-5.3.1-1)

The flexible scheme meant that it was possible for clients to express priorities in very different ways, with little consistency in the approaches that were adopted. For servers, implementing generic support for the scheme was complex. Implementation of priorities was uneven in both clients and servers. Many server deployments ignored client signals when prioritizing their handling of requests.[¶](#section-5.3.1-2)

In short, the prioritization signaling in [RFC 7540](#RFC7540) \[[RFC7540](#RFC7540)] was not successful.[¶](#section-5.3.1-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
