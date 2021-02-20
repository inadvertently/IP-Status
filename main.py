import requests, colorama, time, os
from progress.bar import ChargingBar
from requests import get
from colorama import Fore

def clear():
    os.system("cls")

def check():
    Info = get('https://ipapi.co/json/').text
    mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    bar = ChargingBar(f"Loading...", max = len(mylist))
    for x in mylist:
        bar.next()
        time.sleep(0.1)
    bar.finish()
    clear()
    print(f"{Fore.RED} Info for current IP is: {Info}{Fore.RED}")

if __name__ == "__check__":
   check()

check() 
