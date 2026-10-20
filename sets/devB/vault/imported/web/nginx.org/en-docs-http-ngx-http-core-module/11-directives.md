---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#11-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-11-directives
type: reference
title: Module ngx_http_core_module › Directives (11/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#11-directives
source_hash: 2ee6705e01873fa873659067665890093b4764274ae1a2a494ba6ebdbab4adab
---
Sets the bucket size for the server names hash tables. The default value depends on the size of the processor’s cache line. The details of setting up hash tables are provided in a separate [document](https://nginx.org/en/docs/hash.html).

Syntax: `server_names_hash_max_size size;`  
Default:

```
server_names_hash_max_size 512;
```

Context: `http`

Sets the maximum `size` of the server names hash tables. The details of setting up hash tables are provided in a separate [document](https://nginx.org/en/docs/hash.html).

Syntax: `server_tokens on | off | build | string;`  
Default:

```
server_tokens on;
```

Context: `http`, `server`, `location`

Enables or disables emitting nginx version on error pages and in the “Server” response header field.

The `build` parameter (1.11.10) enables emitting a [build name](https://nginx.org/en/docs/configure.html#build) along with nginx version.

Additionally, as part of our [commercial subscription](https://www.f5.com/products/nginx), starting from version 1.9.13 the signature on error pages and the “Server” response header field value can be set explicitly using the `string` with variables. An empty string disables the emission of the “Server” field.

Syntax: `subrequest_output_buffer_size size;`  
Default:

```
subrequest_output_buffer_size 4k|8k;
```

Context: `http`, `server`, `location`

This directive appeared in version 1.13.10.

Sets the `size` of the buffer used for storing the response body of a subrequest. By default, the buffer size is equal to one memory page. This is either 4K or 8K, depending on a platform. It can be made smaller, however.

The directive is applicable only for subrequests with response bodies saved into memory. For example, such subrequests are created by [SSI](https://nginx.org/en/docs/http/ngx_http_ssi_module.html#ssi_include_set).

Syntax: `tcp_nodelay on | off;`  
Default:

```
tcp_nodelay on;
```

Context: `http`, `server`, `location`

Enables or disables the use of the `TCP_NODELAY` option. The option is enabled when a connection is transitioned into the keep-alive state. Additionally, it is enabled on SSL connections, for unbuffered proxying, and for [WebSocket](https://nginx.org/en/docs/http/websocket.html) proxying.

Syntax: `tcp_nopush on | off;`  
Default:

```
tcp_nopush off;
```

Context: `http`, `server`, `location`

Enables or disables the use of the `TCP_NOPUSH` socket option on FreeBSD or the `TCP_CORK` socket option on Linux. The options are enabled only when [sendfile](#sendfile) is used. Enabling the option allows

- sending the response header and the beginning of a file in one packet, on Linux and FreeBSD 4.\*;
- sending a file in full packets.

Syntax: `try_files file ... uri;`  
`try_files file ... =code;`  
Default: — Context: `server`, `location`

Checks the existence of files in the specified order and uses the first found file for request processing; the processing is performed in the current context. The path to a file is constructed from the `file` parameter according to the [root](#root) and [alias](#alias) directives. It is possible to check directory’s existence by specifying a slash at the end of a name, e.g. “`$uri/`”. If none of the files were found, an internal redirect to the `uri` specified in the last parameter is made. For example:

> ```
> location /images/ {
    try_files $uri /images/default.gif;
}

location = /images/default.gif {
    expires 30s;
}
> ```

The last parameter can also point to a named location, as shown in examples below. Starting from version 0.7.51, the last parameter can also be a `code`:

> ```
> location / {
    try_files $uri $uri/index.html $uri.html =404;
}
> ```

Example in proxying Mongrel:

> ```
> location / {
    try_files /system/maintenance.html
              $uri $uri/index.html $uri.html
              @mongrel;
}

location @mongrel {
    proxy_pass http://mongrel;
}
> ```

Example for Drupal/FastCGI:

> ```
> location / {
    try_files $uri $uri/ @drupal;
}

location ~ \.php$ {
    try_files $uri @drupal;

fastcgi_pass ...;

fastcgi_param SCRIPT_FILENAME /path/to$fastcgi_script_name;
    fastcgi_param SCRIPT_NAME     $fastcgi_script_name;
    fastcgi_param QUERY_STRING    $args;

... other fastcgi_param's
}

location @drupal {
    fastcgi_pass ...;

fastcgi_param SCRIPT_FILENAME /path/to/index.php;
    fastcgi_param SCRIPT_NAME     /index.php;
    fastcgi_param QUERY_STRING    q=$uri&$args;

... other fastcgi_param's
}
> ```

In the following example,

> ```
> location / {
    try_files $uri $uri/ @drupal;
}
> ```

the `try_files` directive is equivalent to

> ```
> location / {
    error_page 404 = @drupal;
    log_not_found off;
}
> ```

And here,

> ```
> location ~ \.php$ {
    try_files $uri @drupal;

fastcgi_pass ...;

fastcgi_param SCRIPT_FILENAME /path/to$fastcgi_script_name;

...
}
> ```

`try_files` checks the existence of the PHP file before passing the request to the FastCGI server.

Example for Wordpress and Joomla:

> ```
> location / {
    try_files $uri $uri/ @wordpress;
}

location ~ \.php$ {
    try_files $uri @wordpress;

fastcgi_pass ...;

fastcgi_param SCRIPT_FILENAME /path/to$fastcgi_script_name;
    ... other fastcgi_param's
}

location @wordpress {
    fastcgi_pass ...;

fastcgi_param SCRIPT_FILENAME /path/to/index.php;
    ... other fastcgi_param's
}
> ```

Syntax: `types { ... }`  
Default:

```
types {
    text/html  html;
    image/gif  gif;
    image/jpeg jpg;
}
```

Context: `http`, `server`, `location`

Maps file name extensions to MIME types of responses. Extensions are case-insensitive. Several extensions can be mapped to one type, for example:

> ```
> types {
    application/octet-stream bin exe dll;
    application/octet-stream deb;
    application/octet-stream dmg;
}
> ```

A sufficiently full mapping table is distributed with nginx in the `conf/mime.types` file.

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
