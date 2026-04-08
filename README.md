# 🧠 OpenEnv Support Ticket Environment

## 📌 Overview
This project implements a real-world OpenEnv environment that simulates customer support ticket triage. The goal is to train and evaluate AI agents to classify support tickets into appropriate priority levels (low, medium, high).

## 🎯 Objective
Agents interact with the environment using the standard OpenEnv API:
- `reset()`
- `step(action)`
- `state()`

The task is to correctly classify tickets based on their content while maximizing reward.

---

## 🧩 Tasks

### 🟢 Easy
Simple and clearly defined tickets with obvious priority.

### 🟡 Medium
Mixed tickets requiring better understanding of context.

### 🔴 Hard
Ambiguous tickets that require reasoning and judgment.

---

## ⚙️ Action Space
Agents perform:
- `classify` → assign priority to a ticket

Example:
```python
Action(
    action_type="classify",
    ticket_id=1,
    predicted_priority="high"
)
