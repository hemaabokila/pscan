import os
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style
import argparse

class ProtScanner:
    def __init__(self,target,port=None,protocol=None):
        self.target=target
        self.port=port
        self.protocol=protocol
        self.ports= {
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

    def tcp_port(self,port):
        so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        try:
            result=so.connect_ex((self.target,port))
            if result==0:
                service=self.service_name(port)
                print(f"{Fore.GREEN}TCP Port {port}: OPEN (Service: {service}){Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error scanning port {port}: {e}{Style.RESET_ALL}")
        finally:
            so.close()
    def udp_port(self,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket.setdefaulttimeout(1)
        try:
            s.sendto(b'', (self.target, port))
            data, _ = s.recvfrom(1024)
            print(f"{Fore.GREEN}UDP Port {port}: OPEN{Style.RESET_ALL}")
        except socket.timeout:
            pass
        except Exception as e:
            print(f"{Fore.RED}Error scanning UDP port {port}: {e}{Style.RESET_ALL}")
        finally:
            s.close()

    def service_name(self,port):
        return self.ports.get(port, "Unknown service")

    def ping_target(self):
        print(f'''
        {Fore.BLUE}
         ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
        |  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
        | |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
        |  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
        |_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
                            
                            Developed by: Ibrahem abo kila
        {Style.RESET_ALL}
        ''')
        response = os.system(f"ping -c 1 {self.target}")
        if response == 0:
            print(f"{Fore.GREEN}{self.target} is up!{Style.RESET_ALL}")
            return True
        else:
            print(f"{Fore.RED}{self.target} is down or not reachable.{Style.RESET_ALL}")
            return False


    def run(self):
        try:
            if not self.ping_target():
                return
            
            print(f"Scanning {self.target} for open ports ...\n")

            if self.protocol.lower() == "t" or not self.protocol:
                scan_func = self.tcp_port
                ports_to_scan = self.ports.keys()
            elif self.protocol.lower() == "u":
                scan_func = self.udp_port
                ports_to_scan = self.ports.keys()
            else:
                print(f"{Fore.RED}Unsupported protocol: {self.protocol}{Style.RESET_ALL}")
                return

            if not self.port:
                with ThreadPoolExecutor(max_workers=100) as executor:
                    {executor.submit(scan_func, i): i for i in ports_to_scan}
            else:
                port = int(self.port)
                scan_func(port)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}Scan interrupted by user.{Style.RESET_ALL}")
                
def main():
    parser = argparse.ArgumentParser(description='Prot scanner')
    parser.add_argument('target', help='The target URL to check for admin panels')
    parser.add_argument("-p", "--port", type=int, help="Port number to scan (leave empty to scan all)",default=None)
    parser.add_argument("-P", "--protocol", type=str, default="t", help="Protocol: 't' for TCP, 'u' for UDP (default: 't')")
   

    args = parser.parse_args()
    
    port_scaneer = ProtScanner(target=args.target, port=args.port, protocol=args.protocol)
    port_scaneer.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"{Fore.BLUE}[*] Exiting...{Style.RESET_ALL}")
        os._exit(0)