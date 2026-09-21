# Explainability Contract: SQLMedic

## Decision

SQLMedic decides whether readable project content contains a SELECT * FROM pattern. A match is treated as a query-hygiene signal and connected to a suggestion to select only required columns.

## Inputs

It uses readable source text from the inspected project and applies a deterministic regular-expression rule. The current rule focuses on wildcard SELECT statements.

## Limits

It cannot determine query performance, schema intent, indexes, permissions, or whether a wildcard is appropriate in a specific context. Generated SQL and unusual formatting may evade the pattern.
