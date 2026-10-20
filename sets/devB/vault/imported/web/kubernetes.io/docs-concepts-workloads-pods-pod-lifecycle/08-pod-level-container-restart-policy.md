---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#08-pod-level-container-restart-policy.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-08-pod-level-container-restart-policy
type: reference
title: Pod Lifecycle › How Pods handle problems with containers › Container restarts › Pod-level container restart policy
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#08-pod-level-container-restart-policy
source_hash: 9b0f79831ce371d9f5797943013b36576281561b773d0575ca080e0b38111b7c
---
The `spec` of a Pod has a `restartPolicy` field with possible values Always, OnFailure, and Never. The default value is Always.

The `restartPolicy` for a Pod applies to [app containers](https://kubernetes.io/docs/reference/glossary/?all=true#term-app-container "A container used to run part of a workload. Compare with init container.") in the Pod and to regular [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/). [Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) ignore the Pod-level `restartPolicy` field: in Kubernetes, a sidecar is defined as an entry inside `initContainers` that has its container-level `restartPolicy` set to `Always`. For init containers that exit with an error, the kubelet restarts the init container if the Pod level `restartPolicy` is either `OnFailure` or `Always`:

- `Always`: Automatically restarts the container after any termination.
- `OnFailure`: Only restarts the container if it exits with an error (non-zero exit status).
- `Never`: Does not automatically restart the terminated container.

##### Restart behavior comparison

The following table shows how containers behave under different restart policies and exit codes:

Exit Code`restartPolicy: Always``restartPolicy: OnFailure``restartPolicy: Never`Sidecar Containers0 (Success)RestartsDoes not restartDoes not restartAlways restartsNon-zero (Failure)RestartsRestartsDoes not restartAlways restarts

#### Note:

The restart behavior is particularly important when choosing between Deployments and Jobs:

- **Deployments** typically use `restartPolicy: Always` (the only allowed value) to keep applications running continuously
- **Jobs** commonly use `restartPolicy: OnFailure` or `restartPolicy: Never` to handle batch processing tasks appropriately
- **Sidecar containers** are init containers that always restart regardless of the Pod's `restartPolicy` because they have their own container-level `restartPolicy: Always`

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
