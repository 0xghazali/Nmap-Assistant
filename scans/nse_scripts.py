"""
NSE script category options
"""
def choose_options():
    options = {
        "1": ("--script=default", "Run the default NSE scripts (safe common checks).", "Active"),
        "2": ("--script=safe", "Run NSE scripts labeled as 'safe' only.", "Active"),
        "3": ("--script=vuln", "Run vulnerability-detection NSE scripts.", "Active"),
        "4": ("--script=auth", "Run authentication-related NSE scripts.", "Active"),
        "5": ("--script=discovery", "Run discovery-category NSE scripts.", "Active"),
        "6": ("--script=intrusive", "Run intrusive scripts (may disrupt services).", "Active"),
        "7": ("--script=<scriptname>", "Run specific script (prompt for name).", "Active"),
        "8": ("--script-args='<k=v,...>'", "Pass arguments to NSE scripts (prompt).", "Active"),
        "9": ("--script-trace", "Show NSE script trace output (debugging).", "Active"),
    }
    print("\n--- NSE Scripts ---")
    for k,v in options.items():
        print(f" {k}. {v[0]} [{v[2]}] - {v[1]}")
    print(" Note: intrusive scripts may be disruptive; use with authorization.")
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
