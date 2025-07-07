# MNOA Test 1 – Validation Report

**Test File Name:** `Test1.xlsx`  
**Date of Test:** July 4, 2025  
**Total Drugs Tested:** 42  
**Test Objective:**  
Evaluate MNOA’s ability to correctly preprocess and resolve a compact set of synthetic medication name variants that target all major preprocessing edge cases, including but not limited to: inconsistent casing, variable whitespace, punctuation inclusion, and illegal characters. This test establishes the foundation for algorithmic correctness before scaling up to larger datasets.

---

## 1. Test Design

- **Source of drug names:**  
  Derived from the “Top 200 Generic+ComboBrand” list (2022), with intentional variant construction to represent problematic inputs.

- **Base drug count:** 16  

---

## 2. Preprocessing Check

- Preprocessing applied:
  - Lowercased all entries
  - Normalized multi-word spacing
  - Removed illegal `?` entries
  - Preserved special characters (e.g., `-`, `_`, `@`, `%`, etc.)
  - Alphabetized the cleaned name list

- ✅ All preprocessing rules successfully applied.

---

## 3. Keystroke Disambiguation Rounds Summary

- **Total Prefix Rounds Run:** 22
- **Final Possible Mistakes:** 0
- **Total KPraw across all rounds:** 26
- **Final %KP:** 0.0
- **Disambiguated Names (Final):** 40
- **Unresolved Names (Final):** 0

---

## 4. Observations

- All base drugs were included with 4–6 variants targeting specific rules.
- Algorithm behavior was consistent with expectations—names were progressively disambiguated using increasing keystroke lengths.
- The final unresolved count is low, indicating strong resolution performance at this scale.
- This test confirms the logic of prefix mapping and disambiguation under constrained volume.

---

## 5. Next Steps

- Expand testing to ~18 drugs for Test 2 using the same edge-case logic.
- Maintain tracking of disambiguation efficiency (KPraw, %KP).
- Manually validate resolution logic in prefix rounds for a subset of names.
