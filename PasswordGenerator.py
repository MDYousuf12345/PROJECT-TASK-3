import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Define character pools based on user preferences
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # Ensure the character pool is not empty
    if not char_pool:
        print("Error: No character types selected. Please include at least one type of character.")
        return None

    # Generate a random password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Error: Password length must be greater than zero.")
            return

        # Get user preferences for character types
        use_letters = input("Include letters? (yes/no): ").strip().lower() == "yes"
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

        # Generate the password
        password = generate_password(length, use_letters, use_numbers, use_symbols)

        if password:
            print(f"\nYour generated password is: {password}")

    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
