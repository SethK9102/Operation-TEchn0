from random import *
from pandas import *
import os
import time

wait = time.sleep
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


class Techno:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}!")






def main():
    print("Hello, World!")
    wait(2)
    clear()
    print("This is a simple Python script.")
    print("Goodbye!")
    return True


if __name__ == "__main__":
    main()