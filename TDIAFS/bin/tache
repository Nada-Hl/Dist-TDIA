#! /usr/bin/env python3
import psutil
import time
from colorama import Fore, Style, init
import os
import GPUtil

init()

def get_gpu_usage():
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            return gpus[0].load * 100.0
        else:
            return 0
    except Exception as e:
        print(f"ERREUR de trouver le  GPU : {e}")
        return 0

def print_usage_with_bar(interval=1, bar_length=20):
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=interval)
            gpu_usage = get_gpu_usage()

            cpu_bar = "█" * int(cpu_usage / 100 * bar_length)
            gpu_bar = "█" * int(gpu_usage / 100 * bar_length)

            spaces = " " * (bar_length - len(cpu_bar))

            print(f"\rCPU:[{Fore.GREEN}{cpu_bar}{Style.RESET_ALL}{spaces}]  {cpu_usage:.2f}%",end="", flush=True)
            print(f"       |      GPU: [{Fore.BLUE}{gpu_bar}{Style.RESET_ALL}] {gpu_usage:.2f}%", end="", flush=True)
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nTache arrete .")

if __name__ == "__main__":
    print("Tappez sur ctrl+c pour quitter")
    print("Tache par seconde (T/s):")
    print_usage_with_bar()


