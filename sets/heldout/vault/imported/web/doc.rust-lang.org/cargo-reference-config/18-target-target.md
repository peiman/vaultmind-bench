---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#18-target-target.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-18-target-target
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[target]`](#target)
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#18-target-target
source_hash: ffd7246f7047845199705e9ab78fa5c8e3994abeffbd7be5a8769be4de6b783b
---
The `[target]` table is used for specifying settings for specific platform targets. It consists of a sub-table which is either a [platform triple](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') or a [`cfg()` expression](https://doc.rust-lang.org/reference/conditional-compilation.html). The given values will be used if the target platform matches either the `<triple>` value or the `<cfg>` expression.

```
[target.thumbv7m-none-eabi]
linker = "arm-none-eabi-gcc"
runner = "my-emulator"
rustflags = ["…", "…"]

[target.'cfg(all(target_arch = "arm", target_os = "none"))']
runner = "my-arm-wrapper"
rustflags = ["…", "…"]
```

`cfg` values come from those built-in to the compiler (run `rustc --print=cfg` to view) and extra `--cfg` flags passed to `rustc` (such as those defined in `RUSTFLAGS`). Do not try to match on `debug_assertions`, `test`, Cargo features like `feature="foo"`, or values set by [build scripts](https://doc.rust-lang.org/cargo/reference/build-scripts.html).

If using a target spec JSON file, the [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') value is the filename stem. For example `--target foo/bar.json` would match `[target.bar]`.

#### `target.<triple>.ar`

This option is deprecated and unused.

#### `target.<triple>.linker`

- Type: string (program path)
- Default: none
- Environment: `CARGO_TARGET_<triple>_LINKER`

Specifies the linker which is passed to `rustc` (via [`-C linker`](https://doc.rust-lang.org/rustc/codegen-options/index.html#linker)) when the [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') is being compiled for. By default, the linker is not overridden.

#### `target.<cfg>.linker`

This is similar to the [target linker](#targettriplelinker), but using a [`cfg()` expression](https://doc.rust-lang.org/reference/conditional-compilation.html). If both a [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') and `<cfg>` linker match, the `<triple>` will take precedence. It is an error if more than one `<cfg>` linker matches the current target.

#### `target.<triple>.runner`

- Type: string or array of strings ([program path with args](#executable-paths-with-arguments))
- Default: none
- Environment: `CARGO_TARGET_<triple>_RUNNER`

If a runner is provided, executables for the target [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') will be executed by invoking the specified runner with the actual executable passed as an argument. This applies to [`cargo run`](https://doc.rust-lang.org/cargo/commands/cargo-run.html), [`cargo test`](https://doc.rust-lang.org/cargo/commands/cargo-test.html) and [`cargo bench`](https://doc.rust-lang.org/cargo/commands/cargo-bench.html) commands. By default, compiled executables are executed directly.

#### `target.<cfg>.runner`

This is similar to the [target runner](#targettriplerunner), but using a [`cfg()` expression](https://doc.rust-lang.org/reference/conditional-compilation.html). If both a [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') and `<cfg>` runner match, the `<triple>` will take precedence. It is an error if more than one `<cfg>` runner matches the current target.

#### `target.<triple>.rustflags`

- Type: string or array of strings
- Default: none
- Environment: `CARGO_TARGET_<triple>_RUSTFLAGS`

Passes a set of custom flags to the compiler for this [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)'). The value may be an array of strings or a space-separated string.

See [`build.rustflags`](#buildrustflags) for more details on the different ways to specific extra flags.

#### `target.<cfg>.rustflags`

This is similar to the [target rustflags](#targettriplerustflags), but using a [`cfg()` expression](https://doc.rust-lang.org/reference/conditional-compilation.html). If several `<cfg>` and [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') entries match the current target, the flags are joined together.

#### `target.<triple>.rustdocflags`

- Type: string or array of strings
- Default: none
- Environment: `CARGO_TARGET_<triple>_RUSTDOCFLAGS`

Passes a set of custom flags to the compiler for this [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)'). The value may be an array of strings or a space-separated string.

See [`build.rustdocflags`](#buildrustdocflags) for more details on the different ways to specific extra flags.

#### `target.<cfg>.rustdocflags`

This is similar to the [target rustdocflags](#targettriplerustdocflags), but using a [`cfg()` expression](https://doc.rust-lang.org/reference/conditional-compilation.html). If several `<cfg>` and [`<triple>`](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') entries match the current target, the flags are joined together.

#### `target.<triple>.<links>`

The links sub-table provides a way to [override a build script](https://doc.rust-lang.org/cargo/reference/build-scripts.html#overriding-build-scripts). When specified, the build script for the given `links` library will not be run, and the given values will be used instead.

```
[target.x86_64-unknown-linux-gnu.foo]
rustc-link-lib = ["foo"]
rustc-link-search = ["/path/to/foo"]
rustc-flags = "-L /some/path"
rustc-cfg = ['key="value"']
rustc-env = {key = "value"}
rustc-cdylib-link-arg = ["…"]
metadata_key1 = "value"
metadata_key2 = "value"
```

### [`[term]`](#term)

The `[term]` table controls terminal output and interaction.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
