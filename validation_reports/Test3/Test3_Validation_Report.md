# MNOA Test 3 – Validation Report

**Test File Name:** `Test3.xlsx`  
**Date of Test:** July 5, 2025  
**Total Drugs Tested:** 48  
**Test Objective:**  
Scale up from Test 2 by doubling the number of base drugs while applying the same exhaustive set of preprocessing edge cases. This test aims to validate the robustness and consistency of the MNOA algorithm as data complexity increases.

---

## 1. Test Design

- **Source of drug names:**  
  Derived from the “Top 200 Generic+ComboBrand” list (2022), with systematic variant generation for each drug including punctuation, spacing, numeric, and formatting deviations.

- **Base drug count:** 48  

---

## 2. Preprocessing Check

- Preprocessing applied:
  - Lowercased all entries
  - Trimmed and normalized all spacing
  - Handled hyphens, underscores, slashes, brackets, and special characters as valid letters
  - Excluded entries with forbidden `?` symbol
  - Alphabetized the cleaned name list

- ✅ All preprocessing rules were followed and applied correctly across 520 names.

---

## 3. Keystroke Disambiguation Rounds Summary

- **Total Prefix Rounds Run:** 21  
- **Final Possible Mistakes:** 0  
- **Total KPraw across all rounds:** 499  
- **Final %KP:** 0.0  
- **Disambiguated Names (Final):** 480  
- **Unresolved Names (Final):** 0  

---

## 4. Observations

- Resolution performance remained consistent despite dataset doubling from Test 2.
- Some names required longer prefix lengths for unique identification, but the algorithm handled them effectively.
- Clear drop in unresolved names by mid-rounds, demonstrating prefix efficiency.
- No preprocessing errors or irregularities were encountered.

---

## 5. Next Steps

- Expand to ~80 base drugs in Test 4 using the same messy variant logic.
- Monitor prefix length inflation and KP trends under larger input volumes.
- Continue validation of per-round disambiguation logic via `prefix_resolution_rounds.csv`.