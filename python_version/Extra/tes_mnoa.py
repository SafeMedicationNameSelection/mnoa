from mnoa_backend_module import run_mnoa

# Sample raw input list
raw_med_names = [
    "Lipitor", "Lisinopril", "Lisinopril HCTZ", "lipi tor", "Li si nopril", "Li@sinopril", "Amoxil", "Amo@xil", "?", "Lipitor"
]

# Run the module
output = run_mnoa(raw_med_names)

# Print results
print("Cleaned Names:")
print(output["cleaned_names"])
print("\nRound Stats:")
for round_data in output["round_stats"]:
    print(round_data)
print("\nPrefix Logs (first 5):")
for log in output["prefix_logs"][:5]:
    print(log)
