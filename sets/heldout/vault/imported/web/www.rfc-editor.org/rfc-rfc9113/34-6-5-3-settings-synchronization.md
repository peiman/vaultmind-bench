---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#34-6-5-3-settings-synchronization.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-34-6-5-3-settings-synchronization
type: reference
title: 'RFC 9113: HTTP/2 › 6. Frame Definitions › 6.5. SETTINGS › 6.5.3. Settings Synchronization'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#34-6-5-3-settings-synchronization
source_hash: 3ccfba6379f6b24e95ae02f7351f881386fc6da650c3394453e985924b3e3fd4
---
Most values in SETTINGS benefit from or require an understanding of when the peer has received and applied the changed parameter values. In order to provide such synchronization timepoints, the recipient of a SETTINGS frame in which the ACK flag is not set MUST apply the updated settings as soon as possible upon receipt. SETTINGS frames are acknowledged in the order in which they are received.[¶](#section-6.5.3-1)

The values in the SETTINGS frame MUST be processed in the order they appear, with no other frame processing between values. Unsupported settings MUST be ignored. Once all values have been processed, the recipient MUST immediately emit a SETTINGS frame with the ACK flag set. Upon receiving a SETTINGS frame with the ACK flag set, the sender of the altered settings can rely on the values from the oldest unacknowledged SETTINGS frame having been applied.[¶](#section-6.5.3-2)

If the sender of a SETTINGS frame does not receive an acknowledgment within a reasonable amount of time, it MAY issue a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [SETTINGS\_TIMEOUT](#SETTINGS_TIMEOUT). In setting a timeout, some allowance needs to be made for processing delays at the peer; a timeout that is solely based on the round-trip time between endpoints might result in spurious errors.[¶](#section-6.5.3-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
