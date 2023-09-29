from util.title import *
from util.methods import *
import time
import os

def menu():
    while True:
        os.system("cls")
        print(titles.menu_title())
        option = input("Select option: ")
        if option == "1":
            options.numeric_list()
        elif option == "2":
            options.absence()
        elif option == "3":
            options.baufort()

class options:
    @staticmethod
    def numeric_list():
        os.system("cls")
        print(titles.numeric_list_title())
        arg1 = input("Argument 1: ")
        arg2 = input("Argument 2: ")
        arg3 = input("Argument 3: ")
        arg4 = input("Argument 4: ")
        arg5 = input("Argument 5: ")

        result = methods.numeric_list(arg1, arg2, arg3, arg4, arg5)
        print(result)
        time.sleep(2)

    @staticmethod
    def absence():
        os.system("cls")
        print(titles.absence_title())
        documented = input("Documented hours: ")
        undocumented = input("Undocumented hours: ")
        hours = input("Total Hours: ")

        result = methods.absence(float(undocumented), float(documented), int(hours))
        print(result)
        time.sleep(2)

    @staticmethod
    def baufort():
        os.system("cls")
        print(titles.baufort_title())
        mps = input("Meters per second: ")

        result = methods.baufort(int(mps))
        print(result)
        time.sleep(2)


menu()
