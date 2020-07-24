print("Infinite VK Online Status")
print("Developed by CatchThels\nFollow me on GitHub :)")

import time
import vk_api
import colorama
from colorama import init, Fore


init()

login = input("Login: ")
password = input("Password: ")
print(Fore.YELLOW + "Authenticating...")
try:
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()
    print(Fore.GREEN + "    Successfully authenticated!")
except:
    print(Fore.RED + "  Failed to authenticate :(")

print(Fore.RESET + "All is ready!")

onlineAttemps = 0
while True:
    print("Setting online(" + Fore.GREEN + str(onlineAttemps) + Fore.RESET + ")...")
    try:
        vk.account.setOnline()
        print(Fore.GREEN + "    Ok!")
    except:
        print(Fore.RED + "  Failed to set Online status! Did you change your password? Or maybe problems with internet connection?")
        exit()

    time.sleep(280)
