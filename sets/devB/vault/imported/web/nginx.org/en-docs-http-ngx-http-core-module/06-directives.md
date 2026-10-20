---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#06-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-06-directives
type: reference
title: Module ngx_http_core_module › Directives (6/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#06-directives
source_hash: bac676cabe7fa89094eec65dcb0f30de64f14fd19814d7d04b7900b2a6a54173
---
Syntax: `listen address[:port] [default_server] [ssl] [http2 | quic] [proxy_protocol] [setfib=number] [fastopen=number] [backlog=number] [rcvbuf=size] [sndbuf=size] [accept_filter=filter] [deferred] [bind] [ipv6only=on|off] [reuseport] [multipath] [so_keepalive=on|off|[keepidle]:[keepintvl]:[keepcnt]];`  
`listen port [default_server] [ssl] [http2 | quic] [proxy_protocol] [setfib=number] [fastopen=number] [backlog=number] [rcvbuf=size] [sndbuf=size] [accept_filter=filter] [deferred] [bind] [ipv6only=on|off] [reuseport] [multipath] [so_keepalive=on|off|[keepidle]:[keepintvl]:[keepcnt]];`  
`listen unix:path [default_server] [ssl] [http2 | quic] [proxy_protocol] [backlog=number] [rcvbuf=size] [sndbuf=size] [accept_filter=filter] [deferred] [bind] [so_keepalive=on|off|[keepidle]:[keepintvl]:[keepcnt]];`  
Default:

```
listen *:80 | *:8000;
```

Context: `server`

Sets the `address` and `port` for IP, or the `path` for a UNIX-domain socket on which the server will accept requests. Both `address` and `port`, or only `address` or only `port` can be specified. An `address` may also be a hostname, for example:

> ```
> listen 127.0.0.1:8000;
listen 127.0.0.1;
listen 8000;
listen *:8000;
listen localhost:8000;
> ```

IPv6 addresses (0.7.36) are specified in square brackets:

> ```
> listen [::]:8000;
listen [::1];
> ```

UNIX-domain sockets (0.8.21) are specified with the “`unix:`” prefix:

> ```
> listen unix:/var/run/nginx.sock;
> ```

If only `address` is given, the port 80 is used.

If the directive is not present then either `*:80` is used if nginx runs with the superuser privileges, or `*:8000` otherwise.

The `default_server` parameter, if present, will cause the server to become the default server for the specified `address`:`port` pair. If none of the directives have the `default_server` parameter then the first server with the `address`:`port` pair will be the default server for this pair.

> In versions prior to 0.8.21 this parameter is named simply `default`.

The `ssl` parameter (0.7.14) allows specifying that all connections accepted on this port should work in SSL mode. This allows for a more compact [configuration](https://nginx.org/en/docs/http/configuring_https_servers.html#single_http_https_server) for the server that handles both HTTP and HTTPS requests.

The `http2` parameter (1.9.5) configures the port to accept [HTTP/2](https://nginx.org/en/docs/http/ngx_http_v2_module.html) connections. Normally, for this to work the `ssl` parameter should be specified as well, but nginx can also be configured to accept HTTP/2 connections without SSL.

> The parameter is deprecated, the [http2](https://nginx.org/en/docs/http/ngx_http_v2_module.html#http2) directive should be used instead.

The `quic` parameter (1.25.0) configures the port to accept [QUIC](https://nginx.org/en/docs/http/ngx_http_v3_module.html) connections.

The `proxy_protocol` parameter (1.5.12) allows specifying that all connections accepted on this port should use the [PROXY protocol](http://www.haproxy.org/download/1.8/doc/proxy-protocol.txt).

> The PROXY protocol version 2 is supported since version 1.13.11.

The `listen` directive can have several additional parameters specific to socket-related system calls. These parameters can be specified in any `listen` directive, but only once for a given `address`:`port` pair.

> In versions prior to 0.8.21, they could only be specified in the `listen` directive together with the `default` parameter.

`setfib`=`number`

this parameter (0.8.44) sets the associated routing table, FIB (the `SO_SETFIB` option) for the listening socket. This currently works only on FreeBSD.

`fastopen`=`number`

enables “[TCP Fast Open](http://en.wikipedia.org/wiki/TCP_Fast_Open)” for the listening socket (1.5.8) and [limits](https://datatracker.ietf.org/doc/html/rfc7413#section-5.1) the maximum length for the queue of connections that have not yet completed the three-way handshake.

> Do not enable this feature unless the server can handle receiving the [same SYN packet with data](https://datatracker.ietf.org/doc/html/rfc7413#section-6.1) more than once.

`backlog`=`number`

sets the `backlog` parameter in the `listen()` call that limits the maximum length for the queue of pending connections. By default, `backlog` is set to -1 on FreeBSD, DragonFly BSD, and macOS, and to 511 on other platforms.

`rcvbuf`=`size`

sets the receive buffer size (the `SO_RCVBUF` option) for the listening socket.

`sndbuf`=`size`

sets the send buffer size (the `SO_SNDBUF` option) for the listening socket.

`accept_filter`=`filter`

sets the name of accept filter (the `SO_ACCEPTFILTER` option) for the listening socket that filters incoming connections before passing them to `accept()`. This works only on FreeBSD and NetBSD 5.0+. Possible values are [dataready](http://man.freebsd.org/accf_data) and [httpready](http://man.freebsd.org/accf_http).

`deferred`

instructs to use a deferred `accept()` (the `TCP_DEFER_ACCEPT` socket option) on Linux.

`bind`

instructs to make a separate `bind()` call for a given `address`:`port` pair. This is useful because if there are several `listen` directives with the same port but different addresses, and one of the `listen` directives listens on all addresses for the given port (`*:port`), nginx will `bind()` only to `*:port`. It should be noted that the `getsockname()` system call will be made in this case to determine the address that accepted the connection. If the `setfib`, `fastopen`, `backlog`, `rcvbuf`, `sndbuf`, `accept_filter`, `deferred`, `ipv6only`, `reuseport`, `multipath`, or `so_keepalive` parameters are used then for a given `address`:`port` pair a separate `bind()` call will always be made.

`ipv6only`=`on`|`off`

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
