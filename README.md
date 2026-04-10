---
title: OpenEnv Support Ticket
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# 🧠 OpenEnv Support Ticket Environment

## 📌 Overview
This project implements an OpenEnv environment for customer support ticket triage. It simulates classification of tickets into priority levels.

## 🎯 Objective
Agents interact using:
- reset()
- step(action)
- state()

Goal: classify tickets correctly and maximize reward.

## 🧩 Tasks
- Easy: Clear priority tickets  
- Medium: Mixed context tickets  
- Hard: Ambiguous tickets  

## ⚙️ Action Space
Agents perform:
- classify → assign priority (low, medium, high)

## ▶️ Run
python inference.py
Action(
    action_type="classify",
    ticket_id=1,
    predicted_priority="high"
)
