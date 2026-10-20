---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#14-complete-deployment.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-14-complete-deployment
type: reference
title: Deployments › Deployment status › Complete Deployment
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#14-complete-deployment
source_hash: 238bc680b826c4c5e98619cf72491817b2fa98d5bfed96b87ddd3d9e727ef82e
---
Kubernetes marks a Deployment as *complete* when it has the following characteristics:

- All of the replicas associated with the Deployment have been updated to the latest version you've specified, meaning any updates you've requested have been completed.
- All of the replicas associated with the Deployment are available.
- No old replicas for the Deployment are running.

When the rollout becomes “complete”, the Deployment controller sets a condition with the following attributes to the Deployment's `.status.conditions`:

- `type: Progressing`
- `status: "True"`
- `reason: NewReplicaSetAvailable`

This `Progressing` condition will retain a status value of `"True"` until a new rollout is initiated. The condition holds even when availability of replicas changes (which does instead affect the `Available` condition).

You can check if a Deployment has completed by using `kubectl rollout status`. If the rollout completed successfully, `kubectl rollout status` returns a zero exit code.

```
kubectl rollout status deployment/nginx-deployment
```

The output is similar to this:

```
Waiting for rollout to finish: 2 of 3 updated replicas are available...
deployment "nginx-deployment" successfully rolled out
```

and the exit status from `kubectl rollout` is 0 (success):

```
echo $?
```

```
0
```

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
