---
# Imported by `vaultmind import` from https://doc.rust-lang.org/cargo/reference/config.html#14-net-ssh-known-hosts.
# The page is the source: re-run the import to refresh it.
id: imported-web-doc-rust-lang-org-cargo-reference-config-14-net-ssh-known-hosts
type: reference
title: Configuration - The Cargo Book › Configuration keys › [`[net]`](#net) › `net.ssh.known-hosts`
url: https://doc.rust-lang.org/cargo/reference/config.html
source: https://doc.rust-lang.org/cargo/reference/config.html#14-net-ssh-known-hosts
source_hash: 21bae4e4a9a860301037ed765d03b05f453d78f1715f0009b59f0005b1f87164
---
- Type: array of strings
- Default: see description
- Environment: not supported

The `known-hosts` array contains a list of SSH host keys that should be accepted as valid when connecting to an SSH server (such as for SSH git dependencies). Each entry should be a string in a format similar to OpenSSH `known_hosts` files. Each string should start with one or more hostnames separated by commas, a space, the key type name, a space, and the base64-encoded key. For example:

```
[net.ssh]
known-hosts = [
    "example.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFO4Q5T0UV0SQevair9PFwoxY9dl4pQl3u5phoqJH3cF"
]
```

Cargo will attempt to load known hosts keys from common locations supported in OpenSSH, and will join those with any listed in a Cargo configuration file. If any matching entry has the correct key, the connection will be allowed.

Cargo comes with the host keys for [github.com](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints) built-in. If those ever change, you can add the new keys to the config or known\_hosts file.

See [Git Authentication](https://doc.rust-lang.org/cargo/appendix/git-authentication.html#ssh-known-hosts) for more details.

Part of [[imported/web/doc.rust-lang.org/cargo-reference-config]].
