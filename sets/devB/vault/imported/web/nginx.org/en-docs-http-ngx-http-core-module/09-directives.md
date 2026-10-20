---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#09-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-09-directives
type: reference
title: Module ngx_http_core_module › Directives (9/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#09-directives
source_hash: 9affe4154e0e0578350ceb43dec6a75e56f812603ce3eb3fb9209e07aa05eaa3
---
Context: `http`, `server`, `location`

Sets a time after which [open\_file\_cache](#open_file_cache) elements should be validated.

Syntax: `output_buffers number size;`  
Default:

```
output_buffers 2 32k;
```

Context: `http`, `server`, `location`

Sets the `number` and `size` of the buffers used for reading a response from a disk.

> Prior to version 1.9.5, the default value was 1 32k.

Syntax: `port_in_redirect on | off;`  
Default:

```
port_in_redirect on;
```

Context: `http`, `server`, `location`

Enables or disables specifying the port in [absolute](#absolute_redirect) redirects issued by nginx.

The use of the primary server name in redirects is controlled by the [server\_name\_in\_redirect](#server_name_in_redirect) directive.

Syntax: `postpone_output size;`  
Default:

```
postpone_output 1460;
```

Context: `http`, `server`, `location`

If possible, the transmission of client data will be postponed until nginx has at least `size` bytes of data to send. The zero value disables postponing data transmission.

Syntax: `read_ahead size;`  
Default:

```
read_ahead 0;
```

Context: `http`, `server`, `location`

Sets the amount of pre-reading for the kernel when working with file.

On Linux, the `posix_fadvise(0, 0, 0, POSIX_FADV_SEQUENTIAL)` system call is used, and so the `size` parameter is ignored.

On FreeBSD, the `fcntl(O_READAHEAD,` `size)` system call, supported since FreeBSD 9.0-CURRENT, is used. FreeBSD 7 has to be [patched](http://sysoev.ru/freebsd/patch.readahead.txt).

Syntax: `recursive_error_pages on | off;`  
Default:

```
recursive_error_pages off;
```

Context: `http`, `server`, `location`

Enables or disables doing several redirects using the [error\_page](#error_page) directive. The number of such redirects is [limited](#internal).

Syntax: `request_pool_size size;`  
Default:

```
request_pool_size 4k;
```

Context: `http`, `server`

Allows accurate tuning of per-request memory allocations. This directive has minimal impact on performance and should not generally be used.

Syntax: `reset_timedout_connection on | off;`  
Default:

```
reset_timedout_connection off;
```

Context: `http`, `server`, `location`

Enables or disables resetting timed out connections and connections [closed](https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#return) with the non-standard code 444 (1.15.2). The reset is performed as follows. Before closing a socket, the `SO_LINGER` option is set on it with a timeout value of 0. When the socket is closed, TCP RST is sent to the client, and all memory occupied by this socket is released. This helps avoid keeping an already closed socket with filled buffers in a FIN\_WAIT1 state for a long time.

It should be noted that timed out keep-alive connections are closed normally.

Syntax: `resolver address ... [valid=time] [ipv4=on|off] [ipv6=on|off] [status_zone=zone];`  
Default: — Context: `http`, `server`, `location`

Configures name servers used to resolve names of upstream servers into addresses, for example:

> ```
> resolver 127.0.0.1 [::1]:5353;
> ```

The address can be specified as a domain name or IP address, with an optional port (1.3.1, 1.2.2). If port is not specified, the port 53 is used. Name servers are queried in a round-robin fashion.

> Before version 1.1.7, only a single name server could be configured. Specifying name servers using IPv6 addresses is supported starting from versions 1.3.1 and 1.2.2.

By default, nginx will look up both IPv4 and IPv6 addresses while resolving. If looking up of IPv4 or IPv6 addresses is not desired, the `ipv4=off` (1.23.1) or the `ipv6=off` parameter can be specified.

> Resolving of names into IPv6 addresses is supported starting from version 1.5.8.

By default, nginx caches answers using the TTL value of a response. An optional `valid` parameter allows overriding it:

> ```
> resolver 127.0.0.1 [::1]:5353 valid=30s;
> ```

> Before version 1.1.9, tuning of caching time was not possible, and nginx always cached answers for the duration of 5 minutes.

> To prevent DNS spoofing, it is recommended configuring DNS servers in a properly secured trusted local network.

The optional `status_zone` parameter (1.17.1) enables [collection](https://nginx.org/en/docs/http/ngx_http_api_module.html#resolvers_) of DNS server statistics of requests and responses in the specified `zone`. The parameter is available as part of our [commercial subscription](https://www.f5.com/products/nginx).

Syntax: `resolver_timeout time;`  
Default:

```
resolver_timeout 30s;
```

Context: `http`, `server`, `location`

Sets a timeout for name resolution, for example:

> ```
> resolver_timeout 5s;
> ```

Syntax: `root path;`  
Default:

```
root html;
```

Context: `http`, `server`, `location`, `if in location`

Sets the root directory for requests. For example, with the following configuration

> ```
> location /i/ {
    root /data/w3;
}
> ```

The `/data/w3/i/top.gif` file will be sent in response to the “`/i/top.gif`” request.

The `path` value can contain variables, except `$document_root` and `$realpath_root`.

A path to the file is constructed by merely adding a URI to the value of the `root` directive. If a URI has to be modified, the [alias](#alias) directive should be used.

Syntax: `satisfy all | any;`  
Default:

```
satisfy all;
```

Context: `http`, `server`, `location`

Allows access if all (`all`) or at least one (`any`) of the [ngx\_http\_access\_module](https://nginx.org/en/docs/http/ngx_http_access_module.html), [ngx\_http\_auth\_basic\_module](https://nginx.org/en/docs/http/ngx_http_auth_basic_module.html), [ngx\_http\_auth\_request\_module](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html), [ngx\_http\_auth\_jwt\_module](https://nginx.org/en/docs/http/ngx_http_auth_jwt_module.html) (1.13.10), or [ngx\_http\_auth\_oidc\_module](https://nginx.org/en/docs/http/ngx_http_auth_jwt_module.html) (1.27.4) modules allow access.

Example:

> ```
> location / {
    satisfy any;

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
