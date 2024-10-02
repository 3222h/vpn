# -*- coding: utf-8 -*-
import time
import os
import subprocess

try:
    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed')

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] Tor is not installed!')
    subprocess.check_output('sudo apt update', shell=True)
    subprocess.check_output('sudo apt install tor -y', shell=True)
    print('[!] Tor is installed successfully')

# Start the Tor service (only once)
os.system("service tor start")
time.sleep(3)

# Notify the user to change their SOCKS proxy settings
print("\033[1;32;40m Change your SOCKS to 127.0.0.1:9050 \n")

# Retrieve and display the current IP assigned by Tor (no changes after this)
def ma_ip():
    url = 'http://checkip.amazonaws.com'
    get_ip = requests.get(url, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
    return get_ip.text

current_ip = ma_ip()
print(f'[+] Your IP is: {current_ip.strip()}')

# No repeated IP changes; the Tor IP will remain active as long as the service runs.
