---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#20-5-1-2-stream-concurrency.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-20-5-1-2-stream-concurrency
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.1. Stream States › 5.1.2. Stream Concurrency'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#20-5-1-2-stream-concurrency
source_hash: 1241567e69c98f1b9a16216a4c89a25b04dce1583f88e1f90455eca64219d5ca
---
A peer can limit the number of concurrently active streams using the [SETTINGS\_MAX\_CONCURRENT\_STREAMS](#SETTINGS_MAX_CONCURRENT_STREAMS) parameter (see [Section 6.5.2](#SettingValues)) within a [SETTINGS](#SETTINGS) frame. The maximum concurrent streams setting is specific to each endpoint and applies only to the peer that receives the setting. That is, clients specify the maximum number of concurrent streams the server can initiate, and servers specify the maximum number of concurrent streams the client can initiate.[¶](#section-5.1.2-1)

Streams that are in the "open" state or in either of the "half-closed" states count toward the maximum number of streams that an endpoint is permitted to open. Streams in any of these three states count toward the limit advertised in the [SETTINGS\_MAX\_CONCURRENT\_STREAMS](#SETTINGS_MAX_CONCURRENT_STREAMS) setting. Streams in either of the "reserved" states do not count toward the stream limit.[¶](#section-5.1.2-2)

Endpoints MUST NOT exceed the limit set by their peer. An endpoint that receives a [HEADERS](#HEADERS) frame that causes its advertised concurrent stream limit to be exceeded MUST treat this as a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR) or [REFUSED\_STREAM](#REFUSED_STREAM). The choice of error code determines whether the endpoint wishes to enable automatic retry (see [Section 8.7](#Reliability) for details).[¶](#section-5.1.2-3)

An endpoint that wishes to reduce the value of [SETTINGS\_MAX\_CONCURRENT\_STREAMS](#SETTINGS_MAX_CONCURRENT_STREAMS) to a value that is below the current number of open streams can either close streams that exceed the new value or allow streams to complete.[¶](#section-5.1.2-4)

### 5.2. Flow Control

Using streams for multiplexing introduces contention over use of the TCP connection, resulting in blocked streams. A flow-control scheme ensures that streams on the same connection do not destructively interfere with each other. Flow control is used for both individual streams and the connection as a whole.[¶](#section-5.2-1)

HTTP/2 provides for flow control through use of the [WINDOW\_UPDATE frame](#WINDOW_UPDATE) ([Section 6.9](#WINDOW_UPDATE)).[¶](#section-5.2-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
