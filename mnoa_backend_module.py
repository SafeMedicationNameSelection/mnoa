# MNOA - Medication Name Overlap Analyzer (Backend Version with Full Documentation)

def clean_names(raw_names):
    """
    Cleans and standardizes medication names:
    - Trims whitespace
    - Converts to lowercase
    - Removes names containing '?'
    - Deduplicates and sorts the final list
    """
    cleaned = []  # List to store valid cleaned names
    for name in raw_names:
        name = name.strip().lower()  # Removes leading/trailing spaces and convert to lowercase
        name = " ".join(name.split())  # Replaces multiple spaces into a single space
        if "?" not in name:  # Excludes names with question marks
            cleaned.append(name)  # Adds valid name to the cleaned list
    return sorted(set(cleaned))  # Deduplicate using set, sort alphabetically, and return


def disambiguate(names):
    """
    Disambiguates medication names using prefix-based matching.
    Each round increases prefix length by one character to reduce ambiguity.
    Returns:
    - round_stats: per-round summary metrics
    - prefix_logs: detailed resolution/unresolved logs per prefix per round
    """
    round_stats = []  # List to store summary stats for each round
    prefix_logs = []  # List to store prefix-level resolution logs

    if not names:
        return round_stats, prefix_logs  # Return empty output if no input names

    total = len(names)  # Total number of names to analyze 
    max_len = max(len(name) for name in names)  # Longest name in the input list
    resolved = set()  # Set to keep track of disambiguated names
    search_pool = names.copy()  # Names yet to be disambiguated, copied to avoid modifying original list
    prev_misses = total - 1  # Initial unresolved count, used to calculate raw KP, number of possible mis-picks

    # Iterate over prefix lengths from 1 to the maximum name length
    for k in range(1, max_len + 1):
        prefix_map = {}  # Dictionary to map prefixes to lists of names sharing them

        # Build prefix map for all names long enough for this round
        for name in search_pool:
            if len(name) >= k:  # Skip names shorter than current prefix length
                prefix = name[:k]  # Extract prefix of length k
                prefix_map.setdefault(prefix, []).append(name)  # Group by prefix

        disamb = []  # Names successfully disambiguated in this round
        unresolved = []  # Names that remain ambiguous after this round

        # Evaluate each prefix group
        for prefix, group in prefix_map.items():
            if len(group) == 1:
                # If prefix maps to one name → resolved
                resolved_name = group[0]
                disamb.append(resolved_name)
                prefix_logs.append({
                    "round": k,
                    "prefix": prefix,
                    "disambiguated": resolved_name,
                    "unresolved": ""
                })
            else:
                # Prefix maps to multiple names → unresolved
                unresolved += group
                prefix_logs.append({
                    "round": k,
                    "prefix": prefix,
                    "disambiguated": "",
                    "unresolved": ", ".join(group)
                })

        # Calculate metrics for this round
        misses = len(unresolved) - 1  # Total remaining possible mistakes
        kp_raw = prev_misses - misses  # Raw Keystroke Power gained this round
        kp_percent = round(kp_raw / total, 4)  # Normalized KP as a percent
        prev_misses = misses  # Update unresolved count for next round

        resolved.update(disamb)  # Add resolved names to the global set
        search_pool = list(set(search_pool) - set(disamb))  # Remove resolved names from next round's pool

        # Record summary statistics for this round
        round_stats.append({
            "characters": k,
            "search_terms": len(prefix_map),
            "search_space_size": len(search_pool) + len(disamb),
            "unresolved_items": len(unresolved),
            "disambiguated_names": len(resolved),
            "possible_misses": misses,
            "KPraw": kp_raw,
            "%KP": kp_percent
        })

        if not unresolved:
            break  # Stop if all names are resolved

    return round_stats, prefix_logs  # Return all round metrics and prefix logs


def run_mnoa(med_names):
    """
    Entrypoint for the MNOA backend.
    Input: unprocessed medication name list
    Output: dictionary with cleaned names, round stats, and resolution logs
    """
    cleaned = clean_names(med_names)  # Step 1: clean raw inputs
    stats, logs = disambiguate(cleaned)  # Step 2: run disambiguation rounds
    return {
        "cleaned_names": cleaned,  # Final cleaned and sorted name list
        "round_stats": stats,      # Per-round performance summary
        "prefix_logs": logs        # Per-prefix resolution/unresolved logs
    }

