# Dev B document licenses

Five of the six dev B documents are included here. Changes to each: the HTML page
was converted to Markdown and split into section notes by `vaultmind import`
(fetched 2026-10-12; snapshot hashes in `sources.yaml`).

| document | license | attribution | basis |
|---|---|---|---|
| Python 3.13 `logging` reference | PSF License Version 2 (`python-LICENSE.txt`) | Copyright (c) 2001-2026 Python Software Foundation; All Rights Reserved. | the Python documentation license |
| Kubernetes: Pod Lifecycle | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | © The Kubernetes Authors, https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ | the kubernetes/website repository license (CC-BY-4.0) |
| nginx: Module ngx_http_core_module | BSD 2-Clause (`nginx-org-LICENSE.txt`) | Copyright (C) 2002-2021 Igor Sysoev; Copyright (C) 2011-2026 Nginx, Inc. | the LICENSE of the nginx.org website and documentation repository |
| RFC 9111: HTTP Caching | IETF Trust Legal Provisions (TLP 5.0, BCP 78), Section 3.c | RFC 9111, R. Fielding, M. Nottingham, J. Reschke (Eds.), June 2022. Copyright (c) 2022 IETF Trust and the persons identified as the document authors. | IETF TLP §3.c permits reproduction of RFCs in full or in part |
| Git 2.51.1: git-config | GNU GPL version 2 (`git-COPYING.txt`) | The Git documentation, © the Git contributors, https://git-scm.com/docs/git-config/2.51.1 | Git and its documentation are distributed under GPL-2.0 |

**Withheld: Redis Cluster specification.** The Redis website and documentation are
licensed CC BY-NC-SA 4.0, with some older portions CC BY-SA 4.0. We have not
established which applies to this snapshot, so its text is not redistributed. Its
nine questions, labels, URL and snapshot hashes are in `queries.yaml` and
`sources.yaml`; the published dev B results were run with its text present. A
re-run from this repository scores those nine questions as misses unless you import
the page yourself (`vaultmind import <url>`; the live page may differ from the snapshot).
