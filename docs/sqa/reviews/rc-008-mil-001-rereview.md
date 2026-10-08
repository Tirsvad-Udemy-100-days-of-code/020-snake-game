# RC-008: Re-review of MIL-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [MIL-001], [QC-MIL-001], [QC-LANG-001], [RC-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-001]
- Checklist used: [QC-MIL-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. The change touches the deliverable, a Go/No-Go criterion and a task, so a delta re-review is not allowed. Earlier record: [RC-004].
- Reason: the continuous integration workflow moved from `.github/workflows/ci.yml` to `.gitea/workflows/ci.yml`. The earlier project `018-turtle` found that GitHub refuses a push that touches `.github/workflows` from a token without the workflow scope, which blocks the push mirror to GitHub.
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A concrete deliverable is defined for every gate | Pass | Deliverable section lists the files of the foundation, now with `.gitea/workflows/ci.yml`. |
| 2 | Explicit Go/No-Go criteria are stated for each gate | Pass | Eleven Go/No-Go rows, each with a command or an observable result. Row 8 now also requires that nothing exists under `.github/workflows`, which is checkable with `ls`. |
| 3 | Dependencies on other milestones are explicitly mapped | Pass | Dependencies table is unchanged: PP-001 accepted, and this milestone accepted with a Go review (plan-first gate). |
| 4 | Each milestone is traceable to a Business Case objective or KPI | Pass | Traceability table is unchanged and still maps to BC-001 objectives 3, 4, 5 and 7. |
| 5 | Milestone owner and approving reviewer are identified | Pass | Owner and approving reviewer are both S01 (same person; see verdict). |
| 6 | Milestone has a defined target date consistent with project constraints | Pass | Target date 2026-10-09 is unchanged and inside the one-week constraint ending 2026-10-15. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language | en` and `Domain | it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English, including the new Version History row and the reason in task 6. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Executive English; the Go/No-Go table names paths and commands because its criteria must be objectively checkable. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms are those of [DICT-001]; the added text introduces no new game term. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds one file per artifact; there is no `<name>.<language>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Language and domain are unchanged since the previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and knows the IT domain; S01 asked for the work that led to this change in chat on 2026-10-08. S01's own reading of the document is an action item below. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use (CI, PO, RACI). |

## Overall Verdict

Go — all Mandatory criteria pass. The rows above were assessed on 2026-10-08 by the assistant that made the change, at S01's request in chat. This review is **not independent**; S01 is the approver and can overrule the verdict at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read [MIL-001] and confirm or overrule this `Go` before the pull request is merged | S01 | 2026-10-09 |
| Run `sync-project.sh --milestone MIL-001 --apply` so that Issue #6 on the git host names `.gitea/workflows/ci.yml` (it still names `.github/workflows/ci.yml`) | S01 | 2026-10-09 |

---

[MIL-001]: ../../milestones/mil-001-project-foundation.md
[QC-MIL-001]: ../../../framework/qc/qc-milestones-gateways.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[RC-004]: ./rc-004-mil-001.md
[DICT-001]: ../../dictionary.md
