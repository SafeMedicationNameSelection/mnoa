"""
MNOA - Medication Name Overlap Analyzer (Backend Module)
This module exposes a single entrypoint: run_mnoa(med_name_list).
"""

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
            continue                            # Exclude entries with question marks
        cleaned.append(name)
    return sorted(set(cleaned))                 # Deduplicate with set and sort alphabetically


def disambiguate(names):
    """
    Runs the MNOA prefix disambiguation algorithm.
    Args:
        names (List[str]): cleaned and sorted medication names
    Returns:
        Tuple: (round_stats, prefix_logs)
          - round_stats: List[Dict], 1 per round, overall summary
          - prefix_logs: List[Dict], 1 per prefix per round, detailed prefix log
    """
    round_stats = []
    prefix_logs = []
    if not names:
        return round_stats, prefix_logs
    
    total_names = len(names)
    max_len = max(len(n) for n in names)
    resolved = set()
    search_space = names.copy()
    previous_misses = total_names - 1  # So KPraw is 0 in round 1

    for k in range(1, max_len + 1):
        prefix_map = {}
        remaining_names = [n for n in search_space if len(n) >= k]

        # Map prefixes to their candidate names
        for name in remaining_names:
            prefix = name[:k]
            prefix_map.setdefault(prefix, []).append(name)
        
        disambiguated = []
        unresolved = []
        
        for prefix, group in prefix_map.items():
            if len(group) == 1:
                disambiguated.append(group[0])
                prefix_logs.append({
                    "round": k,
                    "prefix": prefix,
                    "disambiguated": group[0],
                    "unresolved": ""
                })
            else:
                unresolved.extend(group)
                prefix_logs.append({
                    "round": k,
                    "prefix": prefix,
                    "disambiguated": "",
                    "unresolved": ", ".join(group)
                })

        # Metrics
        possible_misses = sum(len(g) - 1 for g in prefix_map.values() if len(g) > 1)
        KPraw = 0 if k == 1 else previous_misses - possible_misses
        percent_KP = 0.0 if k == 1 else round(KPraw / total_names, 4)
        previous_misses = possible_misses

        resolved.update(disambiguated)
        search_space = list(set(remaining_names) - set(disambiguated))

        round_stats.append({
            "characters": k,
            "search_terms": len(prefix_map),
            "search_space_size": len(remaining_names),
            "unresolved_items": len(unresolved),
            "disambiguated_names": len(resolved),
            "possible_misses": possible_misses,
            "KPraw": KPraw,
            "%KP": percent_KP
        })

        if not unresolved:
            break

    return round_stats, prefix_logs

def run_mnoa(med_name_list):
    """
    The single entry point for backend integration.
    Args:
        med_name_list (List[str]): Unprocessed, pasted list from user.
    Returns:
        Dict: {
            'cleaned_names': List[str],
            'round_stats': List[Dict],
            'prefix_logs': List[Dict]
        }
    """
    cleaned = clean_names(med_name_list)
    round_stats, prefix_logs = disambiguate(cleaned)
    return {
        "cleaned_names": cleaned,
        "round_stats": round_stats,
        "prefix_logs": prefix_logs,
    }
