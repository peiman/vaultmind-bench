---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#09-example-scenarios.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-09-example-scenarios
type: reference
title: 'Pod Lifecycle › How Pods handle problems with containers › Container restarts › Note: › Example scenarios'
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#09-example-scenarios
source_hash: babeb72a3199523940714a77b1ddfa98cf1264708ab5056bfc60fcc577f68e88
---
Here are concrete examples demonstrating the different restart behaviors:

**Example 1: Web server with `restartPolicy: Always` (typical for Deployments)**

```
apiVersion: v1
kind: Pod
metadata:
  name: web-server
spec:
  restartPolicy: Always  # Container restarts regardless of exit code
  containers:
  - name: nginx
    image: nginx:1.14.2
    # If this container crashes or exits for any reason, it will be restarted
```

**Example 2: Batch job with `restartPolicy: OnFailure`**

```
apiVersion: batch/v1
kind: Job
metadata:
  name: data-processor
spec:
  template:
    spec:
      restartPolicy: OnFailure  # Only restart on non-zero exit codes
      containers:
      - name: processor
        image: busybox:1.28
        command: ['sh', '-c', 'echo "Processing data..."; exit 0']
        # Exit code 0: Job completes successfully, no restart
        # Exit code 1+: Container restarts to retry the task
```

**Example 3: One-time task with `restartPolicy: Never`**

```
apiVersion: v1
kind: Pod
metadata:
  name: migration-task
spec:
  restartPolicy: Never  # Never restart, regardless of exit code
  containers:
  - name: migrate
    image: busybox:1.28
    command: ['sh', '-c', 'echo "Running migration..."; exit 1']
    # Even with exit code 1 (failure), the container will not restart
    # The Pod will remain in Failed state
```

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
