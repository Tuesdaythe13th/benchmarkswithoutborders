#!/usr/bin/env python3
"""
Applies targeted improvements to ARTIFEX v7.2 and v7.3 notebooks.
Focuses on: install cell (UV --system), header (HF badge), brutalist_explainer,
watermark cell, README attribution block.
Run: python3 improve_v72_v73.py
"""

import json
from pathlib import Path

def get_source(cell_obj):
    src = cell_obj.get("source", "")
    return "".join(src) if isinstance(src, list) else src

def set_source(cell_obj, text):
    cell_obj["source"] = text

def make_code_cell(source):
    return {"cell_type": "code", "metadata": {}, "source": source,
            "outputs": [], "execution_count": None}

def make_md_cell(source):
    return {"cell_type": "markdown", "metadata": {}, "source": source}

# ════════════════════════════════════════════════════════════════════════════
# SHARED IMPROVED CONTENT (parametrised per notebook)
# ════════════════════════════════════════════════════════════════════════════

def make_readme(version, subtitle, extra_libs=""):
    return f"""\
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Tuesdaythe13th/multilingualcompositionalsafety_evals/blob/main/ARTIFEX_{version}.ipynb)
[![HuggingFace](https://img.shields.io/badge/🤗%20HuggingFace-222tuesday-yellow)](https://huggingface.co/222tuesday)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

---

# ARTIFEX {version} — {subtitle}

**Principal Investigator:** Tuesday @ ARTIFEX Labs
**Contact:** tuesday@artifexlabs.com
**Links:** [linktr.ee/artifexlabs](https://linktr.ee/artifexlabs) · [github.com/tuesdaythe13th](https://github.com/tuesdaythe13th) · [huggingface.co/222tuesday](https://huggingface.co/222tuesday) · [Google Scholar](https://scholar.google.com/citations?user=artifexlabs)

---

## How to Cite

```bibtex
@misc{{tuesday2026artifex{version.replace('.', '').lower()},
  author       = {{Tuesday and {{ARTIFEX Labs}}}},
  title        = {{{{ARTIFEX {version}: {subtitle}}}}},
  year         = {{2026}},
  howpublished = {{\\url{{https://github.com/tuesdaythe13th/multilingualcompositionalsafety_evals}}}},
  note         = {{Multilingual compositional safety evaluation. Aligned with NIST AI 800-3,
                  ISO/IEC 42119-8, MLCommons AILuminate.}}
}}
```

---

## Legal Disclaimer

> **© 2026 ARTIFEX Labs. All Rights Reserved.**
> This notebook is provided for research and educational purposes only. The code may contain errors
> and is not intended for production deployment without independent verification. This notebook may
> not be shared, reproduced, or distributed without written permission from ARTIFEX Labs.
> ARTIFEX Labs makes no warranties, express or implied, regarding accuracy or fitness for a
> particular purpose. Use at your own risk.

---
"""

