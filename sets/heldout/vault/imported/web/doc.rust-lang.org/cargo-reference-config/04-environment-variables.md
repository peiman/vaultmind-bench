---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#04-environment-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-04-environment-variables
type: reference
title: Configuration - The Cargo Book › Environment variables
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#04-environment-variables
source_hash: a58da497ebf618864901e4f8e869f94156fd8dae0ea7124771ddab7333094f53
---
Cargo can also be configured through environment variables in addition to the TOML configuration files. For each configuration key of the form `foo.bar` the environment variable `CARGO_FOO_BAR` can also be used to define the value. Keys are converted to uppercase, dots and dashes are converted to underscores. For example the `target.x86_64-unknown-linux-gnu.runner` key can also be defined by the `CARGO_TARGET_X86_64_UNKNOWN_LINUX_GNU_RUNNER` environment variable.

Environment variables will take precedence over TOML configuration files. Currently only integer, boolean, string and some array values are supported to be defined by environment variables. [Descriptions below](#configuration-keys) indicate which keys support environment variables and otherwise they are not supported due to [technical issues](https://github.com/rust-lang/cargo/issues/5416).

In addition to the system above, Cargo recognizes a few other specific [environment variables](https://doc.rust-lang.org/cargo/reference/environment-variables.html).

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
