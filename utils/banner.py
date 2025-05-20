# banner.py
import os
from colorama import Fore, Style

def show_banner():
    os.system("clear" if os.name == "posix" else "cls")

    print(Fore.CYAN + """
    ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗██╗  ██╗██╗     ██╗     
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██║  ██║██║     ██║     
    ██║  ██║██████╔╝███████║██████╔╝█████╔╝ ███████╗███████║██║     ██║     
    ██║  ██║██╔═══╝ ██╔══██║██╔═══╝ ██╔═██╗ ╚════██║██╔══██║██║     ██║     
    ██████╔╝██║     ██║  ██║██║     ██║  ██╗███████║██║  ██║███████╗███████╗
    ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝
                             BlackShell Offensive Suite
    """ + Style.RESET_ALL)
    
    print(Fore.YELLOW + "[*] Author   : Vitrag00")
    print("[*] Version  : 1.0")
    print("[*] GitHub   : https://github.com/Vitrag00/BlackShell-Offensive-Suite")
    print("[*] Warning  : Use for educational purposes only!" + Style.RESET_ALL)
    print()

if __name__ == "__main__":
    show_banner()
