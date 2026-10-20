‎import os
‎import sys
‎import time
‎
‎def clear_screen():
‎    os.system('cls' if os.name == 'nt' else 'clear')
‎
‎def banner():
‎    clear_screen()
‎    # রঙ ও ডিজাইন টার্মিনালে সুন্দর দেখানোর জন্য
‎    print("\033[1;31m") # লাল রঙ
‎    print("██████╗ ███████╗██████╗     ███████╗██╗ ██████╗ ███╗   ██╗ █████╗ ██╗     ")
‎    print("██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║██╔════╝ ████╗  ██║██╔══██╗██║     ")
‎    print("██████╔╝█████╗  ██║  ██║    ███████╗██║██║  ███╗██╔██╗ ██║███████║██║     ")
‎    print("██╔══██╗██╔══╝  ██║  ██║    ╚════██║██║██║   ██║██║╚██╗██║██╔══██║██║     ")
‎    print("██║  ██║███████╗██████╔╝    ███████║██║╚██████╔╝██║ ╚████║██║  ██║███████╗")
‎    print("╚═╝  ╚═╝╚══════╝╚═════╝     ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝")
‎    print("\033[0m")
‎    
‎    print("\033[1;33m" + "="*65 + "\033[0m")
‎    print("\033[1;36m[=] OWNER      : \033[1;37mJOY XHOWDHORY")
‎    print("\033[1;36m[=] CEO        : \033[1;37mSHIPU XHOWDHORY")
‎    print("\033[1;36m[=] AD. CEO    : \033[1;37mRAJ XHOWDHORY")
‎    print("\033[1;36m[=] FACEBOOK   : \033[1;37mRED SIGNAL CYBER COMMUNITY")
‎    print("\033[1;36m[=] GITHUB     : \033[1;37mRSJOY677")
‎    print("\033[1;36m[=] WHATSAPP   : \033[1;37m01312272440")
‎    print("\033[1;36m[=] FEATURE    : \033[1;37mOLD-CLONE ~ GMAIL ~ RANDOM ~ FILE")
‎    print("\033[1;36m[=] SYSTEM     : \033[1;37mWIFI + DATA + PAID VPN")
‎    print("\033[1;36m[=] STATUS     : \033[1;32mPREMIUM")
‎    print("\033[1;36m[=] VERSION    : \033[1;37m1.0.2")
‎    print("\033[1;33m" + "="*65 + "\033[0m")
‎
‎def main():
‎    banner()
‎    print("\n\033[1;32m[+] টুলটি সফলভাবে লোড হয়েছে!\033[0m")
‎    print("\n[1] Start Cloning")
‎    print("[2] Update Tool")
‎    print("[3] Exit")
‎    
‎    choice = input("\n\033[1;35m==> অপশন বেছে নিন: \033[0m")
‎    
‎    if choice == '1':
‎        print("\n\033[1;31m[!] প্রসেস শুরু হচ্ছে...\033[0m")
‎        time.sleep(2)
‎    elif choice == '2':
‎        print("\n\033[1;32m[!] আপনার টুলটি ইতিমধ্যে আপডেট ভারژনে (1.0.2) রয়েছে।\033[0m")
‎    else:
‎        print("\n[!] বের হয়ে যাওয়া হচ্ছে...")
‎        sys.exit()
‎
‎if __name__ == '__main__':
‎    main()
‎
‎import os
‎import sys
‎import time
‎
‎# টার্মিনাল ক্লিয়ার করার ফাংশন
‎def clear():
‎    os.system('cls' if os.name == 'nt' else 'clear')
‎
‎# অ্যানিমেটেড লোডিং স্ক্রিন
‎def loading_screen():
‎    clear()
‎    colors = ['\033[1;31m', '\033[1;33m', '\033[1;32m', '\033[1;36m', '\033[1;35m']
‎    print("\n\n")
‎    for i in range(1, 101):
‎        color = colors[i % len(colors)]
‎        sys.stdout.write(f"\r{color}[+] LOADING RED SIGNAL TOOL... [{i}%] ")
‎        sys.stdout.flush()
‎        time.sleep(0.03)
‎    print("\n\n\033[1;32m[✓] LOADING COMPLETE!\033[0m")
‎    time.sleep(1)
‎
‎# মূল পেজের ব্যানার ও ইন্টারফেস
‎def display_interface():
‎    clear()
‎    
‎    # রঙ সংজ্ঞা (Color Codes)
‎    RED = '\033[1;31m'
‎    GREEN = '\033[1;32m'
‎    YELLOW = '\033[1;33m'
‎    BLUE = '\033[1;34m'
‎    PURPLE = '\033[1;35m'
‎    CYAN = '\033[1;36m'
‎    WHITE = '\033[1;37m'
‎    RESET = '\033[0m'
‎
‎    # ১. এক্সেস ডিনাইড বক্স (Access Denied Box)
‎    print(YELLOW + "┌" + "─"*56 + "┐")
‎    print(f"│ {RED}[!] ACCESS DENIED{YELLOW}".center(66) + "│")
‎    print("├" + "─"*56 + "┤")
‎    print(f"│ {WHITE}YOUR DEVICE FREE TRIAL HAS EXPIRED/USED.{YELLOW}".ljust(64) + "│")
‎    print(f"│ {WHITE}PLEASE SEND PAYMENT AND GET PAID KEY{YELLOW}".ljust(64) + "│")
‎    print(f"│ {WHITE}TO CONTINUE USING THIS TOOL! 😔{YELLOW}".ljust(64) + "│")
‎    print("└" + "─"*56 + "┘" + RESET)
‎    
‎    print(PURPLE + "─"*58 + RESET)
‎
‎    # ২. প্রজেক্টের ইনফরমেশন সেকশন
‎    print(f"{CYAN}[=] OWNER       {WHITE}: {RED}JOY XHOWDHORY")
‎    print(f"{CYAN}[=] CEO         {WHITE}: {YELLOW}SHIPU XHOWDHORY")
‎    print(f"{CYAN}[=] AD. CEO     {WHITE}: {GREEN}RAJ XHOWDHORY")
‎    print(f"{CYAN}[=] FACEBOOK    {WHITE}: {BLUE}RED SIGNAL CYBER COMMUNITY")
‎    print(f"{CYAN}[=] GITHUB      {WHITE}: {PURPLE}RSJOY677")
‎    print(f"{CYAN}[=] WHATSAPP    {WHITE}: {GREEN}01312272440")
‎    print(f"{CYAN}[=] FEATURE     {WHITE}: {WHITE}OLD-CLONE ~ GMAIL ~ RANDOM ~ FILE")
‎    print(f"{CYAN}[=] SYSTEM      {WHITE}: {CYAN}WIFI + DATA + PAID VPN")
‎    print(f"{CYAN}[=] STATUS      {WHITE}: {RED}PREMIUM")
‎    print(f"{CYAN}[=] VERSION     {WHITE}: {GREEN}1.0.2")
‎    
‎    print(PURPLE + "─"*58 + RESET)
‎
‎    # ৩. অ্যাক্টিভেশন স্ট্যাটাস
‎    print(f"{GREEN}[✓] USER NAME   {WHITE}: {RED}NOT ACTIVATED")
‎    print(f"{GREEN}[✓] USER KEY    {WHITE}: {RED}NOT ACTIVATED")
‎    print(f"{GREEN}[✓] VALIDITY    {WHITE}: {RED}NOT ACTIVATED")
‎    
‎    print(PURPLE + "─"*58 + RESET)
‎
‎def main():
‎    # প্রথমে লোডিং স্ক্রিন দেখাবে
‎    loading_screen()
‎    
‎    # লোডিং শেষে মেইন ইন্টারফেস আসবে
‎    display_interface()
‎    
‎    # ইনপুট নেওয়ার অংশ
‎    try:
‎        user_name = input("\033[1;37m★ Enter Your Name ☞ \033[1;32m")
‎    except KeyboardInterrupt:
‎        print("\n\n\033[1;31m[!] Program Exited.\033[0m")
‎        sys.exit()
‎
‎if __name__ == '__main__':
‎    main()
‎
