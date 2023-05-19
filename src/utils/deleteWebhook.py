import requests
from utils.common import *

def deleteWebhook(url):
    set_console_title("Hoax V1 | Made by Hoax#7907 | Delete Webhook")
    requests.delete(url)
    print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}C{Fore.WHITE}] Deleted Webhook")
    sleep(1)