---
# Imported by `vaultmind import` from https://nginx.org/en/docs/http/ngx_http_core_module.html#13-embedded-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-nginx-org-en-docs-http-ngx-http-core-module-13-embedded-variables
type: reference
title: Module ngx_http_core_module › Embedded Variables (1/2)
url: https://nginx.org/en/docs/http/ngx_http_core_module.html
source: https://nginx.org/en/docs/http/ngx_http_core_module.html#13-embedded-variables
source_hash: 8751791595ff3d99be2b1ee44190c043a217c860eac95b7614a240d9ce6f7571
---
The `ngx_http_core_module` module supports embedded variables with names matching the Apache Server variables. First of all, these are variables representing client request header fields, such as `$http_user_agent`, `$http_cookie`, and so on. Also there are other variables:

`$arg_name`

argument `name` in the request line

`$args`

arguments in the request line

`$binary_remote_addr`

client address in a binary form, value’s length is always 4 bytes for IPv4 addresses or 16 bytes for IPv6 addresses

`$body_bytes_sent`

number of bytes sent to a client, not counting the response header; this variable is compatible with the “`%B`” parameter of the `mod_log_config` Apache module

`$bytes_sent`

number of bytes sent to a client (1.3.8, 1.2.5)

`$connection`

connection serial number (1.3.8, 1.2.5)

`$connection_requests`

current number of requests made through a connection (1.3.8, 1.2.5)

`$connection_time`

connection time in seconds with a milliseconds resolution (1.19.10)

`$content_length`

“Content-Length” request header field

`$content_type`

“Content-Type” request header field

`$cookie_name`

the `name` cookie

`$document_root`

[root](#root) or [alias](#alias) directive’s value for the current request

`$document_uri`

same as `$uri`

`$host`

in this order of precedence: host name from the request line, or host name from the “Host” request header field, or the server name matching a request

`$hostname`

host name

`$http_name`

arbitrary request header field; the last part of a variable name is the field name converted to lower case with dashes replaced by underscores

`$https`

“`on`” if connection operates in SSL mode, or an empty string otherwise

`$is_args`

“`?`” if a request line has arguments, or an empty string otherwise

`$is_request_port`

“`:`” if [$request\_port](#var_request_port) is non-empty, or an empty string otherwise (1.29.3)

`$limit_rate`

setting this variable enables response rate limiting; see [limit\_rate](#limit_rate)

`$msec`

current time in seconds with the milliseconds resolution (1.3.9, 1.2.6)

`$nginx_version`

nginx version

`$pid`

PID of the worker process

`$pipe`

“`p`” if request was pipelined, “`.`” otherwise (1.3.12, 1.2.7)

`$proxy_protocol_addr`

client address from the PROXY protocol header (1.5.12)

The PROXY protocol must be previously enabled by setting the `proxy_protocol` parameter in the [listen](#listen) directive.

`$proxy_protocol_port`

client port from the PROXY protocol header (1.11.0)

The PROXY protocol must be previously enabled by setting the `proxy_protocol` parameter in the [listen](#listen) directive.

`$proxy_protocol_server_addr`

server address from the PROXY protocol header (1.17.6)

The PROXY protocol must be previously enabled by setting the `proxy_protocol` parameter in the [listen](#listen) directive.

`$proxy_protocol_server_port`

server port from the PROXY protocol header (1.17.6)

The PROXY protocol must be previously enabled by setting the `proxy_protocol` parameter in the [listen](#listen) directive.

`$proxy_protocol_tlv_name`

TLV from the PROXY Protocol header (1.23.2). The `name` can be a TLV type name or its numeric value. In the latter case, the value is hexadecimal and should be prefixed with `0x`:

> ```
> $proxy_protocol_tlv_alpn
$proxy_protocol_tlv_0x01
> ```

SSL TLVs can also be accessed by TLV type name or its numeric value, both prefixed by `ssl_`:

> ```
> $proxy_protocol_tlv_ssl_version
$proxy_protocol_tlv_ssl_0x21
> ```

The following TLV type names are supported:

- `alpn` (`0x01`) - upper layer protocol used over the connection
- `authority` (`0x02`) - host name value passed by the client
- `unique_id` (`0x05`) - unique connection id
- `netns` (`0x30`) - name of the namespace
- `ssl` (`0x20`) - binary SSL TLV structure

The following SSL TLV type names are supported:

- `ssl_version` (`0x21`) - SSL version used in client connection
- `ssl_cn` (`0x22`) - SSL certificate Common Name
- `ssl_cipher` (`0x23`) - name of the used cipher
- `ssl_sig_alg` (`0x24`) - algorithm used to sign the certificate
- `ssl_key_alg` (`0x25`) - public-key algorithm

Also, the following special SSL TLV type name is supported:

- `ssl_verify` - client SSL certificate verification result, `0` if the client presented a certificate and it was successfully verified, non-zero otherwise.

The PROXY protocol must be previously enabled by setting the `proxy_protocol` parameter in the [listen](#listen) directive.

`$query_string`

same as `$args`

`$realpath_root`

an absolute pathname corresponding to the [root](#root) or [alias](#alias) directive’s value for the current request, with all symbolic links resolved to real paths

`$remote_addr`

client address

`$remote_port`

client port

`$remote_user`

user name supplied with the Basic authentication

`$request`

full original request line

`$request_body`

request body

The variable’s value is made available in locations processed by the [proxy\_pass](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass), [fastcgi\_pass](https://nginx.org/en/docs/http/ngx_http_fastcgi_module.html#fastcgi_pass), [uwsgi\_pass](https://nginx.org/en/docs/http/ngx_http_uwsgi_module.html#uwsgi_pass), and [scgi\_pass](https://nginx.org/en/docs/http/ngx_http_scgi_module.html#scgi_pass) directives when the request body was read to a [memory buffer](#client_body_buffer_size).

`$request_body_file`

name of a temporary file with the request body

Part of [[imported/web/nginx.org/en-docs-http-ngx-http-core-module]].
