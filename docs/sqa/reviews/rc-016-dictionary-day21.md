# RC-016: Re-review of DICT-001 (day 21)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-016 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001], [RC-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [710784f] |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. Eight rows were added and the row `tail` changed meaning, so a delta re-review is not allowed. Earlier record: [RC-003].
- Reason: Day 21 adds food, eating, growing, the score, the scoreboard, the wall, touching the tail and game over; and "tail" now means every segment behind the head, as the lecture uses it, instead of the last segment.
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All 24 rows have a PO term, `en`, an IT term and a definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Each PO term has one IT term and no IT term is used twice: `segments` (body), `segments[1:]` (tail), `FOOD_COLLISION_DISTANCE` (eat), `TAIL_COLLISION_DISTANCE` (touch), `WALL_LIMIT` (wall), `extend` (grow), `game_over` (game over). |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | No Domain Model exists in this project. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | No Operation Contract, Sequence Diagram, Design Class Diagram or ERD exists in this project. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Every definition is one sentence in English. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | Rows name `BC`, `SA`, `PP`, `MIL` and `PY`; Python source code exists in `src/snake_game/`. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | `Language | en` and `Domain | it` match the registry; every row is `en`. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language | en` and `Domain | it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English, including the new and changed text and the Version History row. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Professional English: precise terms and IDs, no business padding. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms are those of [DICT-001], including its day-21 rows (food, eat, grow, score, scoreboard, wall, touch, tail, game over). A search for the variants 'reach', 'collision', 'heading' and 'turn back' found them only in backticked identifiers, quoted lecture or outline steps, or as ordinary verbs; the phrases 'reaches the food' and 'collision with the wall' were replaced by 'eats' and 'passing the wall' before this review. This document is the dictionary; the other documents were checked against it. |
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
| Read [DICT-001] and confirm or overrule this `Go`, in particular the new meaning of `tail`, before the pull request of MIL-004 is merged | S01 | 2026-10-16 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[BC-001]: ../../business-case.md
[PP-001]: ../../project-plan.md
[RC-003]: ./rc-003-dictionary.md
[710784f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/020-snake-game/commit/710784f2243e7ecf8cec23cbdd9cc58c96cdff96
