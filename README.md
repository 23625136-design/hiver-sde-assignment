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