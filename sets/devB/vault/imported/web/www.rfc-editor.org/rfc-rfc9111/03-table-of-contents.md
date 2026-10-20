---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#03-table-of-contents.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-03-table-of-contents
type: reference
title: 'RFC 9111: HTTP Caching › Table of Contents'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#03-table-of-contents
source_hash: 48ae17c4ed59d64f991f143b232f3ea03e5398e82ab33d72bce69c7e7389e279
---
- [1](#section-1).  [Introduction](#name-introduction)
  
  - [1.1](#section-1.1).  [Requirements Notation](#name-requirements-notation)
  - [1.2](#section-1.2).  [Syntax Notation](#name-syntax-notation)
    
    - [1.2.1](#section-1.2.1).  [Imported Rules](#name-imported-rules)
    - [1.2.2](#section-1.2.2).  [Delta Seconds](#name-delta-seconds)
- [2](#section-2).  [Overview of Cache Operation](#name-overview-of-cache-operation)
- [3](#section-3).  [Storing Responses in Caches](#name-storing-responses-in-caches)
  
  - [3.1](#section-3.1).  [Storing Header and Trailer Fields](#name-storing-header-and-trailer-)
  - [3.2](#section-3.2).  [Updating Stored Header Fields](#name-updating-stored-header-fiel)
  - [3.3](#section-3.3).  [Storing Incomplete Responses](#name-storing-incomplete-response)
  - [3.4](#section-3.4).  [Combining Partial Content](#name-combining-partial-content)
  - [3.5](#section-3.5).  [Storing Responses to Authenticated Requests](#name-storing-responses-to-authen)
- [4](#section-4).  [Constructing Responses from Caches](#name-constructing-responses-from)
  
  - [4.1](#section-4.1).  [Calculating Cache Keys with the Vary Header Field](#name-calculating-cache-keys-with)
  - [4.2](#section-4.2).  [Freshness](#name-freshness)
    
    - [4.2.1](#section-4.2.1).  [Calculating Freshness Lifetime](#name-calculating-freshness-lifet)
    - [4.2.2](#section-4.2.2).  [Calculating Heuristic Freshness](#name-calculating-heuristic-fresh)
    - [4.2.3](#section-4.2.3).  [Calculating Age](#name-calculating-age)
    - [4.2.4](#section-4.2.4).  [Serving Stale Responses](#name-serving-stale-responses)
  - [4.3](#section-4.3).  [Validation](#name-validation)
    
    - [4.3.1](#section-4.3.1).  [Sending a Validation Request](#name-sending-a-validation-reques)
    - [4.3.2](#section-4.3.2).  [Handling a Received Validation Request](#name-handling-a-received-validat)
    - [4.3.3](#section-4.3.3).  [Handling a Validation Response](#name-handling-a-validation-respo)
    - [4.3.4](#section-4.3.4).  [Freshening Stored Responses upon Validation](#name-freshening-stored-responses)
    - [4.3.5](#section-4.3.5).  [Freshening Responses with HEAD](#name-freshening-responses-with-h)
  - [4.4](#section-4.4).  [Invalidating Stored Responses](#name-invalidating-stored-respons)
- [5](#section-5).  [Field Definitions](#name-field-definitions)
  
  - [5.1](#section-5.1).  [Age](#name-age)
  - [5.2](#section-5.2).  [Cache-Control](#name-cache-control)
    
    - [5.2.1](#section-5.2.1).  [Request Directives](#name-request-directives)
      
      - [5.2.1.1](#section-5.2.1.1).  [max-age](#name-max-age)
      - [5.2.1.2](#section-5.2.1.2).  [max-stale](#name-max-stale)
      - [5.2.1.3](#section-5.2.1.3).  [min-fresh](#name-min-fresh)
      - [5.2.1.4](#section-5.2.1.4).  [no-cache](#name-no-cache)
      - [5.2.1.5](#section-5.2.1.5).  [no-store](#name-no-store)
      - [5.2.1.6](#section-5.2.1.6).  [no-transform](#name-no-transform)
      - [5.2.1.7](#section-5.2.1.7).  [only-if-cached](#name-only-if-cached)
    - [5.2.2](#section-5.2.2).  [Response Directives](#name-response-directives)
      
      - [5.2.2.1](#section-5.2.2.1).  [max-age](#name-max-age-2)
      - [5.2.2.2](#section-5.2.2.2).  [must-revalidate](#name-must-revalidate)
      - [5.2.2.3](#section-5.2.2.3).  [must-understand](#name-must-understand)
      - [5.2.2.4](#section-5.2.2.4).  [no-cache](#name-no-cache-2)
      - [5.2.2.5](#section-5.2.2.5).  [no-store](#name-no-store-2)
      - [5.2.2.6](#section-5.2.2.6).  [no-transform](#name-no-transform-2)
      - [5.2.2.7](#section-5.2.2.7).  [private](#name-private)
      - [5.2.2.8](#section-5.2.2.8).  [proxy-revalidate](#name-proxy-revalidate)
      - [5.2.2.9](#section-5.2.2.9).  [public](#name-public)
      - [5.2.2.10](#section-5.2.2.10). [s-maxage](#name-s-maxage)
    - [5.2.3](#section-5.2.3).  [Extension Directives](#name-extension-directives)
    - [5.2.4](#section-5.2.4).  [Cache Directive Registry](#name-cache-directive-registry)
  - [5.3](#section-5.3).  [Expires](#name-expires)
  - [5.4](#section-5.4).  [Pragma](#name-pragma)
  - [5.5](#section-5.5).  [Warning](#name-warning)
- [6](#section-6).  [Relationship to Applications and Other Caches](#name-relationship-to-application)
- [7](#section-7).  [Security Considerations](#name-security-considerations)
  
  - [7.1](#section-7.1).  [Cache Poisoning](#name-cache-poisoning)
  - [7.2](#section-7.2).  [Timing Attacks](#name-timing-attacks)
  - [7.3](#section-7.3).  [Caching of Sensitive Information](#name-caching-of-sensitive-inform)
- [8](#section-8).  [IANA Considerations](#name-iana-considerations)
  
  - [8.1](#section-8.1).  [Field Name Registration](#name-field-name-registration)
  - [8.2](#section-8.2).  [Cache Directive Registration](#name-cache-directive-registratio)
  - [8.3](#section-8.3).  [Warn Code Registry](#name-warn-code-registry)
- [9](#section-9).  [References](#name-references)
  
  - [9.1](#section-9.1).  [Normative References](#name-normative-references)
  - [9.2](#section-9.2).  [Informative References](#name-informative-references)
- [Appendix A](#appendix-A).  [Collected ABNF](#name-collected-abnf)
- [Appendix B](#appendix-B).  [Changes from RFC 7234](#name-changes-from-rfc-7234)
- [](#appendix-C)[Acknowledgements](#name-acknowledgements)
- [](#appendix-D)[Index](#name-index)
- [](#appendix-E)[Authors' Addresses](#name-authors-addresses)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
