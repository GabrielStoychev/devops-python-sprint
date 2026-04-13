import subprocess

def check_linux_directory(path):
    result = subprocess.run(["ls", path], capture_output = True, text = True)

    if result.returncode == 0:
        print(f"Directory {path} exists!")
        print(f"Files found: {result.stdout}")
    else:
        print(f"Error: Directory {path} not found.")
        print(f"Linux says: {result.stderr}")