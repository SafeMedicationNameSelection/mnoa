# MNOA Backend Test Datasets

This folder contains standardized datasets used to test and validate the MNOA backend algorithm. Each file represents a specific test case.

---

## Test File 1: `Test 1.xlsx`

### Purpose
This dataset is designed to rigorously test the **`clean_names` function**. It contains a comprehensive list of medication names with common real-world formatting errors.

### Contents
The spreadsheet contains names with a variety of intentional issues, including:
* Mixed upper and lower case letters (`ADVAIR`, `FaMOTidine`)
* Leading, trailing, and multiple internal spaces (`Aug mentin`)
* Special characters, numbers, and symbols (`Fioricet()`, `123hyzaar4`, `Fent-anyl`, `!Fluticasone`)
* Invalid entries that should be ignored (`?Avalide`, `Atripla?`)

### Expected Outcome
When processed by the MNOA tool, the `clean_names` function should successfully parse this file and produce a clean, alphabetized, and deduplicated list. The final output in the "List Analysed" panel should contain only standardized alphabetic names.

---

## Test File 2: `Test 2.xlsx`

### Purpose
This dataset contains a large, clean list of 200+ unique medication names from the top US prescriptions. It is designed to test the **`disambiguation` algorithm's** performance and its ability to correctly identify and resolve prefix overlaps.

### Contents
The spreadsheet contains a single column of alphabetized, pre-cleaned medication names. The list is intentionally diverse to simulate a real-world analysis scenario with numerous potential overlaps (e.g., "Lisinopril", "Lorazepam", "Losartan", "Lovastatin").

### Expected Outcome
When this list is processed, the tool's output panels should accurately reflect the disambiguation process. The "Round By Round Stats" and "Keystroke Power" tables will be populated with metrics demonstrating how the algorithm resolves conflicts as more characters are added.