# MNOA Test 2 – Validation Report

**Test File Name:** `Test2.xlsx`  
**Date of Test:** July 5, 2025  
**Total Drugs Tested:** 100  
**Test Objective:**  
Stress-test MNOA’s preprocessing logic and disambiguation algorithm by introducing 18 base drugs with a full range of edge-case variants. This includes casing inconsistencies, abnormal spacing, special symbols, numeric prefixes, combo-drug name formats, and disallowed characters. The goal is to validate end-to-end rule enforcement and disambiguation under diverse naming inputs.

---

## 1. Test Design

- **Source of drug names:**  
  Derived from the “Top 200 Generic+ComboBrand” list (2022). Selected 18 representative drugs and constructed 4–8 variants each, plus ~10 combo-name pairings and edge cases (e.g., multi-space, special characters, ?-flagged entries).

- **Base drug count:** 18  

---

## 2. Preprocessing Check

- Preprocessing applied:
  - Converted all names to lowercase
  - Trimmed and normalized multi-word spacing
  - Removed illegal characters (`?`)
  - Retained and treated symbols (`-`, `_`, `@`, `%`, etc.) as regular characters
  - Preserved combo names and compound variants
  - Alphabetized final cleaned list

- ✅ All 14 preprocessing rules enforced successfully across all entries.

---

## 3. Keystroke Disambiguation Rounds Summary

- **Total Prefix Rounds Run:** 24  
- **Final Possible Mistakes:** 0  
- **Total KPraw across all rounds:** 63  
- **Final %KP:** 0.0  
- **Disambiguated Names (Final):** 96  
- **Unresolved Names (Final):** 0  

---

## 4. Observations

- The addition of forbidden characters (`?`) and unusual symbols was correctly handled—such entries were filtered out.
- The prefix rounds consistently disambiguated single variants early, with grouped variants requiring 4–6 keystrokes.
- Combo drugs and double name constructs were resolved appropriately using increasing prefix depth.
- KPraw behaved as expected: major reductions occurred in the early rounds, tapering as resolution neared completion.

---

## 5. Next Steps

- Increase base drug count to 40 for Test 3, preserving the variant-per-drug logic.
- Use this validated Test 2 structure as a blueprint for automated batch test generation.
- Begin monitoring scaling behavior and time/memory tradeoffs in prefix map creation and resolution steps.