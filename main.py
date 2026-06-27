import random
import string
from cryptography.fernet import Fernet

# Load encryption key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)


# ---------------- FUNCTIONS ---------------- #

def generate_password():
    charValues = string.ascii_letters + string.digits + string.punctuation
    password = ""
    pass_len = 12

    for i in range(pass_len):
        password += random.choice(charValues)

    return password


def save_password(website, encrypted_password):
    with open("password_memo.txt", "a") as file:
        file.write(f"{website} : {encrypted_password}\n")


def view_password():
    website = input("Enter website name: ")

    try:
        with open("password_memo.txt", "r") as file:
            for line in file:
                site, encrypted = line.strip().split(" : ")

                if site == website:
                    decrypted = cipher.decrypt(encrypted.encode()).decode()
                    print("Password:", decrypted)
                    return

        print("Website not found!")

    except FileNotFoundError:
        print("No saved passwords yet!")


# ---------------- MENU ---------------- #

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Generate Password")
    print("2. View Password")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        website = input("Enter website name: ")

        password = generate_password()
        print("Generated Password:", password)

        encrypted = cipher.encrypt(password.encode()).decode()
        save_password(website, encrypted)

        print("Saved successfully!")

    elif choice == "2":
        view_password()

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")