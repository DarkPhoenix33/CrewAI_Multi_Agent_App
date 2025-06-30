import subprocess

try:
    result = subprocess.run(
        ["powershell.exe", "-NoProfile", "-Command", "Get-Date"],
        capture_output=True,
        text=True,
        check=True
    )
    print("Stdout:", result.stdout)
    print("Stderr:", result.stderr)
except subprocess.CalledProcessError as e:
    print("Error executing PowerShell command:", e)
    print("Stdout:", e.stdout)
    print("Stderr:", e.stderr)
except FileNotFoundError:
    print("Error: powershell.exe not found. Make sure PowerShell is installed and in your system's PATH.")
except Exception as e:
    print("An unexpected error occurred:", e)