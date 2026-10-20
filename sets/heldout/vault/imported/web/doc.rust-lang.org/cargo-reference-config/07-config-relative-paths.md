---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#07-config-relative-paths.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-07-config-relative-paths
type: reference
title: Configuration - The Cargo Book › Config-relative paths
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#07-config-relative-paths
source_hash: 79bd395210ad506ee7755a50d2dc9e97f26aeed235da7697a0be6c0f91e7ffaf
---
Paths in config files may be absolute, relative, or a bare name without any path separators. Paths for executables without a path separator will use the `PATH` environment variable to search for the executable. Paths for non-executables will be relative to where the config value is defined.

In particular, rules are:

- For environment variables, paths are relative to the current working directory.
- For config values loaded directly from the [`--config KEY=VALUE`](#command-line-overrides) option, paths are relative to the current working directory.
- For config files, paths are relative to the parent directory of the directory where the config files were defined, no matter those files are from either the [hierarchical probing](#hierarchical-structure) or the [`--config <path>`](#command-line-overrides) option.

> **Note:** To maintain consistency with existing `.cargo/config.toml` probing behavior, it is by design that a path in a config file passed via `--config <path>` is also relative to two levels up from the config file itself.
> 
> To avoid unexpected results, the rule of thumb is putting your extra config files at the same level of discovered `.cargo/config.toml` in your project. For instance, given a project `/my/project`, it is recommended to put config files under `/my/project/.cargo` or a new directory at the same level, such as `/my/project/.config`.

```
# Relative path examples.

[target.x86_64-unknown-linux-gnu]
runner = "foo"  # Searches `PATH` for `foo`.

[source.vendored-sources]
# Directory is relative to the parent where `.cargo/config.toml` is located.
# For example, `/my/project/.cargo/config.toml` would result in `/my/project/vendor`.
directory = "vendor"
```

## Executable paths with arguments

Some Cargo commands invoke external programs, which can be configured as a path and some number of arguments.

The value may be an array of strings like `['/path/to/program', 'somearg']` or a space-separated string like `'/path/to/program somearg'`. If the path to the executable contains a space, the list form must be used.

If Cargo is passing other arguments to the program such as a path to open or run, they will be passed after the last specified argument in the value of an option of this format. If the specified program does not have path separators, Cargo will search `PATH` for its executable.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
