# RC-020: Re-review of MIL-005 (task title)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-020 |
| CrossReference | [MIL-005], [QC-MIL-001], [QC-LANG-001], [RC-019] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [710784f] |

---

## Artifact Under Review

- Instance reviewed: [MIL-005]
- Checklist used: [QC-MIL-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. Only the title of task 7 changed, but the milestone is accepted, so it is checked again in full. Earlier record: [RC-019].
- Reason: The first sync of MIL-005 matched task 7 to Issue #17 of MIL-003 because both tasks were titled "Finish the README and the documentation", and overwrote that issue. The title of task 7 of MIL-005 is now "Finish the README for the whole game".
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A concrete deliverable is defined for every gate | Pass | Deliverable section is unchanged. |
| 2 | Explicit Go/No-Go criteria are stated for each gate | Pass | The thirteen Go/No-Go rows are unchanged. |
| 3 | Dependencies on other milestones are explicitly mapped | Pass | Dependencies table is unchanged: MIL-004 accepted and merged. |
| 4 | Each milestone is traceable to a Business Case objective or KPI | Pass | Traceability table is unchanged and maps to BC-001 objectives 9, 2, 4, 5 and 6. |
| 5 | Milestone owner and approving reviewer are identified | Pass | Owner and approving reviewer are both S01 (same person; see verdict). |
| 6 | Milestone has a defined target date consistent with project constraints | Pass | Target date 2026-10-19 is unchanged and inside phase 2, which ends 2026-10-21. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language | en` and `Domain | it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English, including the new and changed text and the Version History row. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Executive English; code names and commands appear in backticks only where a target or a check needs them. The Go/No-Go table names commands because its criteria must be objectively checkable. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms are those of [DICT-001], including its day-21 rows (food, eat, grow, score, scoreboard, wall, touch, tail, game over). A search for the variants 'reach', 'collision', 'heading' and 'turn back' found them only in backticked identifiers, quoted lecture or outline steps, or as ordinary verbs; the phrases 'reaches the food' and 'collision with the wall' were replaced by 'eats' and 'passing the wall' before this review. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds one file per artifact; there is no `<name>.<language>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Language and domain are unchanged since the previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 reads English and knows the IT domain; S01 chose day 21 for this repository in chat on 2026-10-08. The terms were also checked against [DICT-001] by the reviewing assistant; S01's own reading is an action item below. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | New abbreviations are spelled out on first use (none are introduced besides identifiers and IDs). |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. The rows above were assessed on 2026-10-08 by the assistant that made the change, at S01's request in chat ("Day 21 in this repo, plan first"). This review is **not independent**: the drafter and the reviewer are the same assistant, and author and reviewer (S01) are one person in a single-person project. S01 has not read the document line by line and can overrule this verdict.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read [MIL-005] and confirm or overrule this `Go` before any task of it is started | S01 | 2026-10-18 |

---

[MIL-005]: ../../milestones/mil-005-game-over.md
[QC-MIL-001]: ../../../framework/qc/qc-milestones-gateways.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[BC-001]: ../../business-case.md
[DICT-001]: ../../dictionary.md
[PP-001]: ../../project-plan.md
[RC-019]: ./rc-019-mil-005.md
[710784f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/710784f2243e7ecf8cec23cbdd9cc58c96cdff96
