# Codebook

## Intent Definitions

### delivery_issue
Delivery is delayed or there is a problem with delivery.

### delivery_not_received
The customer says the order was not received.

### damaged_or_missing_item
An item arrived damaged, or an expected item is missing.

### refund_issue
The customer has a problem receiving or processing a refund.

### payment_issue
The customer reports a payment, billing, or payment-failure problem.

### return_issue
The customer wants to return an item or has a problem with a return.

### order_issue
A general order problem that does not fit a more specific intent.

### account_issue
The problem concerns the customer account, login, or account access.

### prime_membership_issue
The problem concerns Prime membership.

### digital_device_issue
The problem concerns a digital device or digital service.

### other
The message does not clearly fit any of the above intents.

## Edge Cases

1. If multiple intents appear, choose the customer's main problem.
2. If a refund is specifically the problem, use refund_issue rather than order_issue.
3. If the customer never received the order, use delivery_not_received.
4. If an item is damaged or missing, use damaged_or_missing_item.
5. If the intent is unclear, use other.
6. Do not infer an intent that is not supported by the message.

## Escalation

### Auto-handled
Use when the issue can be handled by the normal automated support flow.

### Escalate
Use when the case requires human review or cannot be safely resolved automatically.

## Annotation Rule

Every golden-set example must contain:
- intent
- should_escalate
- customer text