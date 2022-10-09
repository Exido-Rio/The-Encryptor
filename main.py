from Operations.ency import enc
from Operations.steno import sten
from Operations.dcy import dcy
from Operations.hashing import hasher
from Operations.utils import *


fig = Figlet(font='slant')
Created_by = colored('                                                 By Aditya Prakash\n', 'yellow', attrs=['bold'])
About_tool = colored('  A tool to encrypt and decrypt your data easily using Fernet Encryption.'
                          ' You can also use this on any type of file upto 50GB.', 'blue')
print(colored(fig.renderText('ENCRYPTOR'), 'green'), Created_by, About_tool, '\n')

q = [
    inquirer.List("input", message="What you wanna do ?", choices=[
                  "encrypt", "decrypt", "hash", "stenography", "exit"])
]

inp = inquirer.prompt(q, theme=GreenPassion())

if inp['input'] == "encrypt":
    enc()
elif inp['input'] == "decrypt":
    dcy()
elif inp['input'] == "stenography":
    sten()
elif inp['input'] == "hash":
    hasher()
else:
    exit()
