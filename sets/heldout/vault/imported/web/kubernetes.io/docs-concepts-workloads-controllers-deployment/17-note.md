---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#17-note.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-17-note
type: reference
title: 'Deployments › Clean up Policy › Note:'
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#17-note
source_hash: 4e70bff75eb13c0187092621edf50cacb332b6ace3339bf79635a50700dfe4d5
---
Explicitly setting this field to 0, will result in cleaning up all the history of your Deployment thus that Deployment will not be able to roll back.

The cleanup only starts **after** a Deployment reaches a [complete state](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#complete-deployment). If you set `.spec.revisionHistoryLimit` to 0, any rollout nonetheless triggers creation of a new ReplicaSet before Kubernetes removes the old one.

Even with a non-zero revision history limit, you can have more ReplicaSets than the limit you configure. For example, if pods are crash looping, and there are multiple rolling updates events triggered over time, you might end up with more ReplicaSets than the `.spec.revisionHistoryLimit` because the Deployment never reaches a complete state.

## Canary deployments

If you want to roll out releases to a subset of users or servers using the Deployment, you can create multiple Deployments, one for each release, following the canary pattern described in [managing resources](https://kubernetes.io/docs/concepts/workloads/management/#canary-deployments).

To learn what's involved, follow the [Deploy a Release Using a Canary Deployment](https://kubernetes.io/docs/tutorials/stateless-application/canary-deployment/) tutorial.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
