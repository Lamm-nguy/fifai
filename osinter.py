import os
import time

language = ""                                                    



def loadedscr():
	print(f"""  
 ___       ________  ________  _______   ________  ________  ___
|\  \     |\   __  \|\   __  \|\   ___ \|\  ___ \ |\   ___ \|\  \      
\ \  \    \ \  \|\  \ \  \|\  \ \  \_|\ \ \   __/|\ \  \_|\ \ \  \     
 \ \  \    \ \  \\\  \ \   __  \ \  \ \\ \ \  \_|/_\ \  \ \\ \ \  \    
  \ \  \____\ \  \\\  \ \  \ \  \ \  \_\\ \ \  \_|\ \ \  \_\\ \ \__\   
   \ \_______\ \_______\ \__\ \__\ \_______\ \_______\ \_______\|__|   
    \|_______|\|_______|\|__|\|__|\|_______|\|_______|\|_______|   ___ 
                                                                  |\__\
                                                                  \|__| """)
                                                                       
os.system("clear")
os.system("git clone https://github.com/mxrch/GHunt && git clone https://github.com/spider863644/PhoneNumber-OSINT && git clone https://github.com/knownsec/ZoomEye-python && git clone https://github.com/hippiiee/osgint && git clone https://github.com/megadose/holehe && git clone https://github.com/mrh0wl/Cloudmare && git clone https://github.com/p1ngul1n0/blackbird ")
os.system("pip install -r requirements.txt")
os.system("clear")
time.sleep(2)
loadedscr()
time.sleep(1)
os.system("clear")
time.sleep(1)
loadedscr()
time.sleep(1)
os.system("clear")





def OBanner():
    print(f"""
                                               
           _,.---._      ,-,--.   .=-.-..-._        ,--.--------.    ,----.               
         ,-.' , -  `.  ,-.'-  _\ /==/_ /==/ \  .-._/==/,  -   , -\,-.--` , \  .-.,.---.   
        /==/_,  ,  - \/==/_ ,_.'|==|, ||==|, \/ /, |==\.-.  - ,-./==|-  _.-` /==/  `   \  
       |==|   .=.     \==\  \   |==|  ||==|-  \|  | `--`\==\- \  |==|   `.-.|==|-, .=., | 
       |==|_ : ;=:  - |\==\ -\  |==|- ||==| ,  | -|      \==\_ \/==/_ ,    /|==|   '='  / 
       |==| , '='     |_\==\ ,\ |==| ,||==| -   _ |      |==|- ||==|    .-' |==|- ,   .'  
        \==\ -    ,_ //==/\/ _ ||==|- ||==|  /\ , |      |==|, ||==|_  ,`-._|==|_  . ,'.  
         '.='. -   .' \==\ - , //==/. //==/, | |- |      /==/ -//==/ ,     //==/  /\ ,  ) 
           `--`--''    `--`---' `--`-` `--`./  `--`      `--`--``--`-----`` `--`-`--`--' 
            Made By Infinity's Báo Thủ Team
            """)
                                                                                    
    if language == "en":
        print("----------------------------------------------------------------------------")
        print("Option    |   Tools Name | Description                                     |")
        print("    1     | BlackBird    | Find Social Network Account With Name           |")
        print("    2     | Cloudmare    | Find Any Server's Info                          |")
        print("    3     | Holehe       | Find Any Socials Media Account With Email       |")
        print("    4     | OSGINT       | Find Any Github Accont With Email               |")
        print("    5     | ZoomEye      | Search Any Target's Info. You Need A API Key... |")
        print("    6     | GHunt        | Find Google Account Info By Email               |")
        print("    7     | PhoneNumber..| Find Target's Info With Phonenumer              |")
        print("----------------------------------------------------------------------------")
        print("st For Setting Pages")
    else:
        print("----------------------------------------------------------------------------")
        print("Lựa chọn  |   Tên Công Cụ| Mô tả                                           |")
        print("    1     | BlackBird    | Tìm tài khoản mạng xã hội bèng tên              |")
        print("    2     | Cloudmare    | Tìm thông tin của máy chủ                       |")
        print("    3     | Holehe       | Tìm tài khoản mạng xã hội bằng email            |")
        print("    4     | OSGINT       | Tìm tài khoản Github bằng email                 |")
        print("    5     | ZoomEye      | Tìm thông tin của mục tiêu, bạn cần API Key để..|")
        print("    6     | GHunt        | Tìm thông tin tài khoản Google bằng email       |")
        print("    7     | PhoneNumber..| Tìm thông tin của mục tiêu bằng Số điện thoại   |")
        print("----------------------------------------------------------------------------")
        print("st cho Trang Cài đặt")
    
