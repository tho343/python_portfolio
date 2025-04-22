import subprocess
import socket

# List of IP addresses or hostnames to check
targets = ["8.8.8.8", "google.com", "1.1.1.1"]

def ping_host(host):
    try:
        output = subprocess.check_output(["ping", "-c", "2", host], universal_newlines=True)
        print(f"Ping to {host} successful.")
        return True
    except subprocess.CalledProcessError:
        print(f"Ping to {host} failed.")
        return False

def tcp_check(host, port=80):
    try:
        with socket.create_connection((host, port), timeout=5):
            print(f"TCP connection to {host}:{port} successful.")
            return True
    except Exception as e:
        print(f"TCP connection to {host}:{port} failed: {e}")
        return False

def network_health_check():
    for target in targets:
        print(f"\nChecking {target}...")
        ping_result = ping_host(target)
        tcp_result = tcp_check(target)

        if ping_result and tcp_result:
            print(f"{target} is reachable and accepting TCP connections.")
        else:
            print(f"{target} has issues.")

if __name__ == "__main__":
    network_health_check()
