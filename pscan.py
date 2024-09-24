#!/usr/bin/python3
import os
import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
from optparse import OptionParser

def tcp_port(target,port):
    so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    try:
        result=so.connect_ex((target,port))
        if result==0:
            service=service_name(port)
            print(f"{Fore.BLUE}TCP Port {port}: OPEN (Service: {service}){Style.RESET_ALL}")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    finally:
        so.close()
def udp_port(target,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.setdefaulttimeout(1)
    try:
        s.sendto(b'', (target, port))
        data, _ = s.recvfrom(1024)
        print(f"{Fore.BLUE}UDP Port {port}: OPEN{Style.RESET_ALL}")
    except socket.timeout:
        pass
    except Exception as e:
        print(f"Error scanning UDP port {port}: {e}")
    finally:
        s.close()

def service_name(port):
    return ports.get(port, "Unknown service")

def ping_target(target):
    print(f'''
    {Fore.RED}
     ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
    |  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
    | |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
    |  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
    |_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
                                                            
    {Style.RESET_ALL}
    ''')
    response = os.system(f"ping -c 1 {target}")
    if response == 0:
        print(f"{Fore.BLUE}{target} is up!{Style.RESET_ALL}")
        return True
    else:
        print(f"{Fore.RED}{target} is down or not reachable.{Style.RESET_ALL}")
        return False
    

def port_scan(target,port, protocol):
    if not ping_target(target):
        return
    
    print(f"Scanning {target} for open ports ...\n")

    if protocol.lower() == "t" or not protocol:
        scan_func = tcp_port
    elif protocol.lower() == "u":
        scan_func = udp_port
    else:
        print(f"Unsupported protocol: {protocol}")
        return
    if not  port:
        with ThreadPoolExecutor(max_workers=100) as executor:
            for i in (ports):
                    executor.submit(scan_func, target, i)
    else:
        port=int(port)
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.submit(scan_func, target, port)

ports= {
    20: "FTP Data Transfer",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    137: "NetBIOS Name Service",
    138: "NetBIOS Datagram Service",
    139: "NetBIOS Session Service",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Monitor",
    1521: "Oracle Database",
    1723: "PPTP",
    3306: "MySQL",
    3389: "RDP",
    5060: "SIP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Proxy",
    8443: "HTTPS Proxy"
}
parser = OptionParser(F"""
{Fore.BLUE}
 ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
                                                         
{Style.RESET_ALL}
---------------------------------------------
pscan -t or --target     >>   Target IP or hostname
pscan -p or --port:      >>   Port number to scan (leave empty to scan all)                
pscan -P or --protocol   >>   Protocol: 't' for TCP, 'u' for UDP (default: 't')
---------------------------------------------
Developed by: Ibrahem abo kila
---------------------------------------------
""")
parser.add_option("-t", "--target", dest="target", help="Target IP or hostname")
parser.add_option("-p", "--port", dest="port", help="Port number to scan (leave empty to scan all)")
parser.add_option("-P", "--protocol", dest="protocol", default="t", help="Protocol: 't' for TCP, 'u' for UDP (default: 't')")

(options, args) = parser.parse_args()

if not options.target:
    print(parser.usage)
    print(f"{Fore.RED}Please specify a target using -t or --target{Style.RESET_ALL}")
else:
    port_scan(options.target, options.port, options.protocol)