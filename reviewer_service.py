from fastapi import FastAPI
import re
import argparse
import uvicorn

app = FastAPI()

ESCALATION_PATTERN = r'^(Auto-handled|Escalate: .*)$'


@app.post("/review")
def review(data: dict):
    discrepancies = []
    escalation = str(data.get("should_escalate", ""))

    if not re.match(ESCALATION_PATTERN, escalation):
        discrepancies.append("Invalid escalation format")

    return {
        "audit_status": "APPROVED" if not discrepancies else "REVIEW_REQUIRED",
        "total_discrepancies": len(discrepancies),
        "reviewer_notes": discrepancies or ["All validation checks passed."]
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    uvicorn.run(app, host="0.0.0.0", port=args.port)
