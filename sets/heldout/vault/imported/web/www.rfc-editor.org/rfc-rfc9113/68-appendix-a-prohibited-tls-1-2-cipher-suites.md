---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#68-appendix-a-prohibited-tls-1-2-cipher-suites.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-68-appendix-a-prohibited-tls-1-2-cipher-suites
type: reference
title: 'RFC 9113: HTTP/2 › Appendix A. Prohibited TLS 1.2 Cipher Suites (2/2)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#68-appendix-a-prohibited-tls-1-2-cipher-suites
source_hash: 89d94b78ae5934706d1f9096392f9d05c5b924a9df331644edc80558034feee0
---
For more details, see [Section 9.2.2](#tls12ciphers).[¶](#appendix-A-4)

## Appendix B. Changes from RFC 7540

This revision includes the following substantive changes:[¶](#appendix-B-1)

- Use of TLS 1.3 was defined based on \[[RFC8740](#RFC8740)], which this document obsoletes.[¶](#appendix-B-2.1)
- The priority scheme defined in RFC 7540 is deprecated. Definitions for the format of the [PRIORITY](#PRIORITY) frame and the priority fields in the [HEADERS](#HEADERS) frame have been retained, plus the rules governing when [PRIORITY](#PRIORITY) frames can be sent and received, but the semantics of these fields are only described in RFC 7540. The priority signaling scheme from RFC 7540 was not successful. Using the simpler signaling in \[[HTTP-PRIORITY](#RFC9218)] is recommended.[¶](#appendix-B-2.2)
- The HTTP/1.1 Upgrade mechanism is deprecated and no longer specified in this document. It was never widely deployed, with plaintext HTTP/2 users choosing to use the prior-knowledge implementation instead.[¶](#appendix-B-2.3)
- Validation for field names and values has been narrowed. The validation that is mandatory for intermediaries is precisely defined, and error reporting for requests has been amended to encourage sending 400-series status codes.[¶](#appendix-B-2.4)
- The ranges of codepoints for settings and frame types that were reserved for Experimental Use are now available for general use.[¶](#appendix-B-2.5)
- Connection-specific header fields -- which are prohibited -- are more precisely and comprehensively identified.[¶](#appendix-B-2.6)
- `Host` and "`:authority`" are no longer permitted to disagree.[¶](#appendix-B-2.7)
- Rules for sending Dynamic Table Size Update instructions after changes in settings have been clarified in [Section 4.3.1](#dynamic-table).[¶](#appendix-B-2.8)

Editorial changes are also included. In particular, changes to terminology and document structure are in response to updates to [core HTTP semantics](#RFC9110) \[[HTTP](#RFC9110)]. Those documents now include some concepts that were first defined in RFC 7540, such as the 421 status code or connection coalescing.[¶](#appendix-B-3)

## Acknowledgments

Credit for non-trivial input to this document is owed to a large number of people who have contributed to the HTTP Working Group over the years. \[[RFC7540](#RFC7540)] contains a more extensive list of people that deserve acknowledgment for their contributions.[¶](#appendix-C-1)

## Contributors

Mike Belshe and Roberto Peon authored the text that this document is based on.[¶](#appendix-D-1)

## Authors' Addresses

Martin Thomson (editor)

Mozilla

Australia

Cory Benfield (editor)

Apple Inc.

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
