import requests
from colorama import Fore as fore
from colorama import Fore
import threading
import time
import asyncio
import json
import configparser

config = configparser.ConfigParser()
config.read_file(open(r'config.ini'))
token = config.get('settings', 'token')

r = fore.LIGHTRED_EX
b = fore.LIGHTBLUE_EX
w = fore.WHITE
if(len(token) < 10):
  token = input(f"{fore.BLUE}~/WareName{fore.WHITE}$ Token: ")
else:
  pass
channel = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Channel/GC/DM ID: ")
messageid = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Message ID: ")
amount = input(f"{fore.BLUE}~/Desire{fore.WHITE}$ Amount ID: ")

sessions = requests.Session()
headers = {
  "Authorization": token
}
def info( words):
  print(f"{r}[{Fore.WHITE}Desire{r}] {b}- {Fore.WHITE}{words}")


async def pinspammer(channel,messageid):
    r = sessions.put(
      f"https://discord.com/api/v9/channels/{channel}/pins/{messageid}",
      headers=headers)
    d = sessions.delete(f"https://discord.com/api/v9/channels/{channel}/pins/{messageid}",
      headers=headers)
    if(r.status_code == "204" or r.status_code == 204):
        info("Pinned: " + str(messageid))
        pass
    if(d.status_code == "204" or r.status_code == 204):
        info("unpinned: " + str(messageid))
        pass
    else:
      result = json.loads(r.text)
      seconds = int(result['retry_after'])
      info("Sleeping " + str(float(int(seconds))) + " Seconds to avoid rate limit ban")
      await asyncio.sleep(seconds)
    
    


async def start():
  for i in range(int(amount)):
    await pinspammer(channel,messageid)

loop = asyncio.get_event_loop()
loop.run_until_complete(start())
