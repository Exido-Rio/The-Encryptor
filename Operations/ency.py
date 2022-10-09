from .utils import *


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:

        fullPath = os.path.join(dirName, entry)

        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if fullPath.split(".")[-1] == "cryptokey":
                continue
            else:
                allFiles.append(fullPath)
    return allFiles


def ency(newkey, *files):
    for file in files:
        if file.split(".")[-1] == "crypto":
            cprint(f"{file} file is already encrypted", "red")
            sys.exit(
                "Pls move the encrypted file to seprate folder if you want to encrypt other files in same locaiton")
    count = 1
    for file in files:
        cprint(" Encrypting ..............File no:" + str(count), "green")
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            content_encrypted = Fernet(newkey).encrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(content_encrypted)
            os.rename(file, file+".crypto")
        except:
            print(f"can not encrypt the file :- {file}")
        count = count + 1


def file_get():
    files = list()
    for file in os.listdir():
        if file.split(".")[-1] == "cryptokey":
            continue
        if os.path.isfile(file):
            files.append(file)
    return files


def wrkey(key, path, selc: Optional[str] = ""):
    os.chdir(keydir+r"/Keys")
    if platform == 'win32':
        np = path.split("\\")[-1]
    else:
        np = path.split("/")[-1]

    with open(f"{selc} {np}key.cryptokey", "wb")as thekey:
        thekey.write(key)
    cprint(
        f"Your key files are save in {os.getcwd()} as {selc} {np}key.cryptokey", "blue")


kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                 salt=b'21', iterations=410000)


def skey(a): return base64.urlsafe_b64encode(kdf.derive(a))


def thekey():
    clrscr()
    a = [
        inquirer.List("key_inp", message="Which key you wanna use ?",
                      choices=["system", "own", "exit"])
    ]

    key_inp = inquirer.prompt(a, theme=GreenPassion())
    clrscr()
    if key_inp['key_inp'] == 'system':
        clrscr()
        return Fernet.generate_key()
    elif key_inp['key_inp'] == 'own':
        psw = bytes(askpass("Input your password ", mask="#"), 'utf-8')
        clrscr()
        return skey(psw)
    else:
        exit()


def enc():
    clrscr()
    global keydir
    keydir = os.getcwd()
    a = [
        inquirer.List("file_inp", message="What you wanna encrypt ?", choices=[
                      "text", "file",  "all files inside a directory", "all files inside the directory and subdirectry", "exit"])
    ]

    file_inp = inquirer.prompt(a, theme=GreenPassion())
    clrscr()
    if file_inp['file_inp'] == "text":
        text = bytes(inquirer.text(message="Input the text "), 'utf-8')
        key = thekey()
        print(Fernet(key).encrypt(text))
        wrkey(key, text)
    elif file_inp['file_inp'] == "file":
        filepath = inquirer.text(message=r"Input the files location ")
        cheak = os.path.isfile(filepath)
        if cheak == False:
            sys.exit("File not found")
        key = thekey()
        ency(key, filepath)
        wrkey(key, filepath)
    elif file_inp['file_inp'] == "all files inside a directory":
        filepath = inquirer.text(message="Input the files location ")
        cheak = os.path.isdir(filepath)
        if cheak == False:
            sys.exit("File not found")
        os.chdir(filepath)
        files = file_get()
        key = thekey()
        ency(key, *tuple(files))
        wrkey(key, filepath, file_inp['file_inp'])
    elif file_inp['file_inp'] == "all files inside the directory and subdirectry":
        filepath = inquirer.text(message="Input the files location ")
        cheak = os.path.isdir(filepath)
        if cheak == False:
            sys.exit("File not found")
        os.chdir(filepath)
        files = getListOfFiles(os.getcwd())
        key = thekey()
        ency(key, *tuple(files))
        wrkey(key, filepath, file_inp['file_inp'])
    else:
        exit()
