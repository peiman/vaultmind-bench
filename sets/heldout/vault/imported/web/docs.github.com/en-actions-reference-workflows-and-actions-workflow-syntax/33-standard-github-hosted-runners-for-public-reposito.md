---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#33-standard-github-hosted-runners-for-public-reposito.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-33-standard-github-hosted-runners-for-public-reposito
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `jobs.<job_id>.runs-on` › Standard GitHub-hosted runners for public repositories
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#33-standard-github-hosted-runners-for-public-reposito
source_hash: e6dcd5c460823308c036a6191c628ecd749f2c886c2b8862aa91bb1a49882ba3
---
For public repositories, jobs using the workflow labels shown in the table below will run with the associated specifications. With the exception of single-CPU runners, each GitHub-hosted runner is a new virtual machine (VM) hosted by GitHub. Single-CPU runners are hosted in a container on a shared VM—see [GitHub-hosted runners reference](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#single-cpu-runners). Use of the standard GitHub-hosted runners is free and unlimited on public repositories.

**Virtual machine / container****Processor (CPU)****Memory (RAM)****Storage (SSD)****Architecture****Workflow label**Linux15 GB14 GB x64 `ubuntu-slim` Linux416 GB14 GB x64 `ubuntu-latest`, `ubuntu-24.04`, `ubuntu-22.04`, `ubuntu-26.04` Windows416 GB14 GB x64 `windows-latest`, `windows-2025`, `windows-2025-vs2026`, `windows-2022` Linux416 GB14 GB arm64 `ubuntu-24.04-arm`, `ubuntu-22.04-arm`, `ubuntu-26.04-arm` Windows416 GB14 GBarm64 `windows-11-arm`, `windows-11-vs2026-arm` macOS414 GB14 GB Intel `macos-15-intel`, `macos-26-intel` macOS3 (M1)7 GB14 GB arm64 `macos-latest`, `macos-14`, `macos-15`, `macos-26`, `xcode-27`

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
