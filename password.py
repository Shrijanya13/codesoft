import random
import string

def generate_password(length):
    # Define the character set: lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    # Get the desired length from the user
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length should be at least 1.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()

