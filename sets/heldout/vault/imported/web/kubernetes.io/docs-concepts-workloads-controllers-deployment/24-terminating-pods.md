---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#24-terminating-pods.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-24-terminating-pods
type: reference
title: Deployments › Writing a Deployment Spec › Terminating Pods
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#24-terminating-pods
source_hash: 49a3f1f7899a3521934535bb47b9040ce05de15d9eeba8ced3f6f37e4d84ef36
---
Feature state: Beta since Kubernetes v1.35; enabled by default

You can see the terminating pods only if the `DeploymentReplicaSetTerminatingReplicas` [feature gate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) is enabled on the [API server](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) and on the [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)

Pods that become terminating due to deletion or scale down may take a long time to terminate, and may consume additional resources during that period. As a result, the total number of all pods can temporarily exceed `.spec.replicas`. Terminating pods can be tracked using the `.status.terminatingReplicas` field of the Deployment.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
