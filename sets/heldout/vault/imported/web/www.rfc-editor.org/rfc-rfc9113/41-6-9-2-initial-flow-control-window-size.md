---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#41-6-9-2-initial-flow-control-window-size.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-41-6-9-2-initial-flow-control-window-size
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.9. WINDOW\_UPDATE › 6.9.2. Initial Flow-Control Window Size'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#41-6-9-2-initial-flow-control-window-size
source_hash: 31d742539f182032e88d2d268797d85a3b017082eb705311d16cf8c481b62cfb
---
When an HTTP/2 connection is first established, new streams are created with an initial flow-control window size of 65,535 octets. The connection flow-control window is also 65,535 octets. Both endpoints can adjust the initial window size for new streams by including a value for [SETTINGS\_INITIAL\_WINDOW\_SIZE](#SETTINGS_INITIAL_WINDOW_SIZE) in the [SETTINGS](#SETTINGS) frame. The connection flow-control window can only be changed using WINDOW\_UPDATE frames.[¶](#section-6.9.2-1)

Prior to receiving a [SETTINGS](#SETTINGS) frame that sets a value for [SETTINGS\_INITIAL\_WINDOW\_SIZE](#SETTINGS_INITIAL_WINDOW_SIZE), an endpoint can only use the default initial window size when sending flow-controlled frames. Similarly, the connection flow-control window is set based on the default initial window size until a WINDOW\_UPDATE frame is received.[¶](#section-6.9.2-2)

In addition to changing the flow-control window for streams that are not yet active, a [SETTINGS](#SETTINGS) frame can alter the initial flow-control window size for streams with active flow-control windows (that is, streams in the "open" or "half-closed (remote)" state). When the value of [SETTINGS\_INITIAL\_WINDOW\_SIZE](#SETTINGS_INITIAL_WINDOW_SIZE) changes, a receiver MUST adjust the size of all stream flow-control windows that it maintains by the difference between the new value and the old value.[¶](#section-6.9.2-3)

A change to [SETTINGS\_INITIAL\_WINDOW\_SIZE](#SETTINGS_INITIAL_WINDOW_SIZE) can cause the available space in a flow-control window to become negative. A sender MUST track the negative flow-control window and MUST NOT send new flow-controlled frames until it receives WINDOW\_UPDATE frames that cause the flow-control window to become positive.[¶](#section-6.9.2-4)

For example, if the client sends 60 KB immediately on connection establishment and the server sets the initial window size to be 16 KB, the client will recalculate the available flow-control window to be -44 KB on receipt of the [SETTINGS](#SETTINGS) frame. The client retains a negative flow-control window until WINDOW\_UPDATE frames restore the window to being positive, after which the client can resume sending.[¶](#section-6.9.2-5)

A [SETTINGS](#SETTINGS) frame cannot alter the connection flow-control window.[¶](#section-6.9.2-6)

An endpoint MUST treat a change to [SETTINGS\_INITIAL\_WINDOW\_SIZE](#SETTINGS_INITIAL_WINDOW_SIZE) that causes any flow-control window to exceed the maximum size as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [FLOW\_CONTROL\_ERROR](#FLOW_CONTROL_ERROR).[¶](#section-6.9.2-7)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
