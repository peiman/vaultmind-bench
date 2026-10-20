---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#11-build-rustdocflags.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-11-build-rustdocflags
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[build]`](#build) › `build.rustdocflags`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#11-build-rustdocflags
source_hash: 4abbdc0766abc82f99cb144dcd559a7dd3918bdb1299c46073d3da4f7d1e7d52
---
- Type: string or array of strings
- Default: none
- Environment: `CARGO_BUILD_RUSTDOCFLAGS` or `CARGO_ENCODED_RUSTDOCFLAGS` or `RUSTDOCFLAGS`

Extra command-line flags to pass to `rustdoc`. The value may be an array of strings or a space-separated string.

There are four mutually exclusive sources of extra flags. They are checked in order, with the first one being used:

1. `CARGO_ENCODED_RUSTDOCFLAGS` environment variable.
2. `RUSTDOCFLAGS` environment variable.
3. All matching `target.<triple>.rustdocflags` and `target.<cfg>.rustdocflags` config entries joined together.
4. `build.rustdocflags` config value.

Additional flags may also be passed with the [`cargo rustdoc`](https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html) command.

> **Caution**: Due to the low-level nature of passing flags directly to the compiler, this may cause a conflict with future versions of Cargo which may issue the same or similar flags on its own which may interfere with the flags you specify. This is an area where Cargo may not always be backwards compatible.

#### `build.incremental`

- Type: bool
- Default: from profile
- Environment: `CARGO_BUILD_INCREMENTAL` or `CARGO_INCREMENTAL`

Whether or not to perform [incremental compilation](https://doc.rust-lang.org/cargo/reference/profiles.html#incremental).

In environments with `CI` set, the default if not set is `CARGO_BUILD_INCREMENTAL=false`. Otherwise, the default is to use the value from the [profile](https://doc.rust-lang.org/cargo/reference/profiles.html#incremental).

The `CARGO_INCREMENTAL` environment variable can be set to `1` to force enable incremental compilation for all profiles, or `0` to disable it. This env var overrides the config setting.

#### `build.dep-info-basedir`

- Type: string (path)
- Default: none
- Environment: `CARGO_BUILD_DEP_INFO_BASEDIR`

Strips the given path prefix from [dep info](https://doc.rust-lang.org/cargo/reference/build-cache.html#dep-info-files) file paths. This config setting is intended to convert absolute paths to relative paths for tools that require relative paths.

The setting itself is a config-relative path. So, for example, a value of `"."` would strip all paths starting with the parent directory of the `.cargo` directory.

#### `build.pipelining`

This option is deprecated and unused. Cargo always has pipelining enabled.

### [`[credential-alias]`](#credential-alias)

- Type: string or array of strings
- Default: empty
- Environment: `CARGO_CREDENTIAL_ALIAS_<name>`

The `[credential-alias]` table defines credential provider aliases. These aliases can be referenced as an element of the `registry.global-credential-providers` array, or as a credential provider for a specific registry under `registries.<NAME>.credential-provider`.

If specified as a string, the value will be split on spaces into path and arguments.

For example, to define an alias called `my-alias`:

```
[credential-alias]
my-alias = ["/usr/bin/cargo-credential-example", "--argument", "value", "--flag"]
```

See [Registry Authentication](https://doc.rust-lang.org/cargo/reference/registry-authentication.html) for more information.

### [`[doc]`](#doc)

The `[doc]` table defines options for the [`cargo doc`](https://doc.rust-lang.org/cargo/commands/cargo-doc.html) command.

#### `doc.browser`

- Type: string or array of strings ([program path with args](#executable-paths-with-arguments))
- Default: `BROWSER` environment variable, or, if that is missing, opening the link in a system specific way

This option sets the browser to be used by [`cargo doc`](https://doc.rust-lang.org/cargo/commands/cargo-doc.html), overriding the `BROWSER` environment variable when opening documentation with the `--open` option.

### [`[cargo-new]`](#cargo-new)

The `[cargo-new]` table defines defaults for the [`cargo new`](https://doc.rust-lang.org/cargo/commands/cargo-new.html) command.

#### `cargo-new.name`

This option is deprecated and unused.

#### `cargo-new.email`

This option is deprecated and unused.

#### `cargo-new.vcs`

- Type: string
- Default: `"git"` or `"none"`
- Environment: `CARGO_CARGO_NEW_VCS`

Specifies the source control system to use for initializing a new repository. Valid values are `git`, `hg` (for Mercurial), `pijul`, `fossil` or `none` to disable this behavior. Defaults to `git`, or `none` if already inside a VCS repository. Can be overridden with the `--vcs` CLI option.

### [`[env]`](#env)

The `[env]` section allows you to set additional environment variables for build scripts, rustc invocations, `cargo run` and `cargo build`.

```
[env]
OPENSSL_DIR = "/opt/openssl"
```

By default, the variables specified will not override values that already exist in the environment. This behavior can be changed by setting the `force` flag.

Setting the `relative` flag evaluates the value as a config-relative path that is relative to the parent directory of the `.cargo` directory that contains the `config.toml` file. The value of the environment variable will be the full absolute path.

```
[env]
TMPDIR = { value = "/home/tmp", force = true }
OPENSSL_DIR = { value = "vendor/openssl", relative = true }
```

### [`[future-incompat-report]`](#future-incompat-report)

The `[future-incompat-report]` table controls setting for [future incompat reporting](https://doc.rust-lang.org/cargo/reference/future-incompat-report.html)

#### `future-incompat-report.frequency`

- Type: string
- Default: `"always"`
- Environment: `CARGO_FUTURE_INCOMPAT_REPORT_FREQUENCY`

Controls how often we display a notification to the terminal when a future incompat report is available. Possible values:

- `always` (default): Always display a notification when a command (e.g. `cargo build`) produces a future incompat report
- `never`: Never display a notification

### [`[cache]`](#cache)

The `[cache]` table defines settings for cargo’s caches.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
