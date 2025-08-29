"""
Port scanning techniques
"""
def choose_options():
    options = {
        "1": ("-sS", "TCP SYN (stealth) scan - most used.", "Active"),
        "2": ("-sT", "TCP connect scan - uses OS connect() if raw sockets unavailable.", "Active"),
        "3": ("-sU", "UDP scan - slower and more noisy, needed for UDP services.", "Active"),
        "4": ("-sA", "ACK scan - used to map firewall rules.", "Active"),
        "5": ("-sW", "Window scan - uses TCP window field to infer state.", "Active"),
        "6": ("-sM", "Maimon scan - variant for evasive scanning.", "Active"),
        "7": ("-sF", "FIN scan - stealthy FIN packets.", "Active"),
        "8": ("-sN", "NULL scan - no flags set.", "Active"),
        "9": ("-sX", "XMAS scan - FIN+PSH+URG flags set.", "Active"),
        "10": ("-sY", "SCTP INIT scan - for SCTP services.", "Active"),
        "11": ("-p-","Scan all TCP ports (1-65535).", "Active"),
        "12": ("-p <ports>", "Specify ports to scan (you will be prompted).", "Active"),
        "13": ("--top-ports <N>", "Scan top N most-common ports.", "Active"),
        "14": ("--port-ratio <FLOAT>", "Choose ports by probability (advanced).", "Active"),
    }
    print("\n--- Port Scanning ---")
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
