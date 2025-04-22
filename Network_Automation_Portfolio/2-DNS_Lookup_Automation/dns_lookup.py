import socket

# List of domain names to check
domains = [
    "google.com",
    "amazon.com",
    "openai.com",
    "invalid-domain.example"  # simulate a failure
]

def dns_lookup(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Domain: {domain} | IP: {ip_address}")
        return ip_address
    except socket.gaierror as e:
        print(f"Domain: {domain} | Lookup failed: {e}")
        return None

def main():
    print("Starting DNS Lookup Automation...\n")
    for domain in domains:
        dns_lookup(domain)

if __name__ == "__main__":
    main()