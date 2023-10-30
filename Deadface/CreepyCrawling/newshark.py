import pyshark

def search_ssh_protocol(file_path):
    # Read packets from the pcap file
    packets = pyshark.FileCapture(file_path)

    # Iterate over each packet
    for packet in packets:
        try:
            # Check if the packet is SSH
            if 'SSH' in packet:
                # Extract protocol version
                if hasattr(packet.ssh, 'protocol'):
                    protocol_version = packet.ssh.protocol
                    print(f"SSH protocol version: {protocol_version}")
                    break
        except Exception as e:
            print(f"Error processing packet: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the pcap file: ")
    search_ssh_protocol(file_path)
