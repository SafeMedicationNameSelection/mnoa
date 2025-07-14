import csv  # Standard library module for reading and writing CSV files
import sys  # Provides access to system-specific parameters and functions (e.g., stdin)

# === Step 1: Read raw input from terminal ===
# ⚠️ TESTING ONLY: This function is used only for manual testing in terminal.
def read_input_from_terminal():
    """
    Prompts the user to input medication names via the terminal, one per line.
    Input is terminated by Ctrl+D (macOS) or Ctrl+Z (Windows).
    
    Returns:
        List[str]: A list of non-empty, whitespace-trimmed medication names.
    """
    print("Paste medication names (one per line). Then press Ctrl+D (on Mac) or Ctrl+Z (on Windows) to finish:")
    names = sys.stdin.read().splitlines()  # Reads multi-line input and splits into lines
    return [line.strip() for line in names if line.strip()]  # Trims whitespace and removes empty lines


# === Step 2: Clean input names for standardization ===
def clean_names(raw_names):
    """
    Cleans and normalizes raw input names.
    - Converts to lowercase
    - Removes excess internal whitespace
    - Excludes entries containing '?' (potential invalid entries)
    - Removes duplicates and sorts list

    Args:
        raw_names (List[str]): Unprocessed medication names

    Returns:
        List[str]: Cleaned, sorted, and deduplicated list of medication names
    """
    cleaned = []
    for name in raw_names:
        name = name.strip().lower()             # Normalize: lowercase and trim
        name = " ".join(name.split())           # Replace multiple spaces with a single space
        if "?" in name:
            continue                            # Exclude questionable entries
        cleaned.append(name)
    return sorted(set(cleaned))                 # Deduplicate and sort alphabetically


# === Step 3: Core disambiguation logic ===
# ✅ BACKEND READY (Minor edits needed):
# - The logic is backend-safe and modular.
# - To make it fully backend-friendly:
#   🔸 Remove all print() statements (used for terminal testing).
# - Inputs and outputs are already structured as clean Python data (lists/dicts). 
 

