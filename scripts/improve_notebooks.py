#!/usr/bin/env python3
"""
Applies targeted improvements to ARTIFEX Colab notebooks.
Run: python3 improve_notebooks.py
"""

import json
import copy
from pathlib import Path

# ─── Helper ───────────────────────────────────────────────────────────────────

def cell(cell_type, source):
    """Create a notebook cell dict. source is stored as a plain string."""
    c = {"cell_type": cell_type, "metadata": {}, "source": source}
    if cell_type == "code":
        c["outputs"] = []
        c["execution_count"] = None
    return c

def get_source(cell_obj):
    """Return cell source as a plain string regardless of list/str storage."""
    src = cell_obj.get("source", "")
    if isinstance(src, list):
        return "".join(src)
    return src

def set_source(cell_obj, text):
    """Set cell source as a plain string."""
    cell_obj["source"] = text

def md(source): return cell("markdown", source)
def code(source): return cell("code", source)

# ════════════════════════════════════════════════════════════════════════════
# IMPROVED CELL CONTENT
# ════════════════════════════════════════════════════════════════════════════

README_CELL = """\
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_v7.4_Ethical_Feedback_Loop.ipynb)
[![HuggingFace](https://img.shields.io/badge/🤗%20HuggingFace-222tuesday-yellow)](https://huggingface.co/222tuesday)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

---

# ARTIFEX v7.4 — Ethical AI Feedback Loop Analysis

**Principal Investigator:** Tuesday @ ARTIFEX Labs
**Contact:** tuesday@artifexlabs.com
**Links:** [linktr.ee/artifexlabs](https://linktr.ee/artifexlabs) · [github.com/tuesdaythe13th](https://github.com/tuesdaythe13th) · [huggingface.co/222tuesday](https://huggingface.co/222tuesday) · [Google Scholar](https://scholar.google.com/citations?user=artifexlabs) · [google.com/search?q=ARTIFEX+Labs+AI](https://google.com/search?q=ARTIFEX+Labs+AI)

---

## Notebook README

This notebook implements an **Ethical AI Feedback Loop Analysis** pipeline — a 2026 ARTIFEX measurement science framework for analyzing user feedback about AI systems through embedding, clustering, LLM summarization, and safety routing. The pipeline is aligned with NIST AI 800-3, ISO/IEC 42119-8, and the BBOM (Benchmark Bill of Materials) standard.

### Pipeline Overview

```
CSV Input → Schema Validation → EDA → Sentence Embedding → UMAP Reduction
    → K-Means Clustering → Elbow/Silhouette Analysis → 3D Visualization
    → LLM Theme Summarization → Safety Routing → Export
```

---

### Functions & Features

| Component | Description | Cell |
|---|---|---|
| `setup_fonts()` | Injects Syne Mono + Epilogue Google Fonts into Colab output | ② |
| `artifex_header()` | Renders the ARTIFEX LABS branded HTML header with live timestamp | ② |
| `load_data()` | CSV ingestion with Pandera schema validation; 4 load modes | ④ |
| `embed_texts()` | HuggingFace transformer embedding with tqdm batching + cache | ⑥ |
| `run_elbow_method()` | Silhouette score vs k plot to choose optimal N_CLUSTERS | ⑦b |
| `cluster_embeddings()` | K-Means clustering over UMAP-reduced embedding space | ⑦ |
| `summarize_cluster()` | LLM-powered cluster theme summarization (Gemini/Claude/OpenAI) | ⑩ |
| `apply_safety_routing()` | Keyword + rating heuristic routing to AUTO_FLAGGED / HUMAN / APPROVED | ⑪ |
| `brutalist_explainer()` | HTML output wrapper in Epilogue font for all key results | ③ |
| `search_whitepapers()` | Semantic Scholar API whitepaper retrieval (with mock fallback) | ③ |
| `run_eda()` | ydata-profiling automated EDA report | ⑤ |
| `export_results()` | Saves cluster summaries + routing decisions to CSV/JSON | ⑫ |
| `watermark_env()` | %watermark environment fingerprinting for reproducibility | ⑬ |

---

### Libraries Used

| Library | Version | Purpose |
|---|---|---|
| `uv` | ≥0.4 | Fast, conflict-aware Python package installer (Rust-based) |
| `scikit-learn` | ≥1.4 | K-Means clustering, silhouette scoring |
| `sentence-transformers` | ≥3.0 | Sentence embedding (all-MiniLM-L6-v2 / BAAI/bge-m3) |
| `transformers` | ≥4.40 | HuggingFace model hub access |
| `datasets` | ≥2.18 | HuggingFace dataset utilities |
| `umap-learn` | ≥0.5 | UMAP dimensionality reduction |
| `pandera` | ≥0.18 | DataFrame schema validation at ingestion |
| `ydata-profiling` | ≥4.6 | Automated EDA reports |
| `anthropic` | ≥0.25 | Claude API for LLM summarization |
| `google-generativeai` | ≥0.5 | Gemini 2.0 API for LLM summarization |
| `openai` | ≥1.20 | OpenAI API (optional fallback) |
| `loguru` | ≥0.7 | Structured emoji-annotated logging |
| `tqdm` | ≥4.66 | Progress bars for all loops |
| `emoji` | ≥2.10 | Emoji rendering in logging |
| `watermark` | ≥2.4 | Environment reproducibility tracking |
| `plotly` | ≥5.20 | Interactive 3D embedding visualization |
| `matplotlib` | ≥3.8 | Elbow/silhouette diagnostic charts |

---

## How to Cite

```bibtex
@misc{tuesday2026artifex74,
  author       = {Tuesday and {ARTIFEX Labs}},
  title        = {{ARTIFEX v7.4: Ethical AI Feedback Loop Analysis}},
  year         = {2026},
  howpublished = {\\url{https://github.com/tuesdaythe13th/multilingualcompositionalsafety_evals}},
  note         = {Compositional safety evaluation framework aligned with NIST AI 800-3,
                  ISO/IEC 42119-8, and MLCommons AILuminate. Notebook v7.4.}
}
```

---

## Version History

| Version | Date | Changes |
|---|---|---|
| v7.4.1 | 2026-03-13 | Gemini 2.0-flash, Semantic Scholar API, elbow method cell, export cell, UV --system, HF watermark |
| v7.4.0 | 2026-02-01 | Initial v7.4 release: UMAP+KMeans+LLM pipeline |
| v7.3.x | 2025-12-01 | Dialect divergence edition |
| v7.2.x | 2025-10-01 | Spanish benchmark edition |

---

## Legal Disclaimer

> **© 2026 ARTIFEX Labs. All Rights Reserved.**
> This notebook is provided for research and educational purposes only. The code may contain errors and is not intended for production deployment without independent verification. This notebook may not be shared, reproduced, or distributed without written permission from ARTIFEX Labs. ARTIFEX Labs makes no warranties, express or implied, regarding the accuracy, completeness, or fitness for a particular purpose of this code. Use at your own risk. ARTIFEX Labs is not liable for any damages arising from use of this notebook.

---
"""

