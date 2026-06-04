# Artifex Labs Rubric Design Handbook v1.0
**State-of-the-Art Practices for AI Evaluation — March 2026**

---

## Executive Summary

Modern AI evaluation is shifting from opaque single-score judgments toward **rubric-guided evaluation**, where task success is decomposed into small sets of instruction-derived, atomic, and verifiable criteria. Recent work such as RubricBench (1,147 pairwise comparisons with expert-annotated rubrics) and APEX-Agents (480 professional tasks evaluated with binary criteria) shows that structured rubrics improve transparency, diagnostic power, and resistance to superficial reward hacking [1][2].

The quality of the rubric itself is a major determinant of evaluator reliability. RubricBench reports a persistent **Rubric Gap of approximately 26%**, where human-authored rubrics substantially outperform model-generated ones, especially when prompts contain implicit constraints, misleading surface cues, or safety-sensitive requirements [1][3].

This handbook synthesizes current best practices for writing, validating, and deploying rubrics in benchmark design, LLM-as-judge systems, agent evaluation, and safety review. It is intended for use by Artifex Labs evaluators, benchmark designers, safety teams, and QA engineers.

---

## 1. Introduction: Why Rubrics Matter

A good rubric is not a paragraph about "quality." It is a small set of verifiable checks that define what success means for a specific task. Rubrics make evaluation more transparent, reproducible, and resistant to outputs that sound polished without actually solving the problem [1][4].

Recent state-of-the-art work demonstrates three key findings:

1. **Rubric quality drives evaluator performance.** Even frontier judge models plateau around 85% accuracy on challenging evaluation tasks when given high-quality human rubrics, but drop substantially when forced to generate their own criteria [1].
2. **Human rubrics encode essential constraints that models miss.** Models writing their own rubrics tend to fixate on easy-to-spot formatting while missing logical feasibility, safety requirements, and tacit human priorities — a failure mode known as "attention displacement" [1][3].
3. **Small, atomic rubrics work best.** Recent benchmarks commonly use 2–10 binary yes/no criteria per task, with each criterion testing exactly one requirement [1][2][5].

---

## 2. First Principles

Every rubric should satisfy four core properties, derived from recent evaluation research and rubric formalization work [1][4][6].

### 2.1 Atomicity

Each rubric item tests exactly one thing. RubricBench and APEX-Agents both use short, self-contained criteria that can be graded independently as true or false.

**Practical test:** If a criterion contains "and," it often should be split. If answering "yes" requires checking two unrelated properties, the item is not atomic.

### 2.2 Instruction Alignment

The rubric must be written from the **user instruction**, not from candidate responses. RubricBench explicitly constructs rubrics solely from instructions to avoid post-hoc bias and response-aware leakage [1][3].

**Practical workflow:** Read the prompt → Extract requirements → Draft criteria → Only then examine candidate outputs for validation.

### 2.3 Must-Have Focus

The rubric should prioritize **non-negotiable** task requirements. A rubric is not a wishlist. It should distinguish between what makes a response acceptable versus excellent.

**Practical test:** For each item, ask: *If this criterion fails, should the task still count as successful?* If yes, the item may not belong in the must-have set.

### 2.4 Objectivity

A reasonable grader should be able to answer each item with minimal interpretation. The closer a criterion is to a yes/no observation, the more reliable it becomes.

**Practical test:** Could two independent graders disagree? If disagreement is likely, the criterion may need to be more concrete or split into multiple observable checks.

---

## 3. Rubric Anatomy

### 3.1 The Artifex Labs Rubric Template

| Section | Purpose |
|---|---|
| **Hard Constraints** | Non-negotiable format, factual, or structural conditions explicitly required by the prompt |
| **Core Fulfillment** | Whether the output actually solves the main user task or answers the central question |
| **Implicit Requirements** | Necessary but unstated conditions inferred from context, audience, domain, or feasibility |
| **Pitfall Checks** | Explicit checks that the model did not do something forbidden, unsafe, or disqualifying |

### 3.2 Explicit vs. Implicit Constraints

Rubrics must capture both direct commands and implicit constraints inferred from context:

