---
# Imported by `vaultmind import` from https://docs.python.org/3.13/library/subprocess.html#14-windows-constants.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-python-org-3-13-library-subprocess-14-windows-constants
type: reference
title: subprocess — Subprocess management › Windows Popen Helpers › Windows Constants (1/2)
url: https://docs.python.org/3.13/library/subprocess.html
source: https://docs.python.org/3.13/library/subprocess.html#14-windows-constants
source_hash: 8997ddfebe086f6b905c7e0002f10441a24ef2f2f527fb966d596845d8ec0811
---
The `subprocess` module exposes the following constants.

subprocess.STD\_INPUT\_HANDLE[¶](#subprocess.STD_INPUT_HANDLE "Link to this definition")

The standard input device. Initially, this is the console input buffer, `CONIN$`.

subprocess.STD\_OUTPUT\_HANDLE[¶](#subprocess.STD_OUTPUT_HANDLE "Link to this definition")

The standard output device. Initially, this is the active console screen buffer, `CONOUT$`.

subprocess.STD\_ERROR\_HANDLE[¶](#subprocess.STD_ERROR_HANDLE "Link to this definition")

The standard error device. Initially, this is the active console screen buffer, `CONOUT$`.

subprocess.SW\_HIDE[¶](#subprocess.SW_HIDE "Link to this definition")

Hides the window. Another window will be activated.

subprocess.STARTF\_USESTDHANDLES[¶](#subprocess.STARTF_USESTDHANDLES "Link to this definition")

Specifies that the [`STARTUPINFO.hStdInput`](#subprocess.STARTUPINFO.hStdInput "subprocess.STARTUPINFO.hStdInput"), [`STARTUPINFO.hStdOutput`](#subprocess.STARTUPINFO.hStdOutput "subprocess.STARTUPINFO.hStdOutput"), and [`STARTUPINFO.hStdError`](#subprocess.STARTUPINFO.hStdError "subprocess.STARTUPINFO.hStdError") attributes contain additional information.

subprocess.STARTF\_USESHOWWINDOW[¶](#subprocess.STARTF_USESHOWWINDOW "Link to this definition")

Specifies that the [`STARTUPINFO.wShowWindow`](#subprocess.STARTUPINFO.wShowWindow "subprocess.STARTUPINFO.wShowWindow") attribute contains additional information.

subprocess.STARTF\_FORCEONFEEDBACK[¶](#subprocess.STARTF_FORCEONFEEDBACK "Link to this definition")

A [`STARTUPINFO.dwFlags`](#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") parameter to specify that the *Working in Background* mouse cursor will be displayed while a process is launching. This is the default behavior for GUI processes.

Added in version 3.13.

subprocess.STARTF\_FORCEOFFFEEDBACK[¶](#subprocess.STARTF_FORCEOFFFEEDBACK "Link to this definition")

A [`STARTUPINFO.dwFlags`](#subprocess.STARTUPINFO.dwFlags "subprocess.STARTUPINFO.dwFlags") parameter to specify that the mouse cursor will not be changed when launching a process.

Added in version 3.13.

subprocess.CREATE\_NEW\_CONSOLE[¶](#subprocess.CREATE_NEW_CONSOLE "Link to this definition")

The new process has a new console, instead of inheriting its parent’s console (the default).

subprocess.CREATE\_NEW\_PROCESS\_GROUP[¶](#subprocess.CREATE_NEW_PROCESS_GROUP "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process group will be created. This flag is necessary for using [`os.kill()`](https://docs.python.org/3.13/library/os.html#os.kill "os.kill") on the subprocess.

This flag is ignored if [`CREATE_NEW_CONSOLE`](#subprocess.CREATE_NEW_CONSOLE "subprocess.CREATE_NEW_CONSOLE") is specified.

subprocess.ABOVE\_NORMAL\_PRIORITY\_CLASS[¶](#subprocess.ABOVE_NORMAL_PRIORITY_CLASS "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have an above average priority.

Added in version 3.7.

subprocess.BELOW\_NORMAL\_PRIORITY\_CLASS[¶](#subprocess.BELOW_NORMAL_PRIORITY_CLASS "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have a below average priority.

Added in version 3.7.

subprocess.HIGH\_PRIORITY\_CLASS[¶](#subprocess.HIGH_PRIORITY_CLASS "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have a high priority.

Added in version 3.7.

subprocess.IDLE\_PRIORITY\_CLASS[¶](#subprocess.IDLE_PRIORITY_CLASS "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have an idle (lowest) priority.

Added in version 3.7.

subprocess.NORMAL\_PRIORITY\_CLASS[¶](#subprocess.NORMAL_PRIORITY_CLASS "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have a normal priority. (default)

Added in version 3.7.

subprocess.REALTIME\_PRIORITY\_CLASS[¶](#subprocess.REALTIME_PRIORITY_CLASS "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will have realtime priority. You should almost never use REALTIME\_PRIORITY\_CLASS, because this interrupts system threads that manage mouse input, keyboard input, and background disk flushing. This class can be appropriate for applications that “talk” directly to hardware or that perform brief tasks that should have limited interruptions.

Added in version 3.7.

subprocess.CREATE\_NO\_WINDOW[¶](#subprocess.CREATE_NO_WINDOW "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will not create a window.

Added in version 3.7.

subprocess.DETACHED\_PROCESS[¶](#subprocess.DETACHED_PROCESS "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process will not inherit its parent’s console. This value cannot be used with CREATE\_NEW\_CONSOLE.

Added in version 3.7.

subprocess.CREATE\_DEFAULT\_ERROR\_MODE[¶](#subprocess.CREATE_DEFAULT_ERROR_MODE "Link to this definition")

A [`Popen`](#subprocess.Popen "subprocess.Popen") `creationflags` parameter to specify that a new process does not inherit the error mode of the calling process. Instead, the new process gets the default error mode. This feature is particularly useful for multithreaded shell applications that run with hard errors disabled.

Added in version 3.7.

subprocess.CREATE\_BREAKAWAY\_FROM\_JOB[¶](#subprocess.CREATE_BREAKAWAY_FROM_JOB "Link to this definition")

Part of [[imported/web/docs.python.org/3-13-library-subprocess]].
