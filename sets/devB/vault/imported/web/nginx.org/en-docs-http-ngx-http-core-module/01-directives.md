---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#01-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-01-directives
type: reference
title: Module ngx_http_core_module › Directives (1/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#01-directives
source_hash: d037ebeea576cf2bd0ce4fa1924fa5148d926d523db08876ddfaa194b297d637
---
Syntax: `absolute_redirect on | off;`  
Default:

```
absolute_redirect on;
```

Context: `http`, `server`, `location`

This directive appeared in version 1.11.8.

If disabled, redirects issued by nginx will be relative.

See also [server\_name\_in\_redirect](#server_name_in_redirect) and [port\_in\_redirect](#port_in_redirect) directives.

Syntax: `aio on | off | threads[=pool];`  
Default:

```
aio off;
```

Context: `http`, `server`, `location`

This directive appeared in version 0.8.11.

Enables or disables the use of asynchronous file I/O (AIO) on FreeBSD and Linux:

> ```
> location /video/ {
    aio            on;
    output_buffers 1 64k;
}
> ```

On FreeBSD, AIO can be used starting from FreeBSD 4.3. Prior to FreeBSD 11.0, AIO can either be linked statically into a kernel:

> ```
> options VFS_AIO
> ```

or loaded dynamically as a kernel loadable module:

> ```
> kldload aio
> ```

On Linux, AIO can be used starting from kernel version 2.6.22. Also, it is necessary to enable [directio](#directio), or otherwise reading will be blocking:

> ```
> location /video/ {
    aio            on;
    directio       512;
    output_buffers 1 128k;
}
> ```

On Linux, [directio](#directio) can only be used for reading blocks that are aligned on 512-byte boundaries (or 4K for XFS). File’s unaligned end is read in blocking mode. The same holds true for byte range requests and for FLV requests not from the beginning of a file: reading of unaligned data at the beginning and end of a file will be blocking.

When both AIO and [sendfile](#sendfile) are enabled on Linux, AIO is used for files that are larger than or equal to the size specified in the [directio](#directio) directive, while [sendfile](#sendfile) is used for files of smaller sizes or when [directio](#directio) is disabled.

> ```
> location /video/ {
    sendfile       on;
    aio            on;
    directio       8m;
}
> ```

Finally, files can be read and [sent](#sendfile) using multi-threading (1.7.11), without blocking a worker process:

> ```
> location /video/ {
    sendfile       on;
    aio            threads;
}
> ```

Read and send file operations are offloaded to threads of the specified [pool](https://nginx.org/en/docs/ngx_core_module.html#thread_pool). If the pool name is omitted, the pool with the name “`default`” is used. The pool name can also be set with variables:

> ```
> aio threads=pool$disk;
> ```

By default, multi-threading is disabled, it should be enabled with the `--with-threads` configuration parameter. Currently, multi-threading is compatible only with the [epoll](https://nginx.org/en/docs/events.html#epoll), [kqueue](https://nginx.org/en/docs/events.html#kqueue), and [eventport](https://nginx.org/en/docs/events.html#eventport) methods. Multi-threaded sending of files is only supported on Linux.

See also the [sendfile](#sendfile) directive.

Syntax: `aio_write on | off;`  
Default:

```
aio_write off;
```

Context: `http`, `server`, `location`

This directive appeared in version 1.9.13.

If [aio](#aio) is enabled, specifies whether it is used for writing files. Currently, this only works when using `aio threads` and is limited to writing temporary files with data received from proxied servers.

Syntax: `alias path;`  
Default: — Context: `location`

Defines a replacement for the specified location. For example, with the following configuration

> ```
> location /i/ {
    alias /data/w3/images/;
}
> ```

on request of “`/i/top.gif`”, the file `/data/w3/images/top.gif` will be sent.

The `path` value can contain variables, except `$document_root` and `$realpath_root`.

If `alias` is used inside a location defined with a regular expression then its value specifies a complete file path (0.7.40). Such path should typically refer to the captures contained within the regular expression:

> ```
> location ~ ^/users/(.+\.(?:gif|jpe?g|png))$ {
    alias /data/w3/images/$1;
}
> ```

If `alias` is used inside a predicate location then its value specifies a complete file path.

When location matches the last part of the directive’s value:

> ```
> location /images/ {
    alias /data/w3/images/;
}
> ```

it is better to use the [root](#root) directive instead:

> ```
> location /images/ {
    root /data/w3;
}
> ```

Syntax: `auth_delay time;`  
Default:

```
auth_delay 0s;
```

Context: `http`, `server`, `location`

This directive appeared in version 1.17.10.

Delays processing of unauthorized requests with 401 response code to prevent timing attacks when access is limited by [password](https://nginx.org/en/docs/http/ngx_http_auth_basic_module.html), by the [result of subrequest](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html), or by [JWT](https://nginx.org/en/docs/http/ngx_http_auth_jwt_module.html).

Syntax: `chunked_transfer_encoding on | off;`  
Default:

```
chunked_transfer_encoding on;
```

Context: `http`, `server`, `location`

Allows disabling chunked transfer encoding in HTTP/1.1. It may come in handy when using a software failing to support chunked encoding despite the standard’s requirement.

Syntax: `client_body_buffer_size size;`  
Default:

```
client_body_buffer_size 8k|16k;
```

Context: `http`, `server`, `location`

Sets buffer size for reading client request body. In case the request body is larger than the buffer, the whole body or only its part is written to a [temporary file](#client_body_temp_path). By default, buffer size is equal to two memory pages. This is 8K on x86, other 32-bit platforms, and x86-64. It is usually 16K on other 64-bit platforms.

Syntax: `client_body_early_read string ...;`  
Default: — Context: `http`, `server`

This directive appeared in version 1.31.5.

Enables reading of the client request body immediately after the request headers are received, using the request body read settings from the `server` block. If at least one value of the string parameters is not empty and is not equal to “0”, then nginx reads the request body early.

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
