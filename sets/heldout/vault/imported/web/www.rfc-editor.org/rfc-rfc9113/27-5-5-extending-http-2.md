---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#27-5-5-extending-http-2.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-27-5-5-extending-http-2
type: reference
title: 'RFC 9113: HTTP/2 › 5. Streams and Multiplexing › 5.5. Extending HTTP/2'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#27-5-5-extending-http-2
source_hash: da8cb482dad627c9fa182f08f333c5b03205ad6aebc469c9dea36667ab08b019
---
HTTP/2 permits extension of the protocol. Within the limitations described in this section, protocol extensions can be used to provide additional services or alter any aspect of the protocol. Extensions are effective only within the scope of a single HTTP/2 connection.[¶](#section-5.5-1)

This applies to the protocol elements defined in this document. This does not affect the existing options for extending HTTP, such as defining new methods, status codes, or fields (see [Section 16](https://www.rfc-editor.org/rfc/rfc9110#section-16) of \[[HTTP](#RFC9110)]).[¶](#section-5.5-2)

Extensions are permitted to use new [frame types](#FrameHeader) ([Section 4.1](#FrameHeader)), new [settings](#SETTINGS) ([Section 6.5](#SETTINGS)), or new [error codes](#ErrorCodes) ([Section 7](#ErrorCodes)). Registries for managing these extension points are defined in [Section 11](https://www.rfc-editor.org/rfc/rfc7540#section-11) of \[[RFC7540](#RFC7540)].[¶](#section-5.5-3)

Implementations MUST ignore unknown or unsupported values in all extensible protocol elements. Implementations MUST discard frames that have unknown or unsupported types. This means that any of these extension points can be safely used by extensions without prior arrangement or negotiation. However, extension frames that appear in the middle of a [field block](#FieldBlock) ([Section 4.3](#FieldBlock)) are not permitted; these MUST be treated as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)) of type [PROTOCOL\_ERROR](#PROTOCOL_ERROR).[¶](#section-5.5-4)

Extensions SHOULD avoid changing protocol elements defined in this document or elements for which no extension mechanism is defined. This includes changes to the layout of frames, additions or changes to the way that frames are composed into [HTTP messages](#HttpFraming) ([Section 8.1](#HttpFraming)), the definition of pseudo-header fields, or changes to any protocol element that a compliant endpoint might treat as a [connection error](#ConnectionErrorHandler) ([Section 5.4.1](#ConnectionErrorHandler)).[¶](#section-5.5-5)

An extension that changes existing protocol elements or state MUST be negotiated before being used. For example, an extension that changes the layout of the [HEADERS](#HEADERS) frame cannot be used until the peer has given a positive signal that this is acceptable. In this case, it could also be necessary to coordinate when the revised layout comes into effect. For example, treating frames other than [DATA](#DATA) frames as flow controlled requires a change in semantics that both endpoints need to understand, so this can only be done through negotiation.[¶](#section-5.5-6)

This document doesn't mandate a specific method for negotiating the use of an extension but notes that a [setting](#SettingValues) ([Section 6.5.2](#SettingValues)) could be used for that purpose. If both peers set a value that indicates willingness to use the extension, then the extension can be used. If a setting is used for extension negotiation, the initial value MUST be defined in such a fashion that the extension is initially disabled.[¶](#section-5.5-7)

## 6. Frame Definitions

This specification defines a number of frame types, each identified by a unique 8-bit type code. Each frame type serves a distinct purpose in the establishment and management of either the connection as a whole or individual streams.[¶](#section-6-1)

The transmission of specific frame types can alter the state of a connection. If endpoints fail to maintain a synchronized view of the connection state, successful communication within the connection will no longer be possible. Therefore, it is important that endpoints have a shared comprehension of how the state is affected by the use of any given frame.[¶](#section-6-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
