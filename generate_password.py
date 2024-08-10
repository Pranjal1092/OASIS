import random
import string
import argparse

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Define character sets
    letters = string.ascii_letters if use_letters else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine selected character sets
    all_characters = letters + numbers + symbols
    
    if not all_characters:
        return "Error: No character set selected"
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("--no-letters", action="store_false", dest="use_letters", help="Exclude letters")
    parser.add_argument("--no-numbers", action="store_false", dest="use_numbers", help="Exclude numbers")
    parser.add_argument("--no-symbols", action="store_false", dest="use_symbols", help="Exclude symbols")
    
    args = parser.parse_args()
    
    password = generate_password(args.length, args.use_letters, args.use_numbers, args.use_symbols)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()