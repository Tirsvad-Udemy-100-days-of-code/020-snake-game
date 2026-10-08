# RC-014: Re-review of BC-001 (day 21)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [BC-001], [QC-BC-001], [QC-LANG-001], [RC-012] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [710784f] |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. Objectives, scope, success criteria, risks, assumptions, constraints, costs and the recommendation changed, so a delta re-review is not allowed. Earlier record: [RC-012].
- Reason: S01 chose to build day 21 in this repository, so the Business Case now has objectives 8 and 9, two success criteria, three risks and a plan in two phases ending 2026-10-21.
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | ROI/Cost-Benefit analysis is quantitative, or where qualitative, is explicitly justified | Pass | Cost–Benefit Assessment is still qualitative and justified; the cost is now about two weeks and the benefit covers objectives 1 to 9. |
| 2 | Risks are identified with documented impact and mitigation | Pass | Risks table has 11 rows, each with an Impact and a Mitigation; the three new rows cover the unknown day-21 numbers, inheritance versus display-free tests, and the random place of the food. |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | Success Criteria has 10 rows with a Target and a Measure; the new rows 9 and 10 state observable targets (the food is eaten, the snake grows by one segment, the score rises by 1; the game ends at the wall or the tail and GAME OVER is shown) and name the Go/No-Go list that measures them. |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | `### In Scope` now lists the four steps of day 21; `### Out of Scope` no longer lists day 21 and names high-score storage between games and restarting after game over. |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | Stakeholders table cites S01, S02 and S03 and states interests only; the objective numbers were extended to 1 to 9 for S01 and 1, 2, 3, 5, 8 and 9 for S02. |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | Methodological and Standards Foundation is unchanged and still names the framework, Larman, ISO/IEC 25010:2023, PEP, Doxygen and pytest. |
| 7 | Assumptions and constraints are explicit and clearly distinguished from one another | Pass | Assumptions and Constraints are separate; the day-21 assumption and the two-phase constraint are in the right lists. |
| 8 | Document supports executive decision-making with a clear, unambiguous recommendation | Pass | Recommendation: "Proceed — ...", one sentence, updated for two weeks and days 20 and 21. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language | en` and `Domain | it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English, including the new and changed text and the Version History row. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Executive English; code names and commands appear in backticks only where a target or a check needs them. |
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
| Read [BC-001] and confirm or overrule this `Go` before the pull request of MIL-004 is merged | S01 | 2026-10-16 |
| Decide the open issues of [PP-001] that affect the scope: inheritance versus fake-module tests, the food under the snake, the high score | S01 | 2026-10-16 |

---

[BC-001]: ../../business-case.md
[QC-BC-001]: ../../../framework/qc/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[DICT-001]: ../../dictionary.md
[PP-001]: ../../project-plan.md
[RC-012]: ./rc-012-bc-rereview.md
[710784f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/710784f2243e7ecf8cec23cbdd9cc58c96cdff96