- **Explicit constraints:** exact counts, required formats, specified data sources, mandatory inclusions
- **Implicit constraints:** audience-appropriate tone, domain norms, safety expectations, feasibility, artifact completeness

### 3.3 Grading Targets

Each criterion should specify the **grading target**: the artifact or output type being judged (e.g., `[Message]`, `[File: budget.xlsx]`, `[Code patch]`, `[Presentation]`).

---

## 4. Writing Process

### Step 1: Extract Task Requirements (Instruction-Only)
Read the prompt and extract task objective, required output type, explicit constraints, and likely implicit constraints. **Do this before looking at any candidate outputs.**

### Step 2: List Mandatory Conditions
Identify conditions that must be met for the answer to count as correct, useful, or safe.

### Step 3: Convert to Atomic Binary Criteria
Convert each mandatory condition into a single binary yes/no criterion. If a criterion checks two ideas at once, split it.

**Example transformation:**

- *Poor:* "Is the itinerary detailed, well-written, culturally appropriate, and accessible?"
- *Better (atomic):*
  1. Includes a full one-day itinerary with ordered stops.
  2. Includes a lunch stop.
  3. Uses walking distances appropriate for elderly visitors.
  4. Includes opportunities for rest or low-strain pacing.
  5. Avoids physically demanding or inaccessible recommendations.

### Step 4: Assign Grading Targets
Specify the artifact or output type being judged for each criterion.

### Step 5: Add Pitfall Checks
Add explicit negative constraints covering: hallucinated data, unsafe compliance, unsupported claims, omission of required artifacts, policy violations.

---

## 5. Necessity vs. Rigidity

A good rubric is strict where the task truly demands strictness and flexible where multiple good answers are possible. Avoid **surface obsession** — fixating on formatting while missing logical feasibility, safety, or tacit user priorities [1][3].

---

## 6. Safety and Refusal Logic

Safety rubrics must explicitly ask:
- Did the model refuse the harmful or disallowed request?
- Did it avoid providing prohibited details or instructions?
- Did it explain the refusal appropriately?
- Did it remain helpful within policy bounds?

**Pitfall criteria for safety:**
- Does not comply with requests for explicit, harmful, or policy-violating content
- Does not provide step-by-step instructions for dangerous activities
- Does not hallucinate or fabricate safety-critical information
- Does not use manipulative or deceptive framing

---

## 7. Quality Control

### 7.1 Three-Pass QA Checklist
1. **Logical Consistency:** No two criteria contradict each other.
2. **Minimal Redundancy:** Overlapping items are merged or removed.
3. **Instruction Traceability:** Every item maps back to something explicit or necessary in the original prompt.

### 7.2 Stress Testing
Run the rubric on contrasting outputs:
- High-fluency output that does not solve the task
- Low-fluency output that correctly solves the task
- Output that satisfies explicit constraints but violates implicit ones
- Output that appears complete but contains fabricated information

---

## 8. Scoring Patterns

### 8.1 Decision Rules

```
ALL hard constraints must pass
MOST/ALL core fulfillment items must pass
NO pitfall checks may fail
```

Keep criterion-level results visible for diagnostics. Avoid collapsing to a single opaque score too early.

### 8.2 Weighted vs. Binary Scoring

Binary scoring is preferred for transparency. Use weighted scoring only when:
- Different criteria have clearly different importance levels
- Partial credit is meaningful and well-defined
- Downstream systems require continuous scores

---

## 9. Anti-Patterns

| Anti-Pattern | Description |
|---|---|
| Checklist Bloat | Rubric becomes long and repetitive, making evaluation noisy |
| Surface Obsession | Criteria reward formatting/length instead of task success |
| Response-Shaped Rubrics | Criteria accidentally encode what the model did rather than what was asked |
| Bundled Criteria | One item checks too many things at once |
| Missing Negative Constraints | Rubric forgets to test for forbidden behaviors |
| Low-Necessity Rigidity | Over-focus on formatting details irrelevant to user intent |

---

## 10. Example: Poor vs. Strong Rubric

**Prompt:** "Create a one-day walking itinerary in Kyoto for elderly visitors, with lunch included."

**Poor Rubric:**
> 1. Is the itinerary detailed, well-written, culturally appropriate, and accessible?

**Strong Rubric:**

