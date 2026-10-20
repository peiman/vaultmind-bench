---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#50-8-5-the-connect-method.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-50-8-5-the-connect-method
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.5. The CONNECT Method'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#50-8-5-the-connect-method
source_hash: 43994a7aae78238e969ad6f72622b68e006629cc371e1799c50818610e96296f
---
The CONNECT method ([Section 9.3.6](https://www.rfc-editor.org/rfc/rfc9110#section-9.3.6) of \[[HTTP](#RFC9110)]) is used to convert an HTTP connection into a tunnel to a remote host. CONNECT is primarily used with HTTP proxies to establish a TLS session with an origin server for the purposes of interacting with "`https`" resources.[¶](#section-8.5-1)

In HTTP/2, the CONNECT method establishes a tunnel over a single HTTP/2 stream to a remote host, rather than converting the entire connection to a tunnel. A CONNECT header section is constructed as defined in [Section 8.3.1](#HttpRequest) ("[Request Pseudo-Header Fields](#HttpRequest)"), with a few differences. Specifically:[¶](#section-8.5-2)

- The "`:method`" pseudo-header field is set to `CONNECT`.[¶](#section-8.5-3.1)
- The "`:scheme`" and "`:path`" pseudo-header fields MUST be omitted.[¶](#section-8.5-3.2)
- The "`:authority`" pseudo-header field contains the host and port to connect to (equivalent to the authority-form of the request-target of CONNECT requests; see [Section 3.2.3](https://www.rfc-editor.org/rfc/rfc9112#section-3.2.3) of \[[HTTP/1.1](#RFC9112)]).[¶](#section-8.5-3.3)

A CONNECT request that does not conform to these restrictions is [malformed](#malformed) ([Section 8.1.1](#malformed)).[¶](#section-8.5-4)

A proxy that supports CONNECT establishes a [TCP connection](#RFC0793) \[[TCP](#RFC0793)] to the host and port identified in the "`:authority`" pseudo-header field. Once this connection is successfully established, the proxy sends a [HEADERS](#HEADERS) frame containing a 2xx-series status code to the client, as defined in [Section 9.3.6](https://www.rfc-editor.org/rfc/rfc9110#section-9.3.6) of \[[HTTP](#RFC9110)].[¶](#section-8.5-5)

After the initial [HEADERS](#HEADERS) frame sent by each peer, all subsequent [DATA](#DATA) frames correspond to data sent on the TCP connection. The frame payload of any [DATA](#DATA) frames sent by the client is transmitted by the proxy to the TCP server; data received from the TCP server is assembled into [DATA](#DATA) frames by the proxy. Frame types other than [DATA](#DATA) or stream management frames ([RST\_STREAM](#RST_STREAM), [WINDOW\_UPDATE](#WINDOW_UPDATE), and [PRIORITY](#PRIORITY)) MUST NOT be sent on a connected stream and MUST be treated as a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) if received.[¶](#section-8.5-6)

The TCP connection can be closed by either peer. The END\_STREAM flag on a [DATA](#DATA) frame is treated as being equivalent to the TCP FIN bit. A client is expected to send a [DATA](#DATA) frame with the END\_STREAM flag set after receiving a frame with the END\_STREAM flag set. A proxy that receives a [DATA](#DATA) frame with the END\_STREAM flag set sends the attached data with the FIN bit set on the last TCP segment. A proxy that receives a TCP segment with the FIN bit set sends a [DATA](#DATA) frame with the END\_STREAM flag set. Note that the final TCP segment or [DATA](#DATA) frame could be empty.[¶](#section-8.5-7)

A TCP connection error is signaled with [RST\_STREAM](#RST_STREAM). A proxy treats any error in the TCP connection, which includes receiving a TCP segment with the RST bit set, as a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [CONNECT\_ERROR](#CONNECT_ERROR). Correspondingly, a proxy MUST send a TCP segment with the RST bit set if it detects an error with the stream or the HTTP/2 connection.[¶](#section-8.5-8)

HTTP/2 does not support the 101 (Switching Protocols) informational status code ([Section 15.2.2](https://www.rfc-editor.org/rfc/rfc9110#section-15.2.2) of \[[HTTP](#RFC9110)]).[¶](#section-8.6-1)

The semantics of 101 (Switching Protocols) aren't applicable to a multiplexed protocol. Similar functionality might be enabled through the use of [extended CONNECT](#RFC8441) \[[RFC8441](#RFC8441)], and other protocols are able to use the same mechanisms that HTTP/2 uses to negotiate their use (see [Section 3](#starting)).[¶](#section-8.6-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
