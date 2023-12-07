from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()


master_password = input("What is your master password? ")

# TODO: Fix this to use the correct method to use the password for the key.
key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.rsplit("|")
            print(f"Name: {user}, Password: {fer.decrypt(password.encode()).decode()}")


def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(password.encode()).decode()}\n")


while True:
    mode = input(
        "Would you like to add a new password, view your existing passwords, or quit? (view/add/q) ").lower().strip()
    if mode == "q":
        quit()

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
