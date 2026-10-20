---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#61-using-a-multi-dimensional-matrix.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-61-using-a-multi-dimensional-matrix
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.strategy.matrix` › Using a multi-dimensional matrix
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#61-using-a-multi-dimensional-matrix
source_hash: 9854341d723cb0808b5d0a9a5d76be4c2833e9869b925e073566335bf9059e04
---
Specify multiple variables to create a multi-dimensional matrix. A job will run for each possible combination of the variables.

For example, the following workflow specifies two variables:

- Two operating systems specified in the `os` variable
- Three Node.js versions specified in the `version` variable

The workflow will run six jobs, one for each combination of the `os` and `version` variables. Each job will set the `runs-on` value to the current `os` value and will pass the current `version` value to the `actions/setup-node` action.

```
jobs:
  example_matrix:
    strategy:
      matrix:
        os: [ubuntu-22.04, ubuntu-24.04]
        version: [10, 12, 14]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-node@v7
        with:
          node-version: ${{ matrix.version }}
```

A variable configuration in a matrix can be an `array` of `object`s. For example, the following matrix produces 4 jobs with corresponding contexts.

```
matrix:
  os:
    - ubuntu-latest
    - macos-latest
  node:
    - version: 14
    - version: 20
      env: NODE_OPTIONS=--openssl-legacy-provider
```

Each job in the matrix will have its own combination of `os` and `node` values, as shown below.

```
- matrix.os: ubuntu-latest
  matrix.node.version: 14
- matrix.os: ubuntu-latest
  matrix.node.version: 20
  matrix.node.env: NODE_OPTIONS=--openssl-legacy-provider
- matrix.os: macos-latest
  matrix.node.version: 14
- matrix.os: macos-latest
  matrix.node.version: 20
  matrix.node.env: NODE_OPTIONS=--openssl-legacy-provider
```

## `jobs.<job_id>.strategy.matrix.include`

For each object in the `include` list, the key:value pairs in the object will be added to each of the matrix combinations if none of the key:value pairs overwrite any of the original matrix values. If the object cannot be added to any of the matrix combinations, a new matrix combination will be created instead. Note that the original matrix values will not be overwritten, but added matrix values can be overwritten.

### Example: Expanding configurations

For example, the following workflow will run four jobs, one for each combination of `os` and `node`. When the job for the `os` value of `windows-latest` and `node` value of `16` runs, an additional variable called `npm` with the value of `6` will be included in the job.

```
jobs:
  example_matrix:
    strategy:
      matrix:
        os: [windows-latest, ubuntu-latest]
        node: [14, 16]
        include:
          - os: windows-latest
            node: 16
            npm: 6
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/setup-node@v7
        with:
          node-version: ${{ matrix.node }}
      - if: ${{ matrix.npm }}
        run: npm install -g npm@${{ matrix.npm }}
      - run: npm --version
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
