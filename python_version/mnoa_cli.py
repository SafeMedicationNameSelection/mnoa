from collections import defaultdict
import pandas as pd
import re

# Constants
INPUT_FILE = "Test1.xlsx"
SHEET_NAME = "Sheet1"
OUTPUT_CSV = "mnoa_output.csv"
PREPROCESSED_NAMES_CSV = "preprocessed_names.csv"
PREFIX_DETAIL_CSV = "prefix_resolution_rounds.csv"

# Preprocessing function
def preprocess_names(name_series):
    """
    Cleans and normalizes medication names according to MNOA preprocessing rules:
    - Lowercases all names
    - Preserves multiple words with one space
    - Removes leading/multiple spaces
    - Accepts symbols as regular characters
    - Removes names with '?' characters
    - Sorts and deduplicates final list
    """
    cleaned = (
        name_series.astype(str)
        .str.lower()
        .apply(lambda s: re.sub(r"\s+", " ", s.strip()))  # normalize spaces
        .loc[lambda s: ~s.str.contains(r"\?")]             # exclude names with ?
        .drop_duplicates()
        .sort_values()
    )
    return cleaned.tolist()

# Load data function
def load_med_names(path):
    """
    Loads the Excel input and applies preprocessing to the first column of Sheet1.
    """
    df = pd.read_excel(path, sheet_name=SHEET_NAME, engine="openpyxl")
    return preprocess_names(df.iloc[:, 0])

# Main disambiguation algorithm
def keystroke_disambiguation(names):
    """
    MNOA core algorithm:
    - Each round (k) examines prefixes of length k.
    - Builds a map of names sharing same prefix.
    - If a prefix maps to one name, it's disambiguated.
    - Tracks possible misses and keystroke power (KP).
    - Additionally records per-prefix disambiguation results to a separate CSV.
    """
    total_names = len(names)
    max_len = max(len(n) for n in names)
    resolved_set = set()
    search_space = names.copy()
    results = []
    prefix_details = []  # store rows for prefix_resolution_rounds.csv
    previous_misses = None

    for k in range(1, max_len + 1):
        prefix_map = defaultdict(list)
        names_by_length = [n for n in search_space if len(n) == k]
        remaining_names = [n for n in search_space if len(n) > k]

        for name in remaining_names:
            prefix = name[:k]
            prefix_map[prefix].append(name)

        disambiguated = []
        unresolved = []

        for prefix, group in prefix_map.items():
            if len(group) == 1:
                disambiguated.append(group[0])
                prefix_details.append({
                    "round": k,
                    "prefix": prefix,
                    "disambiguated": group[0],
                    "unresolved": ""
                })
            else:
                unresolved.extend(group)
                prefix_details.append({
                    "round": k,
                    "prefix": prefix,
                    "disambiguated": "",
                    "unresolved": ", ".join(group)
                })

        possible_misses = sum(len(group) - 1 for group in prefix_map.values() if len(group) > 1)
        if k == 1:
            KPraw = 0
            percent_KP = 0.0
        else:
            KPraw = previous_misses - possible_misses
            percent_KP = round(KPraw / total_names, 4)
        previous_misses = possible_misses

        resolved_set.update(disambiguated)
        search_space = list(set(remaining_names) - set(disambiguated))

        print(f"\n--- Round {k} ---")
        print(f"Prefixes: {len(prefix_map)}")
        print(f"Search space size: {len(remaining_names)}")
        print(f"Disambiguated ({len(disambiguated)}): {disambiguated}")
        print(f"Unresolved ({len(unresolved)}): {unresolved}")
        print(f"Possible misses: {possible_misses}")

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

    pd.DataFrame(prefix_details).to_csv(PREFIX_DETAIL_CSV, index=False)
    return pd.DataFrame(results)

# Run if script is executed directly
if __name__ == "__main__":
    print("🔄 Loading medication names...")
    names = load_med_names(INPUT_FILE)

    print(f"📋 Preview of first 20 preprocessed names:\n{names[:20]}")
    print(f"💾 Saving full preprocessed list to {PREPROCESSED_NAMES_CSV}")
    pd.Series(names).to_csv(PREPROCESSED_NAMES_CSV, index=False, header=["name"])

    print("⚙️  Running keystroke disambiguation analysis...")
    df = keystroke_disambiguation(names)

    print(f"💾 Saving output to {OUTPUT_CSV}...")
    df.to_csv(OUTPUT_CSV, index=False)

    print("✅ Done. Preview of first few rows:")
    print(df.head())
