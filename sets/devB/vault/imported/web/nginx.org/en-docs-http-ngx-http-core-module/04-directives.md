---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#04-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-04-directives
type: reference
title: Module ngx_http_core_module › Directives (4/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#04-directives
source_hash: c3ad6a4d6b3161af1eee4ade28878d5c0a4acaf6b3a56e01b5b1c147f02db9e7
---
Specifies how to compare modification time of a response with the time in the “If-Modified-Since” request header field:

`off`

the response is always considered modified (0.7.34);

`exact`

exact match;

`before`

modification time of the response is less than or equal to the time in the “If-Modified-Since” request header field.

Syntax: `ignore_invalid_headers on | off;`  
Default:

```
ignore_invalid_headers on;
```

Context: `http`, `server`

Controls whether header fields with invalid names should be ignored. Valid names are composed of English letters, digits, hyphens, and possibly underscores (as controlled by the [underscores\_in\_headers](#underscores_in_headers) directive).

If the directive is specified on the [server](#server) level, the value from the default server can be used. Details are provided in the “[Virtual server selection](https://nginx.org/en/docs/http/server_names.html#virtual_server_selection)” section.

Syntax: `internal;`  
Default: — Context: `location`

Specifies that a given location can only be used for internal requests. For external requests, the client error 404 (Not Found) is returned. Internal requests are the following:

- requests redirected by the [error\_page](#error_page), [index](https://nginx.org/en/docs/http/ngx_http_index_module.html#index), [internal\_redirect](https://nginx.org/en/docs/http/ngx_http_internal_redirect_module.html#internal_redirect), [random\_index](https://nginx.org/en/docs/http/ngx_http_random_index_module.html#random_index), and [try\_files](#try_files) directives;
- requests redirected by the “X-Accel-Redirect” response header field from an upstream server;
- subrequests formed by the “`include virtual`” command of the [ngx\_http\_ssi\_module](https://nginx.org/en/docs/http/ngx_http_ssi_module.html) module, by the [ngx\_http\_addition\_module](https://nginx.org/en/docs/http/ngx_http_addition_module.html) module directives, and by [auth\_request](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html#auth_request) and [mirror](https://nginx.org/en/docs/http/ngx_http_mirror_module.html#mirror) directives;
- requests changed by the [rewrite](https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#rewrite) directive.

Example:

> ```
> error_page 404 /404.html;

location = /404.html {
    internal;
}
> ```

> There is a limit of 10 internal redirects per request to prevent request processing cycles that can occur in incorrect configurations. If this limit is reached, the error 500 (Internal Server Error) is returned. In such cases, the “rewrite or internal redirection cycle” message can be seen in the error log.

Syntax: `keepalive_disable none | browser ...;`  
Default:

```
keepalive_disable msie6;
```

Context: `http`, `server`, `location`

Disables keep-alive connections with misbehaving browsers. The `browser` parameters specify which browsers will be affected. The value `msie6` disables keep-alive connections with old versions of MSIE, once a POST request is received. The value `safari` disables keep-alive connections with Safari and Safari-like browsers on macOS and macOS-like operating systems. The value `none` enables keep-alive connections with all browsers.

> Prior to version 1.1.18, the value `safari` matched all Safari and Safari-like browsers on all operating systems, and keep-alive connections with them were disabled by default.

Syntax: `keepalive_min_timeout timeout;`  
Default:

```
keepalive_min_timeout 0;
```

Context: `http`, `server`, `location`

This directive appeared in version 1.27.4.

Sets a timeout during which a keep-alive client connection will not be closed on the server side for connection reuse or on graceful shutdown of worker processes.

Syntax: `keepalive_requests number;`  
Default:

```
keepalive_requests 1000;
```

Context: `http`, `server`, `location`

This directive appeared in version 0.8.0.

Sets the maximum number of requests that can be served through one keep-alive connection. After the maximum number of requests are made, the connection is closed.

Closing connections periodically is necessary to free per-connection memory allocations. Therefore, using too high maximum number of requests could result in excessive memory usage and not recommended.

> Prior to version 1.19.10, the default value was 100.

Syntax: `keepalive_time time;`  
Default:

```
keepalive_time 1h;
```

Context: `http`, `server`, `location`

This directive appeared in version 1.19.10.

Limits the maximum time during which requests can be processed through one keep-alive connection. After this time is reached, the connection is closed following the subsequent request processing.

Syntax: `keepalive_timeout timeout [header_timeout];`  
Default:

```
keepalive_timeout 75s;
```

Context: `http`, `server`, `location`

The first parameter sets a timeout during which a keep-alive client connection will stay open on the server side. The zero value disables keep-alive client connections. The optional second parameter sets a value in the “Keep-Alive: timeout=`time`” response header field. Two parameters may differ.

The “Keep-Alive: timeout=`time`” header field is recognized by Mozilla and Konqueror. MSIE closes keep-alive connections by itself in about 60 seconds.

Syntax: `large_client_header_buffers number size;`  
Default:

```
large_client_header_buffers 4 8k;
```

Context: `http`, `server`

Sets the maximum `number` and `size` of buffers used for reading large client request header. A request line cannot exceed the size of one buffer, or the 414 (Request-URI Too Large) error is returned to the client. A request header field cannot exceed the size of one buffer as well, or the 400 (Bad Request) error is returned to the client. Buffers are allocated only on demand. By default, the buffer size is equal to 8K bytes. If after the end of request processing a connection is transitioned into the keep-alive state, these buffers are released.

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
