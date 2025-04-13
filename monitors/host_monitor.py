import subprocess

def discover_hosts_with_arp_scan(subnet):
    print(f"\nDiscovering hosts on {subnet} using arp-scan...")
    result = subprocess.run(
        ['sudo', 'arp-scan', subnet],
        capture_output=True,
        text=True
    )
    print(result.stdout)

discover_hosts_with_arp_scan('192.168.1.0/24')
