import os
import sys
import base64
import signal
import inquirer
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from inquirer.themes import GreenPassion
from termcolor import cprint, colored
from sys import platform
from maskpass import askpass
from typing import Optional
from pyfiglet import Figlet
import hashlib
from hashlib import blake2b


def KeybordInteruptHandler(signal , frame):
    print(Fore.YELLOW,"\nKeybordInterupt (ID: {}) has been caught".format(signal),Fore.RESET)
    exit()

signal.signal(signal.SIGINT, KeybordInteruptHandler)

def clrscr():
    try:
        if platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
