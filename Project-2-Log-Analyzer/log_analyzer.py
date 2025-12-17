from collections import Counter
import re

LOG_FILE = "sample.log"
THRESHOLD = 3

ip_pattern = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")

def extract_failed_ips(log_file):
    failed_ips = []

    with open(log_file, "r") as file:
        for line in file:
            if "Failed password" in line:
                match = ip_pattern.search(line)
                if match:
                    failed_ips.append(match.group())

    return failed_ips


def analyze_ips(ip_list):
    return Counter(ip_list)


def report_suspicious_ips(counter, threshold):
    print("\nSecurity Alert Report")
    print("-" * 30)

    suspicious = False
    for ip, attempts in counter.items():
        if attempts >= threshold:
            print(f"[!] Suspicious IP Detected: {ip} ({attempts} failed attempts)")
            suspicious = True

    if not suspicious:
        print("No suspicious IPs detected.")

    print("\nSummary")
    print(f"Total Failed Attempts: {sum(counter.values())}")
    print(f"Unique IP Addresses: {len(counter)}")


if __name__ == "__main__":
    failed_ips = extract_failed_ips(LOG_FILE)
    ip_counts = analyze_ips(failed_ips)
    report_suspicious_ips(ip_counts, THRESHOLD)
