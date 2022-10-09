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


def decy(newkey, *files):
    count = 1
    for file in files:
        cprint(" Decrypting ..............File no:" + str(count), "green")
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            content_decrypted = Fernet(newkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(content_decrypted)
            os.rename(file, file[:-7])
        except:
            print(f"could not decrypt the file :- {file}")
        count = count + 1


def file_get():
    files = list()
    for file in os.listdir():
        if file.split(".")[-1] == "cryptokey":
            continue
        if os.path.isfile(file):
            files.append(file)
    return files


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
        filepath = inquirer.text(message="Input the key file location ")
        cheak = os.path.isfile(filepath)
        if cheak == False:
            sys.exit("Key File not found")
        with open(filepath, "rb") as thekey:
            clrscr()
            return thekey.read()
    elif key_inp['key_inp'] == 'own':
        psw = bytes(askpass("Input your password ",mask="#"), 'utf-8')
        clrscr()
        return skey(psw)
    else:
        exit()


def dcy():
    clrscr()
    a = [
        inquirer.List("file_inp", message="What you wanna decrypt ?", choices=[
                      "text", "file",  "all files inside a directory", "all files inside the directory and subdirectry", "exit"])
    ]

    file_inp = inquirer.prompt(a, theme=GreenPassion())
    clrscr()
    if file_inp['file_inp'] == "text":
        text = bytes(inquirer.text(message="Input the text "), 'utf-8')
        key = thekey()
        print(Fernet(key).decrypt(text))
    elif file_inp['file_inp'] == "file":
        filepath = inquirer.text(message=r"Input the files location ")
        cheak = os.path.isfile(filepath)
        if cheak == False:
            sys.exit("File not found")
        key = thekey()
        decy(key, filepath)
    elif file_inp['file_inp'] == "all files inside a directory":
        filepath = inquirer.text(message="Input the files location ")
        cheak = os.path.isdir(filepath)
        if cheak == False:
            sys.exit("File not found")
        key = thekey()
        os.chdir(filepath)
        files = file_get()
        decy(key, *tuple(files))
    elif file_inp['file_inp'] == "all files inside the directory and subdirectry":
        filepath = inquirer.text(message="Input the files location ")
        cheak = os.path.isdir(filepath)
        if cheak == False:
            sys.exit("File not found")
        key = thekey()
        os.chdir(filepath)
        files = getListOfFiles(os.getcwd())
        decy(key, *tuple(files))
    else:
        exit()
