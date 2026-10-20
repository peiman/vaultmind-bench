---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#02-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-02-directives
type: reference
title: Module ngx_http_core_module › Directives (2/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#02-directives
source_hash: 4d1a4e96110f5dd37f0903b82caa2bf31e2021d98849ad45e499a1e6aeb67974
---
The directive is incompatible with modules that use unbuffered request body processing, such as the [ngx\_http\_grpc\_module](https://nginx.org/en/docs/http/ngx_http_grpc_module.html) module. The directive is also incompatible with modules which write the request body to a file, such as [ngx\_http\_dav\_module](https://nginx.org/en/docs/http/ngx_http_dav_module.html) module.

The [client\_body\_in\_file\_only](#client_body_in_file_only) directive is ignored when the request body is read early.

Example:

> ```
> map $http_content_type $is_json {
    application/json  1;
}

server {
    listen 8000;

client_body_early_read $is_json;

client_max_body_size    256;
    client_body_buffer_size 256;

return 200 $request_body;
}
> ```

Syntax: `client_body_in_file_only on | clean | off;`  
Default:

```
client_body_in_file_only off;
```

Context: `http`, `server`, `location`

Determines whether nginx should save the entire client request body into a file. This directive can be used during debugging, or when using the `$request_body_file` variable, or the [$r-&gt;request\_body\_file](https://nginx.org/en/docs/http/ngx_http_perl_module.html#methods) method of the module [ngx\_http\_perl\_module](https://nginx.org/en/docs/http/ngx_http_perl_module.html).

When set to the value `on`, temporary files are not removed after request processing.

The value `clean` will cause the temporary files left after request processing to be removed.

Syntax: `client_body_in_single_buffer on | off;`  
Default:

```
client_body_in_single_buffer off;
```

Context: `http`, `server`, `location`

Determines whether nginx should save the entire client request body in a single buffer. The directive is recommended when using the `$request_body` variable, to save the number of copy operations involved.

Syntax: `client_body_temp_path path [level1 [level2 [level3]]];`  
Default:

```
client_body_temp_path client_body_temp;
```

Context: `http`, `server`, `location`

Defines a directory for storing temporary files holding client request bodies. Up to three-level subdirectory hierarchy can be used under the specified directory. For example, in the following configuration

> ```
> client_body_temp_path /spool/nginx/client_temp 1 2;
> ```

a path to a temporary file might look like this:

> ```
> /spool/nginx/client_temp/7/45/00000123457
> ```

Syntax: `client_body_timeout time;`  
Default:

```
client_body_timeout 60s;
```

Context: `http`, `server`, `location`

Defines a timeout for reading client request body. The timeout is set only for a period between two successive read operations, not for the transmission of the whole request body. If a client does not transmit anything within this time, the request is terminated with the 408 (Request Time-out) error.

Syntax: `client_header_buffer_size size;`  
Default:

```
client_header_buffer_size 1k;
```

Context: `http`, `server`

Sets buffer size for reading client request header. For most requests, a buffer of 1K bytes is enough. However, if a request includes long cookies, or comes from a WAP client, it may not fit into 1K. If a request line or a request header field does not fit into this buffer then larger buffers, configured by the [large\_client\_header\_buffers](#large_client_header_buffers) directive, are allocated.

If the directive is specified on the [server](#server) level, the value from the default server can be used. Details are provided in the “[Virtual server selection](https://nginx.org/en/docs/http/server_names.html#virtual_server_selection)” section.

Syntax: `client_header_timeout time;`  
Default:

```
client_header_timeout 60s;
```

Context: `http`, `server`

Defines a timeout for reading client request header. If a client does not transmit the entire header within this time, the request is terminated with the 408 (Request Time-out) error.

Syntax: `client_max_body_size size;`  
Default:

```
client_max_body_size 1m;
```

Context: `http`, `server`, `location`

Sets the maximum allowed size of the client request body. If the size in a request exceeds the configured value, the 413 (Request Entity Too Large) error is returned to the client. Please be aware that browsers cannot correctly display this error. Setting `size` to 0 disables checking of client request body size.

Syntax: `connection_pool_size size;`  
Default:

```
connection_pool_size 256|512;
```

Context: `http`, `server`

Allows accurate tuning of per-connection memory allocations. This directive has minimal impact on performance and should not generally be used. By default, the size is equal to 256 bytes on 32-bit platforms and 512 bytes on 64-bit platforms.

> Prior to version 1.9.8, the default value was 256 on all platforms.

Syntax: `default_type mime-type;`  
Default:

```
default_type text/plain;
```

Context: `http`, `server`, `location`

Defines the default MIME type of a response. Mapping of file name extensions to MIME types can be set with the [types](#types) directive.

Syntax: `directio size | off;`  
Default:

```
directio off;
```

Context: `http`, `server`, `location`

This directive appeared in version 0.7.7.

Enables the use of the `O_DIRECT` flag (FreeBSD, Linux), the `F_NOCACHE` flag (macOS), or the `directio()` function (Solaris), when reading files that are larger than or equal to the specified `size`. The directive automatically disables (0.7.15) the use of [sendfile](#sendfile) for a given request. It can be useful for serving large files:

> ```
> directio 4m;
> ```

or when using [aio](#aio) on Linux.

Syntax: `directio_alignment size;`  
Default:

```
directio_alignment 512;
```

Context: `http`, `server`, `location`

This directive appeared in version 0.8.11.

Sets the alignment for [directio](#directio). In most cases, a 512-byte alignment is enough. However, when using XFS under Linux, it needs to be increased to 4K.

Syntax: `disable_symlinks off;`  
`disable_symlinks on | if_not_owner [from=part];`  
Default:

```
disable_symlinks off;
```

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
