from scapy.all import *
import base64
from tqdm import tqdm

def extract_ssids(pcap_file):
    packets = rdpcap(pcap_file)
    ssids = []

    for packet in tqdm(packets, desc="Processing packets", unit="pkt"):
        if packet.haslayer(Dot11Elt):
            if packet[Dot11Elt].ID == 0:  # SSID Parameter Set
                ssid = packet[Dot11Elt].info
                try:
                    # Try to decode base64
                    decoded_ssid = base64.b64decode(ssid).decode('utf-8')
                    ssids.append(decoded_ssid)
                except:
                    pass

    return ssids

def check_ssid(ssids):
    for ssid in tqdm(ssids, desc="Checking SSIDs", unit="SSID"):
        if 'bctf{' in ssid:
            print(ssid)

if __name__ == "__main__":
    pcap_file = 'frames.pcap'
    ssids = extract_ssids(pcap_file)
    check_ssid(ssids)
