---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#05-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-05-directives
type: reference
title: Module ngx_http_core_module › Directives (5/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#05-directives
source_hash: 5a8c40b4481dd693264e02363116a0ecc9710ba0c3eb04a4d8e7373f540ba656
---
The limits are similarly applied in HTTP/2 and HTTP/3 connections. The size of one buffer limits the maximum size of a request header field compressed with [HPACK](https://datatracker.ietf.org/doc/html/rfc7541) and [QPACK](https://datatracker.ietf.org/doc/html/rfc9204), respectively. Note that if Huffman encoding is applied, the actual size of decompressed name and value strings may be larger. The maximum size of the entire request header is limited after decompression.

If the directive is specified on the [server](#server) level, the value from the default server can be used. Details are provided in the “[Virtual server selection](https://nginx.org/en/docs/http/server_names.html#virtual_server_selection)” section.

Syntax: `limit_except method ... { ... }`  
Default: — Context: `location`

Limits allowed HTTP methods inside a location. The `method` parameter can be one of the following: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `MKCOL`, `COPY`, `MOVE`, `OPTIONS`, `PROPFIND`, `PROPPATCH`, `LOCK`, `UNLOCK`, or `PATCH`. Allowing the `GET` method makes the `HEAD` method also allowed. Access to other methods can be limited using the [ngx\_http\_access\_module](https://nginx.org/en/docs/http/ngx_http_access_module.html), [ngx\_http\_auth\_basic\_module](https://nginx.org/en/docs/http/ngx_http_auth_basic_module.html), and [ngx\_http\_auth\_jwt\_module](https://nginx.org/en/docs/http/ngx_http_auth_jwt_module.html) (1.13.10) modules directives:

> ```
> limit_except GET {
    allow 192.168.1.0/32;
    deny  all;
}
> ```

Please note that this will limit access to all methods **except** GET and HEAD.

Syntax: `limit_rate rate;`  
Default:

```
limit_rate 0;
```

Context: `http`, `server`, `location`, `if in location`

Limits the rate of response transmission to a client. The `rate` is specified in bytes per second. The zero value disables rate limiting. The limit is set per a request, and so if a client simultaneously opens two connections, the overall rate will be twice as much as the specified limit.

Parameter value can contain variables (1.17.0). It may be useful in cases where rate should be limited depending on a certain condition:

> ```
> map $slow $rate {
    1     4k;
    2     8k;
}

limit_rate $rate;
> ```

Rate limit can also be set in the [`$limit_rate`](#var_limit_rate) variable, however, since version 1.17.0, this method is not recommended:

> ```
> server {

if ($slow) {
        set $limit_rate 4k;
    }

...
}
> ```

Rate limit can also be set in the “X-Accel-Limit-Rate” header field of a proxied server response. This capability can be disabled using the [proxy\_ignore\_headers](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_ignore_headers), [fastcgi\_ignore\_headers](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html#fastcgi_ignore_headers), [uwsgi\_ignore\_headers](https://nginx.org/en/docs/http/ngx_http_uwsgi_module.html#uwsgi_ignore_headers), and [scgi\_ignore\_headers](https://nginx.org/en/docs/http/ngx_http_scgi_module.html#scgi_ignore_headers) directives.

Syntax: `limit_rate_after size;`  
Default:

```
limit_rate_after 0;
```

Context: `http`, `server`, `location`, `if in location`

This directive appeared in version 0.8.0.

Sets the initial amount after which the further transmission of a response to a client will be rate limited. Parameter value can contain variables (1.17.0).

Example:

> ```
> location /flv/ {
    flv;
    limit_rate_after 500k;
    limit_rate       50k;
}
> ```

Syntax: `lingering_close off | on | always;`  
Default:

```
lingering_close on;
```

Context: `http`, `server`, `location`

This directive appeared in versions 1.1.0 and 1.0.6.

Controls how nginx closes client connections.

The default value “`on`” instructs nginx to [wait for](#lingering_timeout) and [process](#lingering_time) additional data from a client before fully closing a connection, but only if heuristics suggests that a client may be sending more data.

The value “`always`” will cause nginx to unconditionally wait for and process additional client data.

The value “`off`” tells nginx to never wait for more data and close the connection immediately. This behavior breaks the protocol and should not be used under normal circumstances.

To control closing [HTTP/2](https://nginx.org/en/docs/http/ngx_http_v2_module.html) connections, the directive must be specified on the [server](#server) level (1.19.1).

Syntax: `lingering_time time;`  
Default:

```
lingering_time 30s;
```

Context: `http`, `server`, `location`

When [lingering\_close](#lingering_close) is in effect, this directive specifies the maximum time during which nginx will process (read and ignore) additional data coming from a client. After that, the connection will be closed, even if there will be more data.

Syntax: `lingering_timeout time;`  
Default:

```
lingering_timeout 5s;
```

Context: `http`, `server`, `location`

When [lingering\_close](#lingering_close) is in effect, this directive specifies the maximum waiting time for more client data to arrive. If data are not received during this time, the connection is closed. Otherwise, the data are read and ignored, and nginx starts waiting for more data again. The “wait-read-ignore” cycle is repeated, but no longer than specified by the [lingering\_time](#lingering_time) directive.

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
