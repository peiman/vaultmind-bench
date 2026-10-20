---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#01-introduction.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-01-introduction
type: reference
title: Pod Lifecycle › Introduction
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#01-introduction
source_hash: c62d3c9f6045e0102b996da647d46b8d1daa30f96740c5d19c83f0b0a0bb9aa3
---
This page describes the lifecycle of a Pod. Pods follow a defined lifecycle, starting in the `Pending` [phase](#pod-phase), moving through `Running` if at least one of its primary containers starts OK, and then through either the `Succeeded` or `Failed` phases depending on whether any container in the Pod terminated in failure.

While a Pod runs, the kubelet manages containers and translates the Pod's spec for the container runtime. The kubelet also manages executing [probes](#container-probes) that track the health of your application.

Like individual application containers, Pods are considered to be relatively ephemeral (rather than durable) entities. Pods are created, assigned a unique ID ([UID](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids)), and scheduled to run on nodes where they remain until termination (according to restart policy) or deletion. If a [Node](https://kubernetes.io/docs/concepts/architecture/nodes/ "A node is a worker machine in Kubernetes.") dies, the Pods running on (or scheduled to run on) that node are [marked for deletion](#pod-garbage-collection). The control plane marks the Pods for removal after a timeout period.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
