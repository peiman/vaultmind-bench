---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#47-8-4-server-push.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-47-8-4-server-push
type: reference
title: 'RFC 9113: HTTP/2 › 8. Expressing HTTP Semantics in HTTP/2 › 8.4. Server Push'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#47-8-4-server-push
source_hash: b4f4fe3febf7afc055178af92940689e046eaa63d6c03c1c877b5b672270b17c
---
HTTP/2 allows a server to preemptively send (or "push") responses (along with corresponding "promised" requests) to a client in association with a previous client-initiated request.[¶](#section-8.4-1)

Server push was designed to allow a server to improve client-perceived performance by predicting what requests will follow those that it receives, thereby removing a round trip for them. For example, a request for HTML is often followed by requests for stylesheets and scripts referenced by that page. When these requests are pushed, the client does not need to wait to receive the references to them in the HTML and issue separate requests.[¶](#section-8.4-2)

In practice, server push is difficult to use effectively, because it requires the server to correctly anticipate the additional requests the client will make, taking into account factors such as caching, content negotiation, and user behavior. Errors in prediction can lead to performance degradation, due to the opportunity cost that the additional data on the wire represents. In particular, pushing any significant amount of data can cause contention issues with responses that are more important.[¶](#section-8.4-3)

A client can request that server push be disabled, though this is negotiated for each hop independently. The [SETTINGS\_ENABLE\_PUSH](#SETTINGS_ENABLE_PUSH) setting can be set to 0 to indicate that server push is disabled.[¶](#section-8.4-4)

Promised requests MUST be safe (see [Section 9.2.1](https://www.rfc-editor.org/rfc/rfc9110#section-9.2.1) of \[[HTTP](#RFC9110)]) and cacheable (see [Section 9.2.3](https://www.rfc-editor.org/rfc/rfc9110#section-9.2.3) of \[[HTTP](#RFC9110)]). Promised requests cannot include any content or a trailer section. Clients that receive a promised request that is not cacheable, that is not known to be safe, or that indicates the presence of request content MUST reset the promised stream with a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR). Note that this could result in the promised stream being reset if the client does not recognize a newly defined method as being safe.[¶](#section-8.4-5)

Pushed responses that are cacheable (see [Section 3](https://www.rfc-editor.org/rfc/rfc9111#section-3) of \[[CACHING](#RFC9111)]) can be stored by the client, if it implements an HTTP cache. Pushed responses are considered successfully validated on the origin server (e.g., if the "no-cache" cache response directive is present; see [Section 5.2.2.4](https://www.rfc-editor.org/rfc/rfc9111#section-5.2.2.4) of \[[CACHING](#RFC9111)]) while the stream identified by the promised stream identifier is still open.[¶](#section-8.4-6)

Pushed responses that are not cacheable MUST NOT be stored by any HTTP cache. They MAY be made available to the application separately.[¶](#section-8.4-7)

The server MUST include a value in the "`:authority`" pseudo-header field for which the server is authoritative (see [Section 10.1](#authority)). A client MUST treat a [PUSH\_PROMISE](#PUSH_PROMISE) for which the server is not authoritative as a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-8.4-8)

An intermediary can receive pushes from the server and choose not to forward them on to the client. In other words, how to make use of the pushed information is up to that intermediary. Equally, the intermediary might choose to make additional pushes to the client, without any action taken by the server.[¶](#section-8.4-9)

A client cannot push. Thus, servers MUST treat the receipt of a [PUSH\_PROMISE](#PUSH_PROMISE) frame as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR). A server cannot set the [SETTINGS\_ENABLE\_PUSH](#SETTINGS_ENABLE_PUSH) setting to a value other than 0 (see [Section 6.5.2](#SettingValues)).[¶](#section-8.4-10)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