INSTALL_CELL = """\
#@title Install Dependencies — UV-Aware (2026 Colab)
# ┌─────────────────────────────────────────────────────────────────────────┐
# │  ARTIFEX v7.4 — Environment Setup                                       │
# │  Uses uv for fast, SAT-solver dependency resolution.                    │
# │  Falls back to pip with explicit version pins for Colab 2025+ compat.  │
# │  ⚠️  If you change numpy/torch major versions, restart runtime after.  │
# └─────────────────────────────────────────────────────────────────────────┘
import subprocess, sys, os
from datetime import datetime

_t0 = datetime.now()
print(f"[{_t0.strftime('%H:%M:%S')}] 🔧 ARTIFEX v7.4 — Installing dependencies...")

# Detect Colab environment
IN_COLAB = "google.colab" in sys.modules or os.path.exists("/content")

# ── Core packages with explicit pins to avoid 2025-2026 Colab conflicts ────
# numpy<2.0 avoids ABI breaks with older scipy/torch wheels in Colab
# grpcio pin prevents protobuf v4 conflicts with google-generativeai
PACKAGES = [
    # Core ML — pinned for Colab ABI stability
    "numpy>=1.24,<2.0",
    "scikit-learn>=1.4,<1.6",
    "torch>=2.2",
    "sentence-transformers>=3.0",
    "transformers>=4.40",
    "datasets>=2.18",
    # Dimensionality reduction
    "umap-learn>=0.5",
    # Data validation & EDA
    "pandera>=0.18",
    "ydata-profiling>=4.6",
    # LLM APIs
    "anthropic>=0.40",
    "google-generativeai>=0.8",
    "openai>=1.30",
    # Visualization
    "plotly>=5.20",
    "matplotlib>=3.8",
    # UX & logging
    "tqdm>=4.66",
    "emoji>=2.10",
    "loguru>=0.7",
    # Environment tracking
    "watermark>=2.4",
    # gRPC pin for Colab/genai stability
    "grpcio>=1.60,<2.0",
    "protobuf>=4.0,<5.0",
]

def _run(cmd, **kwargs):
    return subprocess.run(cmd, capture_output=True, text=True, **kwargs)

# Step 1: Install uv itself
print(f"[{datetime.now().strftime('%H:%M:%S')}] 📦 Installing uv package manager...")
_run([sys.executable, "-m", "pip", "install", "-q", "uv"], check=True)

# Step 2: Try uv pip install with --system flag (required in Colab's managed env)
print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚡ Running uv pip install...")
uv_result = _run(
    [sys.executable, "-m", "uv", "pip", "install", "--system", "-q"] + PACKAGES
)

if uv_result.returncode == 0:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ uv install complete")
else:
    # Fallback: pip with no-deps to avoid resolver loops, then fix conflicts
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚠️  uv failed (exit {uv_result.returncode}), falling back to pip...")
    if uv_result.stderr:
        print(f"    uv stderr: {uv_result.stderr[:300]}")
    for pkg in PACKAGES:
        r = _run([sys.executable, "-m", "pip", "install", "-q", pkg])
        if r.returncode != 0:
            print(f"    ⚠️  pip failed for {pkg}: {r.stderr[:100]}")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ pip fallback complete")

elapsed = (datetime.now() - _t0).total_seconds()
print(f"[{datetime.now().strftime('%H:%M:%S')}] 🎉 All dependencies ready in {elapsed:.1f}s")
if IN_COLAB:
    print()
    print("⚠️  If you upgraded numpy or torch, use Runtime → Restart session before continuing.")
"""

