import winreg

def set_flip_flop_wheel():
    path = r'SYSTEM\CurrentControlSet\Enum\HID'
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path) as base_key:
            for i in range(0, winreg.QueryInfoKey(base_key)[0]):
                subkey_name = winreg.EnumKey(base_key, i)
                subkey_path = f"{path}\\{subkey_name}"
                try:
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path) as sub_key:
                        for j in range(0, winreg.QueryInfoKey(sub_key)[0]):
                            sub_subkey_name = winreg.EnumKey(sub_key, j)
                            sub_subkey_path = f"{subkey_path}\\{sub_subkey_name}\\Device Parameters"
                            try:
                                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, sub_subkey_path, 0, winreg.KEY_WRITE) as device_key:
                                    winreg.SetValueEx(device_key, 'FlipFlopWheel', 0, winreg.REG_DWORD, 1)
                                    print(f"Set FlipFlopWheel=1 for {sub_subkey_path}")
                            except FileNotFoundError:
                                # Device Parameters key does not exist
                                pass
                except FileNotFoundError:
                    # Subkey does not exist
                    pass
    except FileNotFoundError:
        print(f"Path {path} does not exist")

if __name__ == "__main__":
    set_flip_flop_wheel()
