import subprocess
import os

extension = ''
if os.name == 'nt':  # Checking if the OS is Windows
    extension = '.exe'
elif os.name == 'posix' and 'darwin' in os.uname().sysname.lower():  # Checking if the OS is macOS
    extension = '.app'

def main():
    rust_info = subprocess.check_output(['rustc', '-vV'], text=True)
    target_triple = None
    for line in rust_info.split('\n'):
        if line.startswith('host:'):
            target_triple = line.split(': ')[1]
            break

    if not target_triple:
        print('Failed to determine platform target triple')
        return

    src_path = f'src-tauri/sidecars/apps{extension}'
    dest_path = f'src-tauri/sidecars/apps-{target_triple}{extension}'
    
    os.rename(src_path, dest_path)
    print(f'Renamed {src_path} to {dest_path}')

try:
    main()
except Exception as e:
    raise e
