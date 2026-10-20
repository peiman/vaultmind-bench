---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#25-7-security-considerations.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-25-7-security-considerations
type: reference
title: 'RFC 9111: HTTP Caching › 7. Security Considerations'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#25-7-security-considerations
source_hash: e624ea152f276d3710afc040e7f84be4e9bf5a22d7505ba3547845afda5acdb0
---
This section is meant to inform developers, information providers, and users of known security concerns specific to HTTP caching. More general security considerations are addressed in "HTTP/1.1" ([Section 11](https://www.rfc-editor.org/rfc/rfc9112#section-11) of \[[HTTP/1.1](#HTTP11)]) and "HTTP Semantics" ([Section 17](https://www.rfc-editor.org/rfc/rfc9110#section-17) of \[[HTTP](#HTTP)]).[¶](#section-7-1)

Caches expose an additional attack surface because the contents of the cache represent an attractive target for malicious exploitation. Since cache contents persist after an HTTP request is complete, an attack on the cache can reveal information long after a user believes that the information has been removed from the network. Therefore, cache contents need to be protected as sensitive information.[¶](#section-7-2)

In particular, because private caches are restricted to a single user, they can be used to reconstruct a user's activity. As a result, it is important for user agents to allow end users to control them, for example, by allowing stored responses to be removed for some or all origin servers.[¶](#section-7-3)

### 7.1. Cache Poisoning

Storing malicious content in a cache can extend the reach of an attacker to affect multiple users. Such "cache poisoning" attacks happen when an attacker uses implementation flaws, elevated privileges, or other techniques to insert a response into a cache. This is especially effective when shared caches are used to distribute malicious content to many clients.[¶](#section-7.1-1)

One common attack vector for cache poisoning is to exploit differences in message parsing on proxies and in user agents; see [Section 6.3](https://www.rfc-editor.org/rfc/rfc9112#section-6.3) of \[[HTTP/1.1](#HTTP11)] for the relevant requirements regarding HTTP/1.1.[¶](#section-7.1-2)

### 7.2. Timing Attacks

Because one of the primary uses of a cache is to optimize performance, its use can "leak" information about which resources have been previously requested.[¶](#section-7.2-1)

For example, if a user visits a site and their browser caches some of its responses and then navigates to a second site, that site can attempt to load responses it knows exist on the first site. If they load quickly, it can be assumed that the user has visited that site, or even a specific page on it.[¶](#section-7.2-2)

Such "timing attacks" can be mitigated by adding more information to the cache key, such as the identity of the referring site (to prevent the attack described above). This is sometimes called "double keying".[¶](#section-7.2-3)

### 7.3. Caching of Sensitive Information

Implementation and deployment flaws (often led to by the misunderstanding of cache operation) might lead to the caching of sensitive information (e.g., authentication credentials) that is thought to be private, exposing it to unauthorized parties.[¶](#section-7.3-1)

Note that the Set-Cookie response header field \[[COOKIE](#COOKIE)] does not inhibit caching; a cacheable response with a Set-Cookie header field can be (and often is) used to satisfy subsequent requests to caches. Servers that wish to control caching of these responses are encouraged to emit appropriate Cache-Control response header fields.[¶](#section-7.3-2)

## 8. IANA Considerations

The change controller for the following registrations is: "IETF (iesg@ietf.org) - Internet Engineering Task Force".[¶](#section-8-1)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
