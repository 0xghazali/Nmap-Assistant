"""
Output & logging options
"""
def choose_options():
    options = {
        "1": ("-oN <file>", "Normal human-readable output to file (prompt file name).", "Both"),
        "2": ("-oX <file>", "XML output to file (prompt file name).", "Both"),
        "3": ("-oG <file>", "Grepable output to file (prompt file name).", "Both"),
        "4": ("-oA <basename>", "Save -oN,-oX,-oG files with given basename (prompt).", "Both"),
        "5": ("-v", "Verbose output", "Both"),
        "6": ("-d", "Debug output", "Both"),
        "7": ("--packet-trace", "Show packet trace (very verbose).", "Both"),
    }
    print("\n--- Output & Logging ---")
    for k,v in options.items():
        print(f" {k}. {v[0]} [{v[2]}] - {v[1]}")
    print(" B. Back")
    choice = input("\nChoose options (comma separated), or B to go back: ").strip()
    if choice.lower() == 'b' or not choice:
        return []
    picks=[]
    for token in [t.strip() for t in choice.split(",") if t.strip()]:
        if token not in options:
            print(f"[!] Invalid: {token} - skipping")
            continue
        picks.append(options[token])
    return picks
