import socket

# DNS database for hostname to IP address mapping and aliasing
DNS_DATABASE = {
    # Address record for facelook.com
    'facelook.com': {'type': 'A', 'value': '192.168.1.1'},
    # Canonical name record for developer.facelook.com
    'developer.facelook.com': {'type': 'CNAME', 'value': 'facelook.com'},

    # Address record for githut.com
    'githut.com': {'type': 'A', 'value': '123.16.51.1'},
    # Canonical name record for user.githut.com
    'user.githut.com': {'type': 'CNAME', 'value': 'githut.com'},

    # Address record for linkin.com
    'linkin.com': {'type': 'A', 'value': '145.65.72.86'},
    # Canonical name record for blog.linkin.com
    'blog.linkin.com': {'type': 'CNAME', 'value': 'linkin.com'},
}

# Function to handle DNS queries
def handle_dns_query(data, client_address):
    query = data.decode().strip()  # Decoding the query from bytes to string
    if query in DNS_DATABASE:
        record = DNS_DATABASE[query]
        # Constructing the DNS response
        response = f"{query} {record['type']} {record['value']}"
    else:
        response = f"Error: {query} not found in DNS database"

    # Sending the response back to the client
    server_socket.sendto(response.encode(), client_address)

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 53)  # DNS standard port
server_socket.bind(server_address)

print("Name: Diya Goyal; StudentID: 2210994878")
# Print server status
print("DNS server is running...")

# Listen for incoming DNS queries
while True:
    # Receive data and client address
    data, client_address = server_socket.recvfrom(1024)
    # Handle the DNS query and send response
    handle_dns_query(data, client_address)
