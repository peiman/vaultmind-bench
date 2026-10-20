# Scores

Set: `sets/devB`

Token method: `tiktoken-cl100k_base`

| system | Hit@1 | Hit@3 | mean tokens | median tokens | mean seconds |
|---|---:|---:|---:|---:|---:|
| vm | 38/50 | 48/50 | 2911.3 | 2870.0 | 1.381 |
| bm25 | 36/50 | 44/50 | 2719.2 | 2526.5 | 0.005 |
| rg | 30/50 | 45/50 | 3200.9 | 3402.0 | 0.084 |
| agent-rg | 41/50 | 48/50 | 6773.9 | 6547.5 | 6.505 |
| agent-vm | 49/50 | 49/50 | 6409.7 | 6526.5 | 6.839 |
| whole | 0/50 | 0/50 | 28632.0 | 19834.0 | 0.004 |

whole fits in 200k tokens: 50/50

## Misses

A miss is a question whose labelled section is not at rank 3 or better.
Rank is 1-based in `ranked`; empty means the id was not in the list.

### vm

- `devB-nginx-07` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-10-directives`)
- `devB-nginx-08` rank 4 (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-11-directives`)

### bm25

- `devB-redis-07` rank 14 (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-23-failure-detection`)
- `devB-kubernetes-09` rank 5 (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-27-garbage-collection-of-pods`)
- `devB-http-caching-02` rank 6 (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-07-3-1-storing-header-and-trailer-fields`)
- `devB-git-config-04` rank 20 (expected `imported-web-git-scm-com-docs-git-config-2-51-1-02-syntax`)
- `devB-git-config-06` rank 4 (expected `imported-web-git-scm-com-docs-git-config-2-51-1-03-includes`)
- `devB-python-logging-01` rank 4 (expected `imported-web-docs-python-org-3-13-library-logging-02-logger-objects`)

### rg

- `devB-redis-07` rank 12 (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-23-failure-detection`)
- `devB-http-caching-07` rank 9 (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-17-4-2-4-serving-stale-responses`)
- `devB-git-config-02` rank 8 (expected `imported-web-git-scm-com-docs-git-config-2-51-1-03-includes`)
- `devB-git-config-04` rank 33 (expected `imported-web-git-scm-com-docs-git-config-2-51-1-02-syntax`)
- `devB-git-config-06` rank 33 (expected `imported-web-git-scm-com-docs-git-config-2-51-1-03-includes`)

### agent-rg

- `devB-redis-07` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-23-failure-detection`)
- `devB-http-caching-03` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-11-4-constructing-responses-from-caches`)

### agent-vm

- `devB-nginx-05` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-09-directives`)

### whole

- `devB-redis-01` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-03-write-safety`)
- `devB-redis-02` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-08-hash-tags`)
- `devB-redis-03` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-14-moved-redirection`)
- `devB-redis-04` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-15-live-reconfiguration`)
- `devB-redis-05` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-17-ask-redirection`)
- `devB-redis-06` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-18-client-connections-and-redirection-handling`)
- `devB-redis-07` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-23-failure-detection`)
- `devB-redis-08` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-34-replica-migration-algorithm`)
- `devB-redis-09` absent (expected `imported-web-redis-io-docs-latest-operate-oss-and-stack-reference-cluster-spec-05-performance`)
- `devB-kubernetes-01` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-02-pod-lifetime`)
- `devB-kubernetes-02` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-03-pods-and-fault-recovery`)
- `devB-kubernetes-03` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-07-how-pods-handle-problems-with-containers`)
- `devB-kubernetes-04` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-08-pod-level-container-restart-policy`)
- `devB-kubernetes-05` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-12-individual-container-restart-policy-and-rules`)
- `devB-kubernetes-06` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-21-container-probes`)
- `devB-kubernetes-07` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-21-container-probes`)
- `devB-kubernetes-08` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-24-pod-termination-flow`)
- `devB-kubernetes-09` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-pods-pod-lifecycle-27-garbage-collection-of-pods`)
- `devB-nginx-01` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-01-directives`)
- `devB-nginx-02` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-11-directives`)
- `devB-nginx-03` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-09-directives`)
- `devB-nginx-04` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-09-directives`)
- `devB-nginx-05` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-09-directives`)
- `devB-nginx-06` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-10-directives`)
- `devB-nginx-07` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-10-directives`)
- `devB-nginx-08` absent (expected `imported-web-nginx-org-en-docs-http-ngx-http-core-module-11-directives`)
- `devB-http-caching-01` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-13-4-2-freshness`)
- `devB-http-caching-02` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-07-3-1-storing-header-and-trailer-fields`)
- `devB-http-caching-03` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-11-4-constructing-responses-from-caches`)
- `devB-http-caching-04` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-12-4-1-calculating-cache-keys-with-the-vary-header-fi`)
- `devB-http-caching-05` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-14-4-2-1-calculating-freshness-lifetime`)
- `devB-http-caching-06` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-15-4-2-2-calculating-heuristic-freshness`)
- `devB-http-caching-07` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-17-4-2-4-serving-stale-responses`)
- `devB-http-caching-08` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9111-23-4-4-invalidating-stored-responses`)
- `devB-git-config-01` absent (expected `imported-web-git-scm-com-docs-git-config-2-51-1-02-syntax`)
- `devB-git-config-02` absent (expected `imported-web-git-scm-com-docs-git-config-2-51-1-03-includes`)
- `devB-git-config-03` absent (expected `imported-web-git-scm-com-docs-git-config-2-51-1-02-syntax`)
- `devB-git-config-04` absent (expected `imported-web-git-scm-com-docs-git-config-2-51-1-02-syntax`)
- `devB-git-config-05` absent (expected `imported-web-git-scm-com-docs-git-config-2-51-1-02-syntax`)
- `devB-git-config-06` absent (expected `imported-web-git-scm-com-docs-git-config-2-51-1-03-includes`)
- `devB-git-config-07` absent (expected `imported-web-git-scm-com-docs-git-config-2-51-1-04-conditional-includes`)
- `devB-git-config-08` absent (expected `imported-web-git-scm-com-docs-git-config-2-51-1-06-values`)
- `devB-python-logging-01` absent (expected `imported-web-docs-python-org-3-13-library-logging-02-logger-objects`)
- `devB-python-logging-02` absent (expected `imported-web-docs-python-org-3-13-library-logging-09-filter-objects`)
- `devB-python-logging-03` absent (expected `imported-web-docs-python-org-3-13-library-logging-03-logger-objects`)
- `devB-python-logging-04` absent (expected `imported-web-docs-python-org-3-13-library-logging-06-handler-objects`)
- `devB-python-logging-05` absent (expected `imported-web-docs-python-org-3-13-library-logging-07-formatter-objects`)
- `devB-python-logging-06` absent (expected `imported-web-docs-python-org-3-13-library-logging-09-filter-objects`)
- `devB-python-logging-07` absent (expected `imported-web-docs-python-org-3-13-library-logging-14-module-level-functions`)
- `devB-python-logging-08` absent (expected `imported-web-docs-python-org-3-13-library-logging-15-module-level-functions`)
