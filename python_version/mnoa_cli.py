import csv

# Step 1: Accept pasted input directly from terminal
import sys

def read_input_from_terminal():
    print("📥 Paste medication names (one per line). Then press Ctrl+D (on Mac) or Ctrl+Z (on Windows) to finish:")
    names = sys.stdin.read().splitlines()
    return [line.strip() for line in names if line.strip()]


# Step 2: Clean names
def clean_names(raw_names):
    cleaned = []
    for name in raw_names:
        name = name.strip().lower()
        name = " ".join(name.split())
        if "?" in name:
            continue
        cleaned.append(name)
    return sorted(set(cleaned))

# Step 3: Disambiguation logic
def disambiguate(names):
    results = []
    prefix_details = []

    if not names:
        print("❗Error: No names to disambiguate.")
        return results, prefix_details

    total_names = len(names)
    max_len = max(len(n) for n in names)
    resolved_set = set()
    search_space = names.copy()
    previous_misses = None

    for k in range(1, max_len + 1):
        prefix_map = {}
        names_by_length = [n for n in search_space if len(n) == k]
        remaining_names = [n for n in search_space if len(n) >= k]  # ✅ FIXED

        for name in remaining_names:
            prefix = name[:k]
            if prefix not in prefix_map:
                prefix_map[prefix] = []
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
        KPraw = 0 if k == 1 else previous_misses - possible_misses
        percent_KP = 0.0 if k == 1 else round(KPraw / total_names, 4)
        previous_misses = possible_misses

        resolved_set.update(disambiguated)
        search_space = list(set(remaining_names) - set(disambiguated))

        # Print round summary to terminal
        print(f"\n--- Round {k} ---")
        print(f"Prefixes tested: {len(prefix_map)}")
        print(f"Names with length = {k}: {len(names_by_length)}")
        print(f"Disambiguated this round: {len(disambiguated)}")
        print(f"Remaining unresolved: {len(unresolved)}")
        print(f"Possible misses: {possible_misses}")
        print(f"KPraw: {KPraw}, %KP: {percent_KP * 100:.2f}%")

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
            break

    return results, prefix_details

# Step 4: Save CSVs
def save_to_csv(results, prefix_data, cleaned_names, output_dir=".", prefix_file="prefix_resolution_rounds.csv", names_file="preprocessed_names.csv", result_file="mnoa_output.csv"):
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

# MAIN
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
