import os
from dotenv import load_dotenv

import paramiko

load_dotenv()

# Access the environment variables
hostname = os.getenv("HOSTNAME")
port = int(os.getenv("WEBPORT"))  # Convert port to an integer
username = os.getenv("SG_USERNAME")
password = os.getenv("SG_PASSWORD")

remote_notes_dir = os.getenv("REMOTE_NOTES_DIR")
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
test_file_path = os.path.join(parent_directory, "dist/notes/index.html")
print(test_file_path)

command = "ls"

try:
    # Establish SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)

    # Execute the command
    stdin, stdout, stderr = ssh.exec_command(command)

    sftp = ssh.open_sftp()
    remote_file_path = remote_notes_dir + "/index.html"
    print(remote_file_path)
    sftp.put(test_file_path, remote_file_path)
    sftp.close()

    # Check for any error output
    error = stderr.read().decode().strip()
    if error:
        print(f"Error occurred: {error}")
    else:
        print("SSH connection successful. Command executed successfully.")

    ssh.close()

except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except paramiko.SSHException as e:
    print(f"SSH connection failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
