from risk_engine import calculate_risk
import socket
import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from services import COMMON_SERVICES
from utils import current_time

open_ports = []

def scan_port(target, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown")
            open_ports.append({
                "port": port,
                "service": service,
                "status": "open"
            })
        sock.close()
    except Exception:
        pass

def main():
    parser = argparse.ArgumentParser(description="PyNetScan - Simple Python Network Scanner")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("-p", "--ports", help="Port range (e.g. 1-1024)", default="1-1024")
    parser.add_argument("-o", "--output", help="Output file (JSON)", default="output/result.json")

    args = parser.parse_args()
    start_port, end_port = map(int, args.ports.split("-"))

    print(f"[+] Scan started at {current_time()}")
    print(f"[+] Target: {args.target}")
    print(f"[+] Ports: {start_port}-{end_port}")

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, args.target, port)

    result = {
        "target": args.target,
        "scan_time": current_time(),
        "open_ports": open_ports
    }

    with open(args.output, "w") as f:
        json.dump(result, f, indent=4)

    print(f"[+] Scan completed. Results saved to {args.output}")

if __name__ == "__main__":
    main()

