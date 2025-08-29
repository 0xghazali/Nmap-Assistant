"""
Firewall/IDS evasion & spoofing options
"""
def choose_options():
    options = {
        "1": ("-f", "Fragment packets to possibly bypass simple filters.", "Active"),
        "2": ("-D RND:10", "Decoy scan - mix decoy addresses with your scan.", "Active"),
        "3": ("-S <ip>", "Spoof source IP (requires proper routing/privileges).", "Active"),
        "4": ("-e <iface>", "Use specified interface for scanning.", "Both"),
        "5": ("--source-port <port>", "Set source port for probes.", "Active"),
        "6": ("--data-length <num>", "Append random data to alter packet sizes.", "Active"),
        "7": ("--badsum", "Send packets with bad checksums (may confuse stacks).", "Active"),
    }
    print("\n--- Evasion & Spoofing ---")
    for k,v in options.items():
        print(f" {k}. {v[0]} [{v[2]}] - {v[1]}")
    print(" Caution: spoofing and decoys require network capability and authorization.")
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
