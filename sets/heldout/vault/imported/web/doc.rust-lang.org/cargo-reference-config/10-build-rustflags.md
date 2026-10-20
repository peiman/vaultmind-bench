---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#10-build-rustflags.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-10-build-rustflags
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[build]`](#build) › `build.rustflags`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#10-build-rustflags
source_hash: c971225071890d97d42ddd5d55996940b4b597aeb556ee9387f2070b429a9c1b
---
- Type: string or array of strings
- Default: none
- Environment: `CARGO_BUILD_RUSTFLAGS` or `CARGO_ENCODED_RUSTFLAGS` or `RUSTFLAGS`

Extra command-line flags to pass to `rustc`. The value may be an array of strings or a space-separated string.

There are four mutually exclusive sources of extra flags. They are checked in order, with the first one being used:

1. `CARGO_ENCODED_RUSTFLAGS` environment variable.
2. `RUSTFLAGS` environment variable.
3. All matching `target.<triple>.rustflags` and `target.<cfg>.rustflags` config entries joined together.
4. `build.rustflags` config value.

Additional flags may also be passed with the [`cargo rustc`](https://doc.rust-lang.org/cargo/commands/cargo-rustc.html) command.

If the `--target` flag (or [`build.target`](#buildtarget)) is used, then the flags will only be passed to the compiler for the target. Things being built for the host, such as build scripts or proc macros, will not receive the args. Without `--target`, the flags will be passed to all compiler invocations (including build scripts and proc macros) because dependencies are shared. If you have args that you do not want to pass to build scripts or proc macros and are building for the host, pass `--target` with the [host triple](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)').

It is not recommended to pass in flags that Cargo itself usually manages. For example, the flags driven by [profiles](https://doc.rust-lang.org/cargo/reference/profiles.html) are best handled by setting the appropriate profile setting.

> **Caution**: Due to the low-level nature of passing flags directly to the compiler, this may cause a conflict with future versions of Cargo which may issue the same or similar flags on its own which may interfere with the flags you specify. This is an area where Cargo may not always be backwards compatible.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
