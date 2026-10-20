---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#17-status-for-pod-readiness.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-17-status-for-pod-readiness
type: reference
title: Pod Lifecycle › Pod conditions › Status for Pod readiness
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#17-status-for-pod-readiness
source_hash: df462bff379cd40b8a614c2e23c2298dd7344fb8b0c37339914babafbd6ed85b
---
The `kubectl patch` command does not support patching object status. To set these `status.conditions` for the Pod, applications and [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/ "A specialized controller used to manage a custom resource") should use the `PATCH` action. You can use a [Kubernetes client library](https://kubernetes.io/docs/reference/using-api/client-libraries/) to write code that sets custom Pod conditions for Pod readiness.

For a Pod that uses custom conditions, that Pod is evaluated to be ready **only** when both the following statements apply:

- All containers in the Pod are ready.
- All conditions specified in `readinessGates` are `True`.

When a Pod's containers are Ready but at least one custom condition is missing or `False`, the kubelet sets the Pod's [condition](#pod-conditions) to `ContainersReady`.

### Pod readiness to start containers

Feature state: Stable since Kubernetes v1.37

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
