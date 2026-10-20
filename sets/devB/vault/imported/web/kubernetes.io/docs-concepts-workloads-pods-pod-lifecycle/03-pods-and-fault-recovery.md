---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#03-pods-and-fault-recovery.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-03-pods-and-fault-recovery
type: reference
title: Pod Lifecycle › Pod lifetime › Pods and fault recovery
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#03-pods-and-fault-recovery
source_hash: e9533c7f0bb091321dec53f4ae2fcb6281086b6edb804151fd59cc9fe6d133b1
---
If one of the containers in the Pod fails, then Kubernetes may try to restart that specific container. Read [How Pods handle problems with containers](#container-restarts) to learn more.

Pods can however fail in a way that the cluster cannot recover from, and in that case Kubernetes does not attempt to heal the Pod further; instead, Kubernetes deletes the Pod and relies on other components to provide automatic healing.

If a Pod is scheduled to a [node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") and that node then fails, the Pod is treated as unhealthy and Kubernetes eventually deletes the Pod. A Pod won't survive an [eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/ "Process of terminating one or more Pods on Nodes") due to a lack of resources or Node maintenance.

Kubernetes uses a higher-level abstraction, called a [controller](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state."), that handles the work of managing the relatively disposable Pod instances.

A given Pod (as defined by a UID) is never "rescheduled" to a different node; instead, that Pod can be replaced by a new, near-identical Pod. If you make a replacement Pod, it can even have same name (as in `.metadata.name`) that the old Pod had, but the replacement would have a different `.metadata.uid` from the old Pod.

Kubernetes does not guarantee that a replacement for an existing Pod would be scheduled to the same node as the old Pod that was being replaced.

### Associated lifetimes

When something is said to have the same lifetime as a Pod, such as a [volume](https://kubernetes.io/docs/concepts/storage/volumes/ "A directory containing data, accessible to the containers in a pod."), that means that the thing exists as long as that specific Pod (with that exact UID) exists. If that Pod is deleted for any reason, and even if an identical replacement is created, the related thing (a volume, in this example) is also destroyed and created anew.

![A multi-container Pod that contains a file puller sidecar and a web server. The Pod uses an ephemeral emptyDir volume for shared storage between the containers.](https://kubernetes.io/images/docs/pod.svg)

#### Figure 1.

A multi-container Pod that contains a file puller [sidecar](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) and a web server. The Pod uses an [ephemeral `emptyDir` volume](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) for shared storage between the containers.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
