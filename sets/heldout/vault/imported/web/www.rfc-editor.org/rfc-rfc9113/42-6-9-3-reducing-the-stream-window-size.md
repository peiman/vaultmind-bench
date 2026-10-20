---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#42-6-9-3-reducing-the-stream-window-size.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-42-6-9-3-reducing-the-stream-window-size
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.9. WINDOW\_UPDATE › 6.9.3. Reducing the Stream Window Size'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#42-6-9-3-reducing-the-stream-window-size
source_hash: ce2662ae7bc803a015ea7ecd57d422b1babdbcce64c181f3f17fc55601e2a13c
---
A receiver that wishes to use a smaller flow-control window than the current size can send a new [SETTINGS](#SETTINGS) frame. However, the receiver MUST be prepared to receive data that exceeds this window size, since the sender might send data that exceeds the lower limit prior to processing the [SETTINGS](#SETTINGS) frame.[¶](#section-6.9.3-1)

After sending a SETTINGS frame that reduces the initial flow-control window size, a receiver MAY continue to process streams that exceed flow-control limits. Allowing streams to continue does not allow the receiver to immediately reduce the space it reserves for flow-control windows. Progress on these streams can also stall, since [WINDOW\_UPDATE](#WINDOW_UPDATE) frames are needed to allow the sender to resume sending. The receiver MAY instead send a [RST\_STREAM](#RST_STREAM) with an error code of [FLOW\_CONTROL\_ERROR](#FLOW_CONTROL_ERROR) for the affected streams.[¶](#section-6.9.3-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
