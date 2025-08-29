
## 🚀 Overview
The **Nmap Automation Framework by 0x** is a modular and interactive Python toolkit that organizes and automates **every Nmap command** into categories.  
It is designed for **ethical hackers, penetration testers, and red teamers** who perform authorized security assessments.  

Instead of remembering complex flags, simply run the script, select a category, and choose the desired scan. The tool handles everything and generates clean reports.  

---

✨ Features
- 🔹 Beautiful **0x ASCII signature** in console and reports  
- 🔹 Full coverage of **all Nmap features**:
  - Host Discovery  
  - Port Scanning  
  - Service & Version Detection  
  - OS Fingerprinting  
  - NSE Scripts (safe, vuln, intrusive, etc.)  
  - Firewall Evasion & Spoofing  
  - Timing & Performance tuning  
  - Output options & reporting  
- 🔹 **Active vs Passive** classification for each scan  
- 🔹 Reports saved in `scan_results/` with timestamps  
- 🔹 Modular codebase for clean GitHub structure  

---

📂 Project Structure

nmap_zerox/
│
├── nmap_zerox.py # Main entry 
├── scans/
│ ├── host_discovery.py # All host discovery methods
│ ├── port_scanning.py # All TCP/UDP/Stealth scans
│ ├── service_detection.py
│ ├── os_detection.py
│ ├── nse_scripts.py
│ ├── firewall_evasion.py
│ ├── timing_perf.py
│ ├── output_options.py
│
├── utils.py # Common functions (runner, report generator)
└── scan_results/ # All saved reports


⚙️ Installation

git clone https://github.com/yourusername/nmap-0x.git
cd nmap-0x
pip install python-nmap

▶️ Usage
python3 nmap_zerox.py

Example Flow:
=== Nmap Automation Framework by 0x ===
Enter target: scanme.nmap.org

Select Category:
1. Host Discovery
2. Port Scanning
3. Service & Version Detection
4. OS Detection
5. NSE Scripts
6. Firewall/Evasion
7. Timing/Performance
0. Exit

Pick a category → choose a scan type → results saved automatically in scan_results/.

📑 Reports

Reports are stored in scan_results/target_timestamp.txt

Each report includes:

  Target

  Command executed

  Mode (Active/Passive)

  Explanation of scan

  Results

⚠️ Disclaimer

This tool is created by 0x strictly for authorized penetration testing and educational purposes only.
The author is not responsible for any misuse.
Always ensure you have explicit permission before scanning any target.


🏆 Credits

Developed with ⚡ by 0x

