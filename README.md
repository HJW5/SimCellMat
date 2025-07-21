# 🧬 SimCellMat: A Python Model for Biomaterial Degradation & Cell Interaction

SimCellMat is a Python simulation tool that models how **biomaterials degrade over time** inside the body and how **cell populations respond** to that degradation.

The goal is to explore how different materials (e.g. PLA, magnesium) behave in biological environments and how their **degradation profiles** affect **cell attachment, growth, or failure** — a key consideration in **biomaterials**, **implants**, and **regenerative medicine**.

---

## 📈 What It Does

- Simulates **mass loss over time** using exponential degradation models
- Allows creation of **custom materials** with properties like:
  - Degradation rate
  - Young’s modulus
  - Density
  - Toxicity threshold (for later biological interaction)
- Plots **degradation curves**
- (Coming soon) Simulates **cell population dynamics** in response to material breakdown

---

## 🧪 Why This Matters

Biomaterials used in implants, scaffolds, or prosthetics **interact dynamically** with surrounding tissue. Understanding how fast a material degrades — and how that impacts cell health — is essential for:

- Designing tissue scaffolds
- Evaluating implant safety
- Balancing resorption rate and tissue regeneration

This project aims to simulate that interaction using simple, accessible tools and a modular Python structure.

---

## 🛠 Features

- `Material` class for defining any degradable material
- Modular functions for:
  - `simulate_degradation()` → exponential decay model
  - `plot_degradation()` → save and view time-series graphs
- Supports multiple material comparisons
- Outputs `.png` plots to the `/plots` folder

---

## 🐍 Requirements

- Python 3.x
- `matplotlib`
- `numpy`

Install dependencies with:

```bash
pip install matplotlib numpy
