---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#05-command-line-overrides.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-05-command-line-overrides
type: reference
title: Configuration - The Cargo Book › Command-line overrides
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#05-command-line-overrides
source_hash: da4e7bb0d25ffa9e59557c5dc0d5481b0ce4ca182c196442e514d021951c30c8
---
Cargo also accepts arbitrary configuration overrides through the `--config` command-line option. The argument should be in TOML syntax of `KEY=VALUE` or provided as a path to an extra configuration file:

```
# With `KEY=VALUE` in TOML syntax
cargo --config net.git-fetch-with-cli=true fetch

# With a path to a configuration file
cargo --config ./path/to/my/extra-config.toml fetch
```

The `--config` option may be specified multiple times, in which case the values are merged in left-to-right order, using the same merging logic that is used when multiple configuration files apply. Configuration values specified this way take precedence over environment variables, which take precedence over configuration files.

When the `--config` option is provided as an extra configuration file, The configuration file loaded this way follow the same precedence rules as other options specified directly with `--config`.

Some examples of what it looks like using Bourne shell syntax:

```
# Most shells will require escaping.
cargo --config http.proxy=\"http://example.com\" …

# Spaces may be used.
cargo --config "net.git-fetch-with-cli = true" …

# TOML array example. Single quotes make it easier to read and write.
cargo --config 'build.rustdocflags = ["--html-in-header", "header.html"]' …

# Example of a complex TOML key.
cargo --config "target.'cfg(all(target_arch = \"arm\", target_os = \"none\"))'.runner = 'my-runner'" …

# Example of overriding a profile setting.
cargo --config profile.dev.package.image.opt-level=3 …
```

## Including extra configuration files

Configuration can include other configuration files using the top-level `include` key. This allows sharing configuration across multiple projects or splitting complex configurations into multiple files.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
