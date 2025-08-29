"""
Host Discovery options
Each option returns (flag_string, short_description, mode)
Mode: Active/Passive/Both
"""

def choose_options():
    options = {
        "1": ("-sn", "Ping scan - discover hosts without port scanning.", "Passive"),
        "2": ("-sL", "List scan - list targets without sending probes (DNS based).", "Passive"),
        "3": ("-PR", "ARP scan - local network ARP discovery (fast, local-only).", "Active"),
        "4": ("-PS", "TCP SYN discovery probes to specified ports (useful behind filters).", "Active"),
        "5": ("-PA", "TCP ACK discovery probes to specified ports.", "Active"),
        "6": ("-PU", "UDP discovery probes to specified ports.", "Active"),
        "7": ("-PE", "ICMP echo request discovery (classic ping).", "Active"),
        "8": ("-PP", "ICMP timestamp request.", "Active"),
        "9": ("-PM", "ICMP netmask request.", "Active"),
        "10": ("--send-ip", "Send raw IP packets rather than using ARP (advanced).", "Active"),
    }
    print("\n--- Host Discovery ---")
    for k, v in options.items():
        print(f" {k}. {v[0]} [{v[2]}] - {v[1]}")
    print(" B. Back")
    choice = input("\nChoose options (comma separated), or B to go back: ").strip()
    if choice.lower() == 'b' or not choice:
        return []
    picks = []
    for token in [t.strip() for t in choice.split(",") if t.strip()]:
        if token not in options:
            print(f"[!] Invalid: {token} - skipping")
            continue
        picks.append(options[token])
    return picks
