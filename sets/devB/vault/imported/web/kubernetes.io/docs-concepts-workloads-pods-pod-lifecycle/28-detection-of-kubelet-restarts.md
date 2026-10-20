---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#28-detection-of-kubelet-restarts.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-28-detection-of-kubelet-restarts
type: reference
title: Pod Lifecycle › Pod behavior during kubelet restarts › Detection of kubelet restarts
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#28-detection-of-kubelet-restarts
source_hash: e7db897030426094cb816c1ef36c50a0d0b662b7544dd2a55ec3999b832cf42f
---
Feature state: Deprecated since Kubernetes v1.35; disabled by default

When the kubelet starts, it checks to see if there is already a Node with bound Pods. If the Node's [`Ready` condition](https://kubernetes.io/docs/reference/node/node-status/#condition) remains unchanged, in other words the condition has not transitioned from true to false, Kubernetes detects this a *kubelet restart*. (It's possible to restart the kubelet in other ways, for example to fix a node bug, but in these cases, Kubernetes picks the safe option and treats this as if you stopped the kubelet and then later started it).

When the kubelet restarts, the container statuses are managed differently based on the feature gate setting:

- By default, the kubelet does not change container statuses after a restart. Containers that were in set to `ready: true` state remain ready.
  
  If you stop the kubelet long enough for it to fail a series of [node heartbeat](https://kubernetes.io/docs/concepts/architecture/leases/#node-heart-beats) checks, and then you wait before you start the kubelet again, Kubernetes may begin to evict Pods from that Node. However, even though Pod evictions begin to happen, Kubernetes does not mark the individual containers in those Pods as `ready: false`. The Pod-level eviction happens after the control plane taints the node as `node.kubernetes.io/not-ready` (due to the failed heartbeats).
- In Kubernetes 1.37 you can opt in to a legacy behavior where the kubelet always modify the containers `ready` value, after a kubelet restart, to be false.
  
  This legacy behavior was the default for a long time, but caused issue for people using Kubernetes, especially in large scale deployments. Although the feature gate allows reverting to this legacy behavior temporarily, the Kubernetes project recommends that you file a bug report if you encounter problems. The `ChangeContainerStatusOnKubeletRestart` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#ChangeContainerStatusOnKubeletRestart) will be removed in the future.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
