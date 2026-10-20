---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#08-credentials.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-08-credentials
type: reference
title: Configuration - The Cargo Book › Credentials
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#08-credentials
source_hash: 4ebc8b2a913a2b3456c81b8ab1f52a4925848bdcb3c7fec54728c9f040bcce2e
---
Configuration values with sensitive information are stored in the `$CARGO_HOME/credentials.toml` file. This file is automatically created and updated by [`cargo login`](https://doc.rust-lang.org/cargo/commands/cargo-login.html) and [`cargo logout`](https://doc.rust-lang.org/cargo/commands/cargo-logout.html) when using the [`cargo:token`](https://doc.rust-lang.org/cargo/reference/registry-authentication.html#cargotoken) credential provider.

Tokens are used by some Cargo commands such as [`cargo publish`](https://doc.rust-lang.org/cargo/commands/cargo-publish.html) for authenticating with remote registries. Care should be taken to protect the tokens and to keep them secret.

It follows the same format as Cargo config files.

```
[registry]
token = "…"   # Access token for crates.io

[registries.<name>]
token = "…"   # Access token for the named registry
```

As with most other config values, tokens may be specified with environment variables. The token for [crates.io](https://crates.io/) may be specified with the `CARGO_REGISTRY_TOKEN` environment variable. Tokens for other registries may be specified with environment variables of the form `CARGO_REGISTRIES_<name>_TOKEN` where `<name>` is the name of the registry in all capital letters.

> **Note:** Cargo also reads and writes credential files without the `.toml` extension, such as `.cargo/credentials`. Support for the `.toml` extension was added in version 1.39. In version 1.68, Cargo writes to the file with the extension by default. However, for backward compatibility reason, when both files exist, Cargo will read and write the file without the extension.

## Configuration keys

This section documents all configuration keys. The description for keys with variable parts are annotated with angled brackets like `target.<triple>` where the `<triple>` part can be any [target triple](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') like `target.x86_64-pc-windows-msvc`.

### `paths`

- Type: array of strings (paths)
- Default: none
- Environment: not supported

An array of paths to local packages which are to be used as overrides for dependencies. For more information see the [Overriding Dependencies guide](https://doc.rust-lang.org/cargo/reference/overriding-dependencies.html#paths-overrides).

### [`[alias]`](#alias)

- Type: string or array of strings
- Default: see below
- Environment: `CARGO_ALIAS_<name>`

The `[alias]` table defines CLI command aliases. For example, running `cargo b` is an alias for running `cargo build`. Each key in the table is the subcommand, and the value is the actual command to run. The value may be an array of strings, where the first element is the command and the following are arguments. It may also be a string, which will be split on spaces into subcommand and arguments. The following aliases are built-in to Cargo:

```
[alias]
b = "build"
c = "check"
d = "doc"
t = "test"
r = "run"
rm = "remove"
```

Aliases are not allowed to redefine existing built-in commands.

Aliases are recursive:

```
[alias]
rr = "run --release"
recursive_example = "rr --example recursions"
```

### [`[build]`](#build)

The `[build]` table controls build-time operations and compiler settings.

#### `build.warnings`

- Type: string
- Default: `"warn"`
- Environment: `CARGO_BUILD_WARNINGS`

Adjust the effective level of lint warnings for local packages. Allowed levels are:

- `"warn"`: continue to emit the lints as warnings (default).
- `"allow"`: hide the lints.
- `"deny"`: emit an error for a crate that has lint warnings. Use `--keep-going` to see the lint warnings for all dependent crates.

Only warnings that are lints (i.e. level is adjustable) are affected, e.g. leaving as-is non-lint warnings or warnings from dependencies visible through `--verbose --verbose`.

> **MSRV:** Respected as of 1.97.

#### `build.jobs`

- Type: integer or string
- Default: number of logical CPUs
- Environment: `CARGO_BUILD_JOBS`

Sets the maximum number of compiler processes to run in parallel. If negative, it sets the maximum number of compiler processes to the number of logical CPUs plus provided value. Should not be 0. If a string `default` is provided, it sets the value back to defaults.

Can be overridden with the `--jobs` CLI option.

#### `build.rustc`

- Type: string (program path)
- Default: `"rustc"`
- Environment: `CARGO_BUILD_RUSTC` or `RUSTC`

Sets the executable to use for `rustc`.

#### `build.rustc-wrapper`

- Type: string (program path)
- Default: none
- Environment: `CARGO_BUILD_RUSTC_WRAPPER` or `RUSTC_WRAPPER`

Sets a wrapper to execute instead of `rustc`. The first argument passed to the wrapper is the path to the actual executable to use (i.e., `build.rustc`, if that is set, or `"rustc"` otherwise).

#### `build.rustc-workspace-wrapper`

- Type: string (program path)
- Default: none
- Environment: `CARGO_BUILD_RUSTC_WORKSPACE_WRAPPER` or `RUSTC_WORKSPACE_WRAPPER`

Sets a wrapper to execute instead of `rustc`, for workspace members only. When building a single-package project without workspaces, that package is considered to be the workspace. The first argument passed to the wrapper is the path to the actual executable to use (i.e., `build.rustc`, if that is set, or `"rustc"` otherwise). It affects the filename hash so that artifacts produced by the wrapper are cached separately.

If both `rustc-wrapper` and `rustc-workspace-wrapper` are set, then they will be nested: the final invocation is `$RUSTC_WRAPPER $RUSTC_WORKSPACE_WRAPPER $RUSTC`.

#### `build.rustdoc`

- Type: string (program path)
- Default: `"rustdoc"`
- Environment: `CARGO_BUILD_RUSTDOC` or `RUSTDOC`

Sets the executable to use for `rustdoc`.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
