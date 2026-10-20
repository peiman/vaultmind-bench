---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#59-10-5-denial-of-service-considerations.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-59-10-5-denial-of-service-considerations
type: reference
title: 'RFC 9113: HTTP/2 › 10. Security Considerations › 10.5. Denial-of-Service Considerations'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#59-10-5-denial-of-service-considerations
source_hash: 816d839b54ca90081a42518da56354c9007e53c2baa7351f27262b7d2d602617
---
An HTTP/2 connection can demand a greater commitment of resources to operate than an HTTP/1.1 connection. Both field section compression and flow control depend on a commitment of a greater amount of state. Settings for these features ensure that memory commitments for these features are strictly bounded.[¶](#section-10.5-1)

The number of [PUSH\_PROMISE](#PUSH_PROMISE) frames is not constrained in the same fashion. A client that accepts server push SHOULD limit the number of streams it allows to be in the "reserved (remote)" state. An excessive number of server push streams can be treated as a [stream error](#StreamErrorHandler) ([Section 5.4.2](#StreamErrorHandler)) of type [ENHANCE\_YOUR\_CALM](#ENHANCE_YOUR_CALM).[¶](#section-10.5-2)

A number of HTTP/2 implementations were found to be vulnerable to denial of service \[[NFLX-2019-002](#NFLX-2019-002)]. Below is a list of known ways that implementations might be subject to denial-of-service attacks:[¶](#section-10.5-3)

- Inefficient tracking of outstanding outbound frames can lead to overload if an adversary can cause large numbers of frames to be enqueued for sending. A peer could use one of several techniques to cause large numbers of frames to be generated:[¶](#section-10.5-4.1.1)
  
  - Providing tiny increments to flow control in [WINDOW\_UPDATE](#WINDOW_UPDATE) frames can cause a sender to generate a large number of [DATA](#DATA) frames.[¶](#section-10.5-4.1.2.1)
  - An endpoint is required to respond to a [PING](#PING) frame.[¶](#section-10.5-4.1.2.2)
  - Each [SETTINGS](#SETTINGS) frame requires acknowledgment.[¶](#section-10.5-4.1.2.3)
  - An invalid request (or server push) can cause a peer to send [RST\_STREAM](#RST_STREAM) frames in response.[¶](#section-10.5-4.1.2.4)
- An attacker can provide large amounts of flow-control credit at the HTTP/2 layer but withhold credit at the TCP layer, preventing frames from being sent. An endpoint that constructs and remembers frames for sending without considering TCP limits might be subject to resource exhaustion.[¶](#section-10.5-4.2)
- Large numbers of small or empty frames can be abused to cause a peer to expend time processing frame headers. Caution is required here as some uses of small frames are entirely legitimate, such as the sending of an empty [DATA](#DATA) or [CONTINUATION](#CONTINUATION) frame at the end of a stream.[¶](#section-10.5-4.3)
- The [SETTINGS](#SETTINGS) frame might also be abused to cause a peer to expend additional processing time. This might be done by pointlessly changing settings, sending multiple undefined settings, or changing the same setting multiple times in the same frame.[¶](#section-10.5-4.4)
- Handling reprioritization with [PRIORITY](#PRIORITY) frames can require significant processing time and can lead to overload if many [PRIORITY](#PRIORITY) frames are sent.[¶](#section-10.5-4.5)
- Field section compression also provides opportunities for an attacker to waste processing resources; see [Section 7](https://www.rfc-editor.org/rfc/rfc7541#section-7) of \[[COMPRESSION](#RFC7541)] for more details on potential abuses.[¶](#section-10.5-4.6)
- Limits in [SETTINGS](#SETTINGS) cannot be reduced instantaneously, which leaves an endpoint exposed to behavior from a peer that could exceed the new limits. In particular, immediately after establishing a connection, limits set by a server are not known to clients and could be exceeded without being an obvious protocol violation.[¶](#section-10.5-4.7)

Most of the features that might be exploited for denial of service -- such as [SETTINGS](#SETTINGS) changes, small frames, field section compression -- have legitimate uses. These features become a burden only when they are used unnecessarily or to excess.[¶](#section-10.5-5)

An endpoint that doesn't monitor use of these features exposes itself to a risk of denial of service. Implementations SHOULD track the use of these features and set limits on their use. An endpoint MAY treat activity that is suspicious as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [ENHANCE\_YOUR\_CALM](#ENHANCE_YOUR_CALM).[¶](#section-10.5-6)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
