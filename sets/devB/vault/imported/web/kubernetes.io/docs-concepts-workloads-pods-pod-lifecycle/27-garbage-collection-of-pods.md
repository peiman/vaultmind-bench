---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#27-garbage-collection-of-pods.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-27-garbage-collection-of-pods
type: reference
title: Pod Lifecycle › Termination of Pods › Garbage collection of Pods
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#27-garbage-collection-of-pods
source_hash: 8c46f8fcfb53a7758d1b6e83d4bfb6d95c4e17417056bbbc0c6d8c0c16ac3050
---
For failed Pods, the API objects remain in the cluster's API until a human or [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") process explicitly removes them.

The Pod garbage collector (PodGC), which is a controller in the control plane, cleans up terminated Pods (with a phase of `Succeeded` or `Failed`), when the number of Pods exceeds the configured threshold (determined by `terminated-pod-gc-threshold` in the kube-controller-manager). This avoids a resource leak as Pods are created and terminated over time.

Additionally, PodGC cleans up any Pods which satisfy any of the following conditions:

1. are orphan Pods - bound to a node which no longer exists,
2. are unscheduled terminating Pods,
3. are terminating Pods, bound to a non-ready node tainted with [`node.kubernetes.io/out-of-service`](https://kubernetes.io/docs/reference/labels-annotations-taints/#node-kubernetes-io-out-of-service).

Along with cleaning up the Pods, PodGC will also mark them as failed if they are in a non-terminal phase. Also, PodGC adds a Pod disruption condition when cleaning up an orphan Pod. See [Pod disruption conditions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-conditions) for more details.

## Pod behavior during kubelet restarts

If you restart the kubelet, Pods (and their containers) continue to run even during the restart. When there are running Pods on a node, stopping or restarting the kubelet on that node does **not** cause the kubelet to stop all local Pods before the kubelet itself stops. To stop the Pods on a node, you can use `kubectl drain`.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
