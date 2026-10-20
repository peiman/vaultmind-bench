---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#58-jobs-job-id-steps-parallel-jobsjob-idstepsparallel.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-58-jobs-job-id-steps-parallel-jobsjob-idstepsparallel
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].parallel`](#jobsjob_idstepsparallel)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#58-jobs-job-id-steps-parallel-jobsjob-idstepsparallel
source_hash: 1b1339bd9f8eb21bf7d356423c496ea372e2a2517e38bbf77996195ac414f7ea
---
Runs a group of steps concurrently, then waits for all of them to finish before continuing. The `parallel` keyword is shorthand: every step in the group runs as a background step, with an implicit `wait` at the end of the group. Use it when you have an independent group of steps that can run at the same time and you don't need to reference them individually.

Use `parallel` when you have a self-contained group of steps that should all finish before the job moves on, such as building several components at once. Use [`background`](#jobsjob_idstepsbackground) when you need finer control: starting a long-running process (like a server or database) that stays up while later steps run, referencing a specific step with [`wait`](#jobsjob_idstepswait) or [`cancel`](#jobsjob_idstepscancel), or interleaving background work with other steps. In short, `parallel` is more limited but more convenient for the "run this group at once" case, while `background` is the general-purpose primitive.

Each step in the group is subject to the same 10-step concurrency limit as other background steps.

Note

You cannot use `parallel` inside a composite action.

### Example: Running steps in parallel

```
steps:
  - uses: actions/checkout@v6

  - parallel:
      - name: Build frontend
        run: npm run build:frontend

      - name: Build backend
        run: npm run build:backend

      - name: Build docs
        run: npm run build:docs

  - name: Run tests after all builds complete
    run: npm test
```

The group above is equivalent to declaring each step with `background: true` followed by a `wait` step.

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
