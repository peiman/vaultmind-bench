---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#24-pod-termination-flow.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-24-pod-termination-flow
type: reference
title: Pod Lifecycle › Termination of Pods › Pod Termination Flow
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
source: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#24-pod-termination-flow
source_hash: 0654197feabd7d52d2dfb2cf13740ef7df6dcee2e42f92ffab266b4da275248a
---
Pod termination flow, illustrated with an example:

1. You use the `kubectl` tool to manually delete a specific Pod, with the default grace period (30 seconds).
2. The Pod in the API server is updated with the time beyond which the Pod is considered "dead" along with the grace period. If you use `kubectl describe` to check the Pod you're deleting, that Pod shows up as "Terminating". On the node where the Pod is running: as soon as the kubelet sees that a Pod has been marked as terminating (a graceful shutdown duration has been set), the kubelet begins the local Pod shutdown process.
   
   1. If one of the Pod's containers has defined a `preStop` [hook](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/) and the `terminationGracePeriodSeconds` in the Pod spec is not set to 0, the kubelet runs that hook inside of the container. The default `terminationGracePeriodSeconds` setting is 30 seconds.
      
      If the `preStop` hook is still running after the grace period expires, the kubelet requests a small, one-off grace period extension of 2 seconds.
   
   #### Note:
   
   If the `preStop` hook needs longer to complete than the default grace period allows, you must modify `terminationGracePeriodSeconds` to suit this.
   
   1. The kubelet triggers the container runtime to send a TERM signal to process 1 inside each container.
      
      There is [special ordering](#termination-with-sidecars) if the Pod has any [sidecar containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/ "An auxilliary container that stays running throughout the lifecycle of a Pod.") defined. Otherwise, the containers in the Pod receive the TERM signal at different times and in an arbitrary order. If the order of shutdowns matters, consider using a `preStop` hook to synchronize (or switch to using sidecar containers).
3. At the same time as the kubelet is starting graceful shutdown of the Pod, the control plane evaluates whether to remove that shutting-down Pod from EndpointSlice objects, where those objects represent a [Service](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.") with a configured [selector](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ "Allows users to filter a list of resources based on labels."). [ReplicaSets](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/ "ReplicaSet ensures that a specified number of Pod replicas are running at one time") and other workload resources no longer treat the shutting-down Pod as a valid, in-service replica.
   
   Pods that shut down slowly should not continue to serve regular traffic and should start terminating and finish processing open connections. Some applications need to go beyond finishing open connections and need more graceful termination, for example, session draining and completion.
   
   Any endpoints that represent the terminating Pods are not immediately removed from EndpointSlices, and a status indicating [terminating state](https://kubernetes.io/docs/concepts/services-networking/endpoint-slices/#conditions) is exposed from the EndpointSlice API. Terminating endpoints always have their `ready` status as `false` (for backward compatibility with versions before 1.26), so load balancers will not use it for regular traffic.
   
   If traffic draining on terminating Pod is needed, the actual readiness can be checked as a condition `serving`. You can find more details on how to implement connections draining in the tutorial [Pods And Endpoints Termination Flow](https://kubernetes.io/docs/tutorials/services/pods-and-endpoint-termination-flow/)
   
   []()
4. [The kubelet ensures the Pod is shut down and terminated]()
   
   1. [When the grace period expires, if there is still any container running in the Pod, the kubelet triggers forcible shutdown. The container runtime sends `SIGKILL` to any processes still running in any container in the Pod. The kubelet also cleans up a hidden `pause` container if that container runtime uses one.]()
   2. [The kubelet transitions the Pod into a terminal phase (`Failed` or `Succeeded` depending on the end state of its containers).]()
   3. [The kubelet triggers forcible removal of the Pod object from the API server, by setting grace period to 0 (immediate deletion).]()
   4. [The API server deletes the Pod's API object, which is then no longer visible from any client.]()

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-pods-pod-lifecycle]].
