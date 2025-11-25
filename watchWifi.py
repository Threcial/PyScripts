import os
from scapy.all import ARP, DHCP,sniff
import json
from datetime import datetime
from win11toast import toast


KNOWN_FILE = os.path.abspath(__file__).replace("watchWifi.py", "known_mac.json")

def load_known_macs():
    if not os.path.exists(KNOWN_FILE):
        return set()
    try:
        with open(KNOWN_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(m.lower() for m in data)
    except Exception:
        return set()
    
known_macs = load_known_macs()

def save_known_mac(mac_set):
    with open(KNOWN_FILE, "w", encoding="utf-8") as f:
        json.dump(list(mac_set), f, ensure_ascii=False, indent=2)

def show_toast(title, msg):
    toast(
        title = title,
        body = msg,
        duration = "long"
    )

def new_device_notify(mac, ip=None, info=""):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text = (
        f"时间:{now}\n"
        f"MAC:{mac}\n"
        f"IP:{ip or 'unknown'}\n"
        f"info:{info}\n"
    )
    print(text)
    show_toast("新设备接入网络", text)

def handle_packet(pkt):
    global known_macs

    mac = None
    ip = None
    info = ""

    if pkt.haslayer(ARP):
        mac = pkt[ARP].hwsrc
        ip = pkt[ARP].psrc
        info = "ARP"
    elif pkt.haslayer(DHCP):
        mac = pkt.src
        info = "DHCP"
    if mac:
        mac = mac.lower()
        if mac not in known_macs:
            known_macs.add(mac)
            save_known_mac(known_macs)
            new_device_notify(mac, ip, info)

if __name__ == "__main__":
    print("start")
    sniff(
        filter="arp or (udp and (port 67 or 68))",
        prn=handle_packet,
        store=0
    )