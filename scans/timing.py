"""
Timing & performance options
"""
def choose_options():
    options = {
        "1": ("-T0", "Paranoid - very slow; useful to evade IDS detection (if possible).", "Passive"),
        "2": ("-T1", "Sneaky - very slow.", "Passive"),
        "3": ("-T2", "Polite - slower, reduces load.", "Passive"),
        "4": ("-T3", "Normal timing.", "Active"),
        "5": ("-T4", "Aggressive - faster, noisier.", "Active"),
        "6": ("-T5", "Insane - fastest and loudest.", "Active"),
        "7": ("--min-rate <n>", "Set minimum packet rate (prompt value).", "Active"),
        "8": ("--max-retries <n>", "Set retry count for probes.", "Active"),
        "9": ("--host-timeout <ms>", "Stop scanning a host after timeout (ms).", "Active"),
    }
    print("\n--- Timing & Performance ---")
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