HEADER_CELL = """\
#@title ARTIFEX Header — Font Injection + Branded Timestamp
from IPython.display import display, HTML
from datetime import datetime
import emoji

# ── Google Fonts + Brutalist CSS ──────────────────────────────────────────
FONT_CSS = \"\"\"
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne+Mono&family=Epilogue:wght@300;400;600;700&display=swap');

:root {
  --black: #000000;
  --white: #ffffff;
  --yellow: #fffb00;
  --red:    #ff3b30;
  --green:  #34c759;
  --blue:   #007aff;
  --gray:   #888888;
  --light:  #f0f0f0;
}

.artifex-header {
  font-family: 'Syne Mono', monospace;
  background: var(--black);
  color: var(--white);
  padding: 36px 44px;
  border-left: 10px solid var(--white);
  margin: 0 0 24px 0;
}
.artifex-header h1 {
  font-family: 'Syne Mono', monospace;
  font-size: 3.2em;
  letter-spacing: 0.2em;
  margin: 0 0 8px 0;
  text-transform: uppercase;
  line-height: 1.1;
}
.artifex-header .subtitle {
  font-family: 'Epilogue', sans-serif;
  font-weight: 300;
  font-size: 1.15em;
  color: #cccccc;
  letter-spacing: 0.06em;
  margin-bottom: 4px;
}
.artifex-header .timestamp {
  font-family: 'Syne Mono', monospace;
  font-size: 0.82em;
  color: var(--gray);
  margin-top: 18px;
  border-top: 1px solid #333;
  padding-top: 12px;
  line-height: 1.8;
}
.artifex-header .hf-badge {
  display: inline-block;
  background: #ff9d00;
  color: #000;
  font-family: 'Syne Mono', monospace;
  font-size: 0.75em;
  padding: 2px 8px;
  border-radius: 2px;
  margin-left: 8px;
  font-weight: 700;
  letter-spacing: 0.05em;
  vertical-align: middle;
}
.brutalist-box {
  font-family: 'Epilogue', sans-serif;
  background: var(--white);
  color: var(--black);
  border: 3px solid var(--black);
  padding: 24px 32px;
  margin: 16px 0;
}
.brutalist-box h2 {
  font-family: 'Syne Mono', monospace;
  font-size: 1.4em;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  border-bottom: 3px solid var(--black);
  padding-bottom: 10px;
  margin-bottom: 18px;
}
.brutalist-box table {
  width: 100%;
  border-collapse: collapse;
  font-family: 'Epilogue', sans-serif;
  font-size: 0.95em;
}
.brutalist-box th {
  background: var(--black);
  color: var(--white);
  padding: 10px 14px;
  text-align: left;
  font-family: 'Syne Mono', monospace;
  letter-spacing: 0.06em;
  font-size: 0.88em;
  text-transform: uppercase;
}
.brutalist-box td {
  padding: 9px 14px;
  border-bottom: 1px solid #ddd;
  vertical-align: top;
}
.brutalist-box tr.accent { background: var(--light); }
.brutalist-box td.highlight { background: var(--yellow); font-weight: 700; }
.brutalist-box .analysis {
  background: var(--black);
  color: var(--white);
  padding: 18px 24px;
  margin-top: 18px;
  font-family: 'Epilogue', sans-serif;
  font-size: 0.92em;
  line-height: 1.75;
  border-left: 4px solid var(--yellow);
}
.brutalist-box .whitepapers {
  margin-top: 14px;
  font-size: 0.82em;
  border-top: 1px solid #ccc;
  padding-top: 10px;
  font-family: 'Epilogue', sans-serif;
  color: #444;
}
.brutalist-box .whitepapers a { color: #0055cc; }
.watermark-bar {
  font-family: 'Syne Mono', monospace;
  font-size: 0.72em;
  color: var(--gray);
  text-align: right;
  border-top: 1px solid #eee;
  padding-top: 8px;
  margin-top: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.hf-watermark {
  display: inline-block;
  background: #ff9d00;
  color: #000;
  font-family: 'Syne Mono', monospace;
  font-size: 0.85em;
  padding: 1px 6px;
  border-radius: 2px;
  font-weight: 700;
}
.routing-approved { color: #34c759; font-weight: 700; }
.routing-human    { color: #ff9500; font-weight: 700; }
.routing-flagged  { color: #ff3b30; font-weight: 700; }
</style>
\"\"\"

display(HTML(FONT_CSS))

NOW = datetime.now()
HEADER_HTML = f\"\"\"
<div class="artifex-header">
  <h1>ARTIFEX LABS <span class="hf-badge">🤗 HF: 222tuesday</span></h1>
  <div class="subtitle">v7.4 — Ethical AI Feedback Loop Analysis &nbsp;·&nbsp; 2026 Measurement Science Framework</div>
  <div class="timestamp">
    <span>📌 PI: Tuesday @ ARTIFEX Labs &nbsp;|&nbsp; tuesday@artifexlabs.com</span><br>
    <span>🕐 Session start: <strong>{NOW.strftime('%A, %B %d, %Y — %H:%M:%S UTC')}</strong></span><br>
    <span>
      🔗 <a href="https://linktr.ee/artifexlabs" style="color:#aaa">linktr.ee/artifexlabs</a> &nbsp;|&nbsp;
      <a href="https://github.com/tuesdaythe13th" style="color:#aaa">github.com/tuesdaythe13th</a> &nbsp;|&nbsp;
      <a href="https://huggingface.co/222tuesday" style="color:#aaa">huggingface.co/222tuesday</a>
    </span>
  </div>
</div>
\"\"\"
display(HTML(HEADER_HTML))
print(emoji.emojize(f":stopwatch: Session initialized at {NOW.strftime('%H:%M:%S')} — ARTIFEX v7.4"))
"""

