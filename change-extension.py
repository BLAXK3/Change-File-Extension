import os
import webbrowser as wb
import platform as pf


def change_extension(file_path, new_ets):
    file_name, old_ets = os.path.splitext(file_path)
    path = file_name + "." + new_ets
    os.rename(file_path, path)


def change_extensions_folder(folder_path, old_ets, new_ets):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(old_ets):
            file_path = os.path.join(folder_path, file_name)
            change_extension(file_path, new_ets)


def main():
    choice = input(">>> ")
    if choice[0:4] == "-ets":
        path = choice[5:]
    elif choice[0:3] == "-ch":
        path = choice[4:]
        try:
            if os.path.isfile(path):
                old_ets = os.path.splitext(path)[1]
                new_ets = input("Enter the new file extension >>> ")
                change_extension(path, new_ets)
                print(
                    f"\033[32mFile extension changed from {old_ets} to {new_ets}.\033[0m"
                )
            elif os.path.isdir(path):
                old_ets = input("Enter the old file extension >>> ")
                new_ets = input("Enter the new file extension >>> ")
                change_extensions_folder(path, old_ets, new_ets)
                print(
                    f"\033[32mAll files with extension {old_ets} in {path} have been changed to {new_ets}\033[0m"
                )
            else:
                print("\033[31mFolder or file not found\033[0m")
        except FileNotFoundError:
            print("\033[31mFolder or File not found.\033[0m")
    elif choice[0:4] == "-ext":
        print("\033[33mThank for using program\033[0m")
        print("\033[33mIf you like it, please give stars to my repo, thanks :)\033[0m")
        ops = pf.system()
        url = "https://github.com/Nutsuki3/Change-File-Extension"
        if ops == "Windows":
            wb.open_new_tab(url, new=2)
        elif ops == "Linux":
            wb.get("xdg-open").open_new_tab(url)
        elif ops == "Darwin":
            wb.get("safari").open_new_tab(url)
        elif os_name == "Android":
            wb.get("android").open_new_tab(url)
        elif os_name == "iOS":
            wb.get("safari").open_new_tab(url)

        return

    elif choice[0:4] == "-help":
        print("-ets for check the extension file")
        print("-ch for change the extension file")
        print("-ext for exit the program")
    else:
        print("-help for commands detials")

while True:
    main()
