import os
import time
import wmi
from os import *
from concurrent.futures import process
from pymem import *
from pypresence import Presence
from time import time
import colorama
from colorama import Fore

# Вот тут вывод в консоль текста (Для любопытных)
colorama.init()
print(Fore.YELLOW + "    ")
print("              Привет!", os.getlogin())
print(Fore.GREEN + "              Version  With Inject ")
print("░█████╗░██████╗░░█████╗░███╗░░██╗██╗██╗░░░██╗███╗░░░███╗")
print("██╔══██╗██╔══██╗██╔══██╗████╗░██║██║██║░░░██║████╗░████║")
print("██║░░╚═╝██████╔╝███████║██╔██╗██║██║██║░░░██║██╔████╔██║")
print("██║░░██╗██╔══██╗██╔══██║██║╚████║██║██║░░░██║██║╚██╔╝██║")
print("╚█████╔╝██║░░██║██║░░██║██║░╚███║██║╚██████╔╝██║░╚═╝░██║")
print("░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝")
print(Fore.RED + " Скрипт активирован успешно // By Ghosvx // Андрюша Душненький")
print(Fore.YELLOW + "       ")
print("[+] Харектеристики вашего устройства")
computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576

print('Процесор: {0}'.format(proc_info.Name))
print('Оперативная Память: {0} GB'.format(system_ram))
print('Видео Карта: {0}'.format(gpu_info.Name))

# Вот тут инжектор (Для Любопытных)

print(Fore.MAGENTA + "   ")
print("██╗███╗░░██╗░░░░░██╗███████╗░█████╗░████████╗░█████╗░██████╗░")
print("██║████╗░██║░░░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print("██║██╔██╗██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝")
print("██║██║╚████║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗")
print("██║██║░╚███║╚█████╔╝███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║")
print("╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
print(Fore.RED + " ")
dll_path = os.path.abspath("C:\\cranium\\Cranium.dll")
dll_path_bytes = bytes(dll_path, "UTF-8")
process_name = input("Введите имя процесса: ")

open_process = Pymem(process_name)
process.inject_dll(open_process.process_handle, dll_path_bytes)


print(Fore.GREEN + " Краниум Успешно Инжектнут!")
print("              Не закрывайте консоль для отображения активности в дискорде")


# Вот тут снизу уже идет Активность для дискорда ( Для Любопытных )

RPC = Presence("1074766803428970557")
btns = [
	{
		"label": "Скачать Cranium + Injector",
		"url": "https://cdn.discordapp.com/attachments/1093570799144812654/1098635045394202745/Injector.zip"

	}	

]
RPC.connect()
RPC.update(
	state="Играет в GMOD",
	details="Софт Cranium (Free)",
	start=time(),
	buttons=btns,
	large_image="cranium",
	small_image="urba",
	large_text="Cranium",
	small_text="https://tapy.me/Urbanichka",

)
input()