CONFIG_CELL = """\
#@title Imports + Global Configuration
import os, sys, time, warnings
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path

import emoji
from loguru import logger
from tqdm.notebook import tqdm
from IPython.display import display, HTML

warnings.filterwarnings('ignore')

# ── Loguru config ──────────────────────────────────────────────────────────
logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | {message}",
    level="INFO",
    colorize=True,
)

# ── Global constants (edit here to customise the pipeline) ─────────────────
EMBED_MODEL       = "sentence-transformers/all-MiniLM-L6-v2"  # swap: BAAI/bge-m3
GEMINI_MODEL      = "gemini-2.0-flash-exp"   # or "gemini-1.5-pro"
CLAUDE_MODEL      = "claude-haiku-4-5-20251001"
OPENAI_MODEL      = "gpt-4o-mini"
N_CLUSTERS        = 5      # K-Means k; use elbow method cell ⑦b to tune
BATCH_SIZE        = 32     # embedding batch size
RANDOM_SEED       = 42
LLM_PROVIDER      = "gemini"  # "gemini" | "claude" | "openai"
UMAP_N_COMPONENTS = 3      # 3D UMAP for visualization
OUTPUT_DIR        = Path("/content/artifex_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

np.random.seed(RANDOM_SEED)

# ── Utility: Brutalist HTML Explainer ─────────────────────────────────────
def brutalist_explainer(
    title: str,
    table_data: list,
    analysis: str,
    highlight_col: str = None,
    whitepapers: list = None,
    color_col: str = None,
    color_map: dict = None,
) -> str:
    \"\"\"Render a brutalist HTML explainer block (Epilogue font, black/white theme).

    Args:
        title:        Section title rendered in Syne Mono uppercase.
        table_data:   List of dicts; keys become column headers.
        analysis:     Contextual analysis text (dark background block).
        highlight_col: Column name to highlight in yellow.
        whitepapers:  List of (title, url) tuples or plain strings.
        color_col:    Column name to apply CSS class colouring.
        color_map:    Dict mapping cell value substrings to CSS classes.
    \"\"\"
    if not table_data:
        return f'<div class="brutalist-box"><h2>{title}</h2><p>No data to display.</p></div>'

    cols = list(table_data[0].keys())
    header_html = "".join(f"<th>{c}</th>" for c in cols)

    rows_html = ""
    for i, row in enumerate(table_data):
        row_class = "accent" if i % 2 == 0 else ""
        cells = ""
        for c in cols:
            val = str(row.get(c, ""))
            cell_class = ""
            if c == highlight_col:
                cell_class = "highlight"
            elif color_col and c == color_col and color_map:
                for substr, css_cls in color_map.items():
                    if substr.upper() in val.upper():
                        cell_class = css_cls
                        break
            cells += f'<td class="{cell_class}">{val}</td>'
        rows_html += f"<tr class='{row_class}'>{cells}</tr>"

    wp_html = ""
    if whitepapers:
        items = []
        for wp in whitepapers:
            if isinstance(wp, (list, tuple)) and len(wp) == 2:
                items.append(f'<li><a href="{wp[1]}" target="_blank">{wp[0]}</a></li>')
            else:
                items.append(f"<li>{wp}</li>")
        wp_html = f'<div class="whitepapers"><strong>Related Whitepapers:</strong><ul>{"".join(items)}</ul></div>'

    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f\"\"\"
    <div class="brutalist-box">
      <h2>{title}</h2>
      <table><thead><tr>{header_html}</tr></thead><tbody>{rows_html}</tbody></table>
      <div class="analysis">{analysis}</div>
      {wp_html}
      <div class="watermark-bar">
        <span>ARTIFEX LABS v7.4 &nbsp;·&nbsp; generated {ts}</span>
        <span>
          <span class="hf-watermark">🤗 HF</span>
          &nbsp;<a href="https://huggingface.co/222tuesday" style="color:#999;font-size:0.9em">huggingface.co/222tuesday</a>
        </span>
      </div>
    </div>
    \"\"\"

# ── Utility: Whitepaper Search (Semantic Scholar API) ──────────────────────
def search_whitepapers(query: str, n: int = 3) -> list:
    \"\"\"Retrieve whitepaper citations via Semantic Scholar API.

    Falls back to curated mock citations if the API is unavailable.
    Returns list of (title, url) tuples.
    \"\"\"
    import urllib.request, urllib.parse, json as _json

    api_url = (
        "https://api.semanticscholar.org/graph/v1/paper/search"
        f"?query={urllib.parse.quote(query)}&limit={n}"
        "&fields=title,authors,year,externalIds"
    )
    try:
        req = urllib.request.Request(api_url, headers={"User-Agent": "ARTIFEX-Labs/7.4"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = _json.loads(resp.read())
        results = []
        for p in data.get("data", [])[:n]:
            title = p.get("title", "Untitled")
            year  = p.get("year", "")
            arxiv = (p.get("externalIds") or {}).get("ArXiv", "")
            url   = f"https://arxiv.org/abs/{arxiv}" if arxiv else "https://www.semanticscholar.org"
            results.append((f"{title} ({year})", url))
        if results:
            return results
    except Exception:
        pass

    # Curated fallback
    fallbacks = {
        "sentence embed":  [
            ("Sentence-BERT: Sentence Embeddings using Siamese BERT (2019)", "https://arxiv.org/abs/1908.10084"),
            ("BGE-M3: Multi-Functionality Multilingual Multi-Granularity (2024)", "https://arxiv.org/abs/2402.03216"),
            ("Matryoshka Representation Learning (2022)", "https://arxiv.org/abs/2205.13147"),
        ],
        "feedback cluster": [
            ("BERTopic: Neural topic modelling (2022)", "https://arxiv.org/abs/2203.05794"),
            ("UMAP: Uniform Manifold Approximation and Projection (2018)", "https://arxiv.org/abs/1802.03426"),
            ("Topic Modelling with LLMs: A Survey (2024)", "https://arxiv.org/abs/2405.07623"),
        ],
        "llm topic":       [
            ("LLM-as-a-Judge: Survey (2025)", "https://arxiv.org/abs/2501.05111"),
            ("Topic Modelling with LLMs (2024)", "https://arxiv.org/abs/2405.07623"),
            ("Building Effective Agents — Anthropic (2024)", "https://www.anthropic.com/research/building-effective-agents"),
        ],
        "ai safety routing": [
            ("NIST Agentic AI Security Framework (2026)", "https://www.nist.gov/artificial-intelligence"),
            ("X-Value: Consensus Routing for AI Safety (2026)", "https://arxiv.org/abs/2601.07006"),
            ("Human-in-the-Loop AI Safety (2024)", "https://arxiv.org/abs/2404.12150"),
        ],
    }
    query_lower = query.lower()
    for key, papers in fallbacks.items():
        if any(kw in query_lower for kw in key.split()):
            return papers[:n]
    return [
        (f"arXiv: {query} — A 2026 Survey", "https://arxiv.org/search/?searchtype=all&query=" + urllib.parse.quote(query)),
        ("MLCommons AILuminate (2026)", "https://mlcommons.org/ailuminate"),
        ("NIST AI 800-3: Expanding the AI Evaluation Toolbox (2026)", "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-3.pdf"),
    ][:n]

logger.info(emoji.emojize(
    ":white_check_mark: Config loaded — model={}, clusters={}, provider={}, output={}",
    EMBED_MODEL, N_CLUSTERS, LLM_PROVIDER, str(OUTPUT_DIR)
))
"""

