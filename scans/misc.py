"""
Misc and advanced flags
"""
def choose_options():
    options = {
        "1": ("--reason", "Show reason for port state (why nmap thinks a port is open/closed).", "Both"),
        "2": ("--open", "Show only open (or possibly open) ports in output.", "Both"),
        "3": ("--append-output", "Append to files instead of overwriting.", "Both"),
        "4": ("--exclude <hosts>", "Exclude hosts from scan (prompt).", "Both"),
        "5": ("--exclude-file <file>", "Exclude hosts listed in file (prompt filename).", "Both"),
        "6": ("--defeat-rst-ratelimit", "Try to defeat RST Ratelimit mitigation.", "Active"),
        "7": ("-6", "Enable IPv6 scanning.", "Both"),
        "8": ("--script-updatedb", "Update NSE script database index.", "Both"),
        "9": ("--min-hostgroup <n>", "Minimum hosts to scan in parallel (advanced).", "Active"),
    }
    print("\n--- Misc & Advanced ---")
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
