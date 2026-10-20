---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#21-container-probes.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-21-container-probes
type: reference
title: Pod Lifecycle › Container probes
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#21-container-probes
source_hash: 21327e05aeefdfb098d8e13fab85f3d5fac2b0105224fe9eba4e05e3c745aa54
---
Kubernetes lets you define *probes* to continuously monitor the health of containers in a Pod. A probe is a diagnostic performed periodically by the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet "An agent that runs on each node in the cluster. It makes sure that containers are running in a pod.") on a container. To perform a diagnostic, the kubelet either executes code within the container or makes a network request.

Based on the probe results, Kubernetes can restart unhealthy containers or stop sending traffic to containers that are not ready.

The kubelet can optionally perform and react to three kinds of probes on running containers, each serving a different purpose. For probe mechanisms (`exec`, `grpc`, `httpGet`, `tcpSocket`), configuration fields, and detailed usage guidance, see [Liveness, Readiness, and Startup Probes](https://kubernetes.io/docs/concepts/workloads/pods/probes/).

### Startup probe

Startup probes verify whether the application within a container is started. If a startup probe is configured, Kubernetes does not execute liveness or readiness probes until the startup probe succeeds, allowing the application time to finish its initialization.

This type of probe is only executed at startup, unlike liveness and readiness probes, which are run periodically.

If the startup probe fails, the kubelet kills the container, and the container is subjected to its [restart policy](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy).

### Liveness probe

Liveness probes determine when to restart a container. For example, liveness probes could catch a deadlock, where an application is running, but unable to make progress. Restarting a container in such a state can help to make the application more available despite bugs.

If a container fails its liveness probe more times than the configured tolerance, the kubelet restarts that container. Liveness probes do not wait for readiness probes to succeed. If you want to wait before executing a liveness probe, you can either define `initialDelaySeconds` or use a startup probe.

### Readiness probe

Readiness probes determine when a container is ready to accept traffic. This is useful when waiting for an application to perform time-consuming initial tasks, such as establishing network connections, loading files, and warming caches. Readiness probes can also be useful later in the container's lifecycle, for example, when recovering from temporary faults or overloads.

If the readiness probe returns a failed state, the [EndpointSlice](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/ "EndpointSlices track the IP addresses of Pods for Services.") controller removes the Pod's IP address from the EndpointSlices of all Services that match the Pod.

Readiness probes run on the container during its whole lifecycle.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