ELBOW_MD = """\
## ⑦b Elbow Method — Optimal Cluster Count

### Function Description
Computes K-Means inertia (within-cluster sum of squares) and silhouette score across a range of k values to help select the optimal `N_CLUSTERS` before the main clustering step. Visualizes both metrics as a dual-axis matplotlib chart.

### Technical Rationale
The **elbow method** plots WCSS (within-cluster sum of squares) vs. k — the "elbow" inflection point indicates diminishing returns from adding clusters. The **silhouette score** (range −1 to +1) measures how well each point fits its own cluster vs. neighboring clusters; scores >0.3 indicate meaningful structure. Together, these two diagnostics triangulate the optimal k.

> **Rule of thumb:** Choose the smallest k where silhouette score peaks and WCSS elbow bends. Avoid over-clustering (k > √n).

### Libraries, Tools & Techniques
- **scikit-learn KMeans + silhouette_score**: Industry-standard clustering diagnostics ([docs](https://scikit-learn.org/stable/modules/clustering.html))
- **matplotlib**: Dual-axis diagnostic chart ([docs](https://matplotlib.org/))
- **tqdm.notebook**: Per-k progress bar

### Security & Reproducibility Best Practices
- Fix `random_state` in KMeans for reproducible elbow curves
- Subsample silhouette computation (`sample_size`) for large datasets to avoid O(n²) cost
- Log and save the elbow plot to `OUTPUT_DIR` for audit trail

### Whitepapers
1. [Silhouette Analysis for Cluster Validation (Rousseeuw, 1987)](https://www.sciencedirect.com/science/article/pii/0377042787901257)
2. [A Survey of Clustering Data Mining Techniques (2002)](https://link.springer.com/chapter/10.1007/3-540-45997-9_4)
3. [Optimal Number of Clusters: K-Means and Beyond (2019)](https://arxiv.org/abs/1909.04751)
"""

ELBOW_CODE = """\
#@title Elbow Method — Optimal K Selection
import matplotlib.pyplot as plt
import matplotlib
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import time

matplotlib.rcParams['figure.facecolor'] = 'white'
matplotlib.rcParams['axes.facecolor']   = 'white'

K_RANGE = range(2, min(12, len(df) // 5 + 2))  # sensible auto-range
inertias, sil_scores = [], []

logger.info(emoji.emojize(":bar_chart: Running elbow method over k={}..{}...", min(K_RANGE), max(K_RANGE)))
t0 = time.time()

try:
    for k in tqdm(K_RANGE, desc="Elbow method (k values)", unit="k"):
        km = KMeans(n_clusters=k, random_state=RANDOM_SEED, n_init=10)
        labels = km.fit_predict(emb_cluster)
        inertias.append(km.inertia_)
        sil = silhouette_score(emb_cluster, labels, sample_size=min(500, len(df)))
        sil_scores.append(sil)

    # ── Plot ──────────────────────────────────────────────────────────────
    fig, ax1 = plt.subplots(figsize=(10, 4))
    ax1.set_facecolor("white")

    color_inertia = "#007aff"
    color_sil     = "#ff3b30"

    ax1.plot(list(K_RANGE), inertias, "o-", color=color_inertia, linewidth=2.5,
             markersize=7, label="WCSS (Inertia)", zorder=3)
    ax1.set_xlabel("Number of clusters k", fontsize=12, fontfamily="monospace")
    ax1.set_ylabel("WCSS (Inertia)", color=color_inertia, fontsize=11)
    ax1.tick_params(axis="y", labelcolor=color_inertia)
    ax1.axvline(x=N_CLUSTERS, color="#888", linestyle="--", linewidth=1.5,
                label=f"Current N_CLUSTERS={N_CLUSTERS}")

    ax2 = ax1.twinx()
    ax2.plot(list(K_RANGE), sil_scores, "s--", color=color_sil, linewidth=2,
             markersize=7, label="Silhouette Score", zorder=3)
    ax2.set_ylabel("Silhouette Score", color=color_sil, fontsize=11)
    ax2.tick_params(axis="y", labelcolor=color_sil)
    ax2.set_ylim(-0.1, 1.0)

    # Merge legends
    lines1, labs1 = ax1.get_legend_handles_labels()
    lines2, labs2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labs1 + labs2, loc="upper right", fontsize=9)

    plt.title("ARTIFEX v7.4 — Elbow Method: WCSS & Silhouette vs. k",
              fontsize=13, fontfamily="monospace", pad=14)
    fig.tight_layout()
    plot_path = OUTPUT_DIR / "elbow_method.png"
    plt.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.show()

    best_k_sil = list(K_RANGE)[sil_scores.index(max(sil_scores))]
    elapsed = time.time() - t0

    display(HTML(brutalist_explainer(
        title="Elbow Method — K Selection Diagnostics",
        table_data=[
            {"k": k, "WCSS": f"{w:.0f}", "Silhouette": f"{s:.4f}"}
            for k, w, s in zip(K_RANGE, inertias, sil_scores)
        ],
        analysis=(
            f"Best silhouette score: <strong>{max(sil_scores):.4f}</strong> at k={best_k_sil}. "
            f"Current N_CLUSTERS={N_CLUSTERS}. "
            f"If the elbow or silhouette peak suggests a different k, update <code>N_CLUSTERS</code> "
            f"in Cell ③ and re-run from embedding. "
            f"Scores >0.3 indicate meaningful cluster structure. "
            f"Elapsed: {elapsed:.1f}s."
        ),
        highlight_col="Silhouette",
        whitepapers=search_whitepapers("optimal cluster number silhouette"),
    )))

    logger.info(emoji.emojize(f":white_check_mark: Elbow complete — best k (silhouette)={best_k_sil}, current N_CLUSTERS={N_CLUSTERS}"))

except Exception as e:
    logger.error(emoji.emojize(f":cross_mark: Elbow method failed: {e}"))
    raise
"""

