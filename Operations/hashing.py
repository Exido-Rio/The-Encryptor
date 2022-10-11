from .utils import *

BUF_SIZE = 32768  # Read file in 32kb chunks

MD5 = hashlib.md5()
SHA1 = hashlib.sha1()
BLAKE2B = hashlib.blake2b()


def file_hasher(file, algo):
    with open(file, 'rb') as taste:
        while True:
            data = taste.read(BUF_SIZE)
            if not data:
                break
            if algo == 'MD5':
                hs_algo = MD5
                MD5.update(data)
            elif algo == 'SHA1':
                hs_algo = SHA1
                SHA1.update(data)
            elif algo == 'BLAKE2B':
                hs_algo = BLAKE2B
                BLAKE2B.update(data)
            else:
                pass

        print(f" Hash with {algo} for {file} : {hs_algo.hexdigest()}")


def text_algo_choice_hash(text):
    h = [
        inquirer.List("algo_inp", message="Which algorithm you wanna use  ?", choices=[
                      "MD5", "SHA1", "BLAKE2B", "exit"])
    ]

    algo_inp = inquirer.prompt(h, theme=GreenPassion())
    algo = algo_inp['algo_inp']
    if algo == 'MD5':
        hs_algo = MD5
        MD5.update(text)
    elif algo == 'SHA1':
        hs_algo = SHA1
        SHA1.update(text)
    elif algo == 'BLAKE2B':
        hs_algo = BLAKE2B
        BLAKE2B.update(text)
    else:
        pass
    text = str(text).split("b", 1)[-1].split("'")[1]
    print(f" Hash with {algo} for {text} : {hs_algo.hexdigest()}")


def file_algo_choice(filepath):
    clrscr()
    h = [
        inquirer.List("algo_inp", message="Which algorithm you wanna use  ?", choices=[
                      "MD5", "SHA1", "BLAKE2B", "exit"])
    ]

    algo_inp = inquirer.prompt(h, theme=GreenPassion())
    clrscr()
    ch = algo_inp['algo_inp']
    if ch == 'MD5':
        file_hasher(filepath, ch)
    elif ch == 'SHA1':
        file_hasher(filepath, ch)
    elif ch == 'BLAKE2B':
        file_hasher(filepath, ch)
    else:
        exit()


def hasher():
    clrscr()
    a = [
        inquirer.List("hash_inp", message="What you wanna hash ?", choices=[
                      "text", "file", "exit"])
    ]

    hash_inp = inquirer.prompt(a, theme=GreenPassion())
    clrscr()
    if hash_inp['hash_inp'] == "text":
        text = bytes(inquirer.text(message="Input the text "), 'utf-8')
        text_algo_choice_hash(text)

    elif hash_inp['hash_inp'] == "file":
        filepath = inquirer.text(message=r"Input the files location ")
        cheak = os.path.isfile(filepath)
        if cheak == False:
            sys.exit("File not found")
        file_algo_choice(filepath)
