import time
import sys
import os
from colorama import init, Fore, Style

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

init()  # Initialize colorama

number = int(input("Enter a starting number: "))
previous_prime = None

try:
    while True:
        number += 1
        if is_prime(number):
            prime_gap = number - previous_prime if previous_prime else None
            prime_info = f"{number} ({prime_gap})" if prime_gap else str(number)
            if previous_prime and prime_gap == 2:
                prime_info = f"{Fore.RED}{prime_info}{Style.RESET_ALL}"
            print(prime_info)
            sys.stdout.write('\a')  # Beep the console
            sys.stdout.flush()  # Flush the output to ensure the beep is heard
            previous_prime = number
        time.sleep(0.25)  # Pause for 0.25 seconds between each iteration

except KeyboardInterrupt:
    pass

# Clear the beep sound on Windows
if os.name == 'nt':
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()

