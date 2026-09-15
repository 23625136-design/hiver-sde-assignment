import json
import requests

with open("primary_eval.json", "r") as f:
    data = json.load(f)

if isinstance(data, list):
    if not data:
        raise ValueError("primary_eval.json is empty")
    data = data[0]

response = requests.post(
    "http://127.0.0.1:8000/review",
    json=data
)

result = response.json()

with open("final_audit_report.json", "w") as f:
    json.dump(result, f, indent=4)

print("Review completed.")
print(json.dumps(result, indent=4))