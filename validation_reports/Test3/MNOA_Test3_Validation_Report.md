# MNOA Test 3 – Validation Report

**Test File Name:** `Test3.xlsx`  
**Date of Test:** July 5, 2025  
**Total Drugs Tested:** 294  
**Test Objective:**  
Evaluate the MNOA algorithm’s accuracy and stability at mid-scale. This test expands on Test 2 by doubling the number of base drugs while preserving variant complexity—such as special characters, spacing issues, forbidden symbols, and combo formats—to stress test preprocessing and resolution logic under increased input size.

---

## 1. Test Design

- **Source of drug names:**  
  Derived from the “Top 200 Generic+ComboBrand” list (2022), expanded to 40 drugs with the same pattern of variant corruption applied in Test 2.

- **Base drug count:** 40  

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

- **Total Prefix Rounds Run:** 36
- **Final Possible Mistakes:** 0.0
- **Total KPraw across all rounds:** 278
- **Final %KP:** 0.0
- **Disambiguated Names (Final):** 258.0
- **Unresolved Names (Final):** 0.0

---

## 4. Observations

- Successfully scaled to 40 drugs while maintaining expected prefix resolution behavior.
- Some prefix conflicts were observed deeper into the keystroke rounds, but the algorithm maintained full disambiguation.
- The result reinforces confidence in the correctness of disambiguation logic under moderate dataset sizes.
- Metrics show effective resolution and progressive reduction in unresolved terms.

---

## 5. Next Steps

- Test 4 will double the dataset again (~80 base drugs) using the same corruptions.
- Begin tracking any runtime or memory overhead as volume increases.
- Continue validating prefix output alignment manually for randomly selected rounds.