def make_install_cell(version, accent_color, subtitle="", extra_pkgs=""):
    base_pkgs = [
        "numpy>=1.24,<2.0",
        "pandas>=2.0",
        "scikit-learn>=1.4,<1.6",
        "torch>=2.2",
        "sentence-transformers>=3.0",
        "transformers>=4.40",
        "bertopic>=0.16",
        "hdbscan>=0.8",
        "umap-learn>=0.5",
        "ydata-profiling>=4.6",
        "pandera>=0.18",
        "plotly>=5.20",
        "matplotlib>=3.8",
        "loguru>=0.7",
        "tqdm>=4.66",
        "emoji>=2.10",
        "watermark>=2.4",
        "huggingface_hub>=0.22",
        "scipy>=1.10",
        "pillow>=10.0",
        "openai>=1.30",
        "google-generativeai>=0.8",
        "pydantic>=2.0",
        "grpcio>=1.60,<2.0",
        "protobuf>=4.0,<5.0",
    ]
    if extra_pkgs:
        base_pkgs.insert(0, extra_pkgs)

    pkgs_str = '",\n    "'.join(base_pkgs)

    return f"""\
#@title Install Dependencies — UV-Aware (2026 Colab)
# ┌─────────────────────────────────────────────────────────────────────────┐
# │  ARTIFEX {version} — Environment Setup                                       │
# │  UV-aware install with explicit version pins for 2025/2026 Colab compat. │
# │  Falls back to pip if uv --system is unavailable.                       │
# └─────────────────────────────────────────────────────────────────────────┘
import os, sys, subprocess
from datetime import datetime
from IPython.display import display, HTML

IN_COLAB = "google.colab" in sys.modules or os.path.exists("/content")
_t0 = datetime.now()

# ── Fonts + Brutalist CSS ────────────────────────────────────────────────
ARTIFEX_CSS = \"\"\"
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne+Mono&family=Epilogue:wght@300;400;600;700&display=swap');
:root {{
  --black: #000000; --white: #ffffff;
  --accent: {accent_color}; --gray: #888888; --light: #f0f0f0;
}}
.artifex-header {{
  font-family: 'Syne Mono', monospace;
  background: var(--black); color: var(--white);
  padding: 32px 40px; border-left: 10px solid var(--accent); margin-bottom: 20px;
}}
.artifex-header h1 {{
  font-family: 'Syne Mono', monospace; font-size: 2.8em;
  letter-spacing: 0.18em; margin: 0 0 6px 0; text-transform: uppercase;
}}
.artifex-header .subtitle {{
  font-family: 'Epilogue', sans-serif; font-weight: 300;
  font-size: 1.1em; color: #cccccc; letter-spacing: 0.05em;
}}
.artifex-header .timestamp {{
  font-family: 'Syne Mono', monospace; font-size: 0.8em;
  color: var(--gray); margin-top: 14px; border-top: 1px solid #333;
  padding-top: 10px; line-height: 1.8;
}}
.artifex-header .hf-badge {{
  display: inline-block; background: #ff9d00; color: #000;
  font-family: 'Syne Mono', monospace; font-size: 0.72em;
  padding: 2px 7px; border-radius: 2px; margin-left: 8px;
  font-weight: 700; letter-spacing: 0.05em; vertical-align: middle;
}}
.brutalist-explainer {{
  font-family: 'Epilogue', sans-serif; background: var(--white); color: var(--black);
  border: 3px solid var(--black); padding: 20px 28px; margin: 14px 0;
}}
.brutalist-explainer h2 {{
  font-family: 'Syne Mono', monospace; font-size: 1.3em;
  text-transform: uppercase; letter-spacing: 0.1em;
  border-bottom: 3px solid var(--black); padding-bottom: 8px; margin-bottom: 14px;
}}
.brutalist-table {{
  width: 100%; border-collapse: collapse;
  font-family: 'Epilogue', sans-serif; font-size: 0.92em;
}}
.brutalist-table th {{
  background: var(--black); color: var(--white);
  padding: 9px 12px; text-align: left;
  font-family: 'Syne Mono', monospace; font-size: 0.85em;
  text-transform: uppercase; letter-spacing: 0.05em;
}}
.brutalist-table td {{ padding: 8px 12px; border-bottom: 1px solid #ddd; }}
.brutalist-table tr:nth-child(even) {{ background: var(--light); }}
.analysis-block {{
  background: var(--black); color: var(--white);
  padding: 14px 20px; margin-top: 14px;
  font-family: 'Epilogue', sans-serif; font-size: 0.9em; line-height: 1.7;
  border-left: 4px solid var(--accent);
}}
.watermark-bar {{
  font-family: 'Syne Mono', monospace; font-size: 0.7em;
  color: var(--gray); text-align: right; border-top: 1px solid #eee;
  padding-top: 8px; margin-top: 12px;
  display: flex; justify-content: space-between; align-items: center;
}}
.hf-watermark {{
  display: inline-block; background: #ff9d00; color: #000;
  font-family: 'Syne Mono', monospace; font-size: 0.85em;
  padding: 1px 6px; border-radius: 2px; font-weight: 700;
}}
</style>
\"\"\"

display(HTML(ARTIFEX_CSS))

NOW = datetime.now()
display(HTML(f\"\"\"
<div class="artifex-header">
  <h1>ARTIFEX LABS <span class="hf-badge">🤗 HF: 222tuesday</span></h1>
  <div class="subtitle">{version} — {subtitle}</div>
  <div class="timestamp">
    📌 PI: Tuesday @ ARTIFEX Labs · tuesday@artifexlabs.com<br>
    🕐 Session: <strong>{{NOW.strftime('%A, %B %d, %Y — %H:%M:%S UTC')}}</strong><br>
    🔗 <a href="https://linktr.ee/artifexlabs" style="color:#aaa">linktr.ee/artifexlabs</a> ·
    <a href="https://github.com/tuesdaythe13th" style="color:#aaa">github.com/tuesdaythe13th</a> ·
    <a href="https://huggingface.co/222tuesday" style="color:#aaa">huggingface.co/222tuesday</a>
  </div>
</div>
\"\"\"))

# ── UV-aware package install ──────────────────────────────────────────────
PACKAGES = [
    "{pkgs_str}",
]

def _run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

print(f"[{{datetime.now().strftime('%H:%M:%S')}}] 📦 Installing uv...")
_run([sys.executable, "-m", "pip", "install", "-q", "uv"])

print(f"[{{datetime.now().strftime('%H:%M:%S')}}] ⚡ uv pip install --system...")
r = _run([sys.executable, "-m", "uv", "pip", "install", "--system", "-q"] + PACKAGES)

if r.returncode == 0:
    print(f"[{{datetime.now().strftime('%H:%M:%S')}}] ✅ uv install complete")
else:
    print(f"[{{datetime.now().strftime('%H:%M:%S')}}] ⚠️  uv failed, falling back to pip...")
    for pkg in PACKAGES:
        _run([sys.executable, "-m", "pip", "install", "-q", pkg])
    print(f"[{{datetime.now().strftime('%H:%M:%S')}}] ✅ pip fallback complete")

elapsed = (datetime.now() - _t0).total_seconds()
print(f"[{{datetime.now().strftime('%H:%M:%S')}}] 🎉 All dependencies ready in {{elapsed:.1f}}s")
if IN_COLAB:
    print("⚠️  If you upgraded numpy/torch, restart runtime before proceeding.")

# ── Core imports (available for all subsequent cells) ─────────────────────
import pandas as pd
import numpy as np
from tqdm.notebook import tqdm
import plotly.express as px
import plotly.graph_objects as go
import emoji
from loguru import logger
from datetime import datetime as _dt
import time, warnings

warnings.filterwarnings('ignore')
logger.remove()
logger.add(sys.stdout, format="<green>{{time:HH:mm:ss}}</green> | <level>{{level: <8}}</level> | {{message}}", level="INFO", colorize=True)

# ── Shared brutalist_explainer ────────────────────────────────────────────
from datetime import datetime as _now_dt
def brutalist_explainer(title, table_rows, analysis, highlight_col=None):
    \"\"\"Render a brutalist HTML explainer. table_rows: list of dicts.\"\"\"
    if not table_rows:
        return f'<div class="brutalist-explainer"><h2>{{title}}</h2><p>No data.</p></div>'
    cols = list(table_rows[0].keys())
    header = "".join(f"<th>{{c}}</th>" for c in cols)
    rows = ""
    for row in table_rows:
        cells = "".join(
            f'<td style="background:#fffb00;font-weight:700">{{row.get(c,"")}}</td>'
            if c == highlight_col else
            f'<td>{{row.get(c,"")}}</td>'
            for c in cols
        )
        rows += f"<tr>{{cells}}</tr>"
    ts = _now_dt.now().strftime('%Y-%m-%d %H:%M:%S')
    return f\"\"\"
    <div class="brutalist-explainer">
      <h2>{{title}}</h2>
      <table class="brutalist-table"><thead><tr>{{header}}</tr></thead><tbody>{{rows}}</tbody></table>
      <div class="analysis-block">{{analysis}}</div>
      <div class="watermark-bar">
        <span>ARTIFEX LABS {version} · generated {{ts}}</span>
        <span><span class="hf-watermark">🤗 HF</span>
          <a href="https://huggingface.co/222tuesday" style="color:#999;font-size:0.9em"> huggingface.co/222tuesday</a>
        </span>
      </div>
    </div>\"\"\"

def artifex_explainer(title, content):
    \"\"\"Legacy wrapper — calls brutalist_explainer with raw HTML content.\"\"\"
    display(HTML(f'<div class="brutalist-explainer"><h2>{{title}}</h2><div>{{content}}</div></div>'))

logger.info(emoji.emojize(":white_check_mark: ARTIFEX {version} system online"))
"""