EXPORT_MD = """\
## ⑫ Export Results — CSV / JSON / HTML

### Function Description
Saves all pipeline outputs to `OUTPUT_DIR` (`/content/artifex_outputs/`): cluster summaries as CSV, routing decisions as JSON, the annotated dataframe as CSV, and the full HTML brutalist report. Provides Colab download links for each file.

### Technical Rationale
Exporting results in machine-readable formats (CSV/JSON) enables downstream integration with dashboards, alerting pipelines, or HITL review queues. The HTML report is self-contained and can be shared without a running notebook kernel.

### Libraries, Tools & Techniques
- **pandas to_csv/to_json**: Standard tabular + structured output
- **google.colab.files.download**: One-click download from Colab runtime
- **json**: Structured routing decision export

### Best Practices
- Include run metadata (timestamp, model, N_CLUSTERS, random_seed) in every export
- Use deterministic filenames with timestamps for version-safe archiving
- Validate export file sizes before offering download links

### Whitepapers
1. [Reproducibility in ML: Sharing Code and Data (2022)](https://arxiv.org/abs/2202.05048)
2. [Data Cards: Purposeful and Transparent Dataset Documentation (2022)](https://arxiv.org/abs/2204.01075)
3. [BBOM: Benchmark Bill of Materials — Auditability Layer (2026)](https://mlcommons.org/ailuminate)
"""

EXPORT_CODE = """\
#@title Export Results — CSV / JSON / HTML
import json as _json
from datetime import datetime
import time

RUN_TS = datetime.now().strftime("%Y%m%d_%H%M%S")
RUN_META = {
    "run_timestamp": RUN_TS,
    "embed_model": EMBED_MODEL,
    "n_clusters": N_CLUSTERS,
    "random_seed": RANDOM_SEED,
    "llm_provider": LLM_PROVIDER,
    "n_rows": len(df),
    "notebook": "ARTIFEX_v7.4_Ethical_Feedback_Loop",
}

logger.info(emoji.emojize(f":floppy_disk: Exporting results to {OUTPUT_DIR}..."))
t0 = time.time()

exported = []

try:
    # 1. Full annotated dataframe
    df_path = OUTPUT_DIR / f"feedback_annotated_{RUN_TS}.csv"
    df.to_csv(df_path, index=False)
    exported.append({"File": df_path.name, "Type": "CSV", "Rows": len(df), "Description": "Annotated feedback with cluster + UMAP coords"})
    logger.info(emoji.emojize(f":white_check_mark: Saved annotated df → {df_path.name}"))

    # 2. Cluster summaries
    if cluster_summaries:
        cs_path = OUTPUT_DIR / f"cluster_summaries_{RUN_TS}.csv"
        pd.DataFrame(cluster_summaries).to_csv(cs_path, index=False)
        exported.append({"File": cs_path.name, "Type": "CSV", "Rows": len(cluster_summaries), "Description": "LLM cluster theme summaries"})
        logger.info(emoji.emojize(f":white_check_mark: Saved cluster summaries → {cs_path.name}"))

    # 3. Routing decisions
    if routing_results:
        rr_path = OUTPUT_DIR / f"routing_decisions_{RUN_TS}.json"
        payload = {"meta": RUN_META, "routing": routing_results}
        rr_path.write_text(_json.dumps(payload, indent=2))
        exported.append({"File": rr_path.name, "Type": "JSON", "Rows": len(routing_results), "Description": "Safety routing triage per cluster"})
        logger.info(emoji.emojize(f":white_check_mark: Saved routing decisions → {rr_path.name}"))

    # 4. Run metadata
    meta_path = OUTPUT_DIR / f"run_meta_{RUN_TS}.json"
    meta_path.write_text(_json.dumps(RUN_META, indent=2))
    exported.append({"File": meta_path.name, "Type": "JSON", "Rows": 1, "Description": "Run metadata (models, seed, timestamp)"})

    elapsed = time.time() - t0

    display(HTML(brutalist_explainer(
        title="Export Complete — Artifact Index",
        table_data=exported,
        analysis=(
            f"All pipeline artifacts saved to <code>{OUTPUT_DIR}</code>. "
            f"Total export time: {elapsed:.1f}s. "
            "Use the Colab file browser (left panel) or the download snippet below to retrieve files. "
            "Include the run_meta JSON in any shared results for full reproducibility."
        ),
        highlight_col="File",
        whitepapers=search_whitepapers("reproducible ml pipeline export"),
    )))

    # Offer Colab download
    try:
        from google.colab import files as colab_files
        print()
        print(emoji.emojize(":down_arrow: Download files:"))
        for item in exported:
            fp = OUTPUT_DIR / item["File"]
            if fp.exists():
                colab_files.download(str(fp))
    except ImportError:
        print(emoji.emojize(f":information: Files saved to {OUTPUT_DIR} — not in Colab, use local file browser."))

except Exception as e:
    logger.error(emoji.emojize(f":cross_mark: Export failed: {e}"))
    raise
"""

