import socket
import threading

print("=" * 50)
print("     Python Network Port Scanner")
print("     Author: Your Name")
print("     For educational use only")
print("=" * 50)

target = input("Enter target IP or hostname: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}\n")

lock = threading.Lock()

def grab_banner(sock, port):
    try:
        # HTTP banner
        if port in [80, 8080, 8000, 443]:
            sock.sendall(b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n")
        return sock.recv(1024).decode(errors="ignore").strip()
    except:
        return None

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        result = s.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            banner = grab_banner(s, port)

            with lock:
                print(f"[+] Port {port:<5} OPEN | Service: {service}")
                if banner:
                    print(f"    Banner: {banner.splitlines()[0]}")

        s.close()
    except:
        pass

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan complete.")