def make_watermark_cell(version):
    return f"""\
#@title Environment Audit — %watermark Fingerprint
import subprocess, sys, importlib, platform
from datetime import datetime
from IPython.display import display, HTML

%load_ext watermark

print("=" * 64)
print("ARTIFEX LABS {version} — Environment Fingerprint")
print(f"Generated: {{datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}}")
print("=" * 64)

%watermark -v -m -p pandas,numpy,bertopic,hdbscan,umap,sentence_transformers,plotly,scikit_learn,openai,pydantic,loguru,tqdm,watermark

print()
print("ARTIFEX Labs | linktr.ee/artifexlabs | github.com/tuesdaythe13th")
print("© 2026 ARTIFEX Labs. All Rights Reserved.")

# ── HF-style watermark HTML ───────────────────────────────────────────────
def _v(name):
    try: return importlib.metadata.version(name)
    except: return "N/A"

PKGS = ["pandas","numpy","bertopic","hdbscan","umap-learn","sentence-transformers",
        "plotly","scikit-learn","openai","pydantic","loguru","tqdm","watermark",
        "torch","transformers","google-generativeai"]

wm_rows = [
    {{"Metric": "Python",    "Value": sys.version.split()[0]}},
    {{"Metric": "Platform",  "Value": platform.platform()}},
    *[{{"Metric": p, "Value": _v(p)}} for p in PKGS],
]

display(HTML(brutalist_explainer(
    title="Environment Fingerprint — Reproducibility Record",
    table_rows=wm_rows,
    analysis=(
        "Full environment fingerprint for ARTIFEX {version}. "
        "Pin these versions in requirements.txt for reproducibility. "
        "NIST AI 800-3 requires metrological traceability — this log is a BBOM Layer 0 gate."
    ),
    highlight_col="Metric",
)))
logger.info(emoji.emojize(":robot: ARTIFEX {version} run complete."))
"""

