---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#10-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-10-directives
type: reference
title: Module ngx_http_core_module › Directives (10/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#10-directives
source_hash: a8a9163acfba4b1a5301d3d718ca69f8ab32ef753c37cce569e8bdfd0e03af00
---
allow 192.168.1.0/32;
    deny  all;

auth_basic           "closed site";
    auth_basic_user_file conf/htpasswd;
}
> ```

Syntax: `send_lowat size;`  
Default:

```
send_lowat 0;
```

Context: `http`, `server`, `location`

If the directive is set to a non-zero value, nginx will try to minimize the number of send operations on client sockets by using either `NOTE_LOWAT` flag of the [kqueue](https://nginx.org/en/docs/events.html#kqueue) method or the `SO_SNDLOWAT` socket option. In both cases the specified `size` is used.

This directive is ignored on Linux, Solaris, and Windows.

Syntax: `send_timeout time;`  
Default:

```
send_timeout 60s;
```

Context: `http`, `server`, `location`

Sets a timeout for transmitting a response to the client. The timeout is set only between two successive write operations, not for the transmission of the whole response. If the client does not receive anything within this time, the connection is closed.

Syntax: `sendfile on | off;`  
Default:

```
sendfile off;
```

Context: `http`, `server`, `location`, `if in location`

Enables or disables the use of `sendfile()`.

Starting from nginx 0.8.12 and FreeBSD 5.2.1, [aio](#aio) can be used to pre-load data for `sendfile()`:

> ```
> location /video/ {
    sendfile       on;
    tcp_nopush     on;
    aio            on;
}
> ```

In this configuration, `sendfile()` is called with the `SF_NODISKIO` flag which causes it not to block on disk I/O, but, instead, report back that the data are not in memory. nginx then initiates an asynchronous data load by reading one byte. On the first read, the FreeBSD kernel loads the first 128K bytes of a file into memory, although next reads will only load data in 16K chunks. This can be changed using the [read\_ahead](#read_ahead) directive.

> Before version 1.7.11, pre-loading could be enabled with `aio sendfile;`.

Syntax: `sendfile_max_chunk size;`  
Default:

```
sendfile_max_chunk 2m;
```

Context: `http`, `server`, `location`

Limits the amount of data that can be transferred in a single `sendfile()` call. Without the limit, one fast connection may seize the worker process entirely.

> Prior to version 1.21.4, by default there was no limit.

Syntax: `server { ... }`  
Default: — Context: `http`

Sets configuration for a virtual server. There is no clear separation between IP-based (based on the IP address) and name-based (based on the “Host” request header field) virtual servers. Instead, the [listen](#listen) directives describe all addresses and ports that should accept connections for the server, and the [server\_name](#server_name) directive lists all server names. Example configurations are provided in the “[How nginx processes a request](https://nginx.org/en/docs/http/request_processing.html)” document.

Syntax: `server_name name ...;`  
Default:

```
server_name "";
```

Context: `server`

Sets names of a virtual server, for example:

> ```
> server {
    server_name example.com www.example.com;
}
> ```

The first name becomes the primary server name.

Server names can include an asterisk (“`*`”) replacing the first or last part of a name:

> ```
> server {
    server_name example.com *.example.com www.example.*;
}
> ```

Such names are called wildcard names.

The first two of the names mentioned above can be combined in one:

> ```
> server {
    server_name .example.com;
}
> ```

It is also possible to use regular expressions in server names, preceding the name with a tilde (“`~`”):

> ```
> server {
    server_name www.example.com ~^www\d+\.example\.com$;
}
> ```

Regular expressions can contain captures (0.7.40) that can later be used in other directives (see [Regular expression captures](https://nginx.org/en/docs/regex_captures.html)):

> ```
> server {
    server_name ~^(www\.)?(.+)$;

location / {
        root /sites/$2;
    }
}

server {
    server_name _;

location / {
        root /sites/default;
    }
}
> ```

Named captures in regular expressions create variables (0.8.25) that can later be used in other directives:

> ```
> server {
    server_name ~^(www\.)?(?<domain>.+)$;

location / {
        root /sites/$domain;
    }
}

server {
    server_name _;

location / {
        root /sites/default;
    }
}
> ```

If the directive’s parameter is set to “`$hostname`” (0.9.4), the machine’s hostname is inserted.

It is also possible to specify an empty server name (0.7.11):

> ```
> server {
    server_name www.example.com "";
}
> ```

It allows this server to process requests without the “Host” header field — instead of the default server — for the given address:port pair. This is the default setting.

> Before 0.8.48, the machine’s hostname was used by default.

The search is performed in the following order of priority and terminates on the first matching variant:

1. the exact name
2. the longest wildcard name starting with an asterisk, e.g. “`*.example.com`”
3. the longest wildcard name ending with an asterisk, e.g. “`mail.*`”
4. the first matching regular expression (in order of appearance in the configuration file)

Detailed description of server names is provided in a separate [Server names](https://nginx.org/en/docs/http/server_names.html) document.

Syntax: `server_name_in_redirect on | off;`  
Default:

```
server_name_in_redirect off;
```

Context: `http`, `server`, `location`

Enables or disables the use of the primary server name, specified by the [server\_name](#server_name) directive, in [absolute](#absolute_redirect) redirects issued by nginx. When the use of the primary server name is disabled, the name from the “Host” request header field is used. If this field is not present, the IP address of the server is used.

The use of a port in redirects is controlled by the [port\_in\_redirect](#port_in_redirect) directive.

Syntax: `server_names_hash_bucket_size size;`  
Default:

```
server_names_hash_bucket_size 32|64|128;
```

Context: `http`

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
