---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#25-revision-history-limit.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-25-revision-history-limit
type: reference
title: Deployments › Writing a Deployment Spec › Revision History Limit
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#25-revision-history-limit
source_hash: b89e8adc4f4fd5002d5cfdfcb9dd1d725cf2e17c7091f5a805f3c6b8299e68ec
---
A Deployment's revision history is stored in the ReplicaSets it controls.

`.spec.revisionHistoryLimit` is an optional field that specifies the number of old ReplicaSets to retain to allow rollback. These old ReplicaSets consume resources in `etcd` and crowd the output of `kubectl get rs`. The configuration of each Deployment revision is stored in its ReplicaSets; therefore, once an old ReplicaSet is deleted, you lose the ability to rollback to that revision of Deployment. By default, 10 old ReplicaSets will be kept, however its ideal value depends on the frequency and stability of new Deployments.

More specifically, setting this field to zero means that all old ReplicaSets with 0 replicas will be cleaned up. In this case, a new Deployment rollout cannot be undone, since its revision history is cleaned up.

### Paused

`.spec.paused` is an optional boolean field for pausing and resuming a Deployment. The only difference between a paused Deployment and one that is not paused, is that any changes into the PodTemplateSpec of the paused Deployment will not trigger new rollouts as long as it is paused. A Deployment is not paused by default when it is created.

## What's next

- Learn more about [Pods](https://kubernetes.io/docs/concepts/workloads/pods/).
- [Run a stateless application using a Deployment](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/).
- Read the [Deployment](https://kubernetes.io/docs/reference/kubernetes-api/apps/deployment-v1/) to understand the Deployment API.
- Read about [PodDisruptionBudget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/) and how you can use it to manage application availability during disruptions.
- Use kubectl to [create a Deployment](https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/).

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
