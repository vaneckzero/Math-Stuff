import time
import sys
import os
from colorama import init, Fore, Style
import matplotlib.pyplot as plt

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

init()  # Initialize colorama

number = int(input("Enter a starting number: "))
previous_twin_prime = None
twin_primes_x = []
twin_primes_y = []

try:
    while True:
        number += 1
        if is_prime(number):
            if previous_twin_prime and number - previous_twin_prime == 2:
                twin_primes_x.append(number)
                twin_primes_y.append(number - previous_twin_prime)

                # Plot the graph after every twin prime
                plt.scatter(twin_primes_x, twin_primes_y)
                plt.xlabel("Twin Prime")
                plt.ylabel("Distance from Last Twin Prime")
                plt.title("Twin Primes and Distance from Last Twin Prime")
                plt.show()

            prime_info = f"{number}"
            if previous_twin_prime and number - previous_twin_prime == 2:
                prime_info = f"{Fore.RED}{prime_info}{Style.RESET_ALL}"
                sys.stdout.write('\a')  # Beep the console
                sys.stdout.flush()  # Flush the output to ensure the beep is heard
                previous_twin_prime = number

            print(prime_info)

        time.sleep(0.25)  # Pause for 0.25 seconds between each iteration

except KeyboardInterrupt:
    pass

# Clear the beep sound on Windows
if os.name == 'nt':
    import msvcrt
    while msvcrt.kbhit():
        msvcrt.getch()
