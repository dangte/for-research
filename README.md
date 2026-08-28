# for-research

Personal collection of Claude Code **skills** for academic research workflows
(literature review, methodology, data analysis, academic writing, citation, review,
research framing, defense prep) plus supplementary skills. Kept as a **private backup**.

## Contents (`skills/`)

**Core research suite**
- `academic-writing`
- `citation-manager`
- `critical-review`
- `data-analysis`
- `defense-prep`
- `literature-review` — includes sub-skill `kiem-tra-gap-con-mo` (validate a research gap is still open / real / feasible)
- `methodology-design`
- `research-framework`

**Supplementary**
- `research-brainstorming` — clarify a research idea before drafting (Socratic gate). Independent reimplementation *inspired by* [obra/superpowers](https://github.com/obra/superpowers) `brainstorming` (MIT); no source text copied.
- `aaouj-compliance` — pre-submission checklist for the *Asian Association of Open Universities Journal* (Emerald). Contains brief quoted guideline text for reference; verify against the official author guidelines before use.
- `compliant-crawl` — compliant web data-collection workflow (robots.txt/ToS, no PII, source attribution, CSV output). Pairs with the runnable toolkit kept in the research project (not in this repo).

**Third-party (redistributed under their own license)**
- `humanizer` — by **blader**, MIT License. See `skills/humanizer/LICENSE`. Source patterns from Wikipedia "Signs of AI writing". Upstream: https://github.com/blader/humanizer

## License & CI

- **License:** `LICENSE` (MIT) covers only the repository owner's original skills; third-party
  and unconfirmed components are carved out — see `PROVENANCE.md`.
- **CI:** `.github/workflows/validate-skills.yml` validates that every `SKILL.md` has valid
  YAML frontmatter with a non-empty `name` and `description`, on every push/PR.

## Provenance & licensing note

The authorship/license of the core research suite is **not fully established**; this
repository is therefore kept **private** as a personal backup, not for public
redistribution. Before making any part public, confirm each skill's origin and add an
explicit license. `humanizer` is redistributed with its MIT license and attribution intact.

> Private-only: `clean-user-facing-text` (watermark/Unicode cleaner) is included as a personal
> backup, but its license/origin is unconfirmed. Do not make this repository public without first
> establishing its license (or removing it). See `PROVENANCE.md`.