# ════════════════════════════════════════════════════════════════════════════
# PATCH FUNCTIONS
# ════════════════════════════════════════════════════════════════════════════

def patch_notebook(nb_path, version, subtitle, accent_color, extra_pkgs=""):
    with open(nb_path) as f:
        nb = json.load(f)

    cells = nb["cells"]

    # ── 1. Insert README as first cell (shift everything down) ─────────────
    readme_src = make_readme(version, subtitle)
    # Check if cell 0 is already a README-style cell (has "How to Cite")
    cell0_src = get_source(cells[0])
    if "How to Cite" in cell0_src or "Legal Disclaimer" in cell0_src:
        # Update in place
        set_source(cells[0], readme_src)
        print(f"  Updated existing README cell")
    else:
        cells.insert(0, make_md_cell(readme_src))
        print(f"  Inserted new README cell at position 0")

    # Re-find install cell (now shifted if we inserted README)
    install_idx = None
    for i, cell in enumerate(cells):
        src = get_source(cell)
        if cell["cell_type"] == "code" and ("INSTALL" in src.upper() or "pip install" in src.lower()):
            install_idx = i
            break

    if install_idx is not None:
        install_src = make_install_cell(version, accent_color, subtitle=subtitle, extra_pkgs=extra_pkgs)
        set_source(cells[install_idx], install_src)
        print(f"  Replaced install cell at index {install_idx}")

    # ── 2. Patch watermark cell (last code cell) ───────────────────────────
    last_code_idx = None
    for i in range(len(cells) - 1, -1, -1):
        if cells[i]["cell_type"] == "code":
            last_code_idx = i
            break

    if last_code_idx is not None:
        last_src = get_source(cells[last_code_idx])
        if "watermark" in last_src.lower():
            set_source(cells[last_code_idx], make_watermark_cell(version))
            print(f"  Replaced watermark cell at index {last_code_idx}")

    with open(nb_path, "w") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    print(f"✅ Patched {nb_path.name} — {len(nb['cells'])} cells total")


if __name__ == "__main__":
    # v7.2 — accent: #FF3E00 (orange-red), extra: fiftyone
    patch_notebook(
        Path("ARTIFEX_v7.2_Spanish_Benchmark.ipynb"),
        version="v7.2",
        subtitle="Spanish Benchmark Edition — Colombia",
        accent_color="#FF3E00",
        extra_pkgs="fiftyone>=0.24",
    )

    # v7.3 — accent: #00FF41 (matrix green), extra: fiftyone
    patch_notebook(
        Path("ARTIFEX_v7.3_Dialect_Divergence.ipynb"),
        version="v7.3",
        subtitle="Spanish Dialect Divergence Benchmark (ES-ES vs ES-MX)",
        accent_color="#00FF41",
        extra_pkgs="fiftyone>=0.24",
    )

    print("\nAll notebooks patched.")
