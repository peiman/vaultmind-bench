---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#20-resizing-by-launching-replacement-pods.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-20-resizing-by-launching-replacement-pods
type: reference
title: Pod Lifecycle › Resizing Pods › Resizing by launching replacement Pods
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#20-resizing-by-launching-replacement-pods
source_hash: 77e73627a81b87f22ea6a2af6e34460abdfadd48462e0e097c3e5e4b98d86de4
---
The more cloud native approach to changing a Pod's resources is through the workload resource that manages it (such as a Deployment or StatefulSet). When you update the resource specifications in the Pod template, the workload's controller creates new Pods with the updated resources and terminates the old Pods according to its update strategy.

This approach:

- Works with any Kubernetes version.
- Can change any Pod specification, not just resources.
- Results in Pod replacement, so you should design your workload to handle [planned disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/). Consider using a [PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) to control availability.
- Requires that your Pods are managed by a workload resource.

You can also use a [VerticalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) to automatically manage Pod resource recommendations and updates.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
