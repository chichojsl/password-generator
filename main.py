import random
import string

def generate_password(length):
    # Combine letters, numbers, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # Choose random characters based on the desired length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("--- Secure Password Generator ---")
try:
    user_length = int(input("Enter the desired password length (e.g., 12): "))
    new_password = generate_password(user_length)
    print(f"Your new password is: {new_password}")
except ValueError:
    print("Error: Please enter a valid number.")
