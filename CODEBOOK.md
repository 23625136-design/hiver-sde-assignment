# Codebook

## Intent Definitions

- delivery_issue: Delivery is delayed or has a delivery problem.
- delivery_not_received: Customer says the order was not received.
- damaged_or_missing_item: Item arrived damaged or an item is missing.
- refund_issue: Problem with receiving or processing a refund.
- payment_issue: Payment, billing, or payment failure problem.
- return_issue: Customer wants to return an item or has a return problem.
- order_issue: General problem with an order.
- account_issue: Account, login, or account access problem.
- prime_membership_issue: Prime membership related problem.
- digital_device_issue: Digital device or digital service problem.
- other: Does not clearly fit another intent.

## Edge Cases

If multiple intents appear, choose the main customer problem.
If the intent is unclear, use other.
