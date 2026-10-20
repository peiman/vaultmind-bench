---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#23-defining-custom-stop-signals.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-23-defining-custom-stop-signals
type: reference
title: Pod Lifecycle › Termination of Pods › Defining custom stop signals
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#23-defining-custom-stop-signals
source_hash: d3b52d282834d245b0c9b2d94594c369475e82145b4865fcb5f62a76f0d0ba41
---
Feature state: Alpha since Kubernetes v1.33; disabled by default

If the `ContainerStopSignals` feature gate is enabled, you can configure a custom stop signal for your containers from the container Lifecycle. We require the Pod's `spec.os.name` field to be present as a requirement for defining stop signals in the container lifecycle. The list of signals that are valid depends on the OS the Pod is scheduled to. For Pods scheduled to Windows nodes, we only support SIGTERM and SIGKILL as valid signals.

Here is an example Pod spec defining a custom stop signal:

```
spec:
  os:
    name: linux
  containers:
    - name: my-container
      image: container-image:latest
      lifecycle:
        stopSignal: SIGUSR1
```

If a stop signal is defined in the lifecycle, this will override the signal defined in the container image. If no stop signal is defined in the container spec, the container would fall back to the default behavior.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
