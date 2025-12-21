from datetime import datetime

def generate_report(system_info, disks, network_result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"=== DIAGNOSTICS REPORT ===\nGenerated: {timestamp}\n\n"

    report += "SYSTEM INFORMATION:\n"
    for k, v in system_info.items():
        report += f"- {k}: {v}\n"

    report += "\nDISK STATUS:\n"
    for d in disks:
        report += f"- {d['Device']} ({d['Mountpoint']}): {d['Usage (%)']}% used of {d['Total Size (GB)']} GB\n"

    report += "\nNETWORK DIAGNOSTICS:\n"

    for check, result in network_result.items():
        line = f"- {check}: {result['status']}"

        if "avg_latency_ms" in result and result["avg_latency_ms"] is not None:
            line += f" ({result['avg_latency_ms']} ms)"

        if "warning" in result and result["warning"]:
            line += f" ⚠ {result['warning']}"

        report += line + "\n"

    return report