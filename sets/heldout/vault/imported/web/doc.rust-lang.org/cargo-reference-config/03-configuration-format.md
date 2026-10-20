---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#03-configuration-format.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-03-configuration-format
type: reference
title: Configuration - The Cargo Book › Configuration format (2/2)
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#03-configuration-format
source_hash: d1cf98d40769d123ae82093dec9bf86eac5fe204e81dd2b8a5f5c3daaadc22f0
---
[target.<triple>]
linker = "…"              # linker to use
runner = "…"              # wrapper to run executables
rustflags = ["…", "…"]    # custom flags for `rustc`
rustdocflags = ["…", "…"] # custom flags for `rustdoc`

[target.<cfg>]
linker = "…"            # linker to use
runner = "…"            # wrapper to run executables
rustflags = ["…", "…"]  # custom flags for `rustc`

[target.<triple>.<links>] # `links` build script override
rustc-link-lib = ["foo"]
rustc-link-search = ["/path/to/foo"]
rustc-flags = "-L /some/path"
rustc-cfg = ['key="value"']
rustc-env = {key = "value"}
rustc-cdylib-link-arg = ["…"]
metadata_key1 = "value"
metadata_key2 = "value"

[term]
quiet = false                    # whether cargo output is quiet
verbose = false                  # whether cargo provides verbose output
color = 'auto'                   # whether cargo colorizes output
hyperlinks = true                # whether cargo inserts links into output
unicode = true                   # whether cargo can render output using non-ASCII unicode characters
progress.when = 'auto'           # whether cargo shows progress bar
progress.width = 80              # width of progress bar
progress.term-integration = true # whether cargo reports progress to terminal emulator
```

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
