# from pyfiglet import Figlet
# custom = Figlet(width=100)
# print(custom.renderText('Website Blocker!'))

import time
from datetime import datetime as dt

temp_file = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts" #PATH TO SYSTEM HOST FILE
redirect = "127.0.0.1"
websites = ["INPUT A LIST OF WEBSITES HERE !"]

# Change this variables to a 24 hour value:
# TIME_1 = START TIME
# TIME_2 = END TIME


while True:
    if dt(dt.now().year,dt.now().month, dt.now().day, TIME_1) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day, TIME_2):
        print("Website Blocker Script running!")
        time.sleep(5)
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect + "       " + website + "\n")

    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()       
            file.seek(0)    
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()

        print("Website Blocker Script stopped!")
    time.sleep(2)



# from 8 to 5
# dt(2020,3,15,8)       dt.now()            dt(2020,3,15,5)
