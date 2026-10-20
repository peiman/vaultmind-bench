---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#18-note.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-18-note
type: reference
title: 'Pod Lifecycle › Pod conditions › Pod readiness to start containers › Note:'
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#18-note
source_hash: b389142abb6cc3e4fe69ba6867a9744580e233d831ed9eaf9b519b52f2576aca
---
During its early development, this condition was named `PodHasNetwork`.

After a Pod gets scheduled on a node, it needs to be admitted by the kubelet and to have any required storage volumes mounted. Once these phases are complete, the kubelet works with a container runtime (using [Container Runtime Interface (CRI)](https://kubernetes.io/docs/concepts/architecture/cri "Protocol for communication between the kubelet and the local container runtime.")) to set up a runtime sandbox and configure networking for the Pod. If the Pod uses [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/), those resources are also allocated during this phase. The `PodReadyToStartContainers` condition is added to the `status.conditions` field of a Pod.

The condition is set to `False` by the kubelet when it detects a Pod does not have a runtime sandbox with networking configured. This occurs in the following scenarios:

- Early in the lifecycle of the Pod, when the kubelet has not yet begun to set up a sandbox for the Pod using the container runtime.
- Later in the lifecycle of the Pod, when the Pod sandbox has been destroyed due to either:
  
  - the node rebooting, without the Pod getting evicted
  - for container runtimes that use virtual machines for isolation, the Pod sandbox virtual machine rebooting, which then requires creating a new sandbox and fresh container network configuration.

After sandbox creation, network configuration, volume mounting, and (if requested) dynamic resource allocation are complete, the kubelet sets the `PodReadyToStartContainers` condition to `True`. Image pulling and container creation occur after this point.

For a Pod with init containers, the kubelet sets the `Initialized` condition to `True` after the init containers have successfully completed (which happens after successful sandbox creation and network configuration by the runtime plugin). For a Pod without init containers, the kubelet sets the `Initialized` condition to `True` before sandbox creation and network configuration starts.

## Resizing Pods

Feature state: Stable since Kubernetes v1.35

More information about this feature

This is a stable feature in Kubernetes, and has been since version v1.35. It was first available in the v1.27 release. You can no longer disable or opt out of this feature or behavior (it is locked); if you explicitly set a value for the associated feature gate `InPlacePodVerticalScaling`, Kubernetes ignores it but does not report any error.

Feature state: Beta since Kubernetes v1.36; enabled by default

Kubernetes supports changing the CPU and memory resources allocated to Pods after they are created. (For other infrastructure resources, you would need to use different techniques specific to those resources.) There are two main approaches to resizing CPU and memory:

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
