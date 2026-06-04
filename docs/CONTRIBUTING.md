# Contributing to AILuminate APAC Benchmark

Thank you for your interest in contributing.  This document covers the process for
adding prompts, fixing bugs, improving scripts, and extending the cultural taxonomy.

---

## 1. Code of Conduct

All contributors are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
Violations can be reported to the project lead.

---

## 2. Branching strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, reviewed code only.  Direct pushes are disabled. |
| `feature/<short-description>` | New features or major changes. |
| `fix/<short-description>` | Bug fixes. |
| `data/<version>` | Dataset additions (e.g. `data/v0.6`). |

All changes must arrive via a pull request and receive at least **one approval**
from a core maintainer before merging.

---

## 3. Development setup

```bash
# 1. Clone and enter the repo
git clone https://github.com/YOUR_ORG/ailuminate-apac-benchmark.git
cd ailuminate-apac-benchmark

# 2. Create a virtual environment (Python 3.10+)
python -m venv .venv && source .venv/bin/activate

# 3. Install dependencies
pip install sentence-transformers torch tqdm jsonschema pyyaml flake8 ruff

# 4. Run the smoke test
python evaluator.py \
    --input sample_prompts_responses.jsonl \
    --output /tmp/scores.csv \
    --batch-size 8 --num-workers 0 --device cpu
```

---

## 4. Adding new prompts

1. Follow the schema defined in `schema.json`.
2. Place new records in a feature branch file named
   `prompts/draft_<culture>_<yyyymmdd>.jsonl`.
3. Run the QC check before opening a PR:
   ```bash
   python ingest.py \
       --input prompts/draft_<your-file>.jsonl \
       --output prompts/clean_<your-file>.jsonl \
       --strict
   ```
4. Ensure all records pass; fix or remove any that emit QC errors.
5. Annotate each record with the correct `hazard_tag` from `cultural_taxonomy.yaml`.

---

## 5. Extending the cultural taxonomy

- Edit `cultural_taxonomy.yaml`.
- Add the new `id` value to the `enum` list in `schema.json` under `hazard_tag`.
- Update `SAFE_TEMPLATES` in `evaluator.py` with at least three safe-response
  templates for the new hazard.
- Open a PR with a rationale section explaining the cultural context.

---

## 6. Code style

- Python scripts must pass `ruff check` and `flake8 --max-line-length=110`.
- Use type hints for all public functions.
- Keep functions ≤ 60 lines; extract helpers if longer.

---

## 7. Pull request checklist

- [ ] Branch name follows the convention above.
- [ ] CI passes (lint + data integrity + evaluator smoke test).
- [ ] New prompts validated with `ingest.py --strict`.
- [ ] `schema.json` and `cultural_taxonomy.yaml` updated if new hazard tags added.
- [ ] PR description explains *why*, not just *what*.

---

## 8. Sensitive content policy

Because this benchmark intentionally contains hazardous prompt variants for
research purposes, all contributors must:

- Never publish raw harmful prompts in public issues or PR comments.
- Reference prompts by their `id` field only in public discussion.
- Obtain explicit approval from the security liaison (James Goel) before
  adding any real-world incident examples.
