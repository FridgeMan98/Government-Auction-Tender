import socket
import sys

hostname = "ep-plain-smoke-a1ayd0lz-pooler.ap-southeast-1.aws.neon.tech"

print(f"Attempting to resolve {hostname}...")

try:
    ip = socket.gethostbyname(hostname)
    print(f"SUCCESS: Resolved {hostname} to {ip}")
except socket.gaierror as e:
    print(f"FAILURE: Could not resolve hostname: {e}")
    print("\nPossible causes:")
    print("1. typo in the hostname")
    print("2. DNS server issues (try 'nslookup' in terminal)")
    print("3. Network firewall blocking DNS queries")
    print("4. The NeonDB project might be paused/deleted")

print("\nAttempting to resolve common domains to check internet...")
try:
    socket.gethostbyname("google.com")
    print("SUCCESS: Internet connectivity seems OK (resolved google.com)")
except:
    print("FAILURE: Could not resolve google.com - Check your internet connection")
