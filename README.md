# Packet Sniffer GUI

> Notes:
> - Don't scan on networks without explicit permission to do so
> - ```sniffer.py``` is old and doesn't run well, remaking it through ```sniffer-cli.py``` w/out scapy 

## Overview
This is a **Packet Sniffer GUI** built using **Python, PySide6, and Scapy**. It allows users to monitor network packets based on selected protocols (TCP, UDP, or ARP), set a specific packet count to capture, and optionally save the captured packets to a `.pcap` file.

## Usage
1. 🛑 Select a protocol (TCP, UDP, or ARP).
2. 🔄 Set the number of packets to capture.
3. 🎯 Click **Run Sniffer** to start capturing packets.
4. 💾 (Optional) Enable "Save to File" to store packets in a `.pcap` file.
5. 🔁 Click **Reset** to clear inputs and start over.
