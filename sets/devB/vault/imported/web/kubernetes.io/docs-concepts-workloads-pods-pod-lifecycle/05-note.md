---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#05-note.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-05-note
type: reference
title: 'Pod Lifecycle › Pod phase › Note:'
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#05-note
source_hash: c89dadbcba2259d7e95c45f2daa5cf93371138e741f1d3538cb7aec4d6c9784e
---
When a pod is failing to start repeatedly, `CrashLoopBackOff` may appear in the `Status` field of some kubectl commands. Similarly, when a pod is being deleted, `Terminating` may appear in the `Status` field of some kubectl commands.

Make sure not to confuse *Status*, a kubectl display field for user intuition, with the pod's `phase`. Pod phase is an explicit part of the Kubernetes data model and of the [Pod API](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/).

```
  NAMESPACE               NAME               READY   STATUS             RESTARTS   AGE
  alessandras-namespace   alessandras-pod    0/1     CrashLoopBackOff   200        2d9h
```

A Pod is granted a term to terminate gracefully, which defaults to 30 seconds. You can use the flag `--force` to [terminate a Pod by force](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-forced).

Since Kubernetes 1.27, the kubelet transitions deleted Pods to a terminal phase (`Failed` or `Succeeded` depending on the exit statuses of the pod containers) before their deletion from the API server, with two exceptions:

- [static Pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) (which are managed directly by the kubelet and represented by [mirror Pods](https://kubernetes.io/docs/reference/glossary/?all=true#term-mirror-pod "An object in the API server that tracks a static pod on a kubelet."))
- [force-deleted Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination-forced) without a finalizer

If a node dies or is disconnected from the rest of the cluster, Kubernetes applies a policy for setting the `phase` of all Pods on the lost node to Failed.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
