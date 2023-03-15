from Operations.ency import enc
from Operations.steno import sten
from Operations.dcy import dcy
from Operations.hashing import hasher
from Operations.utils import *


fig = Figlet(font='slant')
Created_by = colored(
    '                                             By Exido-Rio\n', 'yellow', attrs=['bold'])
About_tool = colored('  A tool to encrypt and decrypt your data easily using Fernet Encryption.'
                     ' You can also use this on any type of file upto 50GB.', 'blue')
print(colored(fig.renderText('           ENCRYPTOR'),
      'green'), Created_by, About_tool, '\n')


@shell(prompt="encrypto>", intro="Welcome to the Encrypto")
def encrypto():
    pass


@encrypto.command
def help():
    print("""
    clear: To clear the shell
    encrypt : To perform the encrytion 
    decrypt : To perfrom the decryption
    hash :  To get the hash
    stenographty : To hide measage into a image
    """)


@encrypto.command
def encrypt():
    enc()


@encrypto.command
def decrypt():
    dcy()


@encrypto.command
def stenography():
    sten()


@encrypto.command
def hash():
    hasher()


@encrypto.command
def clear():
    try:
        os.system("cls")
    except:
        os.system("clear")


try : # using to handle the exception caused within the operation 
    encrypto() 
except:
    pass