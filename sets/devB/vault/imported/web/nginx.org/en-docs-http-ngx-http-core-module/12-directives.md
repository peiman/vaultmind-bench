---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#12-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-12-directives
type: reference
title: Module ngx_http_core_module › Directives (12/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#12-directives
source_hash: 26b83009196b1cda0f1c7259b742e83fc453366db543f485082cbcbe4c5ea959
---
To make a particular location emit the “`application/octet-stream`” MIME type for all requests, the following configuration can be used:

> ```
> location /download/ {
    types        { }
    default_type application/octet-stream;
}
> ```

Syntax: `types_hash_bucket_size size;`  
Default:

```
types_hash_bucket_size 64;
```

Context: `http`, `server`, `location`

Sets the bucket size for the types hash tables. The details of setting up hash tables are provided in a separate [document](https://nginx.org/en/docs/hash.html).

> Prior to version 1.5.13, the default value depended on the size of the processor’s cache line.

Syntax: `types_hash_max_size size;`  
Default:

```
types_hash_max_size 1024;
```

Context: `http`, `server`, `location`

Sets the maximum `size` of the types hash tables. The details of setting up hash tables are provided in a separate [document](https://nginx.org/en/docs/hash.html).

Syntax: `underscores_in_headers on | off;`  
Default:

```
underscores_in_headers off;
```

Context: `http`, `server`

Enables or disables the use of underscores in client request header fields. When the use of underscores is disabled, request header fields whose names contain underscores are marked as invalid and become subject to the [ignore\_invalid\_headers](#ignore_invalid_headers) directive.

If the directive is specified on the [server](#server) level, the value from the default server can be used. Details are provided in the “[Virtual server selection](https://nginx.org/en/docs/http/server_names.html#virtual_server_selection)” section.

Syntax: `variables_hash_bucket_size size;`  
Default:

```
variables_hash_bucket_size 64;
```

Context: `http`

Sets the bucket size for the variables hash table. The details of setting up hash tables are provided in a separate [document](https://nginx.org/en/docs/hash.html).

Syntax: `variables_hash_max_size size;`  
Default:

```
variables_hash_max_size 1024;
```

Context: `http`

Sets the maximum `size` of the variables hash table. The details of setting up hash tables are provided in a separate [document](https://nginx.org/en/docs/hash.html).

> Prior to version 1.5.13, the default value was 512.

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
