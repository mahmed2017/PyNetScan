# PyNetScan 🧠🔍
**AI-Assisted Network Reconnaissance & Risk Assessment Tool**

PyNetScan is an advanced Python-based network scanning tool designed for **defensive security analysis**.  
It goes beyond traditional port scanning by including **intelligent service fingerprinting, system inference, and AI-inspired risk scoring**.

This project is built for **learning, research, and security posture assessment**, not exploitation.

---

## 🚀 Key Features

- **TCP Connect Scan**: Scans target host ports efficiently
- **Smart Service Detection**: Identifies services via port mapping and banner grabbing
- **AI-Inspired Risk Analysis**: Assigns risk levels (LOW / MEDIUM / HIGH) based on exposed services
- **System Profiling**: Infers likely system type (e.g., Windows, Linux) from open ports
- **Structured JSON Output**: Easy to use for reports or integration with other tools

---

## 🔍 How It Works

1. Performs a TCP connect scan on the target host.
2. Identifies services using port mapping and banner grabbing.
3. Applies AI-inspired risk scoring based on exposed services.
4. Infers the likely system type using observed behavior.
5. Outputs structured results in JSON format.

---

## ⚠️ Ethical Disclaimer

This tool is **only** intended for:
- Systems you own
- Lab environments
- Networks where you have **explicit authorization**

Unauthorized scanning of systems you do not own may be illegal.

---

## 🛠️ Installation & Usage

### Clone the repository
```bash
git clone https://github.com/mahmed2017/PyNetScan.git
cd PyNetScan


Run a basic scan
python scanner.py 127.0.0.1

Scan a custom port range
python scanner.py 192.168.1.10 -p 1-1024

Save scan results to a file
python scanner.py 192.168.1.10 -o output/scan.json

📄 Sample Output
{
  "target": "192.168.100.28",
  "scan_time": "2026-02-01 23:39:03",
  "open_ports": [
    {
      "port": 445,
      "service": "SMB",
      "status": "open",
      "banner": "Microsoft Windows SMB"
    }
  ],
  "risk_score": 70,
  "risk_level": "HIGH",
  "system_profile": "Likely Windows System"
}