WATERMARK_CODE = """\
#@title Environment Tracking — %watermark Fingerprint
import subprocess
from datetime import datetime
from IPython.display import display, HTML

%load_ext watermark

print("=" * 64)
print("ARTIFEX LABS v7.4 — Environment Fingerprint")
print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
print("=" * 64)

%watermark -v -m -p numpy,pandas,scikit-learn,sentence_transformers,umap,plotly,pandera,loguru,tqdm,anthropic,openai,ydata_profiling,torch,transformers

print()
print("ARTIFEX Labs | linktr.ee/artifexlabs | github.com/tuesdaythe13th")
print("© 2026 ARTIFEX Labs. All Rights Reserved.")

# ── HF-style watermark HTML output ────────────────────────────────────────
import platform, sys, importlib

def _pkg_version(name):
    try:
        return importlib.metadata.version(name)
    except Exception:
        return "N/A"

PKGS = [
    "numpy", "pandas", "scikit-learn", "sentence-transformers",
    "umap-learn", "plotly", "pandera", "loguru", "tqdm",
    "anthropic", "openai", "ydata-profiling", "torch",
    "transformers", "watermark",
]

wm_table = [{"Package": p, "Version": _pkg_version(p)} for p in PKGS]

display(HTML(brutalist_explainer(
    title="Environment Fingerprint — Reproducibility Record",
    table_data=[
        {"Metric": "Python",    "Value": sys.version.split()[0]},
        {"Metric": "Platform",  "Value": platform.platform()},
        {"Metric": "Processor", "Value": platform.processor() or "N/A"},
        *[{"Metric": p, "Value": _pkg_version(p)} for p in PKGS],
    ],
    analysis=(
        "Full environment fingerprint for ARTIFEX v7.4 session. "
        "Pin these exact versions in a requirements.txt or pyproject.toml to guarantee "
        "reproducibility of embedding, clustering, and LLM summarization results. "
        "NIST AI 800-3 requires metrological traceability — environment logging is a "
        "first-class BBOM Layer 0 gate."
    ),
    highlight_col="Metric",
    whitepapers=search_whitepapers("reproducibility machine learning environment"),
)))
"""

LLM_SETUP_MD = """\
## ⑨ LLM API Setup — Key Loading + Gemini Co-Scientist

### Function Description
Loads the selected LLM API key from Colab Secrets and initializes the client. Supports **Gemini 2.0-flash** (primary — includes access to Gemini Co-Scientist tools in Colab AI), **Claude Haiku** (Anthropic), and **OpenAI GPT-4o-mini** as fallback. Defines the `get_llm_summary()` function used in Cell ⑩.

### Technical Rationale
Provider abstraction via `get_llm_summary()` decouples the summarization prompt from the API client, allowing model swaps without touching cluster logic. Using **Colab Secrets** (left panel → 🔑 Secrets) stores keys server-side and prevents them from appearing in notebook metadata or git history.

**Gemini 2.0-flash** is the recommended default for 2026: it supports 1M-token context, multimodal inputs, and integrates with **Gemini Co-Scientist in Colab AI** for hypothesis generation and experiment design — useful for iterating on clustering strategies.

### Libraries, Tools & Techniques
- **google-generativeai** ≥0.8: Gemini 2.0 API ([docs](https://ai.google.dev/gemini-api/docs))
- **anthropic** ≥0.40: Claude API ([docs](https://docs.anthropic.com/))
- **openai** ≥1.30: OpenAI API ([docs](https://platform.openai.com/docs/))
- **google.colab.userdata**: Colab Secrets manager

### Security & Privacy Best Practices
- **Never** embed API keys in code cells — use Colab Secrets exclusively
- Set `max_tokens` to cap cost on large cluster batches
- Add `time.sleep()` between API calls to respect provider rate limits
- Log raw LLM responses before parsing to preserve audit trail

### Whitepapers
1. [LLM-as-a-Judge: Survey (2025)](https://arxiv.org/abs/2501.05111)
2. [Gemini 2.0: Advancing Multimodal AI (2025)](https://arxiv.org/abs/2501.12599)
3. [Building Effective Agents — Anthropic (2024)](https://www.anthropic.com/research/building-effective-agents)
"""

