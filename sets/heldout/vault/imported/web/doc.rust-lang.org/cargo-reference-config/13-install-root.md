---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#13-install-root.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-13-install-root
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[install]`](#install) › `install.root`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#13-install-root
source_hash: b7ab0fe2f76665dc83a0a5197c761144600a8e4ea9bbbda8de350c78381c7804
---
- Type: string (path)
- Default: Cargo’s home directory
- Environment: `CARGO_INSTALL_ROOT`

Sets the path to the root directory for installing executables for [`cargo install`](https://doc.rust-lang.org/cargo/commands/cargo-install.html). Executables go into a `bin` directory underneath the root.

To track information of installed executables, some extra files, such as `.crates.toml` and `.crates2.json`, are also created under this root.

The default if not specified is Cargo’s home directory (default `.cargo` in your home directory).

Can be overridden with the `--root` command-line option.

### [`[net]`](#net)

The `[net]` table controls networking configuration.

#### `net.retry`

- Type: integer
- Default: 3
- Environment: `CARGO_NET_RETRY`

Number of times to retry possibly spurious network errors.

#### `net.git-fetch-with-cli`

- Type: boolean
- Default: false
- Environment: `CARGO_NET_GIT_FETCH_WITH_CLI`

If this is `true`, then Cargo will use the `git` executable to fetch registry indexes and git dependencies. If `false`, then it uses a built-in `git` library.

Setting this to `true` can be helpful if you have special authentication requirements that Cargo does not support. See [Git Authentication](https://doc.rust-lang.org/cargo/appendix/git-authentication.html) for more information about setting up git authentication.

#### `net.offline`

- Type: boolean
- Default: false
- Environment: `CARGO_NET_OFFLINE`

If this is `true`, then Cargo will avoid accessing the network, and attempt to proceed with locally cached data. If `false`, Cargo will access the network as needed, and generate an error if it encounters a network error.

Can be overridden with the `--offline` command-line option.

#### `net.ssh`

The `[net.ssh]` table contains settings for SSH connections.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
