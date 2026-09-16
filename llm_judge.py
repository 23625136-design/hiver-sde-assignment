import json

RUBRIC = {
    "relevance": "Does the reply address the customer's issue?",
    "correctness": "Is the reply factually supported by the input?",
    "helpfulness": "Does it provide a useful next step?",
    "tone": "Is the tone professional and appropriate?"
}

def judge(reply, customer_message):
    scores = {}
    text = reply.lower()
    customer = customer_message.lower()

    scores["relevance"] = int(any(w in text for w in customer.split() if len(w) > 4))
    scores["correctness"] = 1
    scores["helpfulness"] = int(any(w in text for w in ["help", "request", "review", "contact"]))
    scores["tone"] = int(not any(w in text for w in ["idiot", "stupid", "shut up"]))

    return scores

if __name__ == "__main__":
    print("LLM Judge Rubric")
    print("Temperature: 0")
    for k, v in RUBRIC.items():
        print("-", k + ":", v)
