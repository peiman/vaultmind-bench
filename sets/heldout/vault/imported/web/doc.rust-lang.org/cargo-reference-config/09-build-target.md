---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#09-build-target.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-09-build-target
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[build]`](#build) › `build.target`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#09-build-target
source_hash: 12269820902254229829579f166f9c7654044b205aedf965d671bb234e065005
---
- Type: string or array of strings
- Default: host platform
- Environment: `CARGO_BUILD_TARGET`

The default [target platform triples](https://doc.rust-lang.org/cargo/appendix/glossary.html#target '"target" (glossary)') to compile to.

Possible values:

- Any supported target in `rustc --print target-list`.
- `"host-tuple"`, which will internally be substituted by the host’s target. This can be particularly useful if you’re cross-compiling some crates, and don’t want to specify your host’s machine as a target (for instance, an `xtask` in a shared project that may be worked on by many hosts).
- A path to a custom target specification. See [Custom Target Lookup Path](https://doc.rust-lang.org/rustc/targets/custom.html#custom-target-lookup-path) for more information.

Can be overridden with the `--target` CLI option.

```
[build]
target = ["x86_64-unknown-linux-gnu", "i686-unknown-linux-gnu"]
```

#### `build.target-dir`

- Type: string (path)
- Default: `"target"`
- Environment: `CARGO_BUILD_TARGET_DIR` or `CARGO_TARGET_DIR`

The path to where all compiler output is placed. The default if not specified is a directory named `target` located at the root of the workspace.

Can be overridden with the `--target-dir` CLI option.

For more information see the [build cache documentation](https://doc.rust-lang.org/cargo/reference/build-cache.html).

#### `build.build-dir`

- Type: string (path)
- Default: Defaults to the value of `build.target-dir`
- Environment: `CARGO_BUILD_BUILD_DIR`

The directory where intermediate build artifacts will be stored. Intermediate artifacts are produced by Rustc/Cargo during the build process.

This option supports path templating.

Available template variables:

- `{workspace-root}` resolves to root of the current workspace.
- `{cargo-cache-home}` resolves to `CARGO_HOME`
- `{workspace-path-hash}` resolves to a hash of the manifest path

For more information see the [build cache documentation](https://doc.rust-lang.org/cargo/reference/build-cache.html).

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
