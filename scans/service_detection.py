"""
Service & version detection options
"""
def choose_options():
    options = {
        "1": ("-sV", "Probe open ports to determine service and version.", "Active"),
        "2": ("--version-intensity <level>", "Set intensity (0-9) for version detection.", "Active"),
        "3": ("--version-all", "Try all version probes (more thorough).", "Active"),
        "4": ("--version-light", "Faster, less thorough version detection.", "Active"),
        "5": ("--version-trace", "Show version probe activity (debugging).", "Active"),
        "6": ("-sV --version-all", "Complete version fingerprinting.", "Active"),
    }
    print("\n--- Service & Version Detection ---")
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
