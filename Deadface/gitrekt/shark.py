import pyshark

def search_pcap(file_path, search_text):
    # Read packets from the pcap file
    packets = pyshark.FileCapture(file_path)

    # Iterate over each packet
    for packet_number, packet in enumerate(packets, start=1):
        try:
            # Convert packet to string
            packet_str = str(packet)

            # Search for the text in the packet
            if search_text.lower() in packet_str.lower():
                print(f"Text found in packet {packet_number}: {packet}")
        except Exception as e:
            print(f"Error processing packet {packet_number}: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the pcap file: ")
    search_text = "pass"
    search_pcap(file_path, search_text)
