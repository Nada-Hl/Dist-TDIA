#! /usr/bin/env python3
import time
import argparse
import signal
import subprocess
import os

def run_clock(duration):
    try:
        end_time = time.time() + duration
        while time.time() < end_time:
            current_time = time.strftime('%H:%M:%S %p')
            print(current_time, end="\r", flush=True)
            time.sleep(1)
        print("\nL'horloge s'est arrêtée.")
    except KeyboardInterrupt:
        print("\nL'horloge s'est arrêtée.")

def set_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    remaining_time = total_seconds

    try:
        while remaining_time > 0:
            hours, remainder = divmod(remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)

            timer_str = f"Timer: {hours:02}:{minutes:02}:{seconds:02}"
            print(timer_str, end="\r", flush=True)

            time.sleep(1)
            remaining_time -= 1

        print("\nMinuterie terminée ! La cloche sonnera.")
        os.system("printf '\a'")  # Terminal bell
    except KeyboardInterrupt:
        print("\nL'horloge s'est arrêtée.")

def handle_interrupt(signal, frame):
    subprocess.run('clear' if os.name == 'posix' else 'cls', shell=True)
    print("\nL'horloge s'est arrêtée.")
    exit()

def print_usage():
    print("Usage:")
    print("1. Pour faire fonctionner l'horloge : clock ")
    print("2. Pour régler une minuterie:")
    print("   clock -t [DURATION] (secondes par default)")
    print("   Exemple: clock -t 5 (régle la minuterie sur 5 secondes)")
    print("clock -H [HEURES] ")
    print("clock -M [MINUTES]")
    print("clock -S [SECONDES]")
    print("Example : clock -H 1 -M 2 -S 3 (régle la minuterie sur 1 heure, 2 minutes et 3 secondes)")
    exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clock with Timer")
    parser.add_argument("-t", "--timer", type=int, default=0, help="Définir une durée de minuterie en secondes")
    parser.add_argument("-H", "--hours", type=int, default=0, help="Définir le nombre d'heures pour la minuterie")
    parser.add_argument("-M", "--minutes", type=int, default=0, help="Définir le nombre de minutes pour la minuterie")
    parser.add_argument("-S", "--seconds", type=int, default=0, help="Définir le nombre de secondes pour la minuterie")

    args = parser.parse_args()

    if not args.timer and not args.hours and not args.minutes and not args.seconds:
        run_clock(60)
    elif args.timer and type(args.timer) == int:
        set_timer(0, 0, args.timer)
    elif args.hours or args.minutes or args.seconds:
        set_timer(args.hours, args.minutes, args.seconds)
    else:
        print("Erreur: La durée de la minuterie est requise.")
        print_usage()

    signal.signal(signal.SIGINT, handle_interrupt)
