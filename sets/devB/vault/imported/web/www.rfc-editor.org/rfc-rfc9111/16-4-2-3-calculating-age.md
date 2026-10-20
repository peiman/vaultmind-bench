---
# Imported by `vaultmind import` from https://www.rfc-editor.org/rfc/rfc9111.html#16-4-2-3-calculating-age.
# The page is the source: re-run the import to refresh it.
id: imported-web-www-rfc-editor-org-rfc-rfc9111-16-4-2-3-calculating-age
type: reference
title: 'RFC 9111: HTTP Caching › 4. Constructing Responses from Caches › 4.2. Freshness › 4.2.3. Calculating Age'
url: https://www.rfc-editor.org/rfc/rfc9111.html
source: https://www.rfc-editor.org/rfc/rfc9111.html#16-4-2-3-calculating-age
source_hash: 92dda2712628eb11a7fc91e70b1a072efc54cf5bcf379764a1eb8677849a0001
---
The [Age](#field.age) header field is used to convey an estimated age of the response message when obtained from a cache. The Age field value is the cache's estimate of the number of seconds since the origin server generated or validated the response. The Age value is therefore the sum of the time that the response has been resident in each of the caches along the path from the origin server, plus the time it has been in transit along network paths.[¶](#section-4.2.3-1)

Age calculation uses the following data:[¶](#section-4.2.3-2)

"age\_value"

The term "age\_value" denotes the value of the [Age](#field.age) header field ([Section 5.1](#field.age)), in a form appropriate for arithmetic operation; or 0, if not available.[¶](#section-4.2.3-3.2)

"date\_value"

The term "date\_value" denotes the value of the Date header field, in a form appropriate for arithmetic operations. See [Section 6.6.1](https://www.rfc-editor.org/rfc/rfc9110#section-6.6.1) of \[[HTTP](#HTTP)] for the definition of the Date header field and for requirements regarding responses without it.[¶](#section-4.2.3-3.4)

"now"

The term "now" means the current value of this implementation's clock ([Section 5.6.7](https://www.rfc-editor.org/rfc/rfc9110#section-5.6.7) of \[[HTTP](#HTTP)]).[¶](#section-4.2.3-3.6)

"request\_time"

The value of the clock at the time of the request that resulted in the stored response.[¶](#section-4.2.3-3.8)

"response\_time"

The value of the clock at the time the response was received.[¶](#section-4.2.3-3.10)

A response's age can be calculated in two entirely independent ways:[¶](#section-4.2.3-4)

1. the "apparent\_age": response\_time minus date\_value, if the implementation's clock is reasonably well synchronized to the origin server's clock. If the result is negative, the result is replaced by zero.[¶](#section-4.2.3-5.1)
2. the "corrected\_age\_value", if all of the caches along the response path implement HTTP/1.1 or greater. A cache MUST interpret this value relative to the time the request was initiated, not the time that the response was received.[¶](#section-4.2.3-5.2)

```
  apparent_age = max(0, response_time - date_value);

  response_delay = response_time - request_time;
  corrected_age_value = age_value + response_delay;
```

[¶](#section-4.2.3-6)

The corrected\_age\_value MAY be used as the corrected\_initial\_age. In circumstances where very old cache implementations that might not correctly insert [Age](#field.age) are present, corrected\_initial\_age can be calculated more conservatively as[¶](#section-4.2.3-7)

```
  corrected_initial_age = max(apparent_age, corrected_age_value);
```

[¶](#section-4.2.3-8)

The current\_age of a stored response can then be calculated by adding the time (in seconds) since the stored response was last validated by the origin server to the corrected\_initial\_age.[¶](#section-4.2.3-9)

```
  resident_time = now - response_time;
  current_age = corrected_initial_age + resident_time;
```

[¶](#section-4.2.3-10)

Part of [[imported/web/www.rfc-editor.org/rfc-rfc9111]].
