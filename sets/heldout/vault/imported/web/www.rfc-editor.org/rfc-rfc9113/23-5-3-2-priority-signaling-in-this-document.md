---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#23-5-3-2-priority-signaling-in-this-document.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-23-5-3-2-priority-signaling-in-this-document
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.3. Prioritization › 5.3.2. Priority Signaling in This Document'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#23-5-3-2-priority-signaling-in-this-document
source_hash: 409c9e69d47ed8681d4940c8df91b0c405ee95e392448e232b713d69eb40df5c
---
This update to HTTP/2 deprecates the priority signaling defined in [RFC 7540](#RFC7540) \[[RFC7540](#RFC7540)]. The bulk of the text related to priority signals is not included in this document. The description of frame fields and some of the mandatory handling is retained to ensure that implementations of this document remain interoperable with implementations that use the priority signaling described in RFC 7540.[¶](#section-5.3.2-1)

A thorough description of the RFC 7540 priority scheme remains in [Section 5.3](https://www.rfc-editor.org/rfc/rfc7540#section-5.3) of \[[RFC7540](#RFC7540)].[¶](#section-5.3.2-2)

Signaling priority information is necessary to attain good performance in many cases. Where signaling priority information is important, endpoints are encouraged to use an alternative scheme, such as the scheme described in \[[HTTP-PRIORITY](#RFC9218)].[¶](#section-5.3.2-3)

Though the priority signaling from RFC 7540 was not widely adopted, the information it provides can still be useful in the absence of better information. Endpoints that receive priority signals in [HEADERS](#HEADERS) or [PRIORITY](#PRIORITY) frames can benefit from applying that information. In particular, implementations that consume these signals would not benefit from discarding these priority signals in the absence of alternatives.[¶](#section-5.3.2-4)

Servers SHOULD use other contextual information in determining priority of requests in the absence of any priority signals. Servers MAY interpret the complete absence of signals as an indication that the client has not implemented the feature. The defaults described in [Section 5.3.5](https://www.rfc-editor.org/rfc/rfc7540#section-5.3.5) of \[[RFC7540](#RFC7540)] are known to have poor performance under most conditions, and their use is unlikely to be deliberate.[¶](#section-5.3.2-5)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
