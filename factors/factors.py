#!/usr/bin/python3

import sys
import time


def factorize(num):
    '''Factorize as many numbers as possible into
    a product of two smaller numbers'''

    for i in range(2, int(num** 0.5)+1):
        if num % i == 0:
            return (i, num//i)
    return None


if __name__ == "__main__":
    '''Reads the input file'''

    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        exit()

        input_file = sys.argv[1]
        try:
            with open(input_file, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("File not found")
            exit()

        start_time = time.time()
        '''assume that there will be no empy line,
        and no space before and after the valid number'''

        for line in lines:
            num = int(line.strip())
            factors = factorize(num)
            if factors:
                print(f"{num}-{factors[0]}*{factors[1]}")
            '''Your program will be killed after 5 seconds
            if it hasn’t finish'''

            if time.time() - start_time > 5:
                print("Time limit")
                exit()
