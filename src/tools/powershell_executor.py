import subprocess
import json
from crewai.tools.base_tool import BaseTool

class PowerShellExecutor(BaseTool):
    name: str = "PowerShell Executor"
    description: str = "Executes PowerShell commands and scripts on the server. Attempts to return output in JSON format if possible, otherwise raw text."

    def _run(self, command: str) -> str:
        try:
            # Execute the PowerShell command directly using subprocess.run
            # Wrap the command in a script block for proper execution of multiple statements
            full_command = f"& {{ {command} }}"
            result = subprocess.run(
                ["powershell.exe", "-NoProfile", "-Command", full_command],
                capture_output=True,
                text=True,
                check=True  # Raise an exception for non-zero exit codes
            )

            stdout = result.stdout.strip()
            stderr = result.stderr.strip()

            if stderr:
                return f"Error executing command: {stderr}\nOutput: {stdout}"
            
            try:
                # Attempt to parse output as JSON
                json_output = json.loads(stdout)
                formatted_output = json.dumps(json_output, indent=2)
                return f"JSON Output:\n{formatted_output}"
            except json.JSONDecodeError:
                # If not JSON, return raw stdout
                return stdout

        except subprocess.CalledProcessError as e:
            return f"Error executing PowerShell command (Exit Code: {e.returncode}):\nStdout: {e.stdout}\nStderr: {e.stderr}"
        except Exception as e:
            return f"Failed to execute PowerShell command: {e}"