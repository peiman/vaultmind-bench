---
# Imported by `vaultmind import` from https://git-scm.com/docs/git-config/2.51.1#06-values.
# The page is the source: re-run the import to refresh it.
id: imported-web-git-scm-com-docs-git-config-2-51-1-06-values
type: reference
title: Git - git-config Documentation › Values
url: https://git-scm.com/docs/git-config/2.51.1
source: https://git-scm.com/docs/git-config/2.51.1#06-values
source_hash: febb6c59694b579df512defc2876b590f6f630a4b42c93c97cdf4ebf1badeca6
---
Values of many variables are treated as a simple string, but there are variables that take values of specific types and there are rules as to how to spell them.

[](#Documentation/git-config.txt-boolean)boolean

When a variable is said to take a boolean value, many synonyms are accepted for *true* and *false*; these are all case-insensitive.

[](#Documentation/git-config.txt-true)true

Boolean true literals are `yes`, `on`, `true`, and `1`. Also, a variable defined without `=` *&lt;value&gt;* is taken as true.

[](#Documentation/git-config.txt-false)false

Boolean false literals are `no`, `off`, `false`, `0` and the empty string.

When converting a value to its canonical form using the `--type=bool` type specifier, *git config* will ensure that the output is "true" or "false" (spelled in lowercase).

[](#Documentation/git-config.txt-integer)integer

The value for many variables that specify various sizes can be suffixed with `k`, `M`,…​ to mean "scale the number by 1024", "by 1024x1024", etc.

[](#Documentation/git-config.txt-color)color

The value for a variable that takes a color is a list of colors (at most two, one for foreground and one for background) and attributes (as many as you want), separated by spaces.

The basic colors accepted are `normal`, `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white` and `default`. The first color given is the foreground; the second is the background. All the basic colors except `normal` and `default` have a bright variant that can be specified by prefixing the color with `bright`, like `brightred`.

The color `normal` makes no change to the color. It is the same as an empty string, but can be used as the foreground color when specifying a background color alone (for example, "normal red").

The color `default` explicitly resets the color to the terminal default, for example to specify a cleared background. Although it varies between terminals, this is usually not the same as setting to "white black".

Colors may also be given as numbers between 0 and 255; these use ANSI 256-color mode (but note that not all terminals may support this). If your terminal supports it, you may also specify 24-bit RGB values as hex, like `#ff0ab3`, or 12-bit RGB values like `#f1b`, which is equivalent to the 24-bit color `#ff11bb`.

The accepted attributes are `bold`, `dim`, `ul`, `blink`, `reverse`, `italic`, and `strike` (for crossed-out or "strikethrough" letters). The position of any attributes with respect to the colors (before, after, or in between), doesn’t matter. Specific attributes may be turned off by prefixing them with `no` or `no-` (e.g., `noreverse`, `no-ul`, etc).

The pseudo-attribute `reset` resets all colors and attributes before applying the specified coloring. For example, `reset` `green` will result in a green foreground and default background without any active attributes.

An empty color string produces no color effect at all. This can be used to avoid coloring specific elements without disabling color entirely.

For git’s pre-defined color slots, the attributes are meant to be reset at the beginning of each item in the colored output. So setting `color.decorate.branch` to `black` will paint that branch name in a plain `black`, even if the previous thing on the same output line (e.g. opening parenthesis before the list of branch names in `log` `--decorate` output) is set to be painted with `bold` or some other attribute. However, custom log formats may do more complicated and layered coloring, and the negated forms may be useful there.

[](#Documentation/git-config.txt-pathname)pathname

A variable that takes a pathname value can be given a string that begins with "`~/`" or "`~user/`", and the usual tilde expansion happens to such a string: `~/` is expanded to the value of `$HOME`, and `~user/` to the specified user’s home directory.

If a path starts with `%`(`prefix`)`/`, the remainder is interpreted as a path relative to Git’s "runtime prefix", i.e. relative to the location where Git itself was installed. For example, `%`(`prefix`)`/bin/` refers to the directory in which the Git executable itself lives. If Git was compiled without runtime prefix support, the compiled-in prefix will be substituted instead. In the unlikely event that a literal path needs to be specified that should *not* be expanded, it needs to be prefixed by `./`, like so: `./%`(`prefix`)`/bin`.

Part of [[imported/web/git-scm.com/docs-git-config-2-51-1]].
