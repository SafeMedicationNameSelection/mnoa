import pandas as pd
from collections import defaultdict

# File setup
INPUT_FILE = "Test1.xlsx"
SHEET_NAME = "Sheet1"
OUTPUT_CSV = "mnoa_output.csv"
PREPROCESSED_CSV = "preprocessed_names.csv"

def preprocess_names(name_series):
    cleaned = (
        name_series.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", " ", regex=True)  
        .dropna()
        .loc[lambda s: ~s.str.contains(r"\?")]
        .drop_duplicates()
        .sort_values()
    )
    return cleaned.tolist()

def load_med_names(path):
    df = pd.read_excel(path, sheet_name=SHEET_NAME, engine="openpyxl")
    return preprocess_names(df.iloc[:, 0])

def keystroke_disambiguation(names):
    total_names = len(names)
    max_len = max(len(n) for n in names)
    resolved_set = set()
    search_space = names.copy()
    results = []
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

        for group in prefix_map.values():
            if len(group) == 1:
                disambiguated.append(group[0])
            else:
                unresolved.extend(group)

        possible_misses = sum(len(group) - 1 for group in prefix_map.values() if len(group) > 1)
        KPraw = None if previous_misses is None else previous_misses - possible_misses
        percent_KP = None if KPraw is None else round(KPraw / total_names, 4)
        previous_misses = possible_misses

        resolved_set.update(disambiguated)
        search_space = list(set(remaining_names) - set(disambiguated))

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

    return pd.DataFrame(results)

if __name__ == "__main__":
    print("🔄 Loading medication names...")
    names = load_med_names(INPUT_FILE)

    print("🧪 Preview of first 20 preprocessed names:")
    print(names[:20])

    print(f"💾 Saving full preprocessed list to {PREPROCESSED_CSV}")
    pd.Series(names).to_csv(PREPROCESSED_CSV, index=False)

    print("⚙️  Running keystroke disambiguation analysis...")
    df = keystroke_disambiguation(names)

    print(f"💾 Saving output to {OUTPUT_CSV}...")
    df.to_csv(OUTPUT_CSV, index=False)

    print("✅ Done. Preview of first few rows:")
    print(df.head())
