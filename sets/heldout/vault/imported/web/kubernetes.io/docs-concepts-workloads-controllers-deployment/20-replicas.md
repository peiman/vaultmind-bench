---
# Imported by `vaultmind import` from https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#20-replicas.
# The page is the source: re-run the import to refresh it.
id: imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-20-replicas
type: reference
title: Deployments › Writing a Deployment Spec › Replicas
url: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
source: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#20-replicas
source_hash: 157e42a89953f81de1f111a74f59c39e2c8a76b5bd249a359b84819cfd0c73bb
---
`.spec.replicas` is an optional field that specifies the number of desired Pods. It defaults to 1.

Should you manually scale a Deployment, example via `kubectl scale deployment deployment --replicas=X`, and then you update that Deployment based on a manifest (for example: by running `kubectl apply -f deployment.yaml`), then applying that manifest overwrites the manual scaling that you previously did.

If a [HorizontalPodAutoscaler](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) (or any similar API for horizontal scaling) is managing scaling for a Deployment, don't set `.spec.replicas`.

Instead, allow the Kubernetes [control plane](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane "The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.") to manage the `.spec.replicas` field automatically.

Part of [[imported/web/kubernetes.io/docs-concepts-workloads-controllers-deployment]].
