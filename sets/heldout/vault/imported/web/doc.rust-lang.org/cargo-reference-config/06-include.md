---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#06-include.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-06-include
type: reference
title: Configuration - The Cargo Book › Including extra configuration files › `include`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#06-include
source_hash: 49fdc80a9cd736e57552a9c018b08cdd673cc0da9eb64afbfc6ec9017dff2861
---
- Type: array of strings or tables
- Default: none
- Environment: not supported

Loads additional configuration files. Paths are relative to the configuration file that includes them. Only paths ending with `.toml` are accepted.

Supports the following formats:

```
# array of paths
include = [
    "frodo.toml",
    "samwise.toml",
]

# inline tables for more control
include = [
    { path = "required.toml" },
    { path = "optional.toml", optional = true },
]
```

> **Note:** For better readability and to avoid confusion, it is recommended to:
> 
> - Place `include` at the top of the configuration file
> - Put one include per line for clearer version control diffs
> - Use inline table syntax when optional includes are needed

When using table syntax, the following fields are supported:

- `path` (string, required): Path to the config file to include.
- `optional` (boolean, default: false): If `true`, missing files are silently skipped instead of causing an error.

The merge behavior of `include` is different from other config values:

1. Config values are first loaded from the `include` paths.
   
   - Included files are loaded left to right, with values from later files taking precedence over earlier ones.
   - This step recurses if included config files also contain `include` keys.
2. Then, the config file’s own values are merged on top of the included config, taking highest precedence.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
