---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#13-windows-popen-helpers.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-13-windows-popen-helpers
type: reference
title: subprocess — Subprocess management › Windows Popen Helpers
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#13-windows-popen-helpers
source_hash: 144787af0294b07a3eed84b1c26a9e8a072961a6b1bc6781ea2b1feb1dd9b899
---
The [`STARTUPINFO`](#subprocess.STARTUPINFO "subprocess.STARTUPINFO") class and following constants are only available on Windows.

*class* subprocess.STARTUPINFO(*\**, *dwFlags=0*, *hStdInput=None*, *hStdOutput=None*, *hStdError=None*, *wShowWindow=0*, *lpAttributeList=None*)[¶](#subprocess.STARTUPINFO "Link to this definition")

Partial support of the Windows [STARTUPINFO](https://msdn.microsoft.com/en-us/library/ms686331%28v=vs.85%29.aspx) structure is used for [`Popen`](#subprocess.Popen "subprocess.Popen") creation. The following attributes can be set by passing them as keyword-only arguments.

Changed in version 3.7: Keyword-only argument support was added.

dwFlags[¶](#subprocess.STARTUPINFO.dwFlags "Link to this definition")

A bit field that determines whether certain `STARTUPINFO` attributes are used when the process creates a window.

```
si = subprocess.STARTUPINFO()
si.dwFlags = subprocess.STARTF_USESTDHANDLES | subprocess.STARTF_USESHOWWINDOW
```

hStdInput[¶](#subprocess.STARTUPINFO.hStdInput "Link to this definition")

If [`dwFlags`](#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") specifies [`STARTF_USESTDHANDLES`](#subprocess.STARTF_USESTDHANDLES "subprocess.STARTF_USESTDHANDLES"), this attribute is the standard input handle for the process. If `STARTF_USESTDHANDLES` is not specified, the default for standard input is the keyboard buffer.

hStdOutput[¶](#subprocess.STARTUPINFO.hStdOutput "Link to this definition")

If [`dwFlags`](#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") specifies [`STARTF_USESTDHANDLES`](#subprocess.STARTF_USESTDHANDLES "subprocess.STARTF_USESTDHANDLES"), this attribute is the standard output handle for the process. Otherwise, this attribute is ignored and the default for standard output is the console window’s buffer.

hStdError[¶](#subprocess.STARTUPINFO.hStdError "Link to this definition")

If [`dwFlags`](#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") specifies [`STARTF_USESTDHANDLES`](#subprocess.STARTF_USESTDHANDLES "subprocess.STARTF_USESTDHANDLES"), this attribute is the standard error handle for the process. Otherwise, this attribute is ignored and the default for standard error is the console window’s buffer.

wShowWindow[¶](#subprocess.STARTUPINFO.wShowWindow "Link to this definition")

If [`dwFlags`](#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") specifies [`STARTF_USESHOWWINDOW`](#subprocess.STARTF_USESHOWWINDOW "subprocess.STARTF_USESHOWWINDOW"), this attribute can be any of the values that can be specified in the `nCmdShow` parameter for the [ShowWindow](https://msdn.microsoft.com/en-us/library/ms633548%28v=vs.85%29.aspx) function, except for `SW_SHOWDEFAULT`. Otherwise, this attribute is ignored.

[`SW_HIDE`](#subprocess.SW_HIDE "subprocess.SW_HIDE") is provided for this attribute. It is used when [`Popen`](#subprocess.Popen "subprocess.Popen") is called with `shell=True`.

lpAttributeList[¶](#subprocess.STARTUPINFO.lpAttributeList "Link to this definition")

A dictionary of additional attributes for process creation as given in `STARTUPINFOEX`, see [UpdateProcThreadAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686880%28v=vs.85%29.aspx).

Supported attributes:

**handle\_list**

Sequence of handles that will be inherited. *close\_fds* must be true if non-empty.

The handles must be temporarily made inheritable by [`os.set_handle_inheritable()`](https://docs.python.org/3.13/library/os.html#os.set_handle_inheritable "os.set_handle_inheritable") when passed to the [`Popen`](#subprocess.Popen "subprocess.Popen") constructor, else [`OSError`](https://docs.python.org/3.13/builtins/exceptions.html#OSError "OSError") will be raised with Windows error `ERROR_INVALID_PARAMETER` (87).

Warning

In a multithreaded process, use caution to avoid leaking handles that are marked inheritable when combining this feature with concurrent calls to other process creation functions that inherit all handles such as [`os.system()`](https://docs.python.org/3.13/library/os.html#os.system "os.system"). This also applies to standard handle redirection, which temporarily creates inheritable handles.

Added in version 3.7.

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
