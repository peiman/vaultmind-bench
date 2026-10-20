---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#19-term-quiet.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-19-term-quiet
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[term]`](#term) › `term.quiet`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#19-term-quiet
source_hash: 5662911d9340977d9d2f448bed320d3c2bff074ed69c3d405672a209ad90a1b2
---
- Type: boolean
- Default: false
- Environment: `CARGO_TERM_QUIET`

Controls whether or not log messages are displayed by Cargo.

Specifying the `--quiet` flag will override and force quiet output. Specifying the `--verbose` flag will override and disable quiet output.

#### `term.verbose`

- Type: boolean
- Default: false
- Environment: `CARGO_TERM_VERBOSE`

Controls whether or not extra detailed messages are displayed by Cargo.

Specifying the `--quiet` flag will override and disable verbose output. Specifying the `--verbose` flag will override and force verbose output.

#### `term.color`

- Type: string
- Default: `"auto"`
- Environment: `CARGO_TERM_COLOR`

Controls whether or not colored output is used in the terminal. Possible values:

- `auto` (default): Automatically detect if color support is available on the terminal.
- `always`: Always display colors.
- `never`: Never display colors.

Can be overridden with the `--color` command-line option.

#### `term.hyperlinks`

- Type: bool
- Default: auto-detect
- Environment: `CARGO_TERM_HYPERLINKS`

Controls whether or not hyperlinks are used in the terminal.

#### `term.unicode`

- Type: bool
- Default: auto-detect
- Environment: `CARGO_TERM_UNICODE`

Control whether output can be rendered using non-ASCII unicode characters.

#### `term.progress.when`

- Type: string
- Default: `"auto"`
- Environment: `CARGO_TERM_PROGRESS_WHEN`

Controls whether or not progress bar is shown in the terminal. Possible values:

- `auto` (default): Intelligently guess whether to show progress bar.
- `always`: Always show progress bar.
- `never`: Never show progress bar.

#### `term.progress.width`

- Type: integer
- Default: none
- Environment: `CARGO_TERM_PROGRESS_WIDTH`

Sets the width for progress bar.

#### `term.progress.term-integration`

- Type: bool
- Default: auto-detect
- Environment: `CARGO_TERM_PROGRESS_TERM_INTEGRATION`

Report progress to the terminal emulator for display in places like the task bar.

[](https://doc.rust-lang.org/cargo/reference/profiles.html "Previous chapter")[](https://doc.rust-lang.org/cargo/reference/environment-variables.html "Next chapter")

[](https://doc.rust-lang.org/cargo/reference/profiles.html "Previous chapter")[](https://doc.rust-lang.org/cargo/reference/environment-variables.html "Next chapter")

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
