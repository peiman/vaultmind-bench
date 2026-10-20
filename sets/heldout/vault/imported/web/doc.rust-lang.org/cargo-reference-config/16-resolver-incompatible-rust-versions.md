---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#16-resolver-incompatible-rust-versions.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-16-resolver-incompatible-rust-versions
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[resolver]`](#resolver) › `resolver.incompatible-rust-versions`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#16-resolver-incompatible-rust-versions
source_hash: bb606f931ef35b3b8b25d361c273e226b9547eb71825d818da8940026feeef9c
---
- Type: string
- Default: See [`resolver`](https://doc.rust-lang.org/cargo/reference/resolver.html#resolver-versions) docs
- Environment: `CARGO_RESOLVER_INCOMPATIBLE_RUST_VERSIONS`

When resolving which version of a dependency to use, select how versions with incompatible `package.rust-version`s are treated. Values include:

- `allow`: treat `rust-version`-incompatible versions like any other version
- `fallback`: only consider `rust-version`-incompatible versions if no other version matched

Can be overridden with

- `--ignore-rust-version` CLI option
- Setting the dependency’s version requirement higher than any version with a compatible `rust-version`
- Specifying the version to `cargo update` with `--precise`

See the [resolver](https://doc.rust-lang.org/cargo/reference/resolver.html#rust-version) chapter for more details.

> **MSRV:**
> 
> - `allow` is supported on any version
> - `fallback` is respected as of 1.84

### [`[registries]`](#registries)

The `[registries]` table is used for specifying additional [registries](https://doc.rust-lang.org/cargo/reference/registries.html). It consists of a sub-table for each named registry.

#### `registries.<name>.index`

- Type: string (url)
- Default: none
- Environment: `CARGO_REGISTRIES_<name>_INDEX`

Specifies the URL of the index for the registry.

#### `registries.<name>.token`

- Type: string
- Default: none
- Environment: `CARGO_REGISTRIES_<name>_TOKEN`

Specifies the authentication token for the given registry. This value should only appear in the [credentials](#credentials) file. This is used for registry commands like [`cargo publish`](https://doc.rust-lang.org/cargo/commands/cargo-publish.html) that require authentication.

Can be overridden with the `--token` command-line option.

#### `registries.<name>.credential-provider`

- Type: string or array of path and arguments
- Default: none
- Environment: `CARGO_REGISTRIES_<name>_CREDENTIAL_PROVIDER`

Specifies the credential provider for the given registry. If not set, the providers in [`registry.global-credential-providers`](#registryglobal-credential-providers) will be used.

If specified as a string, path and arguments will be split on spaces. For paths or arguments that contain spaces, use an array.

If the value exists in the [`[credential-alias]`](#credential-alias) table, the alias will be used.

See [Registry Authentication](https://doc.rust-lang.org/cargo/reference/registry-authentication.html) for more information.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
