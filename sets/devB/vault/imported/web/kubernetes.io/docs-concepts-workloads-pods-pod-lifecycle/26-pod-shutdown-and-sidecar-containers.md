---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#26-pod-shutdown-and-sidecar-containers.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-26-pod-shutdown-and-sidecar-containers
type: reference
title: Pod Lifecycle › Termination of Pods › Pod shutdown and sidecar containers
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#26-pod-shutdown-and-sidecar-containers
source_hash: 1a2271286bcfa667acc327d57bde6b76abaf3cf4c2923523ffc78c7ced832980
---
If your Pod includes one or more [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) (init containers with an `Always` restart policy), the kubelet will delay sending the TERM signal to these sidecar containers until the last main container has fully terminated. The sidecar containers will be terminated in the reverse order they are defined in the Pod spec. This ensures that sidecar containers continue serving the other containers in the Pod until they are no longer needed.

This means that slow termination of a main container will also delay the termination of the sidecar containers. If the grace period expires before the termination process is complete, the Pod may enter [forced termination](#pod-termination-beyond-grace-period). In this case, all remaining containers in the Pod will be terminated simultaneously with a short grace period.

Similarly, if the Pod has a `preStop` hook that exceeds the termination grace period, emergency termination may occur. In general, if you have used `preStop` hooks to control the termination order without sidecar containers, you can now remove them and allow the kubelet to manage sidecar termination automatically.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