| # | Criterion | Type |
|---|---|---|
| 1 | [Itinerary] Includes a full one-day itinerary with ordered stops | Hard Constraint |
| 2 | [Itinerary] Includes a designated lunch stop | Hard Constraint |
| 3 | [Itinerary] Uses walking distances appropriate for elderly visitors | Core Fulfillment |
| 4 | [Itinerary] Includes opportunities for rest or low-strain pacing | Implicit Requirement |
| 5 | [Itinerary] Avoids physically demanding or inaccessible sites | Implicit Requirement |
| 6 | [Itinerary] Does not include fabricated or non-existent locations | Pitfall Check |

**Decision rule:** All hard constraints must pass. At least 3 of 4 core/implicit requirements must pass. No pitfall checks may fail.

---

## 11. Domain-Specific Guidelines

### Benchmark Rubrics
- Instruction-only rubric derivation to avoid data contamination
- Diverse implicit constraint coverage to test model reasoning
- Stress test cases with misleading surface cues

### Safety Rubrics
- Explicit refusal criteria and policy boundaries
- Pitfall checks for harmful compliance, fabrication, and manipulation
- Human rubric annotation for high-stakes safety decisions

### Agent Evaluation Rubrics
- Clear grading targets for each artifact or file produced
- Feasibility checks for multi-step plans
- Verification that the agent's actions actually achieved the task objective

### Policy and Perspectivist Safety Rubrics
- Encode context-appropriate norms as explicit criteria
- Use separate rubrics for high-context vs. low-context interaction styles
- Include pitfall checks for pragmatic failures, tone violations, or cultural insensitivity

---

## 12. The Human Rubric Advantage

The most important finding from recent evaluation research: **rubric quality is the limiting factor**, not just which judge model is used. RubricBench reports a ~26% performance gain from human-annotated rubrics over model-generated ones [1][3].

**Use human-authored rubrics for:**
- High-stakes benchmarks and model selection
- Safety-critical evaluation
- Tasks with significant implicit constraints or domain expertise requirements
- Contexts where evaluation failure has compliance, legal, or reputational consequences

---

## 13. Implementation Checklist

1. Read the prompt and extract task requirements **without looking at candidate outputs**
2. List mandatory conditions for task success
3. Convert conditions to atomic binary yes/no criteria (2–10 items typical)
4. Assign grading targets to each criterion
5. Categorize criteria: Hard Constraints, Core Fulfillment, Implicit Requirements, Pitfall Checks
6. Run QA pass: check consistency, redundancy, instruction traceability
7. Stress test on contrasting outputs (weak-but-fluent, polished-but-wrong, correct-but-rough)
8. Document decision rule (what combination of passes constitutes success)
9. Version and store rubric with prompt, grading target, and metadata
10. Monitor rubric performance and iterate based on failure analysis

---

## 14. Final Principle

> A rubric should behave like a unit test for intent. If it mainly rewards outputs for looking polished, it is not a good rubric. If it makes task success legible, auditable, and resistant to superficial reward hacking, it is doing its job.

---

## References

[1] Chen, Y., et al. (2026). RubricBench: Aligning Model-Generated Rubrics with Human Standards. arXiv:2603.01562. https://arxiv.org/abs/2603.01562

[2] Mercor Research Team. (2026). APEX-Agents: An AI Productivity Index for Professional Autonomy. Technical Report. https://arxiv.org/pdf/2601.14242.pdf

[3] Chen, Y., et al. (2026). RubricBench (Extended). arXiv:2603.01562v2. https://arxiv.org/html/2603.01562v2

[4] Emergent Mind Research. (2026). Rubric Formalization in AI and Education. https://www.emergentmind.com/topics/rubric-formalization

[5] Emergent Mind Research. (2026). APEX-Agents Benchmark. https://www.emergentmind.com/topics/apex-agents-benchmark

[6] Wolfe, C. R. (2026). Rubric-Based Rewards for Reinforcement Learning. Deep Learning Focus. https://cameronrwolfe.substack.com/p/rubric-rl

[7] University of Illinois Chicago, CATE. (n.d.). Rubrics: Best Practices for Assessment. https://teaching.uic.edu/cate-teaching-guides/assessment-grading-practices/rubrics/
