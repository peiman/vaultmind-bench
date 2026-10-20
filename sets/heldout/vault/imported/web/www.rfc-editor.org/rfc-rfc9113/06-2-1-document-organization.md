---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#06-2-1-document-organization.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-06-2-1-document-organization
type: reference
title: 'RFC 9113: HTTP/2 › 2. HTTP/2 Protocol Overview › 2.1. Document Organization'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#06-2-1-document-organization
source_hash: 6a306de34cd16d8aabec256c3cd11ac783234eea0abe56aa94d50311bc8e0143
---
The HTTP/2 specification is split into four parts:[¶](#section-2.1-1)

- [Starting HTTP/2](#starting) ([Section 3](#starting)) covers how an HTTP/2 connection is initiated.[¶](#section-2.1-2.1)
- The [frame](#FramingLayer) ([Section 4](#FramingLayer)) and [stream](#StreamsLayer) ([Section 5](#StreamsLayer)) layers describe the way HTTP/2 frames are structured and formed into multiplexed streams.[¶](#section-2.1-2.2)
- [Frame](#FrameTypes) ([Section 6](#FrameTypes)) and [error](#ErrorCodes) ([Section 7](#ErrorCodes)) definitions include details of the frame and error types used in HTTP/2.[¶](#section-2.1-2.3)
- [HTTP mappings](#HttpLayer) ([Section 8](#HttpLayer)) and [additional requirements](#HttpExtra) ([Section 9](#HttpExtra)) describe how HTTP semantics are expressed using frames and streams.[¶](#section-2.1-2.4)

While some of the frame- and stream-layer concepts are isolated from HTTP, this specification does not define a completely generic frame layer. The frame and stream layers are tailored to the needs of HTTP.[¶](#section-2.1-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
