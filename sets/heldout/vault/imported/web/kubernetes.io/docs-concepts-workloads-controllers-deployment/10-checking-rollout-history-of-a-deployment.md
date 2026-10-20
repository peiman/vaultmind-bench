---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#10-checking-rollout-history-of-a-deployment.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-10-checking-rollout-history-of-a-deployment
type: reference
title: Deployments › Rolling Back a Deployment › Checking Rollout History of a Deployment
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#10-checking-rollout-history-of-a-deployment
source_hash: a85e31051876e8f48473a66679880c8a5c4af44f8ba1cc123c5daf7ff890a4ce
---
Follow the steps given below to check the rollout history:

1. First, check the revisions of this Deployment:
   
   ```
   kubectl rollout history deployment/nginx-deployment
   ```
   
   The output is similar to this:
   
   ```
   deployments "nginx-deployment"
   REVISION    CHANGE-CAUSE
   1           <none>
   2           <none>
   3           <none>
   ```
   
   `CHANGE-CAUSE` is copied from the Deployment annotation `kubernetes.io/change-cause` to its revisions upon creation. You can specify the`CHANGE-CAUSE` message by:
   
   - Annotating the Deployment with `kubectl annotate deployment/nginx-deployment kubernetes.io/change-cause="image updated to 1.16.1"`
   - Manually editing the manifest of the resource.
   - Using tooling that sets the annotation automatically.
   
   #### Note:
   
   In older versions of Kubernetes, you could use the `--record` flag with kubectl commands to automatically populate the `CHANGE-CAUSE` field. This flag is deprecated and will be removed in a future release.
2. To see the details of each revision, run:
   
   ```
   kubectl rollout history deployment/nginx-deployment --revision=2
   ```
   
   The output is similar to this:
   
   ```
   deployments "nginx-deployment" revision 2
     Labels:       app=nginx
             pod-template-hash=1159050644
     Containers:
      nginx:
       Image:      nginx:1.16.1
       Port:       80/TCP
        QoS Tier:
           cpu:      BestEffort
           memory:   BestEffort
       Environment Variables:      <none>
     No volumes.
   ```

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
