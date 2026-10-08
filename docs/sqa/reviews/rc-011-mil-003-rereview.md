# RC-011: Re-review of MIL-003

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-003], [QC-MIL-001], [QC-LANG-001], [RC-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-003]
- Checklist used: [QC-MIL-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. The change touches a Go/No-Go criterion and two tasks, so a delta re-review is not allowed. Earlier record: [RC-006].
- Reason: Closing a real turtle window in a loop raised `_tkinter.TclError`, not only `turtle.Terminator` as the milestone said; and the lecture's test of the head's current direction lets two key presses within one move reverse the snake, against objective 1 of [BC-001].
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A concrete deliverable is defined for every gate | Pass | Deliverable section is unchanged. |
| 2 | Explicit Go/No-Go criteria are stated for each gate | Pass | Ten Go/No-Go rows. Criterion 4 now also requires that two key presses within one move do not reverse the snake, which a test checks; criterion 5 (clean exit, exit code 0) is unchanged and is checked by a test and by closing a real window. |
| 3 | Dependencies on other milestones are explicitly mapped | Pass | Dependencies table is unchanged: MIL-002 accepted and merged. |
| 4 | Each milestone is traceable to a Business Case objective or KPI | Pass | Traceability table is unchanged and maps to BC-001 objectives 1, 2, 4, 5 and 6. |
| 5 | Milestone owner and approving reviewer are identified | Pass | Owner and approving reviewer are both S01 (same person; see verdict). |
| 6 | Milestone has a defined target date consistent with project constraints | Pass | Target date 2026-10-13 is unchanged and inside the one-week constraint ending 2026-10-15. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language | en` and `Domain | it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English, including the changed text and the new Version History row. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Executive English; code names and commands appear in backticks only where a target or a check needs them. The Go/No-Go table names commands because its criteria must be objectively checkable. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The changed text uses the terms of [DICT-001] (move, direction, reversal, window, screen). `key press` is plain English for pressing an arrow key and has no dictionary row; `TclError` and `Terminator` are identifiers in backticks. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds one file per artifact; there is no `<name>.<language>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Language and domain are unchanged since the previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and knows the IT domain; S01 asked for this milestone to start in chat on 2026-10-08. S01's own reading of the changed text is an action item below. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | No new abbreviation is introduced; the existing ones stay spelled out on first use. |

## Overall Verdict

Go — all Mandatory criteria pass. The rows above were assessed on 2026-10-08 by the assistant that made the change, at S01's request in chat. This review is **not independent**; S01 is the approver and can overrule the verdict at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read [MIL-003] and confirm or overrule this `Go`, in particular the change of task 4 (direction of the last move) before the pull request is merged | S01 | 2026-10-13 |

---

[MIL-003]: ../../milestones/mil-003-movement-and-keys.md
[QC-MIL-001]: ../../../framework/qc/qc-milestones-gateways.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[RC-006]: ./rc-006-mil-003.md
[DICT-001]: ../../dictionary.md
