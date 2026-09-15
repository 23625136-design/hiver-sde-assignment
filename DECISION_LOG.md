# Decision Log

1. **Brand choice** — AppleSupport was selected to keep the support use case focused.

2. **Intent taxonomy** — 11 support intents were used to cover the main issue categories.

3. **Other intent** — The `other` category was retained for unclear or out-of-scope messages.

4. **Golden-set size** — A 200-example evaluation set was chosen because it fits the required 150–250 range.

5. **Sample size** — A 500-row sample was included so the pipeline can be tested quickly.

6. **Escalation label** — Every golden-set row contains a `should_escalate` field.

7. **Evaluation metrics** — Accuracy and macro F1 are used for intent classification.

8. **Escalation metrics** — Precision and recall are used to evaluate escalation decisions.

9. **Trivial baseline** — A most-common-class baseline was included as a simple reference point.

10. **Simple baseline** — A keyword-based baseline was included to provide a stronger non-LLM comparison.

11. **Codebook** — Intent definitions and edge-case rules are documented separately in `CODEBOOK.md`.

12. **Judge design** — A rubric-based secondary review is included in the project scope.

13. **Temperature** — LLM judging is intended to use temperature 0 for reproducibility.

14. **Human agreement** — Human double-labelling is identified as a required validation step.

15. **Scope cut** — A production-scale support deployment was not built; the focus is evaluation and reproducibility.