---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#17-registries-crates-io-protocol.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-17-registries-crates-io-protocol
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[registries]`](#registries) › `registries.crates-io.protocol`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#17-registries-crates-io-protocol
source_hash: bb7d70ff8f32a7d5cb59191b1d74a43148636a9910e0a8afd7c5a97d430a0d38
---
- Type: string
- Default: `"sparse"`
- Environment: `CARGO_REGISTRIES_CRATES_IO_PROTOCOL`

Specifies the protocol used to access crates.io. Allowed values are `git` or `sparse`.

`git` causes Cargo to clone the entire index of all packages ever published to [crates.io](https://crates.io/) from [https://github.com/rust-lang/crates.io-index/](https://github.com/rust-lang/crates.io-index/). This can have performance implications due to the size of the index. `sparse` is a newer protocol which uses HTTPS to download only what is necessary from [https://index.crates.io/](https://index.crates.io/). This can result in a significant performance improvement for resolving new dependencies in most situations.

More information about registry protocols may be found in the [Registries chapter](https://doc.rust-lang.org/cargo/reference/registries.html).

### [`[registry]`](#registry)

The `[registry]` table controls the default registry used when one is not specified.

#### `registry.index`

This value is no longer accepted and should not be used.

#### `registry.default`

- Type: string
- Default: `"crates-io"`
- Environment: `CARGO_REGISTRY_DEFAULT`

The name of the registry (from the [`registries` table](#registries)) to use by default for registry commands like [`cargo publish`](https://doc.rust-lang.org/cargo/commands/cargo-publish.html).

Can be overridden with the `--registry` command-line option.

#### `registry.credential-provider`

- Type: string or array of path and arguments
- Default: none
- Environment: `CARGO_REGISTRY_CREDENTIAL_PROVIDER`

Specifies the credential provider for [crates.io](https://crates.io/). If not set, the providers in [`registry.global-credential-providers`](#registryglobal-credential-providers) will be used.

If specified as a string, path and arguments will be split on spaces. For paths or arguments that contain spaces, use an array.

If the value exists in the `[credential-alias]` table, the alias will be used.

See [Registry Authentication](https://doc.rust-lang.org/cargo/reference/registry-authentication.html) for more information.

#### `registry.token`

- Type: string
- Default: none
- Environment: `CARGO_REGISTRY_TOKEN`

Specifies the authentication token for [crates.io](https://crates.io/). This value should only appear in the [credentials](#credentials) file. This is used for registry commands like [`cargo publish`](https://doc.rust-lang.org/cargo/commands/cargo-publish.html) that require authentication.

Can be overridden with the `--token` command-line option.

#### `registry.global-credential-providers`

- Type: array
- Default: `["cargo:token"]`
- Environment: `CARGO_REGISTRY_GLOBAL_CREDENTIAL_PROVIDERS`

Specifies the list of global credential providers. If credential provider is not set for a specific registry using `registries.<name>.credential-provider`, Cargo will use the credential providers in this list. Providers toward the end of the list have precedence.

Path and arguments are split on spaces. If the path or arguments contains spaces, the credential provider should be defined in the [`[credential-alias]`](#credential-alias) table and referenced here by its alias.

See [Registry Authentication](https://doc.rust-lang.org/cargo/reference/registry-authentication.html) for more information.

### [`[source]`](#source)

The `[source]` table defines the registry sources available. See [Source Replacement](https://doc.rust-lang.org/cargo/reference/source-replacement.html) for more information. It consists of a sub-table for each named source. A source should only define one kind (directory, registry, local-registry, or git).

#### `source.<name>.replace-with`

- Type: string
- Default: none
- Environment: not supported

If set, replace this source with the given named source or named registry.

#### `source.<name>.directory`

- Type: string (path)
- Default: none
- Environment: not supported

Sets the path to a directory to use as a directory source.

#### `source.<name>.registry`

- Type: string (url)
- Default: none
- Environment: not supported

Sets the URL to use for a registry source.

#### `source.<name>.local-registry`

- Type: string (path)
- Default: none
- Environment: not supported

Sets the path to a directory to use as a local registry source.

#### `source.<name>.git`

- Type: string (url)
- Default: none
- Environment: not supported

Sets the URL to use for a git repository source.

#### `source.<name>.branch`

- Type: string
- Default: none
- Environment: not supported

Sets the branch name to use for a git repository.

If none of `branch`, `tag`, or `rev` is set, defaults to the `master` branch.

#### `source.<name>.tag`

- Type: string
- Default: none
- Environment: not supported

Sets the tag name to use for a git repository.

If none of `branch`, `tag`, or `rev` is set, defaults to the `master` branch.

#### `source.<name>.rev`

- Type: string
- Default: none
- Environment: not supported

Sets the [revision](https://git-scm.com/docs/gitrevisions) to use for a git repository.

If none of `branch`, `tag`, or `rev` is set, defaults to the `master` branch.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
