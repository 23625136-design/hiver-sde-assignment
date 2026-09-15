import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv("data/sample_data.csv")

y_true = df["label"]

# Trivial baseline: most common class
most_common = y_true.mode()[0]
trivial_pred = [most_common] * len(df)


# Simple keyword baseline
def simple_baseline(text):
    text = str(text).lower()

    if "refund" in text:
        return "refund_issue"
    elif "delivery" in text or "late" in text:
        return "delivery_issue"
    elif "payment" in text:
        return "payment_issue"
    elif "return" in text:
        return "return_issue"
    elif "account" in text:
        return "account_issue"
    else:
        return "other"


simple_pred = [simple_baseline(text) for text in df["customer_message"]]

print("Baseline Evaluation")
print("-------------------")
print("Total examples:", len(df))

print("\nTrivial Baseline")
print("Accuracy:", round(accuracy_score(y_true, trivial_pred), 3))
print("Macro F1:", round(f1_score(y_true, trivial_pred, average="macro", zero_division=0), 3))

print("\nSimple Keyword Baseline")
print("Accuracy:", round(accuracy_score(y_true, simple_pred), 3))
print("Macro F1:", round(f1_score(y_true, simple_pred, average="macro", zero_division=0), 3))