import random
import string


def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    try:
        # Get user input for password length
        length = int(input("Enter the desired length of the password: "))

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")


main()
