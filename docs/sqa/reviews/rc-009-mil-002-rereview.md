# RC-009: Re-review of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-002], [QC-MIL-001], [QC-LANG-001], [RC-005] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-MIL-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. The change adds a design statement to the Traceability section, so a delta re-review is not allowed. Earlier record: [RC-005].
- Reason: the action item of [RC-007] asked to decide, before MIL-002 starts, whether the `Snake` class gets a Design Class Diagram or traces to the lecture. S01 asked to start MIL-002 without asking for a diagram, so the milestone now records that the class traces to the lecture, and that this deviates from `QC-PY-001` criterion 10. This closes that action item of [RC-007].
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A concrete deliverable is defined for every gate | Pass | Deliverable section is unchanged: `snake.py`, `main.py`, `__main__.py`, the two test files and the visible result. |
| 2 | Explicit Go/No-Go criteria are stated for each gate | Pass | Seven Go/No-Go rows are unchanged; each names a manual observation by S01, a command or a code property. |
| 3 | Dependencies on other milestones are explicitly mapped | Pass | Dependencies table is unchanged: MIL-001 accepted and merged, with the reason. |
| 4 | Each milestone is traceable to a Business Case objective or KPI | Pass | Traceability table maps to BC-001 objectives 1, 2 and 4 and Success Criteria 1, 2 and 6, and now also records the design basis of the `Snake` class. |
| 5 | Milestone owner and approving reviewer are identified | Pass | Owner and approving reviewer are both S01 (same person; see verdict). |
| 6 | Milestone has a defined target date consistent with project constraints | Pass | Target date 2026-10-11 is unchanged and inside the one-week constraint ending 2026-10-15. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language | en` and `Domain | it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English, including the new Traceability row and the Version History row. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Executive English; the Go/No-Go table names commands because its criteria must be objectively checkable. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms are those of [DICT-001]; the added text introduces no new game term. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds one file per artifact; there is no `<name>.<language>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Language and domain are unchanged since the previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and knows the IT domain; S01 asked for this milestone to start in chat on 2026-10-08. S01's own reading of the document is an action item below. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use (OOP, CI, PO). |

## Overall Verdict

Go — all Mandatory criteria pass. The rows above were assessed on 2026-10-08 by the assistant that made the change, at S01's request in chat. This review is **not independent**; S01 is the approver and can overrule the verdict at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read [MIL-002] and confirm or overrule this `Go`, in particular the decision not to write a Design Class Diagram, before the pull request is merged | S01 | 2026-10-11 |
| Open the pull request of MIL-002 only after the pull request of MIL-001 is merged, or with the MIL-001 branch as its base ([MIL-002] depends on [MIL-001] being merged) | S01 | 2026-10-11 |

---

[MIL-002]: ../../milestones/mil-002-screen-and-snake-body.md
[MIL-001]: ../../milestones/mil-001-project-foundation.md
[QC-MIL-001]: ../../../framework/qc/qc-milestones-gateways.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[RC-005]: ./rc-005-mil-002.md
[RC-007]: ./rc-007-mil-001-code.md
[DICT-001]: ../../dictionary.md
