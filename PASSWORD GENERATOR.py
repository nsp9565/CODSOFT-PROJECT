#PASSWORD GENERATOR



import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return ""

    
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
   
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")


main()

