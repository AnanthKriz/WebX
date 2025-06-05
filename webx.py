#!/usr/bin/env python3
# webX - Vulnerability Testing Tool
# Developed by AnanthKriz

import requests
import sys

def banner():
    print(r"""
 __        __   _     __  __
 \ \      / /| |__ |  \/  | ___  _ __
  \ \ /\ / / _ \ '_ \| |\/| |/ _ \| '_ \
   \ V  V /  _/ |) | |  | | (_) | | | |
    \/\/ \|./||  ||\/|| |_| v1.0
          Developed by AnanthKriz
    """)

def check_url_vuln(url):
    payloads = ["' OR '1'='1", "<script>alert(1)</script>", "../../../../etc/passwd"]
    headers = {"User-Agent": "webX Scanner - AnanthKriz"}

    print(f"\n[+] Scanning URL: {url}\n")

    for payload in payloads:
        try:
            r = requests.get(url + payload, headers=headers, timeout=5)
            if "alert(1)" in r.text or "root:x" in r.text:
                print(f"[!] Potential vulnerability detected with payload: {payload}")
            else:
                print(f"[-] No vuln with payload: {payload}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Request failed: {e}")

# Corrected the spelling of the special variable __name__
if __name__ == "__main__":
    banner()
    if len(sys.argv) != 2:
        print("Usage: python webx.py <URL>")
    else:
        check_url_vuln(sys.argv[1])
