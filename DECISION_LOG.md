# Decision Log

1. Brand choice — AppleSupport was selected for a focused support use case.
2. Taxonomy — 11 intents were used to cover common support problems.
3. Other intent — Kept as a fallback for unclear cases.
4. Golden set size — 200 examples were selected.
5. Sample data — 500 examples were included for quick reproducibility.
6. Escalation — Every golden example includes an escalation label.
7. Evaluation — Intent accuracy and macro F1 are planned.
8. Escalation metrics — Precision and recall are planned.
9. Baselines — Trivial and simple baselines are included in the evaluation scope.
10. LLM judge — A rubric-based review is planned.
11. Temperature — Judge evaluation should use temperature 0.
12. Human agreement — At least 50 examples should be double-labelled.
13. Confidence intervals — Metrics should include uncertainty estimates.
14. Scope cut — A full production support system was not built.
15. Reporting — Failure modes and misleading headline metrics will be documented.
