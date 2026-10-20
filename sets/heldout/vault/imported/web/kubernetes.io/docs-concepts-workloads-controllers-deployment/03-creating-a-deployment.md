---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#03-creating-a-deployment.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-03-creating-a-deployment
type: reference
title: Deployments › Creating a Deployment
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#03-creating-a-deployment
source_hash: 8e71bc26684020193156617150525ab73920013da5b47a2b2f1fdfe53de3a044
---
The following is an example of a Deployment. It creates a ReplicaSet to bring up three `nginx` Pods:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

In this example:

- A Deployment named `nginx-deployment` is created, indicated by the `.metadata.name` field. This name will become the basis for the ReplicaSets and Pods which are created later. See [Writing a Deployment Spec](#writing-a-deployment-spec) for more details.
- The Deployment creates a ReplicaSet that creates three replicated Pods, indicated by the `.spec.replicas` field.
- The `.spec.selector` field defines how the created ReplicaSet finds which Pods to manage. In this case, you select a label that is defined in the Pod template (`app: nginx`). However, more sophisticated selection rules are possible, as long as the Pod template itself satisfies the rule.
  
  #### Note:
  
  The `.spec.selector.matchLabels` field is a map of {key,value} pairs. A single {key,value} in the `matchLabels` map is equivalent to an element of `matchExpressions`, whose `key` field is "key", the `operator` is "In", and the `values` array contains only "value". All of the requirements, from both `matchLabels` and `matchExpressions`, must be satisfied in order to match.
- The `.spec.template` field contains the following sub-fields:
  
  - The Pods are labeled `app: nginx`using the `.metadata.labels` field.
  - The Pod template's specification, or `.spec` field, indicates that the Pods run one container, `nginx`, which runs the `nginx` [Docker Hub](https://hub.docker.com/) image at version 1.14.2.
  - Create one container and name it `nginx` using the `.spec.containers[0].name` field.

Before you begin, make sure your Kubernetes cluster is up and running. Follow the steps given below to create the above Deployment:

1. Create the Deployment by running the following command:
   
   ```
   kubectl apply -f https://k8s.io/examples/controllers/nginx-deployment.yaml
   ```
2. Run `kubectl get deployments` to check if the Deployment was created.
   
   If the Deployment is still being created, the output is similar to the following:
   
   ```
   NAME               READY   UP-TO-DATE   AVAILABLE   AGE
   nginx-deployment   0/3     0            0           1s
   ```
   
   When you inspect the Deployments in your cluster, the following fields are displayed:
   
   - `NAME` lists the names of the Deployments in the namespace.
   - `READY` displays how many replicas of the application are available to your users. It follows the pattern ready/desired.
   - `UP-TO-DATE` displays the number of replicas that have been updated to achieve the desired state.
   - `AVAILABLE` displays how many replicas of the application are available to your users.
   - `AGE` displays the amount of time that the application has been running.
   
   Notice how the number of desired replicas is 3 according to `.spec.replicas` field.
3. To see the Deployment rollout status, run `kubectl rollout status deployment/nginx-deployment`.
   
   The output is similar to:
   
   ```
   Waiting for rollout to finish: 2 out of 3 new replicas have been updated...
   deployment "nginx-deployment" successfully rolled out
   ```
4. Run the `kubectl get deployments` again a few seconds later. The output is similar to this:
   
   ```
   NAME               READY   UP-TO-DATE   AVAILABLE   AGE
   nginx-deployment   3/3     3            3           18s
   ```
   
   Notice that the Deployment has created all three replicas, and all replicas are up-to-date (they contain the latest Pod template) and available.
5. To see the ReplicaSet (`rs`) created by the Deployment, run `kubectl get rs`. The output is similar to this:
   
   ```
   NAME                          DESIRED   CURRENT   READY   AGE
   nginx-deployment-75675f5897   3         3         3       18s
   ```
   
   ReplicaSet output shows the following fields:
   
   - `NAME` lists the names of the ReplicaSets in the namespace.
   - `DESIRED` displays the desired number of *replicas* of the application, which you define when you create the Deployment. This is the *desired state*.
   - `CURRENT` displays how many replicas are currently running.
   - `READY` displays how many replicas of the application are available to your users.
   - `AGE` displays the amount of time that the application has been running.
   
   Notice that the name of the ReplicaSet is always formatted as `[DEPLOYMENT-NAME]-[HASH]`. This name will become the basis for the Pods which are created.
   
   The `HASH` string is the same as the `pod-template-hash` label on the ReplicaSet.
6. To see the labels automatically generated for each Pod, run `kubectl get pods --show-labels`. The output is similar to:
   
   ```
   NAME                                READY     STATUS    RESTARTS   AGE       LABELS
   nginx-deployment-75675f5897-7ci7o   1/1       Running   0          18s       app=nginx,pod-template-hash=75675f5897
   nginx-deployment-75675f5897-kzszj   1/1       Running   0          18s       app=nginx,pod-template-hash=75675f5897
   nginx-deployment-75675f5897-qqcnn   1/1       Running   0          18s       app=nginx,pod-template-hash=75675f5897
   ```
   
   The created ReplicaSet ensures that there are three `nginx` Pods.

### Note:

You must specify an appropriate selector and Pod template labels in a Deployment (in this case, `app: nginx`).

Do not overlap labels or selectors with other controllers (including other Deployments and StatefulSets). Kubernetes doesn't stop you from overlapping, and if multiple controllers have overlapping selectors those controllers might conflict and behave unexpectedly.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
