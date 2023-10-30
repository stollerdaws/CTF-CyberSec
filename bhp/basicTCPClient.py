import socket

target_host = "127.0.0.1"
target_port = 27017

# Create and connect socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

# Send a request for the google.com page
client.send(b"BWAHAHAHAHAHAAHAHA\r\n\r\n")

# Recieve response
response = client.recv(4096)

print(response.decode())

client.close
