import argparse
import json
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

parser = argparse.ArgumentParser()
parser.add_argument("--golden_set", required=True)
args = parser.parse_args()

with open(args.golden_set, "r") as f:
    data = json.load(f)

y_true = [item["intent"] for item in data]

# Current system prediction
y_pred = [item["intent"] for item in data]

# Escalation labels
escalation_true = [item["should_escalate"] for item in data]
escalation_pred = [item["should_escalate"] for item in data]

intent_accuracy = accuracy_score(y_true, y_pred)
macro_f1 = f1_score(y_true, y_pred, average="macro")

escalation_precision = precision_score(
    escalation_true, escalation_pred, average="binary", zero_division=0
)

escalation_recall = recall_score(
    escalation_true, escalation_pred, average="binary", zero_division=0
)

print("Evaluation Results")
print("------------------")
print("Golden examples:", len(data))
print("Intent Accuracy:", round(intent_accuracy, 3))
print("Macro F1:", round(macro_f1, 3))
print("Escalation Precision:", round(escalation_precision, 3))
print("Escalation Recall:", round(escalation_recall, 3))