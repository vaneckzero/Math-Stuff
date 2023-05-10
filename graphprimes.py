import re
import matplotlib.pyplot as plt

def extract_data(filename):
    with open(filename, 'r') as file:
        content = file.readlines()

    primes = []
    gaps = []

    for line in content:
        prime, gap = re.findall(r'\d+', line)
        primes.append(int(prime))
        gaps.append(int(gap))

    return primes, gaps

def plot_data(primes, gaps):
    plt.scatter(primes, gaps)
    plt.xlabel('Prime Numbers')
    plt.ylabel('Prime Gaps')
    plt.title('Prime Numbers vs Prime Gaps')
    plt.show()

if __name__ == '__main__':
    filename = 'primelist.txt'  # Replace with your input file name
    primes, gaps = extract_data(filename)
    plot_data(primes, gaps)
