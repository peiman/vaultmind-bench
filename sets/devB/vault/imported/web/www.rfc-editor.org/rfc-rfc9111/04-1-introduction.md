---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#04-1-introduction.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-04-1-introduction
type: reference
title: 'RFC 9111: HTTP Caching › 1. Introduction'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#04-1-introduction
source_hash: 12b387eed7ea2110a699d1c7d308ddbc43342a0ddbe4d16888c20e1f8c5e7c9d
---
The Hypertext Transfer Protocol (HTTP) is a stateless application-level request/response protocol that uses extensible semantics and self-descriptive messages for flexible interaction with network-based hypertext information systems. It is typically used for distributed information systems, where the use of response caches can improve performance. This document defines aspects of HTTP related to caching and reusing response messages.[¶](#section-1-1)

An HTTP "cache" is a local store of response messages and the subsystem that controls storage, retrieval, and deletion of messages in it. A cache stores cacheable responses to reduce the response time and network bandwidth consumption on future equivalent requests. Any client or server MAY use a cache, though not when acting as a tunnel ([Section 3.7](https://www.rfc-editor.org/rfc/rfc9110#section-3.7) of \[[HTTP](#HTTP)]).[¶](#section-1-2)

A "shared cache" is a cache that stores responses for reuse by more than one user; shared caches are usually (but not always) deployed as a part of an intermediary. A "private cache", in contrast, is dedicated to a single user; often, they are deployed as a component of a user agent.[¶](#section-1-3)

The goal of HTTP caching is significantly improving performance by reusing a prior response message to satisfy a current request. A cache considers a stored response "fresh", as defined in [Section 4.2](#expiration.model), if it can be reused without "validation" (checking with the origin server to see if the cached response remains valid for this request). A fresh response can therefore reduce both latency and network overhead each time the cache reuses it. When a cached response is not fresh, it might still be reusable if validation can freshen it ([Section 4.3](#validation.model)) or if the origin is unavailable ([Section 4.2.4](#serving.stale.responses)).[¶](#section-1-4)

This document obsoletes [RFC 7234](#RFC7234), with the changes being summarized in [Appendix B](#changes.from.rfc.7234).[¶](#section-1-5)

### 1.1. Requirements Notation

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 \[[RFC2119](#RFC2119)] \[[RFC8174](#RFC8174)] when, and only when, they appear in all capitals, as shown here.[¶](#section-1.1-1)

[Section 2](https://www.rfc-editor.org/rfc/rfc9110#section-2) of \[[HTTP](#HTTP)] defines conformance criteria and contains considerations regarding error handling.[¶](#section-1.1-2)

### 1.2. Syntax Notation

This specification uses the Augmented Backus-Naur Form (ABNF) notation of \[[RFC5234](#RFC5234)], extended with the notation for case-sensitivity in strings defined in \[[RFC7405](#RFC7405)].[¶](#section-1.2-1)

It also uses a list extension, defined in [Section 5.6.1](https://www.rfc-editor.org/rfc/rfc9110#section-5.6.1) of \[[HTTP](#HTTP)], that allows for compact definition of comma-separated lists using a "#" operator (similar to how the "\*" operator indicates repetition). [Appendix A](#collected.abnf) shows the collected grammar with all list operators expanded to standard ABNF notation.[¶](#section-1.2-2)

#### 1.2.1. Imported Rules

The following core rule is included by reference, as defined in \[[RFC5234](#RFC5234)], [Appendix B.1](https://www.rfc-editor.org/rfc/rfc5234#appendix-B.1): DIGIT (decimal 0-9).[¶](#section-1.2.1-1)

\[[HTTP](#HTTP)] defines the following rules:[¶](#section-1.2.1-2)

```
  HTTP-date     = <HTTP-date, see [HTTP], Section 5.6.7>
  OWS           = <OWS, see [HTTP], Section 5.6.3>
  field-name    = <field-name, see [HTTP], Section 5.1>
  quoted-string = <quoted-string, see [HTTP], Section 5.6.4>
  token         = <token, see [HTTP], Section 5.6.2>
```

[¶](#section-1.2.1-3)

#### 1.2.2. Delta Seconds

The delta-seconds rule specifies a non-negative integer, representing time in seconds.[¶](#section-1.2.2-1)

```
  delta-seconds  = 1*DIGIT
```

[¶](#section-1.2.2-2)

A recipient parsing a delta-seconds value and converting it to binary form ought to use an arithmetic type of at least 31 bits of non-negative integer range. If a cache receives a delta-seconds value greater than the greatest integer it can represent, or if any of its subsequent calculations overflows, the cache MUST consider the value to be 2147483648 (231) or the greatest positive integer it can conveniently represent.[¶](#section-1.2.2-3)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
