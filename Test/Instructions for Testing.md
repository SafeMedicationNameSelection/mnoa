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
The algorithm correctly processes the 44 raw entries and produces a clean, unique, and alphabetized list of 20 names. This demonstrates that the cleaning logic successfully handles:

- **Case variations:** All names are correctly converted to lowercase.
- **Special Characters:** Hyphens and underscores are correctly treated as spaces.
- **Duplicates:** All variations of a name (e.g., `ferrous_sulfate`, `ferrous-sulfate`) are consolidated into a single entry.
- **Invalid Entry Rejection:** The algorithm is designed to **ignore any name containing a question mark (`?`)**. In this test case, `Atripla?` and `?Avalide` are intentionally dropped.


The final output should match the screenshot below, confirming the data cleaning function is working as expected.

![Test 1 Output](Output%20Images/test-1-output.jpg)

---

## Test Case 2: Disambiguation Performance

### Purpose
This test uses `Test 2.txt` to validate the performance and correctness of the **`disambiguation` algorithm** on a large, clean dataset representative of a real-world formulary.

### Input
The input file `Test 2.txt` contains a list of over 224 medication names.

### Results & Analysis
The algorithm processes the list and provides detailed disambiguation metrics. Key observations from the results include:

-   **Comprehensive Analysis:** The algorithm successfully analyzes the entire list, demonstrating its ability to handle a large number of unique medication names.

-   **Most Powerful Keystroke:** The output correctly identifies the round with the highest Keystroke Power. For this dataset, the highest `KPraw` value is **75**, which occurs in **Round 3**. The display therefore correctly reads **"3"**.

-   **Performance Metrics:** The "Round By Round Stats" table provides a detailed breakdown of the algorithm's efficiency, showing how ambiguity is resolved over time.

The final output should match the screenshot below, confirming the disambiguation engine is performing correctly on a large scale.

![Test 2 Output](Output%20Images/test-2-output.jpg)