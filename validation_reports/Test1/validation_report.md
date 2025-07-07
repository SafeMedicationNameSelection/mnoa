# MNOA Test [X] – Validation Report

**Test File Name:** `Test1.xlsx`  
**Date of Test:** [July 5, 2025]  
**Total Drugs Tested:** [Insert number]  
**Test Objective:**  
[Summarize what this test is meant to evaluate – e.g., preprocessing edge cases, algorithm behavior under large volume, etc.]

---

## 1. Test Design

- **Source of drug names:**  
  [e.g., "Top 200 Generic+ComboBrand list, curated for case/spacing/hyphen/character variants."]

- **Base drug count:** [Insert count]  
- **Variants per drug:** [List if structured – e.g., spacing, casing, symbols, double names, forbidden characters, etc.]  
- **Special edge cases included:**  
  - [ ] Case and space variants  
  - [ ] Hyphens and underscores  
  - [ ] Special characters and punctuation  
  - [ ] Numeric characters and digits  
  - [ ] Double-name combos  
  - [ ] Forbidden characters (e.g., `?`)  
  - [ ] Brackets, braces, parentheses  
  - [ ] Multi-word combinations  

---

## 2. Preprocessing Validation

- **Expected Output:** Alphabetized, lowercase, duplicates removed, `?` excluded  
- **`preprocessed_names.csv` sample:**

```
[Paste a few example names from output here, like a 5–10 line preview]
```

- **Checkpoints:**  
  - ✅ Are all names lowercase?  
  - ✅ Are multiple spaces normalized to one?  
  - ✅ Are forbidden characters excluded?  
  - ✅ Is list alphabetized?

---

## 3. Algorithm Performance (Round Summary)

- **Source File:** `mnoa_output.csv`

| characters | search_terms | search_space_size | names_by_length | unresolved_items | disambiguated_names | possible_misses | KPraw | %KP    |   |
|------------|--------------|-------------------|-----------------|------------------|---------------------|-----------------|-------|--------|---|
| 1          | 16           | 42                | 0               | 29               | 13                  | 26              | 0     | 0.0    |   |
| 2          | 8            | 29                | 0               | 26               | 16                  | 21              | 5     | 0.119  |   |
| 3          | 6            | 26                | 0               | 26               | 16                  | 20              | 1     | 0.0238 |   |
| 4          | 7            | 26                | 0               | 24               | 18                  | 19              | 1     | 0.0238 |   |
| 5          | 5            | 24                | 0               | 24               | 18                  | 19              | 0     | 0.0    |   |
| 6          | 5            | 24                | 0               | 24               | 18                  | 19              | 0     | 0.0    |   |
| 7          | 5            | 24                | 0               | 24               | 18                  | 19              | 0     | 0.0    |   |
| 8          | 20           | 23                | 1               | 5                | 36                  | 3               | 16    | 0.381  |   |
| 9          | 2            | 4                 | 1               | 4                | 36                  | 2               | 1     | 0.0238 |   |


---

## 4. Prefix Resolution Behavior

- **Source File:** `prefix_resolution_rounds.csv`  
- Comments:
  - [Write down any interesting observations like certain prefixes repeatedly failing, late disambiguation, etc.]

---

## 5. Observations & Notes

- [Write human-readable insights – any strange behavior, pattern deviations, or performance bottlenecks.]

---

## 6. Conclusion

- ✅ Did the algorithm perform as expected?
- ❌ Any bugs, unresolved issues, or misclassifications?
- Next actions:  
  [e.g., "Refine preprocessing rules," "Run with increased volume in next test," etc.]
