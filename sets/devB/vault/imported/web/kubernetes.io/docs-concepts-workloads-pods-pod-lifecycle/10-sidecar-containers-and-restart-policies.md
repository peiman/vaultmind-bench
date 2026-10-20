---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#10-sidecar-containers-and-restart-policies.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-10-sidecar-containers-and-restart-policies
type: reference
title: 'Pod Lifecycle › How Pods handle problems with containers › Container restarts › Note: › Sidecar containers and restart policies'
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#10-sidecar-containers-and-restart-policies
source_hash: 866b808f59cee792902b329991ce179e9cc50fcb68c99f2fa0bc49729ad8a0f3
---
[Sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) have special restart behavior that differs from regular app containers:

- **Sidecar containers ignore Pod-level `restartPolicy`** : They use their own container-level `restartPolicy` field, which is always set to `Always`
- **Independent lifecycle**: Sidecar containers can restart independently of the main application container
- **Persistent operation**: Sidecar containers remain running throughout the Pod's lifetime to provide supporting services

**Example: Pod with sidecar container**

```
apiVersion: v1
kind: Pod
metadata:
  name: app-with-sidecar
spec:
  restartPolicy: OnFailure  # Applies to main container only
  initContainers:
  - name: logging-sidecar    # This is a sidecar container
    image: fluent/fluent-bit:1.8
    restartPolicy: Always    # Sidecar always restarts regardless of exit code
    # Provides logging services throughout Pod lifetime
  containers:
  - name: main-app          # This follows Pod-level restartPolicy
    image: nginx:1.14.2
    # Will only restart on failure (non-zero exit) due to Pod's OnFailure policy
```

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
