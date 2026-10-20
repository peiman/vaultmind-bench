---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#14-configurable-container-restart-delay.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-14-configurable-container-restart-delay
type: reference
title: Pod Lifecycle › How Pods handle problems with containers › Configurable container restart delay
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#14-configurable-container-restart-delay
source_hash: 42974f15df58e61265cfd94bd05c9546a8be45d2a2a6a772b014f0dfad937d57
---
Feature state: Beta since Kubernetes v1.35; enabled by default

With the feature gate `KubeletCrashLoopBackOffMax` enabled, you can reconfigure the maximum delay between container start retries from the default of 300s (5 minutes). This configuration is set per node using kubelet configuration. In your [kubelet configuration](https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/), under `crashLoopBackOff` set the `maxContainerRestartPeriod` field between `"1s"` and `"300s"`. As described above in [Container restart policy](#restart-policy), delays on that node will still start at 10s and increase exponentially by 2x each restart, but will now be capped at your configured maximum. If the `maxContainerRestartPeriod` you configure is less than the default initial value of 10s, the initial delay will instead be set to the configured maximum.

See the following kubelet configuration examples:

```
# container restart delays will start at 10s, increasing
# 2x each time they are restarted, to a maximum of 100s
kind: KubeletConfiguration
crashLoopBackOff:
    maxContainerRestartPeriod: "100s"
```

```
# delays between container restarts will always be 2s
kind: KubeletConfiguration
crashLoopBackOff:
    maxContainerRestartPeriod: "2s"
```

If you use this feature along with the alpha feature `ReduceDefaultCrashLoopBackOffDecay` (described above), your cluster defaults for initial backoff and maximum backoff will no longer be 10s and 300s, but 1s and 60s. Per node configuration takes precedence over the defaults set by `ReduceDefaultCrashLoopBackOffDecay`, even if this would result in a node having a longer maximum backoff than other nodes in the cluster.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
