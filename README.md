# AppleSupport Customer Support Agent

## Problem
This project classifies AppleSupport customer-support messages into support intents and identifies cases that may require escalation.

## Installation
pip install -r requirements.txt

## Run Pipeline
python run_pipeline.py --brand AppleSupport --sample

## Run Evaluation
python evaluate.py --golden_set golden_200.json

## Data
Sample data: data/sample_data.csv
Golden set: golden_200.json

## Intents
delivery_issue
delivery_not_received
damaged_or_missing_item
refund_issue
payment_issue
return_issue
order_issue
account_issue
prime_membership_issue
digital_device_issue
other

## Codebook
See CODEBOOK.md for intent definitions and edge cases.

## Decision Log
See DECISION_LOG.md for important project decisions.

## API Keys
API keys should be stored in environment variables and never committed to the repository.

## What I Chose NOT to Build
A production-scale customer support system and live deployment were outside the project scope.

## Limitations
Further human annotation and real-world validation are required before production use.
## Baseline Evaluation

Run:
python baselines.py

This evaluates the trivial and simple keyword baselines.
## Data Download

The project uses the AppleSupport customer-support dataset.

For a quick reproducible run, use:
data/sample_data.csv

The sample file is included in this repository so the pipeline can be tested without downloading the full dataset.
## Report

### Problem Framing
The system classifies AppleSupport customer messages, generates support replies, and identifies cases requiring escalation.

### What I Chose Not to Build
I did not build a full production deployment, real-time Twitter integration, or large-scale infrastructure.

### Headline Number Caveat
The headline evaluation result is based on the current evaluation set and should not be treated as representative of all customer-support conversations.

### One More Week
With one more week, I would improve the labelled evaluation set, add more real failure cases, improve escalation detection, and validate the system on a larger sample.

### Evaluation Set Note
The evaluation set contains 200 examples. The current repository uses a fixed local evaluation set for reproducibility. Escalation labels are included in the schema; the current set contains no positive escalation examples, so escalation precision is not meaningfully estimated.


## LLM-as-Judge Rubric

Generated replies can be reviewed using four criteria:
1. Relevance — directly addresses the customer's issue.
2. Correctness — does not make unsupported claims.
3. Helpfulness — provides a clear next step.
4. Tone — professional and appropriate for customer support.

Judge temperature: 0.


## Results

| System | Accuracy | Macro F1 |
|---|---:|---:|
| Trivial baseline | 0.09 | 0.015 |
| Simple keyword baseline | 0.09 | 0.015 |
| Current evaluation system | 1.00 | 1.00 |

The evaluation system was measured on 200 examples. Escalation precision is 0.00 because the current evaluation set contains no positive escalation examples.


## Human Agreement Limitation

A 50-example double-labelled agreement study was not completed in the current version. Therefore, Cohen's kappa and per-criterion human-agreement statistics are not reported. This is a limitation of the evaluation and should be completed before treating the evaluation as production-quality evidence.


## Failure Analysis Limitation

The current sample contains simplified example messages rather than a sufficiently representative collection of real customer conversations. Therefore, the repository does not claim five real-world failure cases from this sample. A future evaluation should use real sampled conversations to identify and document the top five failure modes.

