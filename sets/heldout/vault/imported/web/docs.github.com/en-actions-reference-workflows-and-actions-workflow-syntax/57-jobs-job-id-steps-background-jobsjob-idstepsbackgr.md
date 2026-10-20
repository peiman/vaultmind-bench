---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#57-jobs-job-id-steps-background-jobsjob-idstepsbackgr.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-57-jobs-job-id-steps-background-jobsjob-idstepsbackgr
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › [`jobs.<job_id>.steps[*].background`](#jobsjob_idstepsbackground)
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#57-jobs-job-id-steps-background-jobsjob-idstepsbackgr
source_hash: c61ffed3477459a8f148e8ed8d166f50cb6947c66eed74fd2cc18db93b227b2a
---
Runs a step asynchronously so the job continues to the next step without waiting for it to finish. Use `background: true` for long-running processes, such as databases, servers, or monitoring tasks, that need to run alongside other steps. You synchronize with background steps later using [`wait`](#jobsjob_idstepswait) or [`wait-all`](#jobsjob_idstepswait-all) or stop them with [`cancel`](#jobsjob_idstepscancel).

You can use `background` on steps that use `run` or `uses`. To reference a background step from [`wait`](#jobsjob_idstepswait) or [`cancel`](#jobsjob_idstepscancel), give it an [`id`](#jobsjob_idstepsid). A maximum of 10 background steps can run concurrently in a single job; additional background steps are queued until a slot is free.

Outputs and environment changes from a background step are only available after you run a `wait` or `wait-all` step that includes it. If a background step fails, the job fails at the next `wait` or `wait-all` that includes it (unless [`continue-on-error`](#jobsjob_idstepscontinue-on-error) is set on that step). An implicit `wait-all` runs before any post-job cleanup.

Use `background` when you need fine-grained control: starting a long-running process (like a server or database) that stays up while later steps run, referencing a specific step with [`wait`](#jobsjob_idstepswait) or [`cancel`](#jobsjob_idstepscancel), or interleaving background work with other steps. If you instead have a self-contained group of steps that should all finish before the job continues, [`parallel`](#jobsjob_idstepsparallel) is a more convenient shorthand.

Note

You cannot use `background` on steps inside a composite action. A composite action can itself run as a background step, but it cannot declare background steps internally.

### Example: Running a step in the background

```
steps:
  - name: Start server
    id: server
    run: npm start
    background: true

  - name: Run tests against the server
    run: npm test

  - name: Wait for the server step to finish
    wait: server
```

## [`jobs.<job_id>.steps[*].wait`](#jobsjob_idstepswait)

Pauses the job until one or more background steps complete. A `wait` step performs no work itself, it only blocks until the referenced background steps finish. Provide a single step `id` as a string, or multiple step `id`s as an array.

After a `wait` step completes, the outputs of the referenced background steps become available to subsequent steps. If a referenced background step failed, the `wait` step fails too.

Note

A `wait` step always runs and does not support the [`if`](#jobsjob_idstepsif) conditional.

### Example: Waiting for specific background steps

```
steps:
  - name: Build frontend
    id: build-frontend
    run: npm run build:frontend
    background: true

  - name: Build backend
    id: build-backend
    run: npm run build:backend
    background: true

  - name: Run linter while builds run
    run: npm run lint

  - name: Wait for both builds to finish
    wait: [build-frontend, build-backend]

  - name: Run tests
    run: npm test
```

## [`jobs.<job_id>.steps[*].wait-all`](#jobsjob_idstepswait-all)

Pauses the job until all active background steps complete. This is useful when several background steps are running and you want them all to finish before continuing. Like `wait`, the `wait-all` step fails if any of the background steps it waits on failed, unless you set [`continue-on-error`](#jobsjob_idstepscontinue-on-error) to `true`.

The `wait-all` keyword takes no arguments.

Note

A `wait-all` step always runs and does not support the [`if`](#jobsjob_idstepsif) conditional.

### Example: Waiting for all background steps

```
steps:
  - name: Start database
    id: db
    run: docker run -d postgres:15
    background: true

  - name: Start cache
    id: cache
    run: docker run -d redis:7
    background: true

  - name: Run integration tests
    run: npm run test:integration

  - name: Wait for all services to stop
    wait-all:
```

## [`jobs.<job_id>.steps[*].cancel`](#jobsjob_idstepscancel)

Gracefully terminates a running background step. The runner sends the step's process a termination signal (`SIGTERM`) so it can clean up, and forcibly stops it (`SIGKILL`) if it does not exit within a short grace period. The `cancel` keyword targets a single background step by its `id`.

Note

A `cancel` step always runs and does not support the [`if`](#jobsjob_idstepsif) conditional.

### Example: Canceling a background step

```
steps:
  - name: Start long-running monitor
    id: monitor
    run: ./scripts/monitor.sh
    background: true

  - name: Run the main task
    run: npm test

  - name: Stop the monitor
    cancel: monitor
```

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
