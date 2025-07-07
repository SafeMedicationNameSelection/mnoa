# MNOA Test 5 – Validation Report

**Test File Name:** `Test5.xlsx`  
**Date of Test:** July 6, 2025  
**Total Drugs Tested:** 223  
**Test Objective:**  
Evaluate algorithm scalability and robustness across the complete 2022 Generic+ComboBrand list. Assess stability of disambiguation metrics (e.g., KPraw, %KP) on the largest, most realistic dataset including full range of messy variants.

---

## 1. Test Design

- **Source of drug names:**  
  All 223 entries from the “Top 200 Generic+ComboBrand” 2022 list (with some combo brand splits).

- **Base drug count:** 223  
- **Variants per drug:**  
  - 18 messy variants per base drug targeting known edge cases  
  - 30 combo drug name pairs with 12 variants each

---

## 2. Preprocessing Check

- ✅ Rules applied:
  - Lowercased all names
  - Trimmed leading/trailing/multiple internal spaces
  - Allowed special characters (symbols, numbers, punctuation)
  - Excluded names with illegal characters (e.g., `?`)
  - Alphabetized the preprocessed name list
- ✅ Total Preprocessed Names: 4,373

---

## 3. Keystroke Disambiguation Rounds Summary

- **Total Prefix Rounds Run:** 30  
- **Final Possible Mistakes:** 0  
- **Total KPraw across all rounds:** 164  
- **Final %KP:** 0.734  
- **Disambiguated Names (Final):** 4,373  
- **Unresolved Names (Final):** 0  

---

## 4. Observations

- The largest stress test passed with no unresolved names.
- Disambiguation continued to improve across all prefix rounds with no stagnation.
- Memory and runtime performance remained stable.
- High %KP and steady KPraw indicate efficient prefix resolution under real-world name distributions.

---

## 5. Next Steps

- Finalize reporting and documentation for publication.
- Begin frontend integration testing using selected edge-case files (Tests 1 & 2).
- Continue benchmarking vs similar disambiguation models if applicable.
