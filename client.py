import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the address and port of the DNS server
server_address = ('localhost', 53)

# Loop to continuously prompt the user for DNS queries
while True:
    # Get user input for hostname / alias name
    hostname = input("Enter hostname / alias name: ")

    # Send DNS query to the server
    client_socket.sendto(hostname.encode(), server_address)

    # Receive and display the response from the server
    response, _ = client_socket.recvfrom(1024)
    print("Response:", response.decode())

    # Prompt user to continue with another DNS query or not
    choice = input("Continue with another DNS query? (yes/no): ")
    if choice.lower() != 'yes':
        break

# Close the client socket
client_socket.close()
