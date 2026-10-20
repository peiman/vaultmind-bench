---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9113.html#02-table-of-contents.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9113-02-table-of-contents
type: reference
title: 'RFC 9113: HTTP/2 › Table of Contents (1/2)'
url: https://www.rfc-editor.org/rfc/rfc9113.html
source: https://www.rfc-editor.org/rfc/rfc9113.html#02-table-of-contents
source_hash: 68045aa58fd730e1d4faf6b21b032e1437e089715ae7ff3d7d851d8779c0e910
---
- [1](#section-1).  [Introduction](#name-introduction)
- [2](#section-2).  [HTTP/2 Protocol Overview](#name-http-2-protocol-overview)

- [2.1](#section-2.1).  [Document Organization](#name-document-organization)
  - [2.2](#section-2.2).  [Conventions and Terminology](#name-conventions-and-terminology)
- [3](#section-3).  [Starting HTTP/2](#name-starting-http-2)

- [3.1](#section-3.1).  [HTTP/2 Version Identification](#name-http-2-version-identificati)
  - [3.2](#section-3.2).  [Starting HTTP/2 for "`https`" URIs](#name-starting-http-2-for-https-u)
  - [3.3](#section-3.3).  [Starting HTTP/2 with Prior Knowledge](#name-starting-http-2-with-prior-)
  - [3.4](#section-3.4).  [HTTP/2 Connection Preface](#name-http-2-connection-preface)
- [4](#section-4).  [HTTP Frames](#name-http-frames)

- [4.1](#section-4.1).  [Frame Format](#name-frame-format)
  - [4.2](#section-4.2).  [Frame Size](#name-frame-size)
  - [4.3](#section-4.3).  [Field Section Compression and Decompression](#name-field-section-compression-a)

- [4.3.1](#section-4.3.1).  [Compression State](#name-compression-state)
- [5](#section-5).  [Streams and Multiplexing](#name-streams-and-multiplexing)

- [5.1](#section-5.1).  [Stream States](#name-stream-states)

- [5.1.1](#section-5.1.1).  [Stream Identifiers](#name-stream-identifiers)
    - [5.1.2](#section-5.1.2).  [Stream Concurrency](#name-stream-concurrency)
  - [5.2](#section-5.2).  [Flow Control](#name-flow-control)

- [5.2.1](#section-5.2.1).  [Flow-Control Principles](#name-flow-control-principles)
    - [5.2.2](#section-5.2.2).  [Appropriate Use of Flow Control](#name-appropriate-use-of-flow-con)
    - [5.2.3](#section-5.2.3).  [Flow-Control Performance](#name-flow-control-performance)
  - [5.3](#section-5.3).  [Prioritization](#name-prioritization)

- [5.3.1](#section-5.3.1).  [Background on Priority in RFC 7540](#name-background-on-priority-in-r)
    - [5.3.2](#section-5.3.2).  [Priority Signaling in This Document](#name-priority-signaling-in-this-)
  - [5.4](#section-5.4).  [Error Handling](#name-error-handling)

- [5.4.1](#section-5.4.1).  [Connection Error Handling](#name-connection-error-handling)
    - [5.4.2](#section-5.4.2).  [Stream Error Handling](#name-stream-error-handling)
    - [5.4.3](#section-5.4.3).  [Connection Termination](#name-connection-termination)
  - [5.5](#section-5.5).  [Extending HTTP/2](#name-extending-http-2)
- [6](#section-6).  [Frame Definitions](#name-frame-definitions)

- [6.1](#section-6.1).  [DATA](#name-data)
  - [6.2](#section-6.2).  [HEADERS](#name-headers)
  - [6.3](#section-6.3).  [PRIORITY](#name-priority)
  - [6.4](#section-6.4).  [RST\_STREAM](#name-rst_stream)
  - [6.5](#section-6.5).  [SETTINGS](#name-settings)

- [6.5.1](#section-6.5.1).  [SETTINGS Format](#name-settings-format)
    - [6.5.2](#section-6.5.2).  [Defined Settings](#name-defined-settings)
    - [6.5.3](#section-6.5.3).  [Settings Synchronization](#name-settings-synchronization)
  - [6.6](#section-6.6).  [PUSH\_PROMISE](#name-push_promise)
  - [6.7](#section-6.7).  [PING](#name-ping)
  - [6.8](#section-6.8).  [GOAWAY](#name-goaway)
  - [6.9](#section-6.9).  [WINDOW\_UPDATE](#name-window_update)

- [6.9.1](#section-6.9.1).  [The Flow-Control Window](#name-the-flow-control-window)
    - [6.9.2](#section-6.9.2).  [Initial Flow-Control Window Size](#name-initial-flow-control-window)
    - [6.9.3](#section-6.9.3).  [Reducing the Stream Window Size](#name-reducing-the-stream-window-)
  - [6.10](#section-6.10). [CONTINUATION](#name-continuation)
- [7](#section-7).  [Error Codes](#name-error-codes)
- [8](#section-8).  [Expressing HTTP Semantics in HTTP/2](#name-expressing-http-semantics-i)

- [8.1](#section-8.1).  [HTTP Message Framing](#name-http-message-framing)

- [8.1.1](#section-8.1.1).  [Malformed Messages](#name-malformed-messages)
  - [8.2](#section-8.2).  [HTTP Fields](#name-http-fields)

- [8.2.1](#section-8.2.1).  [Field Validity](#name-field-validity)
    - [8.2.2](#section-8.2.2).  [Connection-Specific Header Fields](#name-connection-specific-header-)
    - [8.2.3](#section-8.2.3).  [Compressing the Cookie Header Field](#name-compressing-the-cookie-head)
  - [8.3](#section-8.3).  [HTTP Control Data](#name-http-control-data)

- [8.3.1](#section-8.3.1).  [Request Pseudo-Header Fields](#name-request-pseudo-header-field)
    - [8.3.2](#section-8.3.2).  [Response Pseudo-Header Fields](#name-response-pseudo-header-fiel)
  - [8.4](#section-8.4).  [Server Push](#name-server-push)

- [8.4.1](#section-8.4.1).  [Push Requests](#name-push-requests)
    - [8.4.2](#section-8.4.2).  [Push Responses](#name-push-responses)
  - [8.5](#section-8.5).  [The CONNECT Method](#name-the-connect-method)
  - [8.6](#section-8.6).  [The Upgrade Header Field](#name-the-upgrade-header-field)
  - [8.7](#section-8.7).  [Request Reliability](#name-request-reliability)
  - [8.8](#section-8.8).  [Examples](#name-examples)

- [8.8.1](#section-8.8.1).  [Simple Request](#name-simple-request)
    - [8.8.2](#section-8.8.2).  [Simple Response](#name-simple-response)
    - [8.8.3](#section-8.8.3).  [Complex Request](#name-complex-request)
    - [8.8.4](#section-8.8.4).  [Response with Body](#name-response-with-body)
    - [8.8.5](#section-8.8.5).  [Informational Responses](#name-informational-responses)
- [9](#section-9).  [HTTP/2 Connections](#name-http-2-connections)

- [9.1](#section-9.1).  [Connection Management](#name-connection-management)

- [9.1.1](#section-9.1.1).  [Connection Reuse](#name-connection-reuse)
  - [9.2](#section-9.2).  [Use of TLS Features](#name-use-of-tls-features)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9113]].
