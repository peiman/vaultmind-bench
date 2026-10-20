---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#07-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-07-directives
type: reference
title: Module ngx_http_core_module › Directives (7/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#07-directives
source_hash: b735c517de2bc284760e8d9f236daabbc7bdf6799c9dca1525abd91e3d45af58
---
this parameter (0.7.42) determines (via the `IPV6_V6ONLY` socket option) whether an IPv6 socket listening on a wildcard address `[::]` will accept only IPv6 connections or both IPv6 and IPv4 connections. This parameter is turned on by default. It can only be set once on start.

> Prior to version 1.3.4, if this parameter was omitted then the operating system’s settings were in effect for the socket.

`reuseport`

this parameter (1.9.1) instructs to create an individual listening socket for each worker process (using the `SO_REUSEPORT` socket option on Linux 3.9+ and DragonFly BSD, or `SO_REUSEPORT_LB` on FreeBSD 12+), allowing a kernel to distribute incoming connections between worker processes. This currently works only on Linux 3.9+, DragonFly BSD, and FreeBSD 12+ (1.15.1).

> Inappropriate use of this option may have its security [implications](http://man7.org/linux/man-pages/man7/socket.7.html).

`multipath`

this parameter (1.29.7) configures the [Multipath TCP](https://datatracker.ietf.org/doc/html/rfc8684) protocol (`IPPROTO_MPTCP`) for the listening socket. This currently works only on Linux 5.6+.

> Adding or removing this parameter will also enable the `SO_REUSEPORT` socket option, which may have its security [implications](http://man7.org/linux/man-pages/man7/socket.7.html).

`so_keepalive`=`on`|`off`|\[`keepidle`]:\[`keepintvl`]:\[`keepcnt`]

this parameter (1.1.11) configures the “TCP keepalive” behavior for the listening socket. If this parameter is omitted then the operating system’s settings will be in effect for the socket. If it is set to the value “`on`”, the `SO_KEEPALIVE` option is turned on for the socket. If it is set to the value “`off`”, the `SO_KEEPALIVE` option is turned off for the socket. Some operating systems support setting of TCP keepalive parameters on a per-socket basis using the `TCP_KEEPIDLE`, `TCP_KEEPINTVL`, and `TCP_KEEPCNT` socket options. On such systems (currently, Linux, NetBSD, Dragonfly, FreeBSD, and macOS), they can be configured using the `keepidle`, `keepintvl`, and `keepcnt` parameters. One or two parameters may be omitted, in which case the system default setting for the corresponding socket option will be in effect. For example,

> ```
> so_keepalive=30m::10
> ```

will set the idle timeout (`TCP_KEEPIDLE`) to 30 minutes, leave the probe interval (`TCP_KEEPINTVL`) at its system default, and set the probes count (`TCP_KEEPCNT`) to 10 probes.

Example:

> ```
> listen 127.0.0.1 default_server accept_filter=dataready backlog=1024;
> ```

Syntax: `location [ = | ~ | ~* | ^~ ] uri { ... }`  
`location $variable { ... }`  
`location @name { ... }`  
Default: — Context: `server`, `location`

Sets configuration depending on a request URI or the value of a variable (1.31.5).

The matching is performed against a normalized URI, after decoding the text encoded in the “`%XX`” form, resolving references to relative path components “`.`” and “`..`”, and possible [compression](#merge_slashes) of two or more adjacent slashes into a single slash.

A location can be defined by a prefix string, a regular expression, or a predicate (1.31.5). Regular expressions are specified with the preceding “`~*`” modifier (for case-insensitive matching), or the “`~`” modifier (for case-sensitive matching). A predicate is specified with the preceding “`$`” and contains a variable evaluated during request processing. A predicate location matches if the variable value is not empty and is not equal to “0”.

To find location matching a given request, nginx first checks locations defined using the prefix strings (prefix locations). Among them, the location with the longest matching prefix is selected and remembered. Then regular expressions are checked, in the order of their appearance in the configuration file. The search of regular expressions terminates on the first match, and the corresponding configuration is used. If no match with a regular expression is found, predicate locations are checked in the order of their appearance in the configuration file. If no predicate location matches, the configuration of the prefix location remembered earlier is used.

`location` blocks can be nested, with some exceptions mentioned below.

For case-insensitive operating systems such as macOS and Cygwin, matching with prefix strings ignores a case (0.7.7). However, comparison is limited to one-byte locales.

Regular expressions can contain captures (0.7.40) that can later be used in other directives, see [Regular expression captures](https://nginx.org/en/docs/regex_captures.html).

If the longest matching prefix location has the “`^~`” modifier, then regular expressions and predicate locations are not checked.

Also, using the “`=`” modifier it is possible to define an exact match of URI and location. If an exact match is found, the search terminates. For example, if a “`/`” request happens frequently, defining “`location = /`” will speed up the processing of these requests, as search terminates right after the first comparison. Such a location cannot obviously contain nested locations.

> In versions from 0.7.1 to 0.8.41, if a request matched the prefix location without the “`=`” and “`^~`” modifiers, the search also terminated and regular expressions were not checked.

Let’s illustrate the above by an example:

> ```
> location = / {
    [ configuration A ]
}

location / {
    [ configuration B ]
}

location /documents/ {
    [ configuration C ]
}

location ^~ /images/ {
    [ configuration D ]
}

location ~* \.(gif|jpg|jpeg)$ {
    [ configuration E ]
}

location $arg_pred {
    [ configuration F ]
}
> ```

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
