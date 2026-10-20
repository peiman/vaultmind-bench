# Scores

Set: `sets/heldout`

Token method: `tiktoken-cl100k_base`

| system | Hit@1 | Hit@3 | mean tokens | median tokens | mean seconds |
|---|---:|---:|---:|---:|---:|
| vm | 32/50 | 45/50 | 2610.9 | 2875.0 | 2.514 |
| bm25 | 28/50 | 38/50 | 2582.2 | 2436.0 | 0.008 |
| rg | 20/50 | 32/50 | 3284.1 | 3286.0 | 0.125 |
| agent-rg | 42/50 | 44/50 | 8086.2 | 7819.0 | 6.96 |
| agent-vm | 46/50 | 49/50 | 5901.6 | 6539.0 | 8.778 |
| whole | 0/50 | 0/50 | 25585.0 | 16953.0 | 0.006 |

whole fits in 200k tokens: 50/50

## Misses

A miss is a question whose labelled section is not at rank 3 or better.
Rank is 1-based in `ranked`; empty means the id was not in the list.

### vm

- `heldout-rfc-01` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-19-5-1-1-stream-identifiers`)
- `heldout-rfc-06` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-37-6-8-goaway`)
- `heldout-k8s-03` rank 5 (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-07-rollover-aka-multiple-updates-in-flight`)
- `heldout-mdn-06` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-09-preflight-requests-and-credentials`)
- `heldout-gha-03` rank 4 (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-52-jobs-job-id-steps-run-jobsjob-idstepsrun`)

### bm25

- `heldout-rfc-01` rank 21 (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-19-5-1-1-stream-identifiers`)
- `heldout-rfc-07` rank 6 (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-41-6-9-2-initial-flow-control-window-size`)
- `heldout-py-03` rank 6 (expected `imported-web-docs-python-org-3-13-library-subprocess-10-security-considerations`)
- `heldout-py-09` rank 5 (expected `imported-web-docs-python-org-3-13-library-subprocess-24-disabling-use-of-vfork-or-posix-spawn`)
- `heldout-k8s-03` rank 6 (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-07-rollover-aka-multiple-updates-in-flight`)
- `heldout-mdn-02` rank 4 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-03-simple-requests`)
- `heldout-mdn-04` rank 4 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-08-requests-with-credentials`)
- `heldout-mdn-05` rank 7 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-10-credentialed-requests-and-wildcards`)
- `heldout-mdn-06` rank 214 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-09-preflight-requests-and-credentials`)
- `heldout-mdn-07` rank 6 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-07-preflighted-requests-and-redirects`)
- `heldout-gha-03` rank 41 (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-52-jobs-job-id-steps-run-jobsjob-idstepsrun`)
- `heldout-gha-08` rank 5 (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-66-jobs-job-id-uses`)

### rg

- `heldout-rfc-01` rank 25 (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-19-5-1-1-stream-identifiers`)
- `heldout-rfc-05` rank 5 (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-09-3-1-http-2-version-identification`)
- `heldout-rfc-07` rank 8 (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-41-6-9-2-initial-flow-control-window-size`)
- `heldout-rfc-08` rank 9 (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-34-6-5-3-settings-synchronization`)
- `heldout-py-03` rank 13 (expected `imported-web-docs-python-org-3-13-library-subprocess-10-security-considerations`)
- `heldout-py-08` rank 4 (expected `imported-web-docs-python-org-3-13-library-subprocess-22-timeout-behavior`)
- `heldout-py-09` rank 7 (expected `imported-web-docs-python-org-3-13-library-subprocess-24-disabling-use-of-vfork-or-posix-spawn`)
- `heldout-k8s-03` rank 44 (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-07-rollover-aka-multiple-updates-in-flight`)
- `heldout-k8s-07` rank 4 (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-05-note`)
- `heldout-k8s-08` rank 4 (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-22-max-unavailable`)
- `heldout-cargo-03` rank 6 (expected `imported-web-doc-rust-lang-org-cargo-reference-config-05-command-line-overrides`)
- `heldout-cargo-08` rank 4 (expected `imported-web-doc-rust-lang-org-cargo-reference-config-13-install-root`)
- `heldout-mdn-02` rank 5 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-03-simple-requests`)
- `heldout-mdn-05` rank 8 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-10-credentialed-requests-and-wildcards`)
- `heldout-mdn-06` rank 44 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-09-preflight-requests-and-credentials`)
- `heldout-mdn-07` rank 11 (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-07-preflighted-requests-and-redirects`)
- `heldout-gha-03` rank 35 (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-52-jobs-job-id-steps-run-jobsjob-idstepsrun`)
- `heldout-gha-05` rank 4 (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-47-example-using-secrets`)

