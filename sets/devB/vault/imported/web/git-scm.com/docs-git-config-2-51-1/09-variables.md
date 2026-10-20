---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#09-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-09-variables
type: reference
title: Git - git-config Documentation › Variables (3/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#09-variables
source_hash: acd20555539074de425f61aec7ec1163ae7870aebbc0644832bf0393f6a95732
---
If the alias expansion is prefixed with an exclamation point, it will be treated as a shell command. For example, defining `alias.new` `=` `!gitk` `--all` `--not` `ORIG_HEAD`, the invocation `git` `new` is equivalent to running the shell command `gitk` `--all` `--not` `ORIG_HEAD`. Note:

- Shell commands will be executed from the top-level directory of a repository, which may not necessarily be the current directory.
- `GIT_PREFIX` is set as returned by running `git` `rev-parse` `--show-prefix` from the original current directory. See [git-rev-parse\[1\]](https://git-scm.com/docs/git-rev-parse).
- Shell command aliases always receive any extra arguments provided to the Git command-line as positional arguments.

- Care should be taken if your shell alias is a "one-liner" script with multiple commands (e.g. in a pipeline), references multiple arguments, or is otherwise not able to handle positional arguments added at the end. For example: `alias.cmd` `=` `"!echo` `$1` | `grep` `$2"` called as `git` `cmd` `1` `2` will be executed as *echo $1 | grep $2 1 2*, which is not what you want.
  - A convenient way to deal with this is to write your script operations in an inline function that is then called with any arguments from the command-line. For example *alias.cmd = "!c() {* *echo $1 | grep $2 ; }; c"* will correctly execute the prior example.
  - Setting `GIT_TRACE=1` can help you debug the command being run for your alias.

[](#Documentation/git-config.txt-amkeepcr)am.keepcr

If true, git-am will call git-mailsplit for patches in mbox format with parameter `--keep-cr`. In this case git-mailsplit will not remove *\\r* from lines ending with *\\r\\n*. Can be overridden by giving `--no-keep-cr` from the command line. See [git-am\[1\]](https://git-scm.com/docs/git-am), [git-mailsplit\[1\]](https://git-scm.com/docs/git-mailsplit).

[](#Documentation/git-config.txt-amthreeWay)am.threeWay

By default, `git` `am` will fail if the patch does not apply cleanly. When set to true, this setting tells `git` `am` to fall back on 3-way merge if the patch records the identity of blobs it is supposed to apply to and we have those blobs available locally (equivalent to giving the `--3way` option from the command line). Defaults to `false`. See [git-am\[1\]](https://git-scm.com/docs/git-am).

[](#Documentation/git-config.txt-applyignoreWhitespace)apply.ignoreWhitespace

When set to *change*, tells *git apply* to ignore changes in whitespace, in the same way as the `--ignore-space-change` option. When set to one of: no, none, never, false, it tells *git apply* to respect all whitespace differences. See [git-apply\[1\]](https://git-scm.com/docs/git-apply).

[](#Documentation/git-config.txt-applywhitespace)apply.whitespace

Tells *git apply* how to handle whitespace, in the same way as the `--whitespace` option. See [git-apply\[1\]](https://git-scm.com/docs/git-apply).

[](#Documentation/git-config.txt-attrtree)attr.tree

A reference to a tree in the repository from which to read attributes, instead of the `.gitattributes` file in the working tree. If the value does not resolve to a valid tree object, an empty tree is used instead. When the `GIT_ATTR_SOURCE` environment variable or `--attr-source` command line option are used, this configuration variable has no effect.

Note

The configuration options in `bitmapPseudoMerge.*` are considered EXPERIMENTAL and may be subject to change or be removed entirely in the future. For more information about the pseudo-merge bitmap feature, see the "Pseudo-merge bitmaps" section of [gitpacking\[7\]](https://git-scm.com/docs/gitpacking).

[](#Documentation/git-config.txt-bitmapPseudoMergenamepattern)bitmapPseudoMerge.&lt;name&gt;.pattern

Regular expression used to match reference names. Commits pointed to by references matching this pattern (and meeting the below criteria, like `bitmapPseudoMerge.`*&lt;name&gt;*`.sampleRate` and `bitmapPseudoMerge.`*&lt;name&gt;*`.threshold`) will be considered for inclusion in a pseudo-merge bitmap.

Commits are grouped into pseudo-merge groups based on whether or not any reference(s) that point at a given commit match the pattern, which is an extended regular expression.

Within a pseudo-merge group, commits may be further grouped into sub-groups based on the capture groups in the pattern. These sub-groupings are formed from the regular expressions by concatenating any capture groups from the regular expression, with a *-* dash in between.

For example, if the pattern is `refs/tags/`, then all tags (provided they meet the below criteria) will be considered candidates for the same pseudo-merge group. However, if the pattern is instead `refs/remotes/`(\[`0-9`])`+/tags/`, then tags from different remotes will be grouped into separate pseudo-merge groups, based on the remote number.

[](#Documentation/git-config.txt-bitmapPseudoMergenamedecay)bitmapPseudoMerge.&lt;name&gt;.decay

Determines the rate at which consecutive pseudo-merge bitmap groups decrease in size. Must be non-negative. This parameter can be thought of as `k` in the function `f`(`n`) `=` `C` `*` `n^-k`, where `f`(`n`) is the size of the \`n\`th group.

Setting the decay rate equal to `0` will cause all groups to be the same size. Setting the decay rate equal to `1` will cause the `nth` `group` `to` `be` `1/n` the size of the initial group. Higher values of the decay rate cause consecutive groups to shrink at an increasing rate. The default is `1`.

If all groups are the same size, it is possible that groups containing newer commits will be able to be used less often than earlier groups, since it is more likely that the references pointing at newer commits will be updated more often than a reference pointing at an old commit.

[](#Documentation/git-config.txt-bitmapPseudoMergenamesampleRate)bitmapPseudoMerge.&lt;name&gt;.sampleRate

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