def disambiguate(names):
    """
    Performs round-wise prefix-based disambiguation of medication names.
    At each round 'k', the algorithm:
    - Builds a prefix map of the first k characters
    - Identifies unique prefixes that map to a single name (resolved)
    - Tracks unresolved names and possible misses
    - Computes Keystroke Power (KP) metrics

    Args:
        names (List[str]): Preprocessed and sorted medication names

    Returns:
        Tuple[List[Dict], List[Dict]]: Summary metrics per round and detailed prefix disambiguation logs
    """
    results = []          # Stores summary metrics for each round
    prefix_details = []   # Stores detailed log of which prefixes resolved or failed

    if not names:
        print("❗Error: No names to disambiguate.")  # ❌ Backend version will remove this print
        return results, prefix_details

    total_names = len(names)                             # Total number of input names
    max_len = max(len(n) for n in names)                 # Longest name determines max prefix length
    resolved_set = set()                                 # Keeps track of names already disambiguated
    search_space = names.copy()                          # Active pool of names still unresolved
    previous_misses = None                               # To calculate improvement (KP) between rounds

    # Iterate from prefix length k = 1 up to the longest name
    for k in range(1, max_len + 1):
        prefix_map = {}  # Maps each prefix to a list of full names that start with that prefix

        # Categorize names by length
        names_by_length = [n for n in search_space if len(n) == k]   # Names exactly k characters
        remaining_names = [n for n in search_space if len(n) >= k]   # Names long enough to test prefix

        # Build prefix map: prefix → [list of names sharing it]
        for name in remaining_names:
            prefix = name[:k]
            if prefix not in prefix_map:
                prefix_map[prefix] = []
            prefix_map[prefix].append(name)

        disambiguated = []  # Names uniquely resolved this round
        unresolved = []     # Names that are still ambiguous

        # Process each prefix group
        for prefix, group in prefix_map.items():
            if len(group) == 1:
                # ✅ Unique match – resolved
                disambiguated.append(group[0])
                prefix_details.append({
                    "round": k,
                    "prefix": prefix,
                    "disambiguated": group[0],
                    "unresolved": ""
                })
            else:
                # ❌ Ambiguous – unresolved
                unresolved.extend(group)
                prefix_details.append({
                    "round": k,
                    "prefix": prefix,
                    "disambiguated": "",
                    "unresolved": ", ".join(group)
                })

        # Compute Keystroke Power (KP) metrics
        possible_misses = sum(len(group) - 1 for group in prefix_map.values() if len(group) > 1)
        KPraw = 0 if k == 1 else previous_misses - possible_misses
        percent_KP = 0.0 if k == 1 else round(KPraw / total_names, 4)
        previous_misses = possible_misses

        # Update resolved names and shrink the search space
        resolved_set.update(disambiguated)
        search_space = list(set(remaining_names) - set(disambiguated))

        # ❗Terminal-only logging – will be removed in backend version
        print(f"\n--- Round {k} ---")
        print(f"Prefixes tested: {len(prefix_map)}")
        print(f"Names with length = {k}: {len(names_by_length)}")
        print(f"Disambiguated this round: {len(disambiguated)}")
        print(f"Remaining unresolved: {len(unresolved)}")
        print(f"Possible misses: {possible_misses}")
        print(f"KPraw: {KPraw}, %KP: {percent_KP * 100:.2f}%")

        # Save round-level summary
        results.append({
            "characters": k,
            "search_terms": len(prefix_map),
            "search_space_size": len(remaining_names),
            "names_by_length": len(names_by_length),
            "unresolved_items": len(unresolved),
            "disambiguated_names": len(resolved_set),
            "possible_misses": possible_misses,
            "KPraw": KPraw,
            "%KP": percent_KP
        })

        if not unresolved:
            break  # ✅ All names resolved – stop loop early

    return results, prefix_details  # Return round summaries and detailed prefix logs



# === Step 4: Export all results as CSVs ===
# ⚠️ TESTING ONLY: Final app will not write CSVs — this is just for debug/output inspection.
def save_to_csv(
    results,
    prefix_data,
    cleaned_names,
    output_dir=".",
    prefix_file="prefix_resolution_rounds.csv",
    names_file="preprocessed_names.csv",
    result_file="mnoa_output.csv"
):
    """
    Saves all outputs to CSV files.

    Args:
        results (List[Dict]): Round-wise summary statistics
        prefix_data (List[Dict]): Prefix-level disambiguation logs
        cleaned_names (List[str]): Cleaned medication names
        output_dir (str): Output directory path
        prefix_file (str): Filename for prefix resolution details
        names_file (str): Filename for cleaned names
        result_file (str): Filename for round summary output
    """
    if results:
        with open(f"{output_dir}/{result_file}", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)

    if prefix_data:
        with open(f"{output_dir}/{prefix_file}", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=prefix_data[0].keys())
            writer.writeheader()
            writer.writerows(prefix_data)

    if cleaned_names:
        with open(f"{output_dir}/{names_file}", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name"])
            for name in cleaned_names:
                writer.writerow([name])


# === MAIN EXECUTION ===
# ⚠️ TESTING ONLY: This block is for running the script manually in terminal.
if __name__ == "__main__":
    print("🔹 Starting MNOA Terminal Mode...")

    raw = read_input_from_terminal()
    print(f"\nOriginal names ({len(raw)}): {raw}")

    print("\n🔹 Cleaning names...")
    cleaned = clean_names(raw)
    print(f"Cleaned names ({len(cleaned)}): {cleaned}")

    print("\n🔹 Running disambiguation...")
    results, prefix_data = disambiguate(cleaned)

    print("\n🔹 Saving CSV outputs...")
    save_to_csv(results, prefix_data, cleaned)

    print("\n✅ Done.")
