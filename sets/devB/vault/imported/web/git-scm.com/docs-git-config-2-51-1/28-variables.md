---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#28-variables.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-28-variables
type: reference
title: Git - git-config Documentation › Variables (22/56)
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#28-variables
source_hash: 90f1ad34559e34858e204cfa3657652da6f2be4f7805dba185131e274cb50975
---
The command which is used to convert the content of a blob object to a worktree file upon checkout. See [gitattributes\[5\]](https://git-scm.com/docs/gitattributes) for details.

[](#Documentation/git-config.txt-formatattach)format.attach

Enable multipart/mixed attachments as the default for *format-patch*. The value can also be a double quoted string which will enable attachments as the default and set the value as the boundary. See the --attach option in [git-format-patch\[1\]](https://git-scm.com/docs/git-format-patch). To countermand an earlier value, set it to an empty string.

[](#Documentation/git-config.txt-formatfrom)format.from

Provides the default value for the `--from` option to format-patch. Accepts a boolean value, or a name and email address. If false, format-patch defaults to `--no-from`, using commit authors directly in the "From:" field of patch mails. If true, format-patch defaults to `--from`, using your committer identity in the "From:" field of patch mails and including a "From:" field in the body of the patch mail if different. If set to a non-boolean value, format-patch uses that value instead of your committer identity. Defaults to false.

[](#Documentation/git-config.txt-formatforceInBodyFrom)format.forceInBodyFrom

Provides the default value for the `--`\[`no-`]`force-in-body-from` option to format-patch. Defaults to false.

[](#Documentation/git-config.txt-formatnumbered)format.numbered

A boolean which can enable or disable sequence numbers in patch subjects. It defaults to "auto" which enables it only if there is more than one patch. It can be enabled or disabled for all messages by setting it to "true" or "false". See --numbered option in [git-format-patch\[1\]](https://git-scm.com/docs/git-format-patch).

Additional email headers to include in a patch to be submitted by mail. See [git-format-patch\[1\]](https://git-scm.com/docs/git-format-patch).

[](#Documentation/git-config.txt-formatto)format.to

[](#Documentation/git-config.txt-formatcc)format.cc

Additional recipients to include in a patch to be submitted by mail. See the --to and --cc options in [git-format-patch\[1\]](https://git-scm.com/docs/git-format-patch).

[](#Documentation/git-config.txt-formatsubjectPrefix)format.subjectPrefix

The default for format-patch is to output files with the *\[PATCH]* subject prefix. Use this variable to change that prefix.

[](#Documentation/git-config.txt-formatcoverFromDescription)format.coverFromDescription

The default mode for format-patch to determine which parts of the cover letter will be populated using the branch’s description. See the `--cover-from-description` option in [git-format-patch\[1\]](https://git-scm.com/docs/git-format-patch).

[](#Documentation/git-config.txt-formatsignature)format.signature

The default for format-patch is to output a signature containing the Git version number. Use this variable to change that default. Set this variable to the empty string ("") to suppress signature generation.

[](#Documentation/git-config.txt-formatsignatureFile)format.signatureFile

Works just like format.signature except the contents of the file specified by this variable will be used as the signature.

[](#Documentation/git-config.txt-formatsuffix)format.suffix

The default for format-patch is to output files with the suffix `.patch`. Use this variable to change that suffix (make sure to include the dot if you want it).

Encode email headers that have non-ASCII characters with "Q-encoding" (described in RFC 2047) for email transmission. Defaults to true.

[](#Documentation/git-config.txt-formatpretty)format.pretty

The default pretty format for log/show/whatchanged command. See [git-log\[1\]](https://git-scm.com/docs/git-log), [git-show\[1\]](https://git-scm.com/docs/git-show), [git-whatchanged\[1\]](https://git-scm.com/docs/git-whatchanged).

[](#Documentation/git-config.txt-formatthread)format.thread

The default threading style for *git format-patch*. Can be a boolean value, or `shallow` or `deep`. `shallow` threading makes every mail a reply to the head of the series, where the head is chosen from the cover letter, the `--in-reply-to`, and the first patch mail, in this order. `deep` threading makes every mail a reply to the previous one. A true boolean value is the same as `shallow`, and a false value disables threading.

[](#Documentation/git-config.txt-formatsignOff)format.signOff

A boolean value which lets you enable the `-s/--signoff` option of format-patch by default. **Note:** Adding the `Signed-off-by` trailer to a patch should be a conscious act and means that you certify you have the rights to submit this work under the same open source license. Please see the *SubmittingPatches* document for further discussion.

[](#Documentation/git-config.txt-formatcoverLetter)format.coverLetter

A boolean that controls whether to generate a cover-letter when format-patch is invoked, but in addition can be set to "auto", to generate a cover-letter only when there’s more than one patch. Default is false.

[](#Documentation/git-config.txt-formatoutputDirectory)format.outputDirectory

Set a custom directory to store the resulting files instead of the current working directory. All directory components will be created.

[](#Documentation/git-config.txt-formatfilenameMaxLength)format.filenameMaxLength

The maximum length of the output filenames generated by the `format-patch` command; defaults to 64. Can be overridden by the `--filename-max-length=`*&lt;n&gt;* command line option.

[](#Documentation/git-config.txt-formatuseAutoBase)format.useAutoBase

A boolean value which lets you enable the `--base=auto` option of format-patch by default. Can also be set to "whenAble" to allow enabling `--base=auto` if a suitable base is available, but to skip adding base info otherwise without the format dying.

[](#Documentation/git-config.txt-formatnotes)format.notes

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
