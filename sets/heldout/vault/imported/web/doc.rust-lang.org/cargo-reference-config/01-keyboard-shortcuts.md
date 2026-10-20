---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#01-keyboard-shortcuts.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-01-keyboard-shortcuts
type: reference
title: Configuration - The Cargo Book › Keyboard shortcuts
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#01-keyboard-shortcuts
source_hash: 7eb91f2323105f97cc1ccd9cb967626ce01fae8a122626a695d852b303539f2b
---
Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## Configuration

This document explains how Cargo’s configuration system works, as well as available keys or configuration. For configuration of a package through its manifest, see the [manifest format](https://doc.rust-lang.org/cargo/reference/manifest.html).

## Hierarchical structure

Cargo allows local configuration for a particular package as well as global configuration. It looks for configuration files in the current directory and all parent directories. If, for example, Cargo were invoked in `/projects/foo/bar/baz`, then the following configuration files would be probed for and unified in this order:

- `/projects/foo/bar/baz/.cargo/config.toml`
- `/projects/foo/bar/.cargo/config.toml`
- `/projects/foo/.cargo/config.toml`
- `/projects/.cargo/config.toml`
- `/.cargo/config.toml`
- `$CARGO_HOME/config.toml` which defaults to:
  
  - Windows: `%USERPROFILE%\.cargo\config.toml`
  - Unix: `$HOME/.cargo/config.toml`

With this structure, you can specify configuration per-package, and even possibly check it into version control. You can also specify personal defaults with a configuration file in your home directory.

If a key is specified in multiple config files, the values will get merged together. Numbers, strings, and booleans will use the value in the deeper config directory taking precedence over ancestor directories, where the home directory is the lowest priority. Arrays will be joined together with higher precedence items being placed later in the merged array.

At present, when being invoked from a workspace, Cargo does not read config files from crates within the workspace. i.e. if a workspace has two crates in it, named `/projects/foo/bar/baz/mylib` and `/projects/foo/bar/baz/mybin`, and there are Cargo configs at `/projects/foo/bar/baz/mylib/.cargo/config.toml` and `/projects/foo/bar/baz/mybin/.cargo/config.toml`, Cargo does not read those configuration files if it is invoked from the workspace root (`/projects/foo/bar/baz/`).

> **Note:** Cargo also reads config files without the `.toml` extension, such as `.cargo/config`. Support for the `.toml` extension was added in version 1.39 and is the preferred form. If both files exist, Cargo will use the file without the extension.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
