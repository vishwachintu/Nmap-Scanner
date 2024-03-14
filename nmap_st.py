import streamlit as st
import nmap

def run_scan(ip_addr, scan_type):
    scanner = nmap.PortScanner()
    scan_types = {
        '1': ['-v -sS', 'tcp'],
        '2': ['-v -sU', 'udp'],
        '3': ['-v -sS -sV -sC -A -O', 'tcp']
    }
    if scan_type not in scan_types:
        return "Invalid scan type"
    
    st.write("Running Nmap scan...")
    scanner.scan(ip_addr, "1-1024", scan_types[scan_type][0])
    if scanner[ip_addr].state() == 'up':
        protocols = scanner[ip_addr].all_protocols()
        open_ports = scanner[ip_addr][scan_types[scan_type][1]].keys()
        st.write("Scanner Status:", scanner[ip_addr].state())
        st.write("All Protocols:", protocols)
        st.write("Open Ports:", open_ports)
    else:
        st.write("Host is not up or reachable")

def main():
    st.title("DrPinnacle Scanner")
    st.write("Welcome, this is a simple nmap automation tool")
    st.write("<----------------------------------------------------->")

    ip_addr = st.text_input("Please enter the IP address you want to scan:")
    st.write("The IP you entered is:", ip_addr)

    scan_type = st.selectbox("Please select the type of scan you want to run:",
                             ["SYN ACK Scan", "UDP Scan", "Comprehensive Scan"])
    if st.button("Run Scan"):
        if ip_addr:
            if scan_type == "SYN ACK Scan":
                run_scan(ip_addr, '1')
            elif scan_type == "UDP Scan":
                run_scan(ip_addr, '2')
            elif scan_type == "Comprehensive Scan":
                run_scan(ip_addr, '3')
        else:
            st.write("Please enter an IP address")

if __name__ == "__main__":
    main()
