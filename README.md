
```

# Benchmarks Without Borders: ARTIFEX Safety Evals
**Principal Investigator**: Tuesday, ARTIFEX Labs

---

## About Benchmarks Without Borders & Core Pillars

**Benchmarks Without Borders** is a next-generation **multilingual compositional safety evaluation suite** engineered to benchmark, analyze, and audit safety filters, routing mechanisms, and alignment boundaries in frontier AI systems. Built to implement the formal **2026 Measurement Science Framework**, Benchmarks Without Borders resolves the critical **"Validity Sinkhole"** and safeguards benchmarks against rapid saturation and decay (**Goodhart's Law**).

The architecture is structured around five core pillars:

1. **Construct Validity & The "Validity Sinkhole" Resolution**
   Standard static benchmarks suffer from rapid saturation and representation drift. Benchmarks Without Borders uses dynamically generated, compositional, and adversarial prompt matrices to evaluate models at their functional limits rather than matching rote templates.

2. **Adaptive Policy-Based Rubrics (APBR Framework)**
   Rather than treating safety as a simple binary scalar, Benchmarks Without Borders defines safety via multi-dimensional, machine-checkable boolean gates at every pipeline decision point.

3. **Rubric Invariant Failure Mode (RIFT) Verification**
   Automated detection of rubric drift, ensuring that the criteria for evaluating safety do not degrade or mutate under changing model outputs or varying prompting templates.

4. **AdaRubric & Task-Adaptive Evaluation**
   Evaluation criteria dynamically adapt based on target task contexts (e.g., institutional compliance vs. creative writing), maintaining tight scope controls and reducing false-positive rates.

5. **X-Value Cross-Lingual Auditing**
   Audits alignment across distinct languages and cultural contexts, capturing dialect-level divergence (e.g., Castilian vs. Mexican Spanish) rather than relying on automated translations.

---

## Capabilities & Tooling

The suite combines production-grade Python command-line tools, self-contained Google Colab notebooks, and datasets:

- **X-Value Consensus/Pluralism Framework** — Audits cross-lingual value alignment.
- **BBOM (Benchmark Bill of Materials)** — Implements supply-chain auditing for benchmark provenance and integrity.
- **LLM-as-Judge** — Uses bias-corrected estimators and Pydantic structured outputs for high-precision evaluations.
- **Human-in-the-Loop (HITL)** — Employs active learning triplet queries to refine rubrics and resolve corner cases.
- **FiftyOne Integration** — Supports visual dataset curation for multimodal safety annotation.

---

## Citation

To cite **Benchmarks Without Borders** / **ARTIFEX Safety Evals** in your research, safety audits, or publications, please use the following formats:

### BibTeX
```bibtex
@software{Benchmarks Without Borders_2026,
  author       = {Tuesday},
  title        = {{Benchmarks Without Borders: ARTIFEX Multilingual Compositional Safety Evaluation Suite}},
  institution  = {ARTIFEX Labs},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/Tuesdaythe13th/multilingualcompositionalsafety_evals}}
}
```

### APA
> Tuesday. (2026). *Benchmarks Without Borders: ARTIFEX Multilingual Compositional Safety Evaluation Suite* (Version 7-10). ARTIFEX Labs. Available at https://github.com/Tuesdaythe13th/multilingualcompositionalsafety_evals.

---

## Repository Structure

```
multilingualcompositionalsafety_evals/
│
├── 📁 notebooks/                       Jupyter / Colab Notebooks
│   ├── safety_routing_colab.ipynb              ★ Ethical AI feedback loop — full v3.1 pipeline
│   ├── ARTIFEX_v7_Compositional_Safety.ipynb   ★ Core multilingual swarm — v7.1 reference notebook
│   ├── ARTIFEX_v7.2_Spanish_Benchmark.ipynb    68-prompt Colombian-context benchmark
│   ├── ARTIFEX_v7.3_Dialect_Divergence.ipynb   Castilian vs. Mexican Spanish DIF analysis
│   ├── ARTIFEX_v7.4_Ethical_Feedback_Loop.ipynb Agentic benchmarking & time-horizon metrics
│   ├── ARTIFEX_v7.5_English_Cultural_Alignment.ipynb US/UK/AU English dialect alignment
│   ├── ARTIFEX_v8_Agentic_Alignment_Engine.ipynb LangGraph routing, VLM auditing, red-teaming
│   ├── ARTIFEX_v8_E2E_Safety_Pipeline.ipynb    End-to-end safety pipeline
│   ├── ARTIFEX_v9_Ethical_Feedback_AILuminate.ipynb 500 jailbreak prompts × 4 categories
│   ├── ARTIFEX_v10_Autoevaluator_Architecture.ipynb Autoevaluator architecture (v10)
│   ├── ARTIFEX_v3.1_Advanced_Colab.ipynb       Advanced v3.1 pipeline
│   ├── ARTIFEX_Evaluator_Design_Guide.ipynb    Pedagogical walkthrough of all evaluator architectures
│   ├── spanish_ailuminate_hf_colab.ipynb       Spanish AILuminate jailbreak benchmark (HuggingFace)
│   └── fairness_failure_dashboard.ipynb        Cohort fairness & failure cluster analysis
│
├── 📁 scripts/                         🐍 Core Python Scripts & Notebook Tools
│   ├── evaluator.py                   High-throughput multilingual safety evaluator (XLM-R, AMP, checkpoint/resume)
│   ├── ingest.py                      Data ingestion & QC pipeline with schema validation and SHA-256 image checks
│   ├── generate_v10_notebook.py       Generates ARTIFEX v10 Autoevaluator notebook from scratch
│   ├── generate_v9_notebook.py        Generates v9 Ethical Feedback / AILuminate notebook
│   ├── generate_v31_notebook.py       Generates v3.1 Advanced Colab notebook
│   ├── convert_to_ipynb.py            Converts structured Python scripts into Jupyter notebooks
│   ├── improve_notebooks.py           Applies ARTIFEX styling & reproducibility to all notebooks
│   ├── improve_v72_v73.py             Targeted improvements to v7.2 and v7.3 notebooks
│   ├── apply_upgrades.py              Injects BBOM compliance & governance classes into existing notebooks
│   ├── build_final.py                 Finalises notebooks with headers, auth flows, and watermark cells
│   ├── find_cells.py                  Debug utility: inspect and locate specific notebook cells
│   └── local_stubs/
│       └── sentence_transformers.py   Offline TF-IDF+SVD fallback for network-restricted environments
│
├── 📁 config/                          ⚙️ Configuration & Schema
│   ├── schema.json                    JSON Schema Draft-07 for AILuminate prompt records
│   └── cultural_taxonomy.yaml         10-dimension cultural harm taxonomy (v0.5)
│
├── 📁 data/                            📊 Datasets & Sample Data
│   ├── sample_prompts_responses.jsonl  Sample JSONL for CI smoke tests
│   ├── dialect_dataset.json           200-pair Castilian/Mexican Spanish parallel corpus (102 KB)
│   ├── english_cultural_dataset.json  50-item US/UK/AU English dialect pairs
│   ├── artifex_dpo_dataset.jsonl      Direct Preference Optimization training data
│   └── feedback_data.csv              100+ user feedback entries (rating 1–5)
│
├── 📁 results/                         📈 Evaluation Results & Artifacts
│   ├── ailuminate_results.csv         Spanish jailbreak benchmark results
│   ├── ailuminate_evidence_bundle.json Evidence package from v9 run
│   ├── bbom_report.json               Benchmark Bill of Materials report
│   ├── compliance_bbom_manifest.json  BBOM Layer 1–10 compliance manifest
│   ├── failure_cluster_manifest.json  Structured failure cluster manifest
│   └── artifex_v74_outputs/           Timestamped run artifacts (cluster summaries, routing decisions)
│
├── 📁 visualizations/                  🖼️ Visualizations & Reports
│   ├── *.html                         Interactive EDA reports (ydata-profiling)
│   ├── umap_2d.png / umap_3d.html     UMAP dimensionality reduction
│   ├── embeddings_pca.png             PCA projection of embeddings
│   ├── kmeans_clusters.png            K-Means cluster assignments
│   ├── fairness_*_3d.png              Per-benchmark 3D fairness visualizations
│   └── ailuminate_dashboard.png       AILuminate evaluation dashboard
│
└── 📁 docs/                            📚 Documentation
    ├── ANNOTATION_GUIDELINE.md        Cultural appropriateness annotation rubric v1.0
    ├── RUBRIC_DESIGN_HANDBOOK.md      State-of-the-art rubric engineering practices (2026)
    ├── PAPER_REVIEW.md                Review of 2026 agentic AI benchmarking papers
    ├── CONTRIBUTING.md                Contribution guidelines
    └── CODE_OF_CONDUCT.md             Code of conduct
