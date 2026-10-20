---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#59-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-59-variables
type: reference
title: Git - git-config Documentation › Variables (53/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#59-variables
source_hash: b533f8f62ff041792b0c0ff42844d92f932dc8c47694aa7a8baa6518b0947865
---
When both *trailer.&lt;keyAlias&gt;.cmd* and *trailer.&lt;keyAlias&gt;.command* are given for the same &lt;keyAlias&gt;, *trailer.&lt;keyAlias&gt;.cmd* is used and *trailer.&lt;keyAlias&gt;.command* is ignored.

[](#Documentation/git-config.txt-trailerkeyAliascmd)trailer.&lt;keyAlias&gt;.cmd

This option can be used to specify a shell command that will be called once to automatically add a trailer with the specified &lt;keyAlias&gt;, and then called each time a *--trailer &lt;keyAlias&gt;=&lt;value&gt;* argument is specified to modify the &lt;value&gt; of the trailer that this option would produce.

When the specified command is first called to add a trailer with the specified &lt;keyAlias&gt;, the behavior is as if a special *--trailer &lt;keyAlias&gt;=&lt;value&gt;* argument was added at the beginning of the "git interpret-trailers" command, where &lt;value&gt; is taken to be the standard output of the command with any leading and trailing whitespace trimmed off.

If some *--trailer &lt;keyAlias&gt;=&lt;value&gt;* arguments are also passed on the command line, the command is called again once for each of these arguments with the same &lt;keyAlias&gt;. And the &lt;value&gt; part of these arguments, if any, will be passed to the command as its first argument. This way the command can produce a &lt;value&gt; computed from the &lt;value&gt; passed in the *--trailer &lt;keyAlias&gt;=&lt;value&gt;* argument.

[](#Documentation/git-config.txt-transfercredentialsInUrl)transfer.credentialsInUrl

A configured URL can contain plaintext credentials in the form *&lt;protocol&gt;*`://`*&lt;user&gt;*`:`*&lt;password&gt;*`@`*&lt;domain&gt;*`/`*&lt;path&gt;*. You may want to warn or forbid the use of such configuration (in favor of using [git-credential\[1\]](https://git-scm.com/docs/git-credential)). This will be used on [git-clone\[1\]](https://git-scm.com/docs/git-clone), [git-fetch\[1\]](https://git-scm.com/docs/git-fetch), [git-push\[1\]](https://git-scm.com/docs/git-push), and any other direct use of the configured URL.

Note that this is currently limited to detecting credentials in `remote.`*&lt;name&gt;*`.url` configuration; it won’t detect credentials in `remote.`*&lt;name&gt;*`.pushurl` configuration.

You might want to enable this to prevent inadvertent credentials exposure, e.g. because:

- The OS or system where you’re running git may not provide a way or otherwise allow you to configure the permissions of the configuration file where the username and/or password are stored.
- Even if it does, having such data stored "at rest" might expose you in other ways, e.g. a backup process might copy the data to another system.
- The git programs will pass the full URL to one another as arguments on the command-line, meaning the credentials will be exposed to other unprivileged users on systems that allow them to see the full process list of other users. On linux the "hidepid" setting documented in procfs(5) allows for configuring this behavior.

If such concerns don’t apply to you then you probably don’t need to be concerned about credentials exposure due to storing sensitive data in git’s configuration files. If you do want to use this, set `transfer.credentialsInUrl` to one of these values:
- `allow` (default): Git will proceed with its activity without warning.
- `warn`: Git will write a warning message to `stderr` when parsing a URL with a plaintext credential.
- `die`: Git will write a failure message to `stderr` when parsing a URL with a plaintext credential.

[](#Documentation/git-config.txt-transferfsckObjects)transfer.fsckObjects

When `fetch.fsckObjects` or `receive.fsckObjects` are not set, the value of this variable is used instead. Defaults to false.

When set, the fetch or receive will abort in the case of a malformed object or a link to a nonexistent object. In addition, various other issues are checked for, including legacy issues (see `fsck.`*&lt;msg-id&gt;*), and potential security issues like the existence of a `.GIT` directory or a malicious `.gitmodules` file (see the release notes for v2.2.1 and v2.17.1 for details). Other sanity and security checks may be added in future releases.

On the receiving side, failing fsckObjects will make those objects unreachable, see "QUARANTINE ENVIRONMENT" in [git-receive-pack\[1\]](https://git-scm.com/docs/git-receive-pack). On the fetch side, malformed objects will instead be left unreferenced in the repository.

Due to the non-quarantine nature of the `fetch.fsckObjects` implementation it cannot be relied upon to leave the object store clean like `receive.fsckObjects` can.

As objects are unpacked they’re written to the object store, so there can be cases where malicious objects get introduced even though the "fetch" failed, only to have a subsequent "fetch" succeed because only new incoming objects are checked, not those that have already been written to the object store. That difference in behavior should not be relied upon. In the future, such objects may be quarantined for "fetch" as well.

For now, the paranoid need to find some way to emulate the quarantine environment if they’d like the same protection as "push". E.g. in the case of an internal mirror do the mirroring in two steps, one to fetch the untrusted objects, and then do a second "push" (which will use the quarantine) to another internal repo, and have internal clients consume this pushed-to repository, or embargo internal fetches and only allow them once a full "fsck" has run (and no new fetches have happened in the meantime).

[](#Documentation/git-config.txt-transferhideRefs)transfer.hideRefs

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
