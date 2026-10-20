---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#12-individual-container-restart-policy-and-rules.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-12-individual-container-restart-policy-and-rules
type: reference
title: Pod Lifecycle › How Pods handle problems with containers › Container restarts › Individual container restart policy and rules
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#12-individual-container-restart-policy-and-rules
source_hash: d9711a35c08b80df6b88ce709fba638bc3cfc9117b16c08754b5738a039ab557
---
Feature state: Beta since Kubernetes v1.35; enabled by default

If your cluster has the feature gate `ContainerRestartRules` enabled, you can specify `restartPolicy` and `restartPolicyRules` on *individual containers* to override the Pod restart policy. Container restart policy and rules applies to [app containers](https://kubernetes.io/docs/reference/glossary/?all=true#term-app-container "A container used to run part of a workload. Compare with init container.") in the Pod and to regular [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/).

A Kubernetes-native [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) has its container-level `restartPolicy` set to `Always`.

The container restarts will follow the same exponential backoff as pod restart policy described above. Supported container restart policies:

- `Always`: Automatically restarts the container after any termination.
- `OnFailure`: Only restarts the container if it exits with an error (non-zero exit status).
- `Never`: Does not automatically restart the terminated container.

Additionally, *individual containers* can specify `restartPolicyRules`. If the `restartPolicyRules` field is specified, then container `restartPolicy` **must** also be specified. The `restartPolicyRules` define a list of rules to apply on container exit. Each rule will consist of a condition and an action. The supported condition is `exitCodes`, which compares the exit code of the container with a list of given values. The supported action is `Restart`, which means the container will be restarted. The rules will be evaluated in order. On the first match, the action will be applied. If none of the rules’ conditions matched, Kubernetes fallback to container’s configured `restartPolicy`.

For example, a Pod with OnFailure restart policy that have a `try-once` container. This allows Pod to only restart certain containers:

```
apiVersion: v1
kind: Pod
metadata:
  name: on-failure-pod
spec:
  restartPolicy: OnFailure
  containers:
  - name: try-once-container    # This container will run only once because the restartPolicy is Never.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Only running once" && sleep 10 && exit 1']
    restartPolicy: Never     
  - name: on-failure-container  # This container will be restarted on failure.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Keep restarting" && sleep 1800 && exit 1']
```

A Pod with `Always` restart policy with an init container that only execute once. If the init container fails, the Pod fails. This allows the Pod to fail if the initialization failed, but also keep running once the initialization succeeds:

```
apiVersion: v1
kind: Pod
metadata:
  name: fail-pod-if-init-fails
spec:
  restartPolicy: Always
  initContainers:
  - name: init-once      # This init container will only try once. If it fails, the pod will fail.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'echo "Failing initialization" && sleep 10 && exit 1']
    restartPolicy: Never
  containers:
  - name: main-container # This container will always be restarted once initialization succeeds.
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'sleep 1800 && exit 0']
```

A Pod with Never restart policy with a container that ignores and restarts on specific exit codes. This is useful to differentiate between restartable errors and non-restartable errors:

```
apiVersion: v1
kind: Pod
metadata:
  name: restart-on-exit-codes
spec:
  restartPolicy: Never
  containers:
  - name: restart-on-exit-codes
    image: registry.k8s.io/busybox:1.27.2
    command: ['sh', '-c', 'sleep 60 && exit 0']
    restartPolicy: Never     # Container restart policy must be specified if rules are specified
    restartPolicyRules:      # Only restart the container if it exits with code 42
    - action: Restart
      exitCodes:
        operator: In
        values: [42]
```

Restart rules can be used for many more advanced lifecycle management scenarios. Note, restart rules are affected by the same inconsistencies as the regular restart policy. The kubelet restarts, container runtime garbage collection, intermitted connectivity issues with the control plane may cause the state loss and containers may be re-run even when you expect a container not to be restarted.

#### Restart All Containers

Feature state: Beta since Kubernetes v1.36; enabled by default

If your cluster has the feature gate `RestartAllContainersOnContainerExits` enabled, you can specify `RestartAllContainers` as an action in `restartPolicyRules` at container level. When a container's exit matches a rule with this action, the entire Pod is terminated and restarted in-place.

This "in-place" restart offers a more efficient way to reset a Pod's state compared to full deletion and recreation. This is especially valuable for workloads where rescheduling is costly, such as batch jobs or AI/ML training tasks.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
