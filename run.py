#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nmap Automation Framework by 0x
Main runner script.
Single-target, menu-driven, modular.
"""

from __future__ import annotations
import shutil
import sys
import os
from typing import List, Tuple
from utils import check_nmap, ts, mkdirp, safe_filename, run_nmap_and_save

# Import category modules
from scans import (
    host_discovery,
    port_scanning,
    service_detection,
    os_detection,
    nse_scripts,
    evasion,
    timing,
    output_options,
    misc,
)

BANNER = r"""
============================================================ 
                 Nmap Automation Framework
                       by 0x
============================================================
"""

CATEGORIES = [
    ("1", "Host Discovery", host_discovery),
    ("2", "Port Scanning", port_scanning),
    ("3", "Service & Version Detection", service_detection),
    ("4", "OS Detection", os_detection),
    ("5", "NSE Scripts", nse_scripts),
    ("6", "Evasion & Spoofing", evasion),
    ("7", "Timing & Performance", timing),
    ("8", "Output & Logging", output_options),
    ("9", "Misc & Advanced", misc),
]

def print_banner():
    print(BANNER)
    print("Legal: Only scan systems you have explicit authorization to test.")
    print("This tool is for authorized/ethical testing only.\n")

def select_category() -> Tuple[str, object]:
    print("\nSelect a category:")
    for key, name, _mod in CATEGORIES:
        print(f" {key}. {name}")
    print(" 0. Finish selection & Run scan")
    choice = input("\nEnter category number (or 0 to run): ").strip()
    for key, name, mod in CATEGORIES:
        if choice == key:
            return name, mod
    if choice == "0":
        return "RUN", None
    return "", None

def main():
    check_nmap()
    print_banner()
    target = input("Enter single target (IP or hostname): ").strip()
    if not target:
        print("[!] No target provided. Exiting.")
        sys.exit(1)

    mkdirp("scan_results")

    selected_flags: List[Tuple[str,str,str]] = []  # list of (flag,desc,mode)
    mode_notes: List[str] = []

    while True:
        cat_name, module = select_category()
        if cat_name == "RUN":
            break
        if not module:
            print("[!] Invalid selection.")
            continue

        picks = module.choose_options()
        if not picks:
            # user returned/back
            continue
        # Extend selections
        for flag, desc, mode in picks:
            selected_flags.append((flag, desc, mode))
            mode_notes.append(f"{flag} -> {mode} -- {desc}")

        cont = input("\nAdd more categories? (y)es to continue selecting, (r)un now, (c)lear selections, (q)uit: ").strip().lower()
        if cont == "y" or cont == "":
            continue
        if cont == "c":
            selected_flags.clear()
            mode_notes.clear()
            print("[0x] selections cleared.")
            continue
        if cont == "q":
            print("[0x] exiting without running.")
            sys.exit(0)
        if cont == "r":
            break

    if not selected_flags:
        print("[!] No options selected. Exiting.")
        sys.exit(1)

    # Build command by asking modules if any special placeholders required
    # For this main design, each module returns full strings (flags possibly containing placeholders),
    # and utils.build_command will prompt for values if needed.
    from utils import build_command
    extra_outfiles = {}
    cmdlist, used_flags = build_command(target, selected_flags, extra_outfiles)

    # Run and save
    outdir = "scan_results"
    run_nmap_and_save(cmdlist, used_flags, target, mode_notes, outdir)
    print("\n[0x] All done. Check scan_results/ for outputs and the generated report.")

if __name__ == "__main__":
    main()
