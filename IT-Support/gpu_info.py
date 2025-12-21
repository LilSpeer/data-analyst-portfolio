import subprocess

def get_gpu_info():
    """
    Retrieves GPU information using Windows WMIC.
    Returns a list of GPU descriptions.
    """
    gpus = []

    try:
        output = subprocess.check_output(
            ["wmic", "path", "win32_videocontroller", "get", "Name,AdapterRAM,DriverVersion"],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )

        lines = [line.strip() for line in output.splitlines() if line.strip()]
        for line in lines[1:]:
            gpus.append(line)

    except Exception:
        gpus.append("GPU information unavailable")

    return gpus