### agent-rg

- `heldout-k8s-01` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-09-note`)
- `heldout-k8s-05` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-16-note`)
- `heldout-k8s-07` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-05-note`)
- `heldout-k8s-09` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-17-note`)
- `heldout-cargo-01` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-01-keyboard-shortcuts`)
- `heldout-cargo-08` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-13-install-root`)

### agent-vm

- `heldout-py-06` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-06-popen-constructor`)

### whole

- `heldout-rfc-01` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-19-5-1-1-stream-identifiers`)
- `heldout-rfc-02` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-22-5-2-2-appropriate-use-of-flow-control`)
- `heldout-rfc-03` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-20-5-1-2-stream-concurrency`)
- `heldout-rfc-04` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-11-3-4-http-2-connection-preface`)
- `heldout-rfc-05` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-09-3-1-http-2-version-identification`)
- `heldout-rfc-06` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-37-6-8-goaway`)
- `heldout-rfc-07` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-41-6-9-2-initial-flow-control-window-size`)
- `heldout-rfc-08` absent (expected `imported-web-www-rfc-editor-org-rfc-rfc9113-34-6-5-3-settings-synchronization`)
- `heldout-py-01` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-11-popen-objects`)
- `heldout-py-02` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-09-exceptions`)
- `heldout-py-03` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-10-security-considerations`)
- `heldout-py-04` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-07-popen-constructor`)
- `heldout-py-05` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-12-popen-objects`)
- `heldout-py-06` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-06-popen-constructor`)
- `heldout-py-07` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-16-older-high-level-api`)
- `heldout-py-08` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-22-timeout-behavior`)
- `heldout-py-09` absent (expected `imported-web-docs-python-org-3-13-library-subprocess-24-disabling-use-of-vfork-or-posix-spawn`)
- `heldout-k8s-01` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-09-note`)
- `heldout-k8s-02` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-08-label-selector-updates`)
- `heldout-k8s-03` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-07-rollover-aka-multiple-updates-in-flight`)
- `heldout-k8s-04` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-12-proportional-scaling`)
- `heldout-k8s-05` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-16-note`)
- `heldout-k8s-06` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-21-selector`)
- `heldout-k8s-07` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-05-note`)
- `heldout-k8s-08` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-22-max-unavailable`)
- `heldout-k8s-09` absent (expected `imported-web-kubernetes-io-docs-concepts-workloads-controllers-deployment-17-note`)
- `heldout-cargo-01` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-01-keyboard-shortcuts`)
- `heldout-cargo-02` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-04-environment-variables`)
- `heldout-cargo-03` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-05-command-line-overrides`)
- `heldout-cargo-04` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-10-build-rustflags`)
- `heldout-cargo-05` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-12-global-caches`)
- `heldout-cargo-06` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-11-build-rustdocflags`)
- `heldout-cargo-07` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-15-patch-patch`)
- `heldout-cargo-08` absent (expected `imported-web-doc-rust-lang-org-cargo-reference-config-13-install-root`)
- `heldout-mdn-01` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-02-functional-overview`)
- `heldout-mdn-02` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-03-simple-requests`)
- `heldout-mdn-03` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-05-preflighted-requests`)
- `heldout-mdn-04` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-08-requests-with-credentials`)
- `heldout-mdn-05` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-10-credentialed-requests-and-wildcards`)
- `heldout-mdn-06` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-09-preflight-requests-and-credentials`)
- `heldout-mdn-07` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-07-preflighted-requests-and-redirects`)
- `heldout-mdn-08` absent (expected `imported-web-developer-mozilla-org-en-us-docs-web-http-guides-cors-12-access-control-allow-origin`)
- `heldout-gha-01` absent (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-13-on-schedule`)
- `heldout-gha-02` absent (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-12-git-diff-comparisons`)
- `heldout-gha-03` absent (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-52-jobs-job-id-steps-run-jobsjob-idstepsrun`)
- `heldout-gha-04` absent (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-42-using-job-outputs-in-a-matrix-job`)
- `heldout-gha-05` absent (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-47-example-using-secrets`)
- `heldout-gha-06` absent (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-63-jobs-job-id-strategy-fail-fast`)
- `heldout-gha-07` absent (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-59-jobs-job-id-timeout-minutes`)
- `heldout-gha-08` absent (expected `imported-web-docs-github-com-en-actions-reference-workflows-and-actions-workflow-syntax-66-jobs-job-id-uses`)
