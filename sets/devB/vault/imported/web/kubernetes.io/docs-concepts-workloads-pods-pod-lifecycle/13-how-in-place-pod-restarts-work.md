---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#13-how-in-place-pod-restarts-work.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-13-how-in-place-pod-restarts-work
type: reference
title: Pod Lifecycle › How Pods handle problems with containers › Container restarts › Restart All Containers › How in-place Pod restarts work
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#13-how-in-place-pod-restarts-work
source_hash: 20d69b8654e555a4771ec29d88d64f9772b4068f67e28574bae4d8ad2876dc98
---
When a `RestartAllContainers` action is triggered, the kubelet performs the following steps:

1. **Fast Termination**: All running containers in the Pod are terminated. The configured `terminationGracePeriodSeconds` is not respected, and any configured `preStop` hooks are not executed. This ensures a swift shutdown.
2. **Preservation of Pod Resources**: The Pod's essential resources are preserved:
   
   - Pod UID, IP address, and network namespace
   - Pod sandbox and any attached devices
   - All volumes, including `emptyDir` and mounted volumes
3. **Pod Status Update**: The Pod's status is updated with a `PodRestartInPlace` condition set to `True`. This makes the restart process observable.
4. **Full Restart Sequence**: Once all containers are terminated, the `PodRestartInPlace` condition is set to `False`, and the Pod begins the standard startup process:
   
   - **Init containers are re-run** in order.
   - Sidecar and regular containers are started.

A key aspect of this feature is that **all** containers are restarted, including those that previously completed successfully or failed. The `RestartAllContainers` action overrides any configured container-level or Pod-level `restartPolicy`.

This mechanism is useful in scenarios where a clean slate for all containers is necessary, such as:

- When an `init` container sets up an environment that can become corrupted, this feature ensures the setup process is re-executed.
- A sidecar container can monitor the health of a main application and trigger a full Pod restart if the application enters an unrecoverable state.

Consider a workload where a watcher sidecar is responsible for restarting the main application from a known-good state if it encounters an error. The watcher can exit with a specific code to trigger a full, in-place restart of the worker Pod.

```
apiVersion: v1
kind: Pod
metadata:
  name: ml-worker
spec:
  restartPolicy: Never # The pod itself should not restart unless explicitly told to.
  initContainers:
  - name: setup-environment
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Setting up environment"']
    # This init container runs once to prepare the environment.
    # It will run again after a RestartAllContainers action.
  - name: watcher-sidecar
    image: registry.k8s.io/busybox:1.27.2
    # In a real-world scenario, this would be a dedicated watcher image.
    # This command simulates the watcher exiting with a special code.
    command: ['sh', '-c', 'sleep 60; exit 88']
    restartPolicy: Always
    restartPolicyRules:
    - action: RestartAllContainers
      exitCodes:
        # Exit code 88 triggers a full pod restart.
        operator: In
        values: [88]
  containers:
  - name: main-application
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Application is running"; sleep 3600']
```

In this example:

- The Pod's overall `restartPolicy` is `Never`.
- The `watcher-sidecar` runs a command and then exits with code `88`.
- The exit code matches the rule, triggering the `RestartAllContainers` action.
- The entire Pod, including the `setup-environment` init container and the `main-application` container, is then restarted in-place. The pod keeps its UID, sandbox, IP, and volumes.

### Reduced container restart delay

Feature state: Alpha since Kubernetes v1.33; disabled by default

With the alpha feature gate `ReduceDefaultCrashLoopBackOffDecay` enabled, container start retries across your cluster will be reduced to begin at 1s (instead of 10s) and increase exponentially by 2x each restart until a maximum delay of 60s (instead of 300s which is 5 minutes).

If you use this feature along with the alpha feature `KubeletCrashLoopBackOffMax` (described below), individual nodes may have different maximum delays.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
