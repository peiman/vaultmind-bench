---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#08-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-08-directives
type: reference
title: Module ngx_http_core_module › Directives (8/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#08-directives
source_hash: 80440db35820de69b015870ed97e28856c47ce25135282a9e3c630f5fef34993
---
The “`/`” request will match configuration A, the “`/index.html`” request will match configuration B, the “`/documents/document.html`” request will match configuration C, the “`/images/1.gif`” request will match configuration D, the “`/documents/1.jpg`” request will match configuration E, and the “`/documents/index.html?pred=1`” request will match configuration F.

The “`@`” prefix defines a named location. Such a location is not used for a regular request processing, but instead used for request redirection. They cannot be nested, and cannot contain nested locations.

If a location is defined by a prefix string that ends with the slash character, and requests are processed by one of [proxy\_pass](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass), [fastcgi\_pass](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html#fastcgi_pass), [uwsgi\_pass](https://nginx.org/en/docs/http/ngx_http_uwsgi_module.html#uwsgi_pass), [scgi\_pass](https://nginx.org/en/docs/http/ngx_http_scgi_module.html#scgi_pass), [memcached\_pass](https://nginx.org/en/docs/http/ngx_http_memcached_module.html#memcached_pass), or [grpc\_pass](https://nginx.org/en/docs/http/ngx_http_grpc_module.html#grpc_pass), then the special processing is performed. In response to a request with URI equal to this string, but without the trailing slash, a permanent redirect with the code 301 will be returned to the requested URI with the slash appended. If this is not desired, an exact match of the URI and location could be defined like this:

> ```
> location /user/ {
    proxy_pass http://user.example.com;
}

location = /user {
    proxy_pass http://login.example.com;
}
> ```

Syntax: `log_not_found on | off;`  
Default:

```
log_not_found on;
```

Context: `http`, `server`, `location`

Enables or disables logging of errors about not found files into [error\_log](https://nginx.org/en/docs/ngx_core_module.html#error_log).

Syntax: `log_subrequest on | off;`  
Default:

```
log_subrequest off;
```

Context: `http`, `server`, `location`

Enables or disables logging of subrequests into [access\_log](https://nginx.org/en/docs/http/ngx_http_log_module.html#access_log).

Syntax: `max_headers number;`  
Default:

```
max_headers 1000;
```

Context: `http`, `server`

This directive appeared in version 1.29.8.

Sets the maximum allowed number of header lines in requests. If this limit is reached, the error 400 (Bad Request) is returned.

Syntax: `max_ranges number;`  
Default: — Context: `http`, `server`, `location`

This directive appeared in version 1.1.2.

Limits the maximum allowed number of ranges in byte-range requests. Requests that exceed the limit are processed as if there were no byte ranges specified. By default, the number of ranges is not limited. The zero value disables the byte-range support completely.

Syntax: `merge_slashes on | off;`  
Default:

```
merge_slashes on;
```

Context: `http`, `server`

Enables or disables compression of two or more adjacent slashes in a URI into a single slash.

Note that compression is essential for the correct matching of prefix string and regular expression locations. Without it, the “`//scripts/one.php`” request would not match

> ```
> location /scripts/ {
    ...
}
> ```

and might be processed as a static file. So it gets converted to “`/scripts/one.php`”.

Turning the compression `off` can become necessary if a URI contains base64-encoded names, since base64 uses the “`/`” character internally. However, for security considerations, it is better to avoid turning the compression off.

If the directive is specified on the [server](#server) level, the value from the default server can be used. Details are provided in the “[Virtual server selection](https://nginx.org/en/docs/http/server_names.html#virtual_server_selection)” section.

Syntax: `msie_padding on | off;`  
Default:

```
msie_padding on;
```

Context: `http`, `server`, `location`

Enables or disables adding comments to responses for MSIE clients with status greater than 400 to increase the response size to 512 bytes.

Syntax: `msie_refresh on | off;`  
Default:

```
msie_refresh off;
```

Context: `http`, `server`, `location`

Enables or disables issuing refreshes instead of redirects for MSIE clients.

Syntax: `open_file_cache off;`  
`open_file_cache max=N [inactive=time];`  
Default:

```
open_file_cache off;
```

Context: `http`, `server`, `location`

Configures a cache that can store:

- open file descriptors, their sizes and modification times;
- information on existence of directories;
- file lookup errors, such as “file not found”, “no read permission”, and so on.

> Caching of errors should be enabled separately by the [open\_file\_cache\_errors](#open_file_cache_errors) directive.

The directive has the following parameters:

`max`

sets the maximum number of elements in the cache; on cache overflow the least recently used (LRU) elements are removed;

`inactive`

defines a time after which an element is removed from the cache if it has not been accessed during this time; by default, it is 60 seconds;

`off`

disables the cache.

Example:

> ```
> open_file_cache          max=1000 inactive=20s;
open_file_cache_valid    30s;
open_file_cache_min_uses 2;
open_file_cache_errors   on;
> ```

Syntax: `open_file_cache_errors on | off;`  
Default:

```
open_file_cache_errors off;
```

Context: `http`, `server`, `location`

Enables or disables caching of file lookup errors by [open\_file\_cache](#open_file_cache).

Syntax: `open_file_cache_min_uses number;`  
Default:

```
open_file_cache_min_uses 1;
```

Context: `http`, `server`, `location`

Sets the minimum `number` of file accesses during the period configured by the `inactive` parameter of the [open\_file\_cache](#open_file_cache) directive, required for a file descriptor to remain open in the cache.

Syntax: `open_file_cache_valid time;`  
Default:

```
open_file_cache_valid 60s;
```

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
