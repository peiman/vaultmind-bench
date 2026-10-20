---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#04-pod-phase.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-04-pod-phase
type: reference
title: Pod Lifecycle › Pod phase
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#04-pod-phase
source_hash: 6ad51bdac2cd9e26c6a409e3dd596d094398aa6cc8cdb378ab539fe5a8a2ca14
---
A Pod's `status` field is a [PodStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.37/#podstatus-v1-core) object, which has a `phase` field.

The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The phase is not intended to be a comprehensive rollup of observations of container or Pod state, nor is it intended to be a comprehensive state machine.

The number and meanings of Pod phase values are tightly guarded. Other than what is documented here, nothing should be assumed about Pods that have a given `phase` value.

Here are the possible values for `phase`:

ValueDescription`Pending`The Pod has been accepted by the Kubernetes cluster, but one or more of the containers has not been set up and made ready to run. This includes time a Pod spends waiting to be scheduled as well as the time spent downloading container images over the network.`Running`The Pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting.`Succeeded`All containers in the Pod have terminated in success, and will not be restarted.`Failed`All containers in the Pod have terminated, and at least one container has terminated in failure. That is, the container either exited with non-zero status or was terminated by the system, and is not set for automatic restarting.`Unknown`For some reason the state of the Pod could not be obtained. This phase typically occurs due to an error in communicating with the node where the Pod should be running.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