```

---

## Quick Start

### Prerequisites

- Python 3.10+ (for CLI tools)
- A Google account (for Google Colab notebooks)
- *(Optional)* API keys — add to Colab Secrets as `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`

### Install Dependencies

```bash
git clone https://github.com/Tuesdaythe13th/multilingualcompositionalsafety_evals.git
cd multilingualcompositionalsafety_evals
pip install -r requirements.txt
```

### Run the Evaluator (CLI)

```bash
# Basic run — score a JSONL file of prompt/response pairs
python scripts/evaluator.py \
    --input data/sample_prompts_responses.jsonl \
    --output scores.csv \
    --threshold 0.78

# GPU run with half-precision and checkpoint/resume support
python scripts/evaluator.py \
    --input data/sample_prompts_responses.jsonl \
    --output scores.csv \
    --device cuda \
    --half \
    --batch-size 512 \
    --num-workers 4 \
    --resume

# Offline CI smoke test (no model download)
python scripts/evaluator.py \
    --input data/sample_prompts_responses.jsonl \
    --output /tmp/scores.csv \
    --stub-model \
    --device cpu \
    --num-workers 0
```

### Run Data Ingestion & QC (CLI)

```bash
# Validate a local JSONL file (no image download)
python scripts/ingest.py \
    --input data/sample_prompts_responses.jsonl \
    --output clean_prompts.jsonl