def Main():
    OBanner()
    while True:
        OOption = input("Option > ")
        if OOption == "1":
            os.system("clear")
            print(f"""
                ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████ 
                ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
                ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
                ███    ███   ███        ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
                ███    ███ ▀███████████ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
                ███    ███          ███ ███  ███   ███     ███       ███    █▄  ▀███████████ 
                ███    ███    ▄█    ███ ███  ███   ███     ███       ███    ███   ███    ███ 
       `         ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███ """)
            tg = input("TARGET: ")
            os.system("cd blackbird && python blackbird.py -u " + tg)
        if OOption == "2":
            os.system("clear")
            print(f"""
                ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
                ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
                ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
                ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
                ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
                ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
                ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
                ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░         ░     ░░   ░ 
                ░ ░        ░   ░           ░             ░  ░   ░     """)
            tg2 = input("TARGET: ")
            os.system("cd Cloudmare && python Cloudmare.py -u " + tg2)
        if OOption == "3":
            os.system("clear")
            print(f"""
                  ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████ 
                ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
                ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
                ███    ███   ███        ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
                ███    ███ ▀███████████ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
                ███    ███          ███ ███  ███   ███     ███       ███    █▄  ▀███████████ 
                ███    ███    ▄█    ███ ███  ███   ███     ███       ███    ███   ███    ███ 
       `         ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███ """)
            tg3 = input("TARGET: ")
            os.system("cd holehe && python setup.py install && holehe " + tg3)
        if OOption == "4":
            os.system("clear")
            print(f"""
                ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
                ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
                ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
                ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
                ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
                ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
                ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
                ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░         ░     ░░   ░ 
                ░ ░        ░   ░           ░             ░  ░   ░     """)
            tg4 = input("TARGET: ")
            os.system("cd osgint && python osgint.py -e " + tg4)
        if OOption == "5":
            os.system("clear")
            print(f"""
                  ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████ 
                ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
                ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
                ███    ███   ███        ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
                ███    ███ ▀███████████ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
                ███    ███          ███ ███  ███   ███     ███       ███    █▄  ▀███████████ 
                ███    ███    ▄█    ███ ███  ███   ███     ███       ███    ███   ███    ███ 
       `         ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███ """)
            tg5 = input("TARGET: ")
            api = input("API KEY: ")
            os.system("cd ZoomEye-python && python setup.py install && zoomeye init -apikey " + api)
            os.system("cd ZoomEye-python && zoomeye search " + tg5)
        if OOption == "6":
            os.system("clear")
            print(f"""
                ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
                ▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
                ▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
                ▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
                ░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
                ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
                ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
                ░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░         ░     ░░   ░ """)
            tg6 = input("TARGET: ")
            os.system("cd GHunt && python main.py login")
            os.system("cd GHunt && python main.py email " + tg6)
        if OOption == "7":
            os.system("clear")
            print(f"""
                  ▄██████▄     ▄████████  ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████ 
                ███    ███   ███    ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███ 
                ███    ███   ███    █▀  ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███ 
                ███    ███   ███        ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
                ███    ███ ▀███████████ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
                ███    ███          ███ ███  ███   ███     ███       ███    █▄  ▀███████████ 
                ███    ███    ▄█    ███ ███  ███   ███     ███       ███    ███   ███    ███ 
       `         ▀██████▀   ▄████████▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███ """)
            os.system("cd PhoneNumber-OSINT && python phonenumber_osint.py")
   	 if OOption == "st":
     	   os.system("clear")
     	   print(f"""
        	                                ,----,       ,----,                                  
       	 	                                ,/   .`|     ,/   .`|                 ,--.             
       	     .--.--.       ,---,.    ,`   .'  :   ,`   .'  :   ,---,       ,--.'|  ,----..    
          	  /  /    '.   ,'  .' |  ;    ;     / ;    ;     /,`--.' |   ,--,:  : | /   /   \   
          	  |  :  /`. / ,---.'   |.'___,/    ,'.'___,/    ,' |   :  :,`--.'`|  ' :|   :     :  
          	  ;  |  |--`  |   |   .'|    :     | |    :     |  :   |  '|   :  :  | |.   |  ;. /  
		  |  :  ;_    :   :  |-,;    |.';  ; ;    |.';  ;  |   :  |:   |   \ | :.   ; /--`   
         	   \  \    `. :   |  ;/|`----'  |  | `----'  |  |  '   '  ;|   : '  '; |;   | ;  __  
		   `----.   \|   :   .'    '   :  ;     '   :  ;  |   |  |'   ' ;.    ;|   : |.' .' 
          	  __ \  \  ||   |  |-,    |   |  '     |   |  '  '   :  ;|   | | \   |.   | '_.' : 
		  /  /`--'  /'   :  ;/|    '   :  |     '   :  |  |   |  ''   : |  ; .''   ; : \  | 
	    	'--'.     / |   |    \    ;   |.'      ;   |.'   '   :  ||   | '`--'  '   | '/  .' 
		`--'---'  |   :   .'    '---'        '---'     ;   |.' '   : |      |   :    /   
          	              |   | ,'                             '---'   ;   |.'       \   \ .'    
            	            `----'                                       '---'          `---`     """) 
	 	print("Welcome to the setting pages!")
		 print("1. Language")
   	    	 print("2. Speak")
		 stp = input("> ")
      	  if stp == "1":
        	    print("1: Vietnamese")
         	   print("2: English")
         	   lh = input("Choose: ")
          	  if lh == "1":
          	      language = "vi"
          	  if lh == "2":
          	      language = "en"
        	    else: 
         	       print("invalid option!")
	  if stp == "2":
	      print("1. ON")
              print("2. OFF")
	      tga = input("> ")
	      if tga == "1":
		spk = True
	      if tga == "2":
                spk = False
            
try:
    Main()
except KeyboardInterrupt:
    print("Interrupt By User")
