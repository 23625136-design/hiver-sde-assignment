import pandas as pd


df = pd.read_csv("data/sample_data.csv")

# Trivial baseline: always predict the most common intent
most_common = df["label"].mode()[0]


# Simple baseline: keyword-based prediction
def simple_baseline(text):
    text = text.lower()

    if "refund" in text:
        return "refund_issue"
    if "delivery" in text or "late" in text:
        return "delivery_issue"
    if "payment" in text:
        return "payment_issue"
    if "return" in text:
        return "return_issue"
    if "account" in text:
        return "account_issue"

    return "other"


print("Baseline evaluation")
print("Most common intent:", most_common)
print("Trivial baseline: always predicts", most_common)
print("Simple baseline: keyword-based classifier")
print("Total examples:", len(df))