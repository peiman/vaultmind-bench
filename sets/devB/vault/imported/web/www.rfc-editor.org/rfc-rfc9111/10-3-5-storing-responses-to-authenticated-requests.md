---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#10-3-5-storing-responses-to-authenticated-requests.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-10-3-5-storing-responses-to-authenticated-requests
type: reference
title: 'RFC 9111: HTTP Caching › 3. Storing Responses in Caches › 3.5. Storing Responses to Authenticated Requests'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#10-3-5-storing-responses-to-authenticated-requests
source_hash: 3fdb21ffaf0205b43e358b96ac79ff4e2a2c9022ef595c541895b455b7955674
---
A shared cache MUST NOT use a cached response to a request with an Authorization header field ([Section 11.6.2](https://www.rfc-editor.org/rfc/rfc9110#section-11.6.2) of \[[HTTP](#HTTP)]) to satisfy any subsequent request unless the response contains a [Cache-Control](#field.cache-control) field with a response directive ([Section 5.2.2](#cache-response-directive)) that allows it to be stored by a shared cache, and the cache conforms to the requirements of that directive for that response.[¶](#section-3.5-1)

In this specification, the following response directives have such an effect: must-revalidate ([Section 5.2.2.2](#cache-response-directive.must-revalidate)), public ([Section 5.2.2.9](#cache-response-directive.public)), and s-maxage ([Section 5.2.2.10](#cache-response-directive.s-maxage)).[¶](#section-3.5-2)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
