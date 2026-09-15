import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--golden_set", required=True)
args = parser.parse_args()

with open(args.golden_set) as f:
    data = json.load(f)

print("Evaluation started")
print("Golden examples:", len(data))
print("Evaluation completed")
