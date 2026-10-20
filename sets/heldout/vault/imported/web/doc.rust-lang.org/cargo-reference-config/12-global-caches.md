---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#12-global-caches.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-12-global-caches
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[cache]`](#cache) › Global caches
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#12-global-caches
source_hash: dc2343eddcb3c5a9402949bac22480dd7a1e05da15eeac2becfdeba889c54cf4
---
When running `cargo` commands, Cargo will automatically track which files you are using within the global cache. Periodically, Cargo will delete files that have not been used for some period of time. It will delete files that have to be downloaded from the network if they have not been used in 3 months. Files that can be generated without network access will be deleted if they have not been used in 1 month.

The automatic deletion of files only occurs when running commands that are already doing a significant amount of work, such as all of the build commands (`cargo build`, `cargo test`, `cargo check`, etc.), and `cargo fetch`.

Automatic deletion is disabled if cargo is offline such as with `--offline` or `--frozen` to avoid deleting artifacts that may need to be used if you are offline for a long period of time.

> **Note**: This tracking is currently only implemented for the global cache in Cargo’s home directory. This includes registry indexes and source files downloaded from registries and git dependencies. Support for tracking build artifacts is not yet implemented, and tracked in [cargo#13136](https://github.com/rust-lang/cargo/issues/13136).
> 
> Additionally, there is an unstable feature to support *manually* triggering cache cleaning, and to further customize the configuration options. See the [Unstable chapter](https://doc.rust-lang.org/cargo/reference/unstable.html#gc) for more information.

#### `cache.auto-clean-frequency`

- Type: string
- Default: `"1 day"`
- Environment: `CARGO_CACHE_AUTO_CLEAN_FREQUENCY`

This option defines how often Cargo will automatically delete unused files in the global cache. This does *not* define how old the files must be, those thresholds are described [above](#global-caches).

It supports the following settings:

- `"never"` — Never deletes old files.
- `"always"` — Checks to delete old files every time Cargo runs.
- An integer followed by “seconds”, “minutes”, “hours”, “days”, “weeks”, or “months” — Checks to delete old files at most the given time frame.

### [`[http]`](#http)

The `[http]` table defines settings for HTTP behavior. This includes fetching crate dependencies and accessing remote git repositories.

#### `http.debug`

- Type: boolean
- Default: false
- Environment: `CARGO_HTTP_DEBUG`

If `true`, enables debugging of HTTP requests. The debug information can be seen by setting the `CARGO_LOG=network=debug` environment variable (or use `network=trace` for even more information).

Be wary when posting logs from this output in a public location. The output may include headers with authentication tokens which you don’t want to leak! Be sure to review logs before posting them.

#### `http.proxy`

- Type: string
- Default: none
- Environment: `CARGO_HTTP_PROXY` or `HTTPS_PROXY` or `https_proxy` or `http_proxy`

Sets an HTTP and HTTPS proxy to use. The format is in [libcurl format](https://everything.curl.dev/transfers/conn/proxies#proxy-types) as in `[protocol://]host[:port]`. If not set, Cargo will also check the `http.proxy` setting in your global git configuration. If none of those are set, the `HTTPS_PROXY` or `https_proxy` environment variables set the proxy for HTTPS requests, and `http_proxy` sets it for HTTP requests.

#### `http.timeout`

- Type: integer
- Default: 30
- Environment: `CARGO_HTTP_TIMEOUT` or `HTTP_TIMEOUT`

Sets the timeout for each HTTP request, in seconds.

#### `http.cainfo`

- Type: string (path)
- Default: none
- Environment: `CARGO_HTTP_CAINFO`

Path to a Certificate Authority (CA) bundle file, used to verify TLS certificates. If not specified, Cargo attempts to use the system certificates.

#### `http.proxy-cainfo`

- Type: string (path)
- Default: falls back to `http.cainfo` if not set
- Environment: `CARGO_HTTP_PROXY_CAINFO`

Path to a Certificate Authority (CA) bundle file, used to verify proxy TLS certificates.

#### `http.check-revoke`

- Type: boolean
- Default: true (Windows) false (all others)
- Environment: `CARGO_HTTP_CHECK_REVOKE`

This determines whether or not TLS certificate revocation checks should be performed. This only works on Windows.

#### `http.ssl-version`

- Type: string or min/max table
- Default: none
- Environment: `CARGO_HTTP_SSL_VERSION`

This sets the minimum TLS version to use. It takes a string, with one of the possible values of `"default"`, `"tlsv1"`, `"tlsv1.0"`, `"tlsv1.1"`, `"tlsv1.2"`, or `"tlsv1.3"`.

This may alternatively take a table with two keys, `min` and `max`, which each take a string value of the same kind that specifies the minimum and maximum range of TLS versions to use.

The default is a minimum version of `"tlsv1.0"` and a max of the newest version supported on your platform, typically `"tlsv1.3"`.

#### `http.low-speed-limit`

- Type: integer
- Default: 10
- Environment: `CARGO_HTTP_LOW_SPEED_LIMIT`

This setting controls timeout behavior for slow connections. If the average transfer speed in bytes per second is below the given value for [`http.timeout`](#httptimeout) seconds (default 30 seconds), then the connection is considered too slow and Cargo will abort and retry.

#### `http.multiplexing`

- Type: boolean
- Default: true
- Environment: `CARGO_HTTP_MULTIPLEXING`

When `true`, Cargo will attempt to use the HTTP2 protocol with multiplexing. This allows multiple requests to use the same connection, usually improving performance when fetching multiple files. If `false`, Cargo will use HTTP 1.1 without pipelining.

#### `http.user-agent`

- Type: string
- Default: Cargo’s version
- Environment: `CARGO_HTTP_USER_AGENT`

Specifies a custom user-agent header to use. The default if not specified is a string that includes Cargo’s version.

### [`[install]`](#install)

The `[install]` table defines defaults for the [`cargo install`](https://doc.rust-lang.org/cargo/commands/cargo-install.html) command.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
