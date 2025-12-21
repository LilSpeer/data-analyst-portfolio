import system_info
import disk_checks
import network_checks
import report


def main():
    sys_info = system_info.get_system_info()
    disks = disk_checks.check_disks()
    network = network_checks.full_network_diagnostics()
    

    rep = report.generate_report(sys_info, disks, network)
    print(rep)

    with open("logs/diagnostics.log", "a") as f:
        f.write(rep + "\n\n")


if __name__ == "__main__":
    main()