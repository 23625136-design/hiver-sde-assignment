import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--brand", default="AppleSupport")
parser.add_argument("--sample", action="store_true")
args = parser.parse_args()

df = pd.read_csv("data/sample_data.csv")

print("AppleSupport Customer Support Pipeline")
print("Brand:", args.brand)
print("Sample mode:", args.sample)
print("Total rows:", len(df))
print("Pipeline completed successfully")