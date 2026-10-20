---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#60-10-5-1-limits-on-field-block-size.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-60-10-5-1-limits-on-field-block-size
type: reference
title: 'RFC 9113: HTTP/2 › 10. Security Considerations › 10.5. Denial-of-Service Considerations › 10.5.1. Limits on Field Block Size'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#60-10-5-1-limits-on-field-block-size
source_hash: 44ca71e4acdca589eee919cb8409bf41ccc3e707461d7d13437b03a6ed6894d6
---
A large [field block](#FieldBlock) ([Section 4.3](#FieldBlock)) can cause an implementation to commit a large amount of state. Field lines that are critical for routing can appear toward the end of a field block, which prevents streaming of fields to their ultimate destination. This ordering and other reasons, such as ensuring cache correctness, mean that an endpoint might need to buffer the entire field block. Since there is no hard limit to the size of a field block, some endpoints could be forced to commit a large amount of available memory for field blocks.[¶](#section-10.5.1-1)

An endpoint can use the [SETTINGS\_MAX\_HEADER\_LIST\_SIZE](#SETTINGS_MAX_HEADER_LIST_SIZE) to advise peers of limits that might apply on the size of uncompressed field blocks. This setting is only advisory, so endpoints MAY choose to send field blocks that exceed this limit and risk the request or response being treated as malformed. This setting is specific to a connection, so any request or response could encounter a hop with a lower, unknown limit. An intermediary can attempt to avoid this problem by passing on values presented by different peers, but they are not obliged to do so.[¶](#section-10.5.1-2)

A server that receives a larger field block than it is willing to handle can send an HTTP 431 (Request Header Fields Too Large) status code \[[RFC6585](#RFC6585)]. A client can discard responses that it cannot process. The field block MUST be processed to ensure a consistent connection state, unless the connection is closed.[¶](#section-10.5.1-3)

#### 10.5.2. CONNECT Issues

The CONNECT method can be used to create disproportionate load on a proxy, since stream creation is relatively inexpensive when compared to the creation and maintenance of a TCP connection. A proxy might also maintain some resources for a TCP connection beyond the closing of the stream that carries the CONNECT request, since the outgoing TCP connection remains in the TIME\_WAIT state. Therefore, a proxy cannot rely on [SETTINGS\_MAX\_CONCURRENT\_STREAMS](#SETTINGS_MAX_CONCURRENT_STREAMS) alone to limit the resources consumed by CONNECT requests.[¶](#section-10.5.2-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
