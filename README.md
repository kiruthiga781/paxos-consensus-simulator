# 🧠 Paxos Consensus Algorithm Simulator

## 📘 Overview
This mini project simulates the **Paxos Consensus Algorithm**, a fundamental concept in distributed systems used to achieve **agreement (consensus)** among multiple nodes even in the presence of failures or network delays.  

It demonstrates how proposers and acceptors communicate to agree on a single value using two main phases — *Prepare* and *Accept*.

---

## 🎯 Objectives
- To understand how distributed systems reach agreement.
- To simulate the **Paxos algorithm** using Python.
- To visualize how proposals are accepted or rejected based on majority voting.

---

## ⚙️ How the Algorithm Works

### 🔹 Roles
- **Proposers** – Send proposals with a unique proposal ID.
- **Acceptors** – Promise to consider only higher proposal IDs and accept a single value.
- **Learners** – Learn the final chosen value.

### 🔹 Phases
1. **Prepare Phase**
   - Proposer sends a prepare request with a proposal number.
   - Acceptors promise not to accept proposals with lower numbers.
2. **Accept Phase**
   - Proposer sends an accept request.
   - If a majority of acceptors accept, the value is chosen.

---

## 💻 Implementation (Python)
The simulation code is available in the file:
