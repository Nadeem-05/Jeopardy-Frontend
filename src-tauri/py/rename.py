from sys import platform
import os


if platform == "linux" or platform == "linux2":
    src_path = 'src-tauri/sidecars/apps'
    dest_path = 'src-tauri/sidecars/apps-x86_64-unknown-linux-gnu'
    os.rename(src_path, dest_path)
elif platform == "darwin":
    import platform
    print(platform.processor())
    if platform.processor() == "i386":
        src_path = 'src-tauri/sidecars/apps'
        dest_path = 'src-tauri/sidecars/apps-x86_64-apple-darwin'
        os.rename(src_path, dest_path)
    elif platform.processor() == "arm":
        src_path = 'src-tauri/sidecars/apps'
        dest_path = 'src-tauri/sidecars/apps-aarch64-apple-darwin'
        os.rename(src_path, dest_path)

elif platform == "win32":
    src_path = f'src-tauri/sidecars/apps.exe'
    dest_path = f'src-tauri/sidecars/apps-x86_64-pc-windows-msvc.exe'
    os.rename(src_path, dest_path)

