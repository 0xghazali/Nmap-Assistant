"""
OS detection options
"""
def choose_options():
    options = {
        "1": ("-O", "Enable OS detection via TCP/IP fingerprinting.", "Active"),
        "2": ("--osscan-guess", "Guess OS when detection is not certain.", "Active"),
        "3": ("--osscan-limit", "Limit OS detection to promising targets.", "Active"),
        "4": ("-sV -O", "Combine service detection with OS detection.", "Active"),
    }
    print("\n--- OS Detection ---")
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
