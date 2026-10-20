---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#02-use-case.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-02-use-case
type: reference
title: Deployments › Use Case
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#02-use-case
source_hash: bb92ca5d77a568771b30de322b1f0a0b65aa43a8d437b1d731ad9e41d525de32
---
The following are typical use cases for Deployments:

- [Create a Deployment to rollout a ReplicaSet](#creating-a-deployment). The ReplicaSet creates Pods in the background. Check the status of the rollout to see if it succeeds or not.
- [Declare the new state of the Pods](#updating-a-deployment) by updating the PodTemplateSpec of the Deployment. A new ReplicaSet is created, and the Deployment gradually scales it up while scaling down the old ReplicaSet, ensuring Pods are replaced at a controlled rate. Each new ReplicaSet updates the revision of the Deployment.
- [Rollback to an earlier Deployment revision](#rolling-back-a-deployment) if the current state of the Deployment is not stable. Each rollback updates the revision of the Deployment.
- [Scale up the Deployment to facilitate more load](#scaling-a-deployment).
- [Pause the rollout of a Deployment](#pausing-and-resuming-a-deployment) to apply multiple fixes to its PodTemplateSpec and then resume it to start a new rollout.
- [Use the status of the Deployment](#deployment-status) as an indicator that a rollout has stuck.
- [Clean up older ReplicaSets](#clean-up-policy) that you don't need anymore.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
