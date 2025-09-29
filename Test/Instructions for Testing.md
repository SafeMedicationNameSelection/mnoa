# MNOA Test Guide

This folder contains two standardized text files with datasets for testing and validating the MNOA backend algorithm. This guide explains how to use them and what the results signify.

---

## How to Run a Test

To use these test files, follow these steps:

1.  Ensure the MNOA application is running and accessible in your web browser.
2.  Open either `Test 1.txt` or `Test 2.txt` on your computer.
3.  Select and copy the entire list of medication names (you can use `Cmd+A` or `Ctrl+A` to select all).
4.  Paste the copied list into the input text area on the MNOA web interface.
5.  Click the "Analyze" button (▶) to process the list and view the results.

---

## Test Case 1: Data Cleaning Validation

### Purpose
This test uses `Test 1.txt` to validate the robustness of the algorithm's **`clean_names` function** against messy, real-world data.

### Input
The input file `Test 1.txt` contains 46 raw medication names with a variety of intentional formatting issues.

### Results & Analysis
The algorithm processes the 44 valid entries (after dropping two names containing a "?") and produces a clean, unique, and alphabetized list of 43 names. This demonstrates that the cleaning logic successfully handles:

- **Case and Spacing:** All names are correctly converted to lowercase, and extra spaces are normalized.
- **Character Preservation:** The algorithm correctly preserves all numbers and special characters (e.g., `()`, `[]`, `{}`, `*`, `!`, `#`, `@`, `:`, `;`, `,`, `-`, `_`), treating them as part of the medication name.
- **Duplicate Removal:** The algorithm correctly identifies and removes a duplicate entry (e.g., `FerrOUS sulfate` and `ferrous SULFATE`).
- **Invalid Entry Rejection:** The algorithm correctly drops any name containing a question mark (`?`).

### Expected Output
The final results in the application should match the summary statistics below.

**Overall List Stats:** 
Names Provided: 46
Names Dropped: 2
Duplicates Removed: 1
Names Analysed: 43

**Disambiguation Stats:** 
Most Powerful Keystroke: 1
(KPraw = 15)
Total Rounds to Disambiguate: 12

For a complete list of all cleaned names and detailed round-by-round logs, please see the **[Test 1 Output Logs](Test%201%20Output%20Logs.md)**.

The visual output in the application should also match the screenshot below.

![Test 1 Output](Output%20Images/test-1-output.jpg)

---

## Test Case 2: Disambiguation Performance

### Purpose
This test uses `Test 2.txt` to validate the performance and correctness of the **`disambiguation` algorithm** on a large, clean dataset representative of a real-world formulary.

### Input
The input file `Test 2.txt` contains 224 raw medication names.

### Results & Analysis
Based on the test output, the algorithm successfully processes the input list and provides detailed disambiguation metrics. Key observations from the results include:

-   **Duplicate Removal:** The algorithm correctly identifies that there are no duplicate entries in the raw list that become identical after cleaning, resulting in a final analyzed list of 224 unique names.
-   **Most Powerful Keystroke:** The output correctly identifies the round with the highest Keystroke Power. For this dataset, the highest `KPraw` value is **75**, which occurs in **Round 3**.
-   **Performance Metrics:** The "Round By Round Stats" table provides a detailed breakdown of the algorithm's efficiency, showing how ambiguity is resolved over time.

### Expected Output
The final results in the application should match the following summary statistics.

**Overall List Stats:**
Names Provided: 224
Names Dropped: 0
Duplicates Removed: 0
Names Analysed: 224

**Disambiguation Stats:**
Most Powerful Keystroke: 3
(KPraw = 75)
Total Rounds to Disambiguate: 12

For a detailed breakdown of the final cleaned list and round-by-round statistics, please see the **[Test 2 Output Logs](Test%202%20Output%20Logs.md)**.

The visual output in the application should also match the screenshot below.

![Test 2 Output](Output%20Images/test-2-output.jpg)