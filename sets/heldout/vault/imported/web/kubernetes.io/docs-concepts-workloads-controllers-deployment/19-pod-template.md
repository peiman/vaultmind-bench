---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#19-pod-template.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-19-pod-template
type: reference
title: Deployments › Writing a Deployment Spec › Pod Template
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#19-pod-template
source_hash: d2bb391b9fb00c637b37288ced243a6e92099330833c4b637ec132eb523576d3
---
The `.spec.template` and `.spec.selector` are the only required fields of the `.spec`.

The `.spec.template` is a [Pod template](https://kubernetes.io/docs/concepts/workloads/pods/#pod-templates). It has exactly the same schema as a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/ "A Pod represents a set of running containers in your cluster."), except it is nested and does not have an `apiVersion` or `kind`.

In addition to required fields for a Pod, a Pod template in a Deployment must specify appropriate labels and an appropriate restart policy. For labels, make sure not to overlap with other controllers. See [selector](#selector).

Only a [`.spec.template.spec.restartPolicy`](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy) equal to `Always` is allowed, which is the default if not specified.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
