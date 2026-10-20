---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#14-embedded-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-14-embedded-variables
type: reference
title: Module ngx_http_core_module › Embedded Variables (2/2)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#14-embedded-variables
source_hash: 9327ff4712ee3557355bbe88b77e630538120f56d9ea03c54afed2bc7ac720c9
---
At the end of processing, the file needs to be removed. To always write the request body to a file, [client\_body\_in\_file\_only](#client_body_in_file_only) needs to be enabled. When the name of a temporary file is passed in a proxied request or in a request to a FastCGI/uwsgi/SCGI server, passing the request body should be disabled by the [proxy\_pass\_request\_body off](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass_request_body), [fastcgi\_pass\_request\_body off](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html#fastcgi_pass_request_body), [uwsgi\_pass\_request\_body off](https://nginx.org/en/docs/http/ngx_http_uwsgi_module.html#uwsgi_pass_request_body), or [scgi\_pass\_request\_body off](https://nginx.org/en/docs/http/ngx_http_scgi_module.html#scgi_pass_request_body) directives, respectively.

`$request_completion`

“`OK`” if a request has completed, or an empty string otherwise

`$request_filename`

file path for the current request, based on the [root](#root) or [alias](#alias) directives, and the request URI

`$request_id`

unique request identifier generated from 16 random bytes, in hexadecimal (1.11.0)

`$request_length`

request length (including request line, header, and request body) (1.3.12, 1.2.7)

`$request_method`

request method, usually “`GET`” or “`POST`”

`$request_port`

in this order of precedence: port number from the [URI](https://datatracker.ietf.org/doc/html/rfc9110#section-4.2.1) authority component, or port number from the “Host” request header field (1.29.3)

`$request_time`

request processing time in seconds with a milliseconds resolution (1.3.9, 1.2.6); time elapsed since the first bytes were read from the client

`$request_uri`

full original request URI (with arguments)

`$scheme`

request scheme, “`http`” or “`https`”

`$sent_http_name`

arbitrary response header field; the last part of a variable name is the field name converted to lower case with dashes replaced by underscores

`$sent_trailer_name`

arbitrary field sent at the end of the response (1.13.2); the last part of a variable name is the field name converted to lower case with dashes replaced by underscores

`$server_addr`

an address of the server which accepted a request

Computing a value of this variable usually requires one system call. To avoid a system call, the [listen](#listen) directives must specify addresses and use the `bind` parameter.

`$server_name`

name of the server which accepted a request

`$server_port`

port of the server which accepted a request

`$server_protocol`

request protocol, usually “`HTTP/1.0`”, “`HTTP/1.1`”, “[HTTP/2.0](https://nginx.org/en/docs/http/ngx_http_v2_module.html)”, or “[HTTP/3.0](https://nginx.org/en/docs/http/ngx_http_v3_module.html)”

`$status`

response status (1.3.2, 1.2.2)

`$tcpinfo_rtt`, `$tcpinfo_rttvar`, `$tcpinfo_snd_cwnd`, `$tcpinfo_rcv_space`

information about the client TCP connection; available on systems that support the `TCP_INFO` socket option

`$time_iso8601`

local time in the ISO 8601 standard format (1.3.12, 1.2.7)

`$time_iso8601_ms`

local time in the ISO 8601 standard format with a millisecond resolution (1.29.8)

> This variable is available as part of our [commercial subscription](https://www.f5.com/products/nginx).

`$time_local`

local time in the Common Log Format (1.3.12, 1.2.7)

`$uri`

current URI in request, [normalized](#location)

The value of `$uri` may change during request processing, e.g. when doing internal redirects, or when using index files.

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
