---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#34-standard-github-hosted-runners-for-private-reposit.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-34-standard-github-hosted-runners-for-private-reposit
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.runs-on` › Standard GitHub-hosted runners for private repositories
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#34-standard-github-hosted-runners-for-private-reposit
source_hash: c08082d003f0a10bc154f696dceb8d772f03052f49dbc711f406ab11a419da8c
---
For private repositories, jobs using the workflow labels shown in the table below will run on virtual machines with the associated specifications. These runners use your GitHub account's allotment of free minutes, and are then charged at the per minute rates. See [Actions runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing).

**Virtual Machine****Processor (CPU)****Memory (RAM)****Storage (SSD)****Architecture****Workflow label**Linux15 GB14 GB x64 `ubuntu-slim` Linux28 GB14 GB x64 `ubuntu-latest`, `ubuntu-24.04`, `ubuntu-22.04`, `ubuntu-26.04` Windows28 GB14 GB x64 `windows-latest`, `windows-2025`, `windows-2022` Linux28 GB14 GB arm64 `ubuntu-24.04-arm`, `ubuntu-22.04-arm`, `ubuntu-26.04-arm` Windows28 GB14 GB arm64 `windows-11-arm`, `windows-11-vs2026-arm` macOS414 GB14 GB Intel `macos-15-intel`, `macos-26-intel` macOS3 (M1)7 GB14 GB arm64 `macos-latest`, `macos-14`, `macos-15`, `macos-26`, `xcode-27`

In addition to the standard GitHub-hosted runners, GitHub offers customers on GitHub Team and GitHub Enterprise Cloud plans a range of managed virtual machines with advanced features - for example, more cores and disk space, GPU-powered machines, and ARM-powered machines. For more information, see [Larger runners](https://docs.github.com/en/actions/concepts/runners/larger-runners).

Note

The `-latest` runner images are the latest stable images that GitHub provides, and might not be the most recent version of the operating system available from the operating system vendor.

Warning

Beta and Deprecated Images are provided "as-is", "with all faults" and "as available" and are excluded from the service level agreement and warranty. Beta Images may not be covered by customer support.

#### Example: Specifying an operating system

```
runs-on: ubuntu-latest
```

For more information, see [GitHub-hosted runners](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
