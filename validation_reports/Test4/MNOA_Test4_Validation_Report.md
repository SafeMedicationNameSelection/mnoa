# MNOA Test 4 – Validation Report

**Test File Name:** `Test4.xlsx`  
**Date of Test:** July 6, 2025  
**Total Drugs Tested:** 1136  
**Test Objective:**  
Evaluate the scalability and performance of the MNOA algorithm when resolving a mid-size input containing ~80 base drugs with their full edge-case variant sets. This includes all key preprocessing rules exercised previously, now distributed across a broader input to simulate real-world complexity and test memory/speed behavior.

---

## 1. Test Design

- **Source of drug names:**  
  Derived from the “Top 200 Generic+ComboBrand” list (2022). Each of the ~80 base medications is expanded into a suite of edge-case variants for preprocessing stress testing.

- **Base drug count:** ~80  

---

## 2. Preprocessing Check

- Preprocessing applied:
  - Converted all names to lowercase
  - Removed leading/trailing and excess internal spaces
  - Preserved special characters (`-`, `_`, `@`, `%`, etc.)
  - Removed any names with the illegal `?` character
  - Alphabetized the cleaned list

- ✅ Preprocessing rules were successfully and consistently applied across a large input set.

---

## 3. Keystroke Disambiguation Rounds Summary

- **Total Prefix Rounds Run:** 30  
- **Final Possible Mistakes:** 0  
- **Total KPraw across all rounds:** 1111  
- **Final %KP:** 0.0  
- **Disambiguated Names (Final):** 1036  
- **Unresolved Names (Final):** 0  

---

## 4. Observations

- The number of rounds required scaled predictably with name length.
- Every unresolved case was eventually disambiguated before the final round.
- Despite the increased number of inputs, algorithm performance remained efficient and consistent.
- No unexpected formatting or disambiguation failures were observed during prefix resolution.
- Edge-case handling remains robust even with significantly more names than in prior tests.

---

## 5. Next Steps

- Proceed to Test 5, which will serve as a full stress test of all 223 base drugs with expanded variants.
- Assess resolution times and memory behavior in high-scale contexts.
- Continue detailed manual validation of disambiguation correctness for selected entries from each test.
