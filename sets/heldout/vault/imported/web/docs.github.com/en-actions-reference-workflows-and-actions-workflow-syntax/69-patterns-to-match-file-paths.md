---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#69-patterns-to-match-file-paths.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-69-patterns-to-match-file-paths
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › Filter pattern cheat sheet › Patterns to match file paths
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#69-patterns-to-match-file-paths
source_hash: 907092bb5d00b01b65e00e90a9750a561a0ff77d819924bdd5aebea64177180c
---
Path patterns must match the whole path, and start from the repository's root.

PatternDescription of matchesExample matches`'*'`The `*` wildcard matches any character, but does not match slash (`/`). The `*` character is a special character in YAML. When you start a pattern with `*`, you must use quotes.`README.md`

`server.rb`

`'*.jsx?'`The `?` character matches zero or one of the preceding character.`page.js`

`page.jsx`

`'**'`The `**` wildcard matches any character including slash (`/`). This is the default behavior when you don't use a `path` filter.`all/the/files.md``'*.js'`The `*` wildcard matches any character, but does not match slash (`/`). Matches all `.js` files at the root of the repository.`app.js`

`index.js`

`'**.js'`Matches all `.js` files in the repository.`index.js`

`js/index.js`

`src/js/app.js`

`docs/*`All files within the root of the `docs` directory only, at the root of the repository.`docs/README.md`

`docs/file.txt`

`docs/**`Any files in the `docs` directory and its subdirectories at the root of the repository.`docs/README.md`

`docs/mona/octocat.txt`

`docs/**/*.md`A file with a `.md` suffix anywhere in the `docs` directory.`docs/README.md`

`docs/mona/hello-world.md`

`docs/a/markdown/file.md`

`'**/docs/**'`Any files in a `docs` directory anywhere in the repository.`docs/hello.md`

`dir/docs/my-file.txt`

`space/docs/plan/space.doc`

`'**/README.md'`A README.md file anywhere in the repository.`README.md`

`js/README.md`

`'**/*src/**'`Any file in a folder with a `src` suffix anywhere in the repository.`a/src/app.js`

`my-src/code/js/app.js`

`'**/*-post.md'`A file with the suffix `-post.md` anywhere in the repository.`my-post.md`

`path/their-post.md`

`'**/migrate-*.sql'`A file with the prefix `migrate-` and suffix `.sql` anywhere in the repository.`migrate-10909.sql`

`db/migrate-v1.0.sql`

`db/sept/migrate-v1.sql`

`'*.md'`

`'!README.md'`

Using an exclamation mark (`!`) in front of a pattern negates it. When a file matches a pattern and also matches a negative pattern defined later in the file, the file will not be included.`hello.md`

*Does not match*

`README.md`

`docs/hello.md`

`'*.md'`

`'!README.md'`

`README*`

Patterns are checked sequentially. A pattern that negates a previous pattern will re-include file paths.`hello.md`

`README.md`

`README.doc`

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
