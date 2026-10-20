---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#03-directives.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-03-directives
type: reference
title: Module ngx_http_core_module › Directives (3/12)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#03-directives
source_hash: ade69587c246fbd24f7cf48747be59da05ee2ff3b5a6df152aacfdf12f86b6a4
---
Context: `http`, `server`, `location`

This directive appeared in version 1.1.15.

Determines how symbolic links should be treated when opening files:

`off`

Symbolic links in the pathname are allowed and not checked. This is the default behavior.

`on`

If any component of the pathname is a symbolic link, access to a file is denied.

`if_not_owner`

Access to a file is denied if any component of the pathname is a symbolic link, and the link and object that the link points to have different owners.

`from`=`part`

When checking symbolic links (parameters `on` and `if_not_owner`), all components of the pathname are normally checked. Checking of symbolic links in the initial part of the pathname may be avoided by specifying additionally the `from`=`part` parameter. In this case, symbolic links are checked only from the pathname component that follows the specified initial part. If the value is not an initial part of the pathname checked, the whole pathname is checked as if this parameter was not specified at all. If the value matches the whole file name, symbolic links are not checked. The parameter value can contain variables.

Example:

> ```
> disable_symlinks on from=$document_root;
> ```

This directive is only available on systems that have the `openat()` and `fstatat()` interfaces. Such systems include modern versions of FreeBSD, Linux, and Solaris.

Parameters `on` and `if_not_owner` add a processing overhead.

> On systems that do not support opening of directories only for search, to use these parameters it is required that worker processes have read permissions for all directories being checked.

> The [ngx\_http\_autoindex\_module](https://nginx.org/en/docs/http/ngx_http_autoindex_module.html), [ngx\_http\_random\_index\_module](https://nginx.org/en/docs/http/ngx_http_random_index_module.html), and [ngx\_http\_dav\_module](https://nginx.org/en/docs/http/ngx_http_dav_module.html) modules currently ignore this directive.

Syntax: `early_hints string ...;`  
Default: — Context: `http`, `server`, `location`

This directive appeared in version 1.29.0.

Defines conditions under which the 103 (Early Hints) response will be passed to a client. If at least one value of the string parameters is not empty and is not equal to “0” then the response will be passed:

> ```
> map $http_sec_fetch_mode $early_hints {
    navigate $http2$http3;
}

server {
    ...
    location / {
        early_hints $early_hints;
        proxy_pass http://example.com;
    }
}
> ```

> 103 (Early Hints) responses received from an upstream server are passed to a client as is, without interpretation.

Syntax: `error_log_tag name value;`  
Default: — Context: `http`, `server`, `location`

This directive appeared in version 1.29.8.

Defines an additional context tag for HTTP [error log](https://nginx.org/en/docs/ngx_core_module.html#error_log) messages in text or [JSON](https://nginx.org/en/docs/ngx_core_module.html#error_log_json) format, in addition to default tags. The `value` can contain text, variables, and their combination:

> ```
> error_log_tag  request_id  $request_id;
> ```

Several `error_log_tag` directives can be specified on the same level. These directives are inherited from the previous configuration level if and only if there are no `error_log_tag` directives defined on the current level.

> This directive is available as part of our [commercial subscription](https://www.f5.com/products/nginx).

Syntax: `error_page code ... [=[response]] uri;`  
Default: — Context: `http`, `server`, `location`, `if in location`

Defines the URI that will be shown for the specified errors. A `uri` value can contain variables.

Example:

> ```
> error_page 404             /404.html;
error_page 500 502 503 504 /50x.html;
> ```

This causes an internal redirect to the specified `uri` with the client request method changed to “`GET`” (for all methods other than “`GET`” and “`HEAD`”).

Furthermore, it is possible to change the response code to another using the “`=response`” syntax, for example:

> ```
> error_page 404 =200 /empty.gif;
> ```

If an error response is processed by a proxied server or a FastCGI/uwsgi/SCGI/gRPC server, and the server may return different response codes (e.g., 200, 302, 401 or 404), it is possible to respond with the code it returns:

> ```
> error_page 404 = /404.php;
> ```

If there is no need to change URI and method during internal redirection it is possible to pass error processing into a named location:

> ```
> location / {
    error_page 404 = @fallback;
}

location @fallback {
    proxy_pass http://backend;
}
> ```

> If `uri` processing leads to an error, the status code of the last occurred error is returned to the client.

It is also possible to use URL redirects for error processing:

> ```
> error_page 403      http://example.com/forbidden.html;
error_page 404 =301 http://example.com/notfound.html;
> ```

In this case, by default, the response code 302 is returned to the client. It can only be changed to one of the redirect status codes (301, 302, 303, 307, and 308).

> The code 307 was not treated as a redirect until versions 1.1.16 and 1.0.13.

> The code 308 was not treated as a redirect until version 1.13.0.

These directives are inherited from the previous configuration level if and only if there are no `error_page` directives defined on the current level.

Syntax: `etag on | off;`  
Default:

```
etag on;
```

Context: `http`, `server`, `location`

This directive appeared in version 1.3.3.

Enables or disables automatic generation of the “ETag” response header field for static resources.

Syntax: `http { ... }`  
Default: — Context: `main`

Provides the configuration file context in which the HTTP server directives are specified.

Syntax: `if_modified_since off | exact | before;`  
Default:

```
if_modified_since exact;
```

Context: `http`, `server`, `location`

This directive appeared in version 0.7.24.

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
