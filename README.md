# SQLMedic

> Portable agent for identifying broad SQL selection patterns that deserve review.

## What it does

SQLMedic scans available project source for wildcard queries of the form `SELECT * FROM ...`. It reports the observed pattern and recommends narrowing queries to the columns actually required.

### Diagnostic fingerprint

**SQL pattern → query-risk signal → evidence → targeted remediation**

## Why this agent is distinct

SQLMedic does not pretend that a single SQL pattern proves a performance or security failure. Its purpose is narrower: surface a recognizable query pattern that deserves review.

That deterministic boundary makes its output reproducible and explainable.

## Workflow

```text
SQL/source files
      ↓
Pattern scanner
      ↓
Wildcard-query rule
      ↓
Evidence-backed finding
      ↓
Query refinement plan
```

## Verification

Included:
- OpenGAP-compatible passport
- SQL-focused broken-project fixture
- explainability and behavior contracts
- OpenAI, CrewAI, Claude Code, and Lyzr adapters
- adapter verification tests

The OpenGAP validator passed, and all four framework exports have been exercised successfully.

## Design principle

**A signal is not a verdict.** SQLMedic flags a concrete pattern and leaves broader performance or security conclusions to deeper analysis.

## Medic family

SQLMedic contributes a database-specific diagnostic to the Medic family, preserving a common portable contract while maintaining a distinct technical focus.