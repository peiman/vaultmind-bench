---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#11-3-4-http-2-connection-preface.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-11-3-4-http-2-connection-preface
type: reference
title: 'RFC 9113: HTTP/2 › 3. Starting HTTP/2 › 3.4. HTTP/2 Connection Preface'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#11-3-4-http-2-connection-preface
source_hash: 951567825df6944b0b89093186ac0ceb4bf989055f9047cac3cc4bf8395a77ed
---
In HTTP/2, each endpoint is required to send a connection preface as a final confirmation of the protocol in use and to establish the initial settings for the HTTP/2 connection. The client and server each send a different connection preface.[¶](#section-3.4-1)

The client connection preface starts with a sequence of 24 octets, which in hex notation is:[¶](#section-3.4-2)

```
  0x505249202a20485454502f322e300d0a0d0a534d0d0a0d0a
```

[¶](#section-3.4-3)

That is, the connection preface starts with the string "`PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n`". This sequence MUST be followed by a [SETTINGS](#SETTINGS) frame ([Section 6.5](#SETTINGS)), which MAY be empty. The client sends the client connection preface as the first application data octets of a connection.[¶](#section-3.4-4)

The server connection preface consists of a potentially empty [SETTINGS](#SETTINGS) frame ([Section 6.5](#SETTINGS)) that MUST be the first frame the server sends in the HTTP/2 connection.[¶](#section-3.4-6)

The [SETTINGS](#SETTINGS) frames received from a peer as part of the connection preface MUST be acknowledged (see [Section 6.5.3](#SettingsSync)) after sending the connection preface.[¶](#section-3.4-7)

To avoid unnecessary latency, clients are permitted to send additional frames to the server immediately after sending the client connection preface, without waiting to receive the server connection preface. It is important to note, however, that the server connection preface [SETTINGS](#SETTINGS) frame might include settings that necessarily alter how a client is expected to communicate with the server. Upon receiving the [SETTINGS](#SETTINGS) frame, the client is expected to honor any settings established. In some configurations, it is possible for the server to transmit [SETTINGS](#SETTINGS) before the client sends additional frames, providing an opportunity to avoid this issue.[¶](#section-3.4-8)

Clients and servers MUST treat an invalid connection preface as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR). A [GOAWAY](#GOAWAY) frame ([Section 6.8](#GOAWAY)) MAY be omitted in this case, since an invalid preface indicates that the peer is not using HTTP/2.[¶](#section-3.4-9)

## 4. HTTP Frames

Once the HTTP/2 connection is established, endpoints can begin exchanging frames.[¶](#section-4-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