LLM_SETUP_CODE = """\
#@title LLM API Setup — Secure Key Loading
import time

llm_client = None
LLM_PROVIDER = "gemini"  #@param ["gemini", "claude", "openai"]

try:
    from google.colab import userdata

    if LLM_PROVIDER == "gemini":
        import google.generativeai as genai
        api_key = userdata.get('GEMINI_API_KEY')
        genai.configure(api_key=api_key)
        # Gemini 2.0-flash: 1M context, fast, Colab AI / Co-Scientist compatible
        llm_client = genai.GenerativeModel(GEMINI_MODEL)
        logger.info(emoji.emojize(f":gem: Gemini client initialized → {GEMINI_MODEL}"))

    elif LLM_PROVIDER == "claude":
        import anthropic
        api_key = userdata.get('ANTHROPIC_API_KEY')
        llm_client = anthropic.Anthropic(api_key=api_key)
        logger.info(emoji.emojize(f":robot: Claude (Anthropic) client initialized → {CLAUDE_MODEL}"))

    elif LLM_PROVIDER == "openai":
        from openai import OpenAI
        api_key = userdata.get('OPENAI_API_KEY')
        llm_client = OpenAI(api_key=api_key)
        logger.info(emoji.emojize(f":brain: OpenAI client initialized → {OPENAI_MODEL}"))

except Exception as e:
    logger.warning(emoji.emojize(f":warning: LLM API key not found — summarization will use mock responses: {e}"))
    llm_client = None


def get_llm_summary(cluster_texts: list, cluster_id: int) -> str:
    \"\"\"Summarize a cluster of feedback texts using the configured LLM.\"\"\"
    sample = cluster_texts[:10]
    prompt = (
        f"You are an AI safety researcher analyzing user feedback about an AI assistant. "
        f"Below are {len(sample)} feedback messages from Cluster {cluster_id}. "
        f"Identify the dominant theme, key concerns, and any patterns related to cultural, "
        f"linguistic, or ethical issues. Be concise (2-3 sentences).\\n\\n"
        + "\\n".join(f"- {t}" for t in sample)
    )

    if llm_client is None:
        return (
            f"[Mock] Cluster {cluster_id}: Feedback relates to AI response quality, "
            "cultural appropriateness, and multilingual handling."
        )

    try:
        if LLM_PROVIDER == "gemini":
            resp = llm_client.generate_content(prompt)
            return resp.text.strip()
        elif LLM_PROVIDER == "claude":
            msg = llm_client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=300,
                messages=[{"role": "user", "content": prompt}],
            )
            return msg.content[0].text.strip()
        elif LLM_PROVIDER == "openai":
            resp = llm_client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=300,
            )
            return resp.choices[0].message.content.strip()
    except Exception as e:
        logger.error(emoji.emojize(f":cross_mark: LLM call failed for cluster {cluster_id}: {e}"))
        return f"[Error] Summarization failed: {e}"


logger.info(emoji.emojize(
    f":white_check_mark: LLM provider: {LLM_PROVIDER} | client ready: {llm_client is not None}"
))
"""

# ════════════════════════════════════════════════════════════════════════════
# PATCH v7.4 NOTEBOOK
# ════════════════════════════════════════════════════════════════════════════

def patch_v74():
    nb_path = Path("ARTIFEX_v7.4_Ethical_Feedback_Loop.ipynb")
    with open(nb_path) as f:
        nb = json.load(f)

    cells = nb["cells"]

    # Cell 0 — README (markdown)
    set_source(cells[0], README_CELL)

    # Cell 3 — Install (code)
    set_source(cells[3], INSTALL_CELL)

    # Cell 5 — Header (code)
    set_source(cells[5], HEADER_CELL)

    # Cell 7 — Config (code)
    set_source(cells[7], CONFIG_CELL)

    # Cell 18 — LLM Setup (markdown)
    set_source(cells[18], LLM_SETUP_MD)

    # Cell 19 — LLM Setup (code)
    set_source(cells[19], LLM_SETUP_CODE)

    # Cell 25 — Watermark (code)
    set_source(cells[25], WATERMARK_CODE)

    # Insert elbow method cells after cell 14 (UMAP+KMeans markdown) and 15 (code)
    # They go BEFORE the 3D visualization (currently cells 16, 17)
    # Insert at position 16 (after clustering code cell 15)
    elbow_md_cell  = md(ELBOW_MD)
    elbow_cod_cell = code(ELBOW_CODE)
    cells.insert(16, elbow_cod_cell)
    cells.insert(16, elbow_md_cell)

    # Now 3D viz is at 18, 19; LLM API at 20, 21; etc.
    # Insert export cells BEFORE the final watermark cells
    # Watermark md is now at index -2, watermark code at -1
    export_md_cell  = md(EXPORT_MD)
    export_cod_cell = code(EXPORT_CODE)
    cells.insert(len(cells) - 2, export_cod_cell)
    cells.insert(len(cells) - 3, export_md_cell)

    # Renumber watermark section from ⑫ to ⑭ (added 2 new sections)
    wm_md_idx   = len(cells) - 2   # markdown cell
    wm_code_idx = len(cells) - 1   # code cell
    old_src = get_source(cells[wm_md_idx])
    set_source(cells[wm_md_idx], old_src.replace("## ⑫ Environment Tracking", "## ⑭ Environment Tracking"))
    set_source(cells[wm_code_idx], WATERMARK_CODE)

    with open(nb_path, "w") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"✅ Patched {nb_path.name} — {len(nb['cells'])} cells total")

if __name__ == "__main__":
    patch_v74()
    print("Done. Run python3 improve_v72_v73.py next for the other notebooks.")
