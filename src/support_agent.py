import argparse
import pandas as pd


def classify(text):
    text = text.lower()

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--brand", default="AppleSupport")
    parser.add_argument("--sample", action="store_true")
    args = parser.parse_args()

    print("Support Agent Pipeline")
    print("Brand:", args.brand)

    if args.sample:
        print("Sample mode enabled")


if __name__ == "__main__":
    main()