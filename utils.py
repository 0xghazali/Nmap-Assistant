#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility helpers for nmap_0x project.
"""

from __future__ import annotations
import shutil
import sys
import os
import datetime
import subprocess
from typing import List, Tuple, Dict

def check_nmap():
    if shutil.which("nmap") is None:
        print("[!] nmap not found in PATH. Please install nmap first.")
        sys.exit(1)

def ts() -> str:
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

def mkdirp(d: str):
    os.makedirs(d, exist_ok=True)

def safe_filename(s: str) -> str:
    return "".join(c if c.isalnum() or c in '-_.@' else '_' for c in s)

def build_command(target: str,
                  selected_flags: List[Tuple[str,str,str]],
                  extra_outfiles: Dict[str,str]) -> Tuple[List[str], List[Tuple[str,str]]]:
    """
    Build nmap command list and return (cmdlist, used_flags_desc)
    selected_flags: list of (flag, description, mode)
    """
    cmd = ["nmap"]
    used = []
    for flag, desc, mode in selected_flags:
        # Detect placeholders and prompt the user as needed
        if "<ports>" in flag:
            val = input(f"Provide ports for '{flag}' (e.g. 22,80,1-1024): ").strip()
            flag_filled = flag.replace("<ports>", val)
            cmd.extend(flag_filled.split())
            used.append((flag_filled, desc))
        elif "<file>" in flag:
            val = input(f"Provide filename for '{flag}': ").strip()
            flag_filled = flag.replace("<file>", val)
            cmd.extend(flag_filled.split())
            used.append((flag_filled, desc))
        elif "<basename>" in flag:
            val = input(f"Provide basename for outputs (no ext) for '{flag}': ").strip()
            flag_filled = flag.replace("<basename>", val)
            cmd.extend(flag_filled.split())
            used.append((flag_filled, desc))
        elif "<scriptname>" in flag:
            val = input(f"Provide NSE script name for '{flag}' (e.g. http-enum): ").strip()
            flag_filled = flag.replace("<scriptname>", val)
            cmd.extend(flag_filled.split())
            used.append((flag_filled, desc))
        elif "<ip>" in flag:
            val = input(f"Provide IP for '{flag}' (e.g. spoof source IP): ").strip()
            flag_filled = flag.replace("<ip>", val)
            cmd.extend(flag_filled.split())
            used.append((flag_filled, desc))
        elif "<k=v,...>" in flag:
            val = input(f"Provide script-args for '{flag}' (k=v,k2=v2): ").strip()
            flag_filled = flag.replace("<k=v,...>", val)
            cmd.extend(flag_filled.split())
            used.append((flag_filled, desc))
        else:
            cmd.extend(flag.split())
            used.append((flag, desc))
    # Append target at the end
    cmd.append(target)
    return cmd, used

def run_nmap_and_save(cmdlist: List[str],
                      used_flags: List[Tuple[str,str]],
                      target: str,
                      mode_notes: List[str],
                      outdir: str):
    """
    Runs nmap command and save report + preserve nmap outputs if they exist.
    """
    mkdirp(outdir)
    timestamp = ts()
    base = f"{safe_filename(target)}_{timestamp}"
    # default filenames (if nmap writes them)
    default_oN = os.path.join(outdir, base + ".nmap")
    default_oX = os.path.join(outdir, base + ".xml")
    default_oG = os.path.join(outdir, base + ".gnmap")

    joined = " ".join(cmdlist)
    # If user didn't include -o options in cmd, add -oN and -oX and -oG for consistent storage
    if not any(x in joined for x in ["-oN", "-oX", "-oG", "-oA"]):
        cmdlist = cmdlist + ["-oN", default_oN, "-oX", default_oX, "-oG", default_oG]

    print("\n[0x] Running the following nmap command:\n")
    print(" " + " ".join(cmdlist) + "\n")
    print("[0x] This may take time depending on choices and timing options.\n")

    try:
        proc = subprocess.run(cmdlist, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    except Exception as e:
        print(f"[!] Failed to run nmap: {e}")
        return

    stdout = proc.stdout
    stderr = proc.stderr
    rc = proc.returncode

    report_file = os.path.join(outdir, base + "_report.txt")
    with open(report_file, "w") as rf:
        rf.write("="*70 + "\n")
        rf.write("Nmap Automation Framework - Report by 0x\n")
        rf.write("="*70 + "\n\n")
        rf.write(f"Target: {target}\n")
        rf.write(f"Timestamp: {timestamp}\n")
        rf.write("Command: " + " ".join(cmdlist) + "\n\n")
        rf.write("Used Flags and Descriptions:\n")
        for flag, desc in used_flags:
            rf.write(f" - {flag} : {desc}\n")
        rf.write("\nMode Notes:\n")
        for m in mode_notes:
            rf.write(f" - {m}\n")
        rf.write("\nReturn code: " + str(rc) + "\n\n")
        rf.write("="*70 + "\n\n")
        rf.write("STDOUT (nmap console output):\n")
        rf.write(stdout + "\n")
        rf.write("\nSTDERR (nmap errors/warnings):\n")
        rf.write(stderr + "\n")

    print(f"[0x] Report saved to: {report_file}")
    # Show any nmap output files created
    print("\n[0x] Nmap-created output files (if present):")
    for path in (default_oN, default_oX, default_oG):
        if os.path.exists(path):
            print(" - " + path)
    print("\n[0x] Done.")
