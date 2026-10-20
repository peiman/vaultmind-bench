---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#02-syntax.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-02-syntax
type: reference
title: Git - git-config Documentation › Syntax
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#02-syntax
source_hash: f7db88b17efe426c53d5670a90c78129cdf415a3e3190df631adcc3660cf022c
---
The syntax is fairly flexible and permissive. Whitespace characters, which in this context are the space character (SP) and the horizontal tabulation (HT), are mostly ignored. The *#* and *;* characters begin comments to the end of line. Blank lines are ignored.

The file consists of sections and variables. A section begins with the name of the section in square brackets and continues until the next section begins. Section names are case-insensitive. Only alphanumeric characters, `-` and `.` are allowed in section names. Each variable must belong to some section, which means that there must be a section header before the first setting of a variable.

Sections can be further divided into subsections. To begin a subsection put its name in double quotes, separated by space from the section name, in the section header, like in the example below:

```
	[section "subsection"]
```

Subsection names are case sensitive and can contain any characters except newline and the null byte. Doublequote `"` and backslash can be included by escaping them as *\\"* and *\\\\*, respectively. Backslashes preceding other characters are dropped when reading; for example, *\\t* is read as `t` and *\\0* is read as `0`. Section headers cannot span multiple lines. Variables may belong directly to a section or to a given subsection. You can have \[`section`] if you have \[`section` `"subsection"`], but you don’t need to.

There is also a deprecated \[`section.subsection`] syntax. With this syntax, the subsection name is converted to lower-case and is also compared case sensitively. These subsection names follow the same restrictions as section names.

All the other lines (and the remainder of the line after the section header) are recognized as setting variables, in the form *name = value* (or just *name*, which is a short-hand to say that the variable is the boolean "true"). The variable names are case-insensitive, allow only alphanumeric characters and `-`, and must start with an alphabetic character.

Whitespace characters surrounding `name`, `=` and `value` are discarded. Internal whitespace characters within *value* are retained verbatim. Comments starting with either `#` or *;* and extending to the end of line are discarded. A line that defines a value can be continued to the next line by ending it with a backslash (*\\*); the backslash and the end-of-line characters are discarded.

If `value` needs to contain leading or trailing whitespace characters, it must be enclosed in double quotation marks (`"`). Inside double quotation marks, double quote (`"`) and backslash (*\\*) characters must be escaped: use *\\"* for `"` and *\\\\* for *\\*.

The following escape sequences (beside *\\"* and *\\\\*) are recognized: *\\n* for newline character (NL), *\\t* for horizontal tabulation (HT, TAB) and *\\b* for backspace (BS). Other char escape sequences (including octal escape sequences) are invalid.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
