---
# Imported by `vaultmind import` from https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#13-on-schedule.
# The page is the source: re-run the import to refresh it.
id: imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-13-on-schedule
type: reference
title: Workflow syntax for GitHub Actions - GitHub Docs › `on.schedule`
url: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#13-on-schedule
source_hash: a30568945b1a24985d48be5eecddc9e9d8d970e4e7e0c882a6457b6057eaacf7
---
You can use `on.schedule` to define a time schedule for your workflows.

Use [POSIX cron syntax](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html#tag_20_25_07) to schedule workflows to run at specific times. By default, scheduled workflows run in UTC. You can optionally specify a timezone using an [IANA timezone string](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for timezone-aware scheduling. Scheduled workflows run on the latest commit on the default branch. The shortest interval you can run scheduled workflows is once every 5 minutes.

Note

For schedules that set `timezone` to a time zone that observes daylight saving time (DST), during DST spring-forward transitions, scheduled workflows in skipped hours advance to the next valid time. For example, a 2:30 AM schedule advances to 3:00 AM.

Cron syntax has five fields separated by a space, and each field represents a unit of time.

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12 or JAN-DEC)
│ │ │ │ ┌───────────── day of the week (0 - 6 or SUN-SAT)
│ │ │ │ │
* * * * *
```

You can use these operators in any of the five fields:

OperatorDescriptionExample\*Any value`15 * * * *` runs at every minute 15 of every hour of every day.,Value list separator`2,10 4,5 * * *` runs at minute 2 and 10 of the 4th and 5th hour of every day.-Range of values`30 4-6 * * *` runs at minute 30 of the 4th, 5th, and 6th hour./Step values`20/15 * * * *` runs every 15 minutes starting from minute 20 through 59 (minutes 20, 35, and 50).

This example triggers the workflow to run at 5:30 AM in the America/New\_York timezone every Monday through Friday:

```
on:
  schedule:
    - cron: '30 5 * * 1-5'
      timezone: "America/New_York"
```

A single workflow can be triggered by multiple `schedule` events. Access the `schedule` event that triggered the workflow through the `github.event.schedule` context. This example triggers the workflow to run at 5:30 UTC every Monday-Thursday, and 17:30 UTC on Tuesdays and Thursdays, but skips the `Not on Monday or Wednesday` step on Monday and Wednesday.

```
on:
  schedule:
    - cron: '30 5 * * 1,3'
    - cron: '30 5,17 * * 2,4'

jobs:
  test_schedule:
    runs-on: ubuntu-latest
    steps:
      - name: Not on Monday or Wednesday
        if: github.event.schedule != '30 5 * * 1,3'
        run: echo "This step will be skipped on Monday and Wednesday"
      - name: Every time
        run: echo "This step will always run"
```

For more information about `schedule` events, see [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## `on.workflow_call`

Use `on.workflow_call` to define the inputs and outputs for a reusable workflow. You can also map the secrets that are available to the called workflow. For more information on reusable workflows, see [Reuse workflows](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows).

Part of [[imported/web/docs.github.com/en-actions-reference-workflows-and-actions-workflow-syntax]].
