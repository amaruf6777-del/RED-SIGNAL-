import os
import sys
import time

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear_screen()
    print("""
    ==================================================
                 RED SIGNAL CYBER COMMUNITY           
    ==================================================
    [•] OWNER      : JOY XHOWDHORY
    [•] CEO        : SHIPU XHOWDHORY
    [•] AD. CEO    : RAJ XHOWDHORY
    [•] FACEBOOK   : RED SIGNAL CYBER COMMUNITY
    [•] GITHUB     : RSJOY677
    [•] WHATSAPP   : 01312272440
    ==================================================
    [•] FEATURE    : OLD-CLONE ~ GMAIL ~ RANDOM ~ FILE
    [•] SYSTEM     : WIFI + DATA + PAID VPN
    [•] STATUS     : PREMIUM
    [•] VERSION    : 1.0.2
    ==================================================
    """)

def main_menu():
    banner()
    print("[1] Start Program")
    print("[0] Exit")
    choice = input("\nChoose Option: ")
    if choice == '1':
        print("\nProgram Running...")
    else:
        sys.exit()

if __name__ == "__main__":
    main_menu()