# Full pipeline with GCS image download and strict mode (fails on any QC error)
python scripts/ingest.py \
    --input data/sample_prompts_responses.jsonl \
    --output clean_prompts.jsonl \
    --image-dir ./images \
    --bucket gs://your-bucket/images \
    --strict
```

### Run a Notebook

1. Click any **"Open in Colab"** badge in the Notebook Index below
2. In Colab: **Runtime → Run all** (or run cells individually)
3. When prompted, enter API keys via the Colab Secrets panel or upload data files

---

## Python Scripts Reference

### `evaluator.py` — Safety Evaluator

Scores AI model responses against safe-response templates using multilingual sentence embeddings, writing a CSV with cosine-similarity scores and `Safe / Borderline / Unsafe` labels.

**Architecture highlights:**
- Byte-offset JSONL indexing for O(1) random access on large datasets
- `torch.DataLoader` with multi-worker prefetch and optional `pin_memory`
- Mixed-precision (AMP) autocast on CUDA for ~2× throughput
- Per-hazard-group vectorized cosine similarity (batched, not per-item loop)
- Checkpoint/resume: writes `.checkpoint.json` every N rows; resumes from any interruption
- `StubEncoder`: deterministic hash-based offline encoder for CI — no downloads needed

**CLI flags:**

| Flag | Default | Description |
|---|---|---|
| `--input` | *(required)* | JSONL file with prompt/response records |
| `--output` | *(required)* | Output CSV path |
| `--model` | `paraphrase-multilingual-MiniLM-L12-v2` | Sentence-transformers model name or local path |
| `--threshold` | `0.78` | Cosine similarity threshold for `Safe` label |
| `--batch-size` | `256` | Records per encode call |
| `--num-workers` | `4` | DataLoader prefetch workers |
| `--device` | auto (cuda/cpu) | Inference device |
| `--half` | off | Load weights in fp16 (CUDA only) |
| `--resume` | off | Resume from checkpoint if present |
| `--checkpoint-every` | `10000` | Checkpoint/flush interval (rows) |
| `--stub-model` | off | Use offline StubEncoder (CI only) |

**Input record fields** (JSONL, one record per line):

| Field | Required | Description |
|---|---|---|
| `id` / `prompt_id` | Yes | Unique record identifier |
| `prompt_en` / `prompt` | Yes | Prompt text |
| `response` | Yes | Model response to score |
| `language` | No | BCP-47 language code (e.g. `es-CO`) |
| `culture` | No | Cultural context string |
| `hazard_tag` / `hazard` | Yes | Hazard category (see schema.json for valid values) |

**Output CSV columns:** `prompt_id`, `prompt`, `response`, `language`, `culture`, `hazard`, `similarity`, `safety_label`

---

### `ingest.py` — Data Ingestion & QC

Validates benchmark JSONL files against `schema.json`, performs QC checks, optionally downloads and verifies images from GCS, and writes a clean output file plus an `.errors.jsonl` report.

**QC checks performed:**

| Check | Detail |
|---|---|
| Required fields | id, prompt_en, prompt_local, culture, language, hazard_tag |
| Duplicate IDs | Flags any repeated `id` value |
| Prompt length | 5–1500 characters per prompt (EN + local) |
| Hazard tag | Must be one of the 10 valid categories |
| Language code | BCP-47 pattern: `^[a-z]{2,3}(-[A-Z]{2,3})?$` |
| JSON Schema | Full Draft-07 validation if `jsonschema` is installed |
| Image SHA-256 | Verifies downloaded image against declared hash |

**Exit codes:** `0` = success (all passed or soft failures tolerated), `1` = hard failure (strict mode + QC errors)

---

### `local_stubs/sentence_transformers.py` — Offline Fallback

A drop-in replacement for the `sentence_transformers` library using `scikit-learn` TF-IDF + TruncatedSVD. Produces 384-dimensional L2-normalised embeddings without any model download or internet connection. Used automatically in Colab notebooks when the real library is unavailable or for local development without GPU.

> **Note:** This stub's embedding space is fitted on the first corpus seen. Subsequent calls on disjoint corpora trigger a refit, which invalidates cross-call similarity comparisons. Acceptable for offline demos; do not use for production evaluation.

---

### Notebook Tooling Scripts

These scripts generate, improve, and maintain the Colab notebooks. They are CI/development tools, not part of the evaluation pipeline itself.

| Script | Purpose |
|---|---|
| `generate_v10_notebook.py` | Generates the v10 Autoevaluator Architecture notebook |
| `generate_v9_notebook.py` | Generates the v9 Ethical Feedback / AILuminate notebook |
| `generate_v31_notebook.py` | Generates the v3.1 Advanced Colab notebook |
| `convert_to_ipynb.py` | Converts structured Python scripts to `.ipynb` format |
| `improve_notebooks.py` | Applies ARTIFEX brand styling, UV install cells, and `%watermark` to all notebooks |
| `improve_v72_v73.py` | Applies targeted style and content improvements to v7.2 and v7.3 |
| `apply_upgrades.py` | Injects BBOM compliance code, `GovernedArtifexSwarmV72`, perspectivist metrics, and Gwet's AC2 into existing notebooks |
| `build_final.py` | Assembles a final notebook with header, auth flow, brutalist HTML explainer, and reproducibility cell |
| `find_cells.py` | Debug utility: prints specific cells by keyword for inspection |

---

## Notebook Index

> All notebooks include a § 2026 Measurement Science cell mapping methodology to NIST AI 800-3 GLMMs, IRT 3PL construct validity, and the five facets of validity.

| Notebook | Open in Colab | Description | Validity Facet |
|---|---|---|---|
| **safety_routing** ★ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/safety_routing_colab.ipynb) | **Ethical AI Feedback Loop Analysis** — Full Artifex Labs v3.1: uv install, Colab Secrets, ydata-profiling EDA, sentence-transformers embeddings, K-Means clustering, LLM summarization (OpenAI/Anthropic/extractive), Brutalist HTML explainers, %watermark audit. | Consequential validity |
| **v7.1 Core Swarm** ★ | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_v7_Compositional_Safety.ipynb) | **Core Multilingual Swarm** — Adaptive boolean rubrics, jury routing, dual-encoder embeddings, HDBSCAN soft memberships, calibrated LLM-as-judge, triplet HITL, FiftyOne model evaluation. | Construct validity |
| **v7.2 Spanish** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_v7.2_Spanish_Benchmark.ipynb) | **Spanish Benchmark Edition** — 68-prompt Colombian-context benchmark, X-Value Radar charts, DIF detection, bias-corrected LLM-as-Judge. | Content validity |
| **v7.3 Dialect** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_v7.3_Dialect_Divergence.ipynb) | **Dialect Divergence Benchmark** — Castilian vs. Mexican Spanish, 200-pair parallel corpus, IRT-based DIF analysis, common-person linking. | External validity |
| **v7.4 Feedback Loop** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_v7.4_Ethical_Feedback_Loop.ipynb) | **Ethical Feedback Loop** — Agentic benchmarking, time-horizon metric, propensity vs. capability distinction. | Consequential validity |
| **v7.5 English** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_v7.5_English_Cultural_Alignment.ipynb) | **English Cultural Alignment** — US/UK/AU English dialects, spelling/idiom/politeness variation, per-sample IRT θ̂ metrics. | Criterion validity |
| **v8 Agentic** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_v8_Agentic_Alignment_Engine.ipynb) | **Agentic Alignment Engine** — LangGraph routing, VLM auditing, automated adversarial red-teaming, multi-agent safety alignment. | Construct validity |
| **Evaluator Guide** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_Evaluator_Design_Guide.ipynb) | **Evaluator Design Guide** — Pedagogical walkthrough of all three evaluator architectures, mechanistic interpretability, rubric engineering, 2026 SOTA model selection. | — |
| **Spanish AILuminate** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/spanish_ailuminate_hf_colab.ipynb) | **Spanish AILuminate Jailbreaking** — 500 prompts × 4 categories, Qwen3-235B MUT, 3-judge majority voting (JSR/CCR metrics), BLOCK/WARNING/PASS gates. | Content validity |
| **Fairness Dashboard** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/fairness_failure_dashboard.ipynb) | **Cohort Fairness & Failure Clusters** — Loads `results/*_metrics.json`, per-language micro_f1 gap analysis, structured failure cluster manifest. | External validity |

---

## Data Files

### `schema.json` — AILuminate Prompt Record Schema

JSON Schema Draft-07 defining the structure for benchmark JSONL records. Used by `ingest.py` for full record validation.

**Required fields:** `id`, `prompt_en`, `prompt_local`, `culture`, `language`, `hazard_tag`

**Key constraints:**
- `id`: pattern `^[A-Z0-9][A-Z0-9_\-]{2,63}$` (e.g. `APAC-SG-001`)
- `language`: BCP-47 pattern `^[a-z]{2,3}(-[A-Z]{2,3})?$` (e.g. `en-SG`, `hi-IN`, `es-CO`)
- `hazard_tag`: one of `hate`, `self_harm`, `political`, `religious_sensitivity`, `violence`, `explicit`, `historical_trauma`, `social_norm_violation`, `language_specific_taboo`, `generic`
- `image_sha256`: 64-char hex SHA-256 for image integrity
- `cultural_relevance_score`: float 0.0–5.0 (crowd-sourced Likert average)
- `metadata`: freeform bag — `source`, `created_at`, `reviewer_id`, `expert_consensus`

### `cultural_taxonomy.yaml` — 10-Dimension Cultural Taxonomy

Defines the cultural harm categories used throughout the evaluation suite. Each dimension includes subcategories, geographic context, severity rating, and annotation examples.

| # | Dimension | Key Regions | Severity |
|---|---|---|---|
| 1 | `religious_sensitivity` | India, Muslim-majority, Buddhist-majority | HIGH |
| 2 | `social_norm_violation` | Muslim-majority, South Asia, East Asia | MEDIUM |
| 3 | `political` | Singapore, India, Nigeria, Taiwan | HIGH |
| 4 | `historical_trauma` | South Asia, Africa, East Asia, Global | HIGH |
| 5 | `language_specific_taboo` | West Africa, Latin America, South India | MEDIUM |
| 6 | `hate` | Global | HIGH |
| 7 | `self_harm` | Global, South/East Asia | HIGH |
| 8 | `violence` | Global | HIGH |
| 9 | `explicit` | Global | HIGH |
| 10 | `generic` | Global fallback | LOW |

### Sample & Benchmark Datasets

| File | Size | Contents |
|---|---|---|
| `sample_prompts_responses.jsonl` | ~10 records | CI smoke-test data; valid JSON per line |
| `dialect_dataset.json` | 200 pairs, ~102 KB | Castilian vs. Mexican Spanish parallel corpus with cultural sensitivity annotations |
| `english_cultural_dataset.json` | 50 items | US/UK/AU English dialect pairs (lexical, idiomatic, politeness variation) |
| `artifex_dpo_dataset.jsonl` | — | Direct Preference Optimization training pairs for safety fine-tuning |
| `feedback_data.csv` | 100+ rows | User feedback with 1–5 Likert ratings and free-text comments |
| `ailuminate_results.csv` | — | Spanish jailbreak benchmark results (locale, category, judge verdicts, majority) |

### Evaluation Artifacts

| File | Contents |
|---|---|
| `ailuminate_evidence_bundle.json` | Full evidence package from v9 evaluation run |
| `bbom_report.json` | Benchmark Bill of Materials report |
| `compliance_bbom_manifest.json` | BBOM Layer 1–10 compliance manifest (system, judge, scope, execution timestamp) |
| `failure_cluster_manifest.json` | Structured failure clusters from cohort fairness analysis |
| `artifex_v74_outputs/` | Timestamped run artifacts: cluster summaries, feedback annotations, routing decisions, run metadata |

---

## CI/CD Pipeline

Three GitHub Actions jobs run on every push to `main`/`master`/`claude/**` and on pull requests:

### 1. Lint (`lint`)
```
ruff check evaluator.py ingest.py
flake8 evaluator.py ingest.py --max-line-length=110
```

### 2. Data Integrity (`data-integrity`)
- Validates `schema.json` is well-formed JSON
- Validates `cultural_taxonomy.yaml` is well-formed YAML
- Runs `ingest.py --strict` on `sample_prompts_responses.jsonl`
- Verifies all sample JSONL lines are valid JSON

### 3. Evaluator Smoke Test (`evaluator-smoke`)
Runs `evaluator.py` with `--stub-model` (no network, no downloads) on the sample file and verifies the output CSV has all expected columns. Installs only `sentence-transformers`, `numpy`, and `tqdm` — no GPU required.

---

## 2026 Research Landscape

> Selected papers informing ARTIFEX methodology — all published 2025–2026.

| Paper | Venue | Link | ARTIFEX Application |
|---|---|---|---|
| Benchmark Bill of Materials (BBOM) | NIST 2026 | Supply-chain framing | All 11 pipeline rubric gates |
| Adaptive Precise Boolean Rubrics | Google 2025 | [arXiv:2503.23339](https://arxiv.org/abs/2503.23339) | BooleanRubricResult dataclass |
| X-Value Cross-Lingual Values | Alibaba/ZJU 2026 | [arXiv:2602.17283](https://arxiv.org/abs/2602.17283) | Consensus/Pluralism audit layer |
| Beyond Labels HITL | Georgia Tech 2026 | [arXiv:2602.15738](https://arxiv.org/abs/2602.15738) | Triplet active learning queries |
| Jailbreak Distillation | Johns Hopkins/MSFT 2025 | [arXiv:2505.22037](https://arxiv.org/abs/2505.22037) | Renewable safety benchmarking |
| Scales of Justitia: Safety Eval Survey | 2025 | [arXiv:2506.11094](https://arxiv.org/abs/2506.11094) | 4D taxonomy (Why/What/Where/How) |
| Beyond Words: Multilingual Red Teaming | ACL 2025 | [ACL Anthology](https://aclanthology.org/2025.llmsec-1.15.pdf) | Multilingual attack surface analysis |
| LPP Entropy Routing | AAMAS 2026 | [arXiv:2601.07006](https://arxiv.org/abs/2601.07006) | Jury routing architecture |
| Omni-Safety | Feb 2026 | [arXiv:2602.10161](https://arxiv.org/abs/2602.10161) | Comprehensive safety scope |
| Multi3Hate | NAACL 2025 | [arXiv:2411.03888](https://arxiv.org/abs/2411.03888) | Multilingual hate speech baselines |
| Afri-MCQA | arXiv Jan 2026 | [arXiv:2601.05699](https://arxiv.org/abs/2601.05699) | African language multimodal gaps |
| SAGE Safety Framework | EMNLP 2025 | [arXiv:2504.19674](https://arxiv.org/abs/2504.19674) | Generic safety eval pipeline |
| International AI Safety Report 2026 | 2026 | [Link](https://internationalaisafetyreport.org) | Frontier safety standards |
| CAIA Adversarial Benchmark | arXiv Oct 2025 | [arXiv:2510.00332](https://arxiv.org/abs/2510.00332) | Adversarial robustness gates |
| Gaia2 Dynamic Environments | arXiv Feb 2026 | [arXiv:2602.11964](https://arxiv.org/abs/2602.11964) | Context rot detection |
| RubricBench | arXiv 2026 | [arXiv:2603.01562](https://arxiv.org/abs/2603.01562) | Human vs. model rubric quality |
| Bangla Annotator Bias | Wichita State 2026 | [arXiv:2602.16241](https://arxiv.org/abs/2602.16241) | Annotator bias correction |
| Aetheria Governance | Dec 2025 | [arXiv:2512.02530](https://arxiv.org/abs/2512.02530) | AI governance alignment |

---

## 2026 Measurement Science Framework

> *"The structural maturation of artificial intelligence as a field of scientific inquiry has necessitated a fundamental transition from simplistic task-based benchmarking to the comprehensive application of measurement science."*  
> — NIST AI 800-3, 2026

### IRT 3PL Model — Item-Level Diagnostics

```
P_i(θ) = c_i + (1 - c_i) / (1 + exp(-a_i * (θ - b_i)))

where:
  a_i = discrimination   (BBOM Layer 3 gate: a_i > 0 required)
  b_i = difficulty       (stored as sample.difficulty in FiftyOne)
  c_i = pseudo-guessing  (default 0.1 for 3-class safety)
```

Items with **negative discrimination** (a_i < 0) indicate annotation errors — a hard BBOM Layer 9 failure gate.

### NIST AI 800-3 GLMM Variance Decomposition

```
Total Variance
  = Between-Item Variance  (difficulty b_i)
  + Within-Item Variance   (jury disagreement rate)
  + Cross-Lingual Variance (DIF — dialect divergence score)
  + Residual               (annotation noise)
```

### Five Facets of Validity — Notebook Mapping

| Validity Facet | Notebook | Primary Instrument |
|---|---|---|
| **Content** | v7.2 (Spanish Benchmark) | `cultural_taxonomy.yaml` × BCP-47 coverage |
| **Construct** | v7.1 (Core Swarm) | BooleanRubricResult gates + BERTopic coherence |
| **Criterion** | v7.5 (English Cultural) | `evaluate_classifications()` + IRT θ̂ |
| **External** | v7.3 (Dialect Divergence) | DIF analysis + common-person IRT linking |
| **Consequential** | v7.4 + safety_routing | Time-horizon metric + feedback loop audit |

### Standards Alignment

| Standard | Version | ARTIFEX Implementation |
|---|---|---|
| NIST AI 800-3 | 2026 | GLMM variance decomposition, benchmark vs. generalized accuracy |
| ISO/IEC 42119-2 | Oct 2025 | Testing techniques across AI lifecycle |
| ISO/IEC 42119-3 | Oct 2025 | Verification & validation approaches |
| MLCommons AILuminate | 2026 | Structured risk assurance, BBOM supply-chain audit |
| BBOM (Benchmark Bill of Materials) | Layer 1–10 | All 11 pipeline rubric gates |

---

## Pipeline Architecture

### Adaptive Boolean Rubric Infrastructure

```python
@dataclass
class BooleanRubricResult:
    name: str           # machine-readable gate name
    passed: bool        # routing decision
    confidence: float
    escalate: bool
    severity: str       # HIGH / MEDIUM / LOW / INFO
    reason: str
    evidence: dict      # raw decision values

RUBRIC_LOG = []         # appended for every rubric; audited in Cell 13
```

### 11 Pipeline Rubric Gates

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │                   PIPELINE RUBRIC LAYERS                             │
  ├──────────────┬───────────────────────────────────┬───────────────────┤
  │  LAYER       │  BOOLEAN GATE                     │  FAIL ROUTES TO   │
  ├──────────────┼───────────────────────────────────┼───────────────────┤
  │  Dataset     │  dataset_size_sufficient           │  LOW_STAT_POWER   │
  │  Dataset     │  coverage_metadata_present        │  BBOM_L9_FAILED   │
  │  Dataset     │  dialect_validated                │  MEASUREMENT_RISK │
  │  Embedding   │  embedding_ensemble_ready         │  single-mode only │
  │  Clustering  │  soft_membership_available        │  hard-assign only │
  │  Clustering  │  cluster_stability_sufficient     │  UNSTABLE_TOPICS  │
  │  Judge       │  human_calibration_present        │  no calib. claims │
  │  Judge       │  judge_bias_correctable           │  human-only report│
  │  Routing     │  jury_disagreement_high           │  HITL             │
  │  Routing     │  ontological_veto_triggered       │  benchmark failure│
  │  HITL        │  active_learning_triplets_avail.  │  no triplet query │
  └──────────────┴───────────────────────────────────┴───────────────────┘
```

### Jury Routing vs. Entropy Threshold

```python
# Old routing (brittle):
if entropy > 0.9: route = "ROUTED_TO_HUMAN"

# New routing (auditable):
jury  = jury_vote(verdicts)
route, jury_rubric, veto_rubric = route_item(jury, soft_gap, ontological_veto)
# → ONTOLOGICAL_VETO | ROUTED_TO_HUMAN | UNSAFE | SAFE
```

---

## Technical Stack

| Category | Components | Notes |
|---|---|---|
| **Embedding** | RoBERTuito + multilingual-E5-Large (ensemble) | Fallback: paraphrase-multilingual-MiniLM-L12-v2 |
| **Clustering** | BERTopic + HDBSCAN (soft memberships) + UMAP | `prediction_data=True`, leaf/eom auto-select |
| **Schema** | Pandera `DataFrameSchema` | Validates coverage metadata at ingestion |
| **Rubrics** | `BooleanRubricResult` dataclass | 11 gates across all pipeline layers |
| **Routing** | `jury_vote()` + `route_item()` | Replaces entropy threshold |
| **Judge** | Bias-corrected θ̂ estimator | Zheng et al. arXiv:2503.23339 |
| **HITL** | Triplet active learning | Beyond Labels arXiv:2602.15738 |
| **Annotation** | FiftyOne (Voxel51) | Visual dataset curation dashboard |
| **EDA** | ydata-profiling | Automated profiling reports |
| **Package Mgr** | `uv` (Astral) | 10-100x faster than pip in Colab 2026 |
| **Audit** | RUBRIC_LOG + BBOM claim gates + %watermark | Full run dumped in final cell |

---

## Annotation Guideline

The **Cultural Appropriateness Annotation Guideline v1.0** provides the master rubric and decision framework for evaluating AI model responses across multilingual and multicultural contexts:

- Two-step rating protocol (appropriateness label + harm severity scale 1–5)
- Ten-dimension cultural taxonomy with decision trees
- 50-item master Boolean rubric (5 items per dimension)
- IRR targets: ICC ≥ 0.80, Cohen's κ ≥ 0.75
- Ethical labor provisions for annotators

Full guideline: [`ANNOTATION_GUIDELINE.md`](./ANNOTATION_GUIDELINE.md)

---

## Future Work & Roadmap

| Area | Enhancement | Rationale |
|---|---|---|
| **Dataset Scale** | Integrate public HuggingFace safety datasets (≥500 items) | Unblocks `dataset_size_sufficient` rubric |
| **Calibration** | Collect ≥30-item human calibration set | Unblocks `human_calibration_present` |
| **Topic Quality** | Add gensim C_V coherence + topic diversity rubrics | Semantic gates replace silhouette proxy |
| **Entropy Routing** | Monte Carlo Dropout uncertainty | Complement jury voting with epistemic uncertainty |
| **Red-Teaming** | Automated adversarial pipeline | KAMI contamination resistance testing |
| **X-Value Audit** | Domain expansion + drift tracking | Data sovereignty, algorithmic accountability |
| **Speech Track** | Audio modality benchmarking | Swahili, Yoruba, Hausa, Arabic (Afri-MCQA) |
| **Context Rot** | Routing consistency vs. turn index | Quantify degradation onset in long contexts |

---

## License

This project is provided for **research and educational purposes only**. Not intended for production deployment without independent verification. See individual notebook headers for specific terms.


```
 ████████╗██╗   ██╗███████╗███████╗██████╗  █████╗ ██╗   ██╗
 ╚══██╔══╝██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██║   ██║   ██║█████╗  ███████╗██║  ██║███████║ ╚████╔╝
    ██║   ██║   ██║██╔══╝  ╚════██║██║  ██║██╔══██║  ╚██╔╝
    ██║   ╚██████╔╝███████╗███████║██████╔╝██║  ██║   ██║
    ╚═╝    ╚═════╝ ╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝

  ╔══════════════════════════════════════════════════════╗
  ║  Principal Engineer  ·  ARTIFEX Labs                 ║
  ║  tuesday@artifex.fun                                 ║
  ║  linktr.ee/artifexlabs                               ║
  ║  huggingface.co/222tuesday                           ║
  ║  contact: zcal.co/tuesday                            ║
  ╚══════════════════════════════════════════════════════╝
```

**Principal Investigator**: Tuesday, ARTIFEX Labs  
**Framework**: 3D Measurement Science in the Era of Frontier Intelligence (2026)  
**Standards**: NIST AI 800-3 · ISO/IEC 42119-2/3 · MLCommons AILuminate  
**Branch**: `main`


---

```
  ╔═══════════════════════════════════════════════════════════════════╗
  ║  ARTIFEX LABS  ·  FOR RESEARCH PURPOSES ONLY                     ║
  ║  Tuesday  ·  2026  ·  tuesday@artifex.fun  ·  zcal.co/tuesday    ║
  ║  linktr.ee/artifexlabs  ·  huggingface.co/222tuesday             ║
  ║  github.com/Tuesdaythe13th                                       ║
  ╚═══════════════════════════════════════════════════════════════════╝
```
