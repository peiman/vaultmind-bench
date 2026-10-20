---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config
type: reference
title: Configuration - The Cargo Book
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html
source_hash: 39ac34c2f0b926acd96fb9e898b9bf6365be16ae261ff2e546fae89c6592b7c0
---
Configuration - The Cargo Book: 19 sections.

- [[imported/web/doc.rust-lang.org/cargo-reference-config/01-keyboard-shortcuts|Keyboard shortcuts]] — Press `←` or `→` to navigate between chapters
- [[imported/web/doc.rust-lang.org/cargo-reference-config/02-configuration-format|Configuration format (1/2)]] — Configuration files are written in the [TOML format](https://toml.io/) (like the manifest), with simple key-value pairs …
- [[imported/web/doc.rust-lang.org/cargo-reference-config/03-configuration-format|Configuration format (2/2)]] — [target.<triple>]
- [[imported/web/doc.rust-lang.org/cargo-reference-config/04-environment-variables|Environment variables]] — Cargo can also be configured through environment variables in addition to the TOML configuration files. For each configu…
- [[imported/web/doc.rust-lang.org/cargo-reference-config/05-command-line-overrides|Command-line overrides]] — Cargo also accepts arbitrary configuration overrides through the `--config` command-line option. The argument should be …
- [[imported/web/doc.rust-lang.org/cargo-reference-config/06-include|Including extra configuration files › `include`]] — - Type: array of strings or tables
- [[imported/web/doc.rust-lang.org/cargo-reference-config/07-config-relative-paths|Config-relative paths]] — Paths in config files may be absolute, relative, or a bare name without any path separators. Paths for executables witho…
- [[imported/web/doc.rust-lang.org/cargo-reference-config/08-credentials|Credentials]] — Configuration values with sensitive information are stored in the `$CARGO_HOME/credentials.toml` file. This file is auto…
- [[imported/web/doc.rust-lang.org/cargo-reference-config/09-build-target|Configuration keys › [`[build]`](#build) › `build.target`]] — - Type: string or array of strings
- [[imported/web/doc.rust-lang.org/cargo-reference-config/10-build-rustflags|Configuration keys › [`[build]`](#build) › `build.rustflags`]] — - Type: string or array of strings
- [[imported/web/doc.rust-lang.org/cargo-reference-config/11-build-rustdocflags|Configuration keys › [`[build]`](#build) › `build.rustdocflags`]] — - Type: string or array of strings
- [[imported/web/doc.rust-lang.org/cargo-reference-config/12-global-caches|Configuration keys › [`[cache]`](#cache) › Global caches]] — When running `cargo` commands, Cargo will automatically track which files you are using within the global cache. Periodi…
- [[imported/web/doc.rust-lang.org/cargo-reference-config/13-install-root|Configuration keys › [`[install]`](#install) › `install.root`]] — - Type: string (path)
- [[imported/web/doc.rust-lang.org/cargo-reference-config/14-net-ssh-known-hosts|Configuration keys › [`[net]`](#net) › `net.ssh.known-hosts`]] — - Type: array of strings
- [[imported/web/doc.rust-lang.org/cargo-reference-config/15-patch-patch|Configuration keys › [`[patch]`](#patch)]] — Just as you can override dependencies using [`[patch]` in `Cargo.toml`](https://doc.rust-lang.org/cargo/reference/overri…
- [[imported/web/doc.rust-lang.org/cargo-reference-config/16-resolver-incompatible-rust-versions|Configuration keys › [`[resolver]`](#resolver) › `resolver.incompatible-rust-versions`]] — - Type: string
- [[imported/web/doc.rust-lang.org/cargo-reference-config/17-registries-crates-io-protocol|Configuration keys › [`[registries]`](#registries) › `registries.crates-io.protocol`]] — - Type: string
- [[imported/web/doc.rust-lang.org/cargo-reference-config/18-target-target|Configuration keys › [`[target]`](#target)]] — The `[target]` table is used for specifying settings for specific platform targets. It consists of a sub-table which is …
- [[imported/web/doc.rust-lang.org/cargo-reference-config/19-term-quiet|Configuration keys › [`[term]`](#term) › `term.quiet`]] — - Type: boolean
