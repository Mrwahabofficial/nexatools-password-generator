import random
import string
import os
import sys

def print_banner():
    print("=" * 55)
    print("   NexaTools Password Generator Pro")
    print("   Generate strong secure passwords instantly")
    print("=" * 55)
    print()

def check_strength(password):
    score = 0
    if len(password) >= 8:  score += 1
    if len(password) >= 12: score += 1
    if len(password) >= 16: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 3:   return "WEAK", "!"
    elif score <= 5: return "MEDIUM", "~"
    else:            return "STRONG", "✓"

def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_chars=""):
    chars = ""
    if use_upper:   chars += string.ascii_uppercase
    if use_lower:   chars += string.ascii_lowercase
    if use_digits:  chars += string.digits
    if use_symbols: chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    for ch in exclude_chars:
        chars = chars.replace(ch, "")

    if not chars:
        print("Error: Select at least one character type!")
        return None

    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        has_upper  = any(c.isupper() for c in password) if use_upper else True
        has_lower  = any(c.islower() for c in password) if use_lower else True
        has_digit  = any(c.isdigit() for c in password) if use_digits else True
        has_symbol = any(c in string.punctuation for c in password) if use_symbols else True
        if has_upper and has_lower and has_digit and has_symbol:
            return password

def save_passwords(passwords, filename="generated_passwords.txt"):
    with open(filename, 'w') as f:
        f.write("=" * 55 + "\n")
        f.write("   NexaTools Password Generator Pro\n")
        f.write("   Generated Passwords\n")
        f.write("=" * 55 + "\n\n")
        for i, pwd in enumerate(passwords, 1):
            strength, icon = check_strength(pwd)
            f.write(f"{i}. {pwd}  [{icon} {strength}]\n")
        f.write(f"\nTotal: {len(passwords)} passwords\n")
        f.write("Keep this file safe!\n")
    return filename

def main():
    print_banner()

    print("Options:")
    print("  1. Generate passwords")
    print("  2. Check password strength")
    print()

    choice = input("Enter choice (1/2): ").strip()

    if choice == "2":
        pwd = input("\nEnter password to check: ").strip()
        strength, icon = check_strength(pwd)
        print(f"\n  Password : {pwd}")
        print(f"  Length   : {len(pwd)} characters")
        print(f"  Strength : {icon} {strength}")
        print()
        input("Press Enter to exit...")
        return

    print("\nPassword Settings:")
    
    try:
        length = int(input("  Password length (8-64): ").strip())
        if length < 8:  length = 8
        if length > 64: length = 64
    except:
        length = 16

    try:
        count = int(input("  How many passwords (1-50): ").strip())
        if count < 1:  count = 1
        if count > 50: count = 50
    except:
        count = 5

    print("\n  Character types:")
    use_upper   = input("  Include UPPERCASE? (y/n): ").strip().lower() != 'n'
    use_lower   = input("  Include lowercase? (y/n): ").strip().lower() != 'n'
    use_digits  = input("  Include numbers? (y/n): ").strip().lower() != 'n'
    use_symbols = input("  Include symbols? (y/n): ").strip().lower() != 'n'
    exclude     = input("  Exclude characters (or press Enter to skip): ").strip()

    print(f"\n  Generating {count} password(s)...\n")
    print("=" * 55)

    passwords = []
    for i in range(count):
        pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude)
        if pwd:
            strength, icon = check_strength(pwd)
            print(f"  {i+1:2}. {pwd}  [{icon} {strength}]")
            passwords.append(pwd)

    print("=" * 55)

    if passwords:
        save_choice = input("\n  Save passwords to file? (y/n): ").strip().lower()
        if save_choice == 'y':
            filename = save_passwords(passwords)
            print(f"\n  Saved to: {filename}")
            print("  Keep this file safe!")

    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
