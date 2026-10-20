---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#08-3-starting-http-2.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-08-3-starting-http-2
type: reference
title: 'RFC 9113: HTTP/2 › 3. Starting HTTP/2'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#08-3-starting-http-2
source_hash: 1c34a348a9e24a2c02dd236c40e6e3d7868e40dc5bf7f3cf38d272f09398c378
---
Implementations that generate HTTP requests need to discover whether a server supports HTTP/2.[¶](#section-3-1)

HTTP/2 uses the "`http`" and "`https`" URI schemes defined in [Section 4.2](https://www.rfc-editor.org/rfc/rfc9110#section-4.2) of \[[HTTP](#RFC9110)], with the same default port numbers as HTTP/1.1 \[[HTTP/1.1](#RFC9112)]. These URIs do not include any indication about what HTTP versions an upstream server (the immediate peer to which the client wishes to establish a connection) supports.[¶](#section-3-2)

The means by which support for HTTP/2 is determined is different for "`http`" and "`https`" URIs. Discovery for "`https`" URIs is described in [Section 3.2](#discover-https). HTTP/2 support for "`http`" URIs can only be discovered by out-of-band means and requires prior knowledge of the support as described in [Section 3.3](#known-http).[¶](#section-3-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
