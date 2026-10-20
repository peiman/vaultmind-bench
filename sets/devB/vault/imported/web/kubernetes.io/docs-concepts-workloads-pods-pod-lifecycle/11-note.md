---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#11-note.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-11-note
type: reference
title: 'Pod Lifecycle › How Pods handle problems with containers › Container restarts › Note:'
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#11-note
source_hash: f8dc0a6d4ad448d42167015c797e098f00a8af5fb2c1f50426aa7e2b1454f91f
---
While the main application container follows the Pod's `restartPolicy: OnFailure`, the sidecar container will restart regardless of its exit code because sidecar containers always have `restartPolicy: Always` at the container level.

When the kubelet is handling container restarts according to the configured restart policy, that only applies to restarts that make replacement containers inside the same Pod and running on the same node. After containers in a Pod exit, the kubelet restarts them with an exponential backoff delay (10s, 20s, 40s, …), that is capped at 300 seconds (5 minutes). Once a container has executed for 10 minutes without any problems, the kubelet resets the restart backoff timer for that container. [Sidecar containers and Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/#sidecar-containers-and-pod-lifecycle) explains the behaviour of `init containers` when specify `restartPolicy` field on it.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
