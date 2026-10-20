---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#02-pod-lifetime.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-02-pod-lifetime
type: reference
title: Pod Lifecycle › Pod lifetime
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#02-pod-lifetime
source_hash: 6743fb97ef46a1bd079ce1ca16766ab6940463890a98c441e3c0cf5a8460c3ba
---
While a Pod is running, the kubelet is able to restart containers to handle some kind of faults. Within a Pod, Kubernetes tracks different container [states](#container-states) and determines what action to take to make the Pod healthy again. This is done in a [polling loop](https://kubernetes.io/docs/reference/node/kubelet-sync-loop/) that periodically reconciles the desired state (a Pod spec) with the actual state of the running containers.

In the Kubernetes API, Pods have both a specification and an actual status. The status for a Pod object consists of a set of [Pod conditions](#pod-conditions). You can also inject [custom readiness information](#pod-readiness-gate) into the condition data for a Pod, if that is useful to your application.

Pods are only [scheduled](https://kubernetes.io/docs/concepts/scheduling-eviction/) once in their lifetime; assigning a Pod to a specific node is called *binding*, and the process of selecting which node to use is called *scheduling*. Once a Pod has been scheduled and is bound to a node, Kubernetes tries to run that Pod on the node. The Pod runs on that node until it stops, or until the Pod is [terminated](#pod-termination); if Kubernetes isn't able to start the Pod on the selected node (for example, if the node crashes before the Pod starts), then that particular Pod never starts.

You can use [Pod Scheduling Readiness](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/) to delay scheduling for a Pod until all its *scheduling gates* are removed. For example, you might want to define a set of Pods but only trigger scheduling once all the Pods have been created.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
