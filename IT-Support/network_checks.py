import subprocess
import socket
import re


def run_ping(host, count=4):
    try:
        output = subprocess.check_output(
            ["ping", "-n", str(count), host],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )

        # Extract average latency (Windows format)
        match = re.search(r"Average = (\d+)ms", output)
        avg_latency = int(match.group(1)) if match else None

        status = "Success"
        warning = None

        if avg_latency is not None and avg_latency > 100:
            warning = f"High latency detected ({avg_latency} ms)"

        return {
            "status": status,
            "avg_latency_ms": avg_latency,
            "warning": warning,
            "details": output
        }

    except subprocess.CalledProcessError as e:
        return {
            "status": "Failed",
            "avg_latency_ms": None,
            "warning": "Ping failed",
            "details": e.output
        }


def check_local_stack():
    # Loopback test
    return run_ping("127.0.0.1")


def check_gateway():
    # Default Gateway test
    return run_ping("192.168.1.1")


def check_dns():
    try:
        socket.gethostbyname("google.com")
        return {"status": "Success", "details": "DNS resolution successful"}
    except socket.error:
        return {"status": "Failed", "details": "DNS resolution failed"}


def check_external_connectivity():
    # Public DNS server
    return run_ping("8.8.8.8")


def full_network_diagnostics():
    return {
        "Local Stack": check_local_stack(),
        "Gateway Reachability": check_gateway(),
        "DNS Resolution": check_dns(),
        "External Connectivity": check_external_connectivity(),
        "Nearest Server Latency": check_latency_to_nearest()
    }

def check_latency_to_nearest():
    # Cloudflare DNS (globally distributed, low latency)
    return run_ping("1.1.1.1")
