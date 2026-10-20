---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#06-container-states.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-06-container-states
type: reference
title: Pod Lifecycle › Container states
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#06-container-states
source_hash: 93f3d8cab0e07c8c09abede1258a75deb596eeedf5fc7482d2e1f8e2c295cc8c
---
As well as the [phase](#pod-phase) of the Pod overall, Kubernetes tracks the state of each container inside a Pod. You can use [container lifecycle hooks](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) to trigger events to run at certain points in a container's lifecycle.

Once the [scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/ "Control plane component that watches for newly created pods with no assigned node, and selects a node for them to run on.") assigns a Pod to a Node, the kubelet starts creating containers for that Pod using a [container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes "The container runtime is the software that is responsible for running containers."). There are three possible container states: `Waiting`, `Running`, and `Terminated`.

To check the state of a Pod's containers, you can use `kubectl describe pod <name-of-pod>`. The output shows the state for each container within that Pod.

Each state has a specific meaning:

### `Waiting`

If a container is not in either the `Running` or `Terminated` state, it is `Waiting`. A container in the `Waiting` state is still running the operations it requires in order to complete start up: for example, pulling the container image from a container image registry, or applying [Secret](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.") data. When you use `kubectl` to query a Pod with a container that is `Waiting`, you also see a Reason field to summarize why the container is in that state.

### `Running`

The `Running` status indicates that a container is executing without issues. If there was a `postStart` hook configured, it has already executed and finished. When you use `kubectl` to query a Pod with a container that is `Running`, you also see information about when the container entered the `Running` state.

### `Terminated`

A container in the `Terminated` state began execution and then either ran to completion or failed for some reason. When you use `kubectl` to query a Pod with a container that is `Terminated`, you see a reason, an exit code, and the start and finish time for that container's period of execution.

If a container has a `preStop` hook configured, this hook runs before the container enters the `Terminated` state.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
