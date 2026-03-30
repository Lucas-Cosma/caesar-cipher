# Caesar Cipher Tool
# A command-line tool to encrypt, decrypt, and brute force Caesar cipher messages

# ANSI colour codes for terminal output
RED    = "\033[31m"
YELLOW = "\033[33m"
GREEN  = "\033[32m"
CYAN   = "\033[36m"
BOLD   = "\033[1m"
DIM    = "\033[2m"   # dimmed/greyed out text
RESET  = "\033[0m"   # resets all formatting back to default



def encrypt(message, key):
    # Encrypts a message by shifting each letter forward by the key amount
    result = ""  # start with an empty string to build our encrypted message

    for char in message:  # loop through every character in the message
        if char.isalpha():  # only shift letters, leave spaces/numbers/symbols alone

            if char.isupper():
                # ord('A') = 65, subtract 65 to get 0-25 range
                # add the key (shift), wrap with % 26, then add 65 back
                shifted = (ord(char) - ord('A') + key) % 26 + ord('A')
            else:
                # same logic for lowercase, using 'a' (97) as the base
                shifted = (ord(char) - ord('a') + key) % 26 + ord('a')

            result += chr(shifted)  # chr() converts the number back to a letter
        else:
            result += char  # not a letter, add it unchanged

    return result  # return the full encrypted message



def decrypt(message, key):
    # Decrypts a message by shifting each letter backward by the key amount
    result = ""  # empty string to build our decrypted message

    for char in message:  # loop through every character
        if char.isalpha():  # only shift letters

            if char.isupper():
                # same as encrypt but subtract the key to shift backwards
                # % 26 handles wrapping e.g. A - 3 = X not a negative number
                shifted = (ord(char) - ord('A') - key) % 26 + ord('A')
            else:
                # same for lowercase
                shifted = (ord(char) - ord('a') - key) % 26 + ord('a')

            result += chr(shifted)  # convert number back to letter
        else:
            result += char  # not a letter, leave it unchanged

    return result



def brute_force(message):
    # Tries all 25 possible shift values to crack a message without knowing the key
    # There are only 25 possible keys in a Caesar cipher so we can try them all
    print(f"\n{BOLD}  All possible decryptions:{RESET}")
    print(f"  {'─' * 40}")

    for key in range(1, 26):  # loop through every possible shift value (1 to 25)
        attempt = decrypt(message, key)  # decrypt using the current key
        print(f"  {DIM}Shift {RESET}{CYAN}{key:>2}{RESET}{DIM}:{RESET}  {attempt}")  # :>2 right-aligns the number so output lines up neatly



def validate_key(key_input):
    # Checks that the key is a valid number between 1 and 25
    # Returns the key as an integer if valid, or None if not
    try:
        key = int(key_input)  # int() converts the input string to a number
        if 1 <= key <= 25:    # key must be between 1 and 25
            return key
        else:
            return None
    except ValueError:        # catches the error if the user types letters instead of a number
        return None



def print_header():
    # Prints a decorative header using box-drawing characters
    print(f"\n{BOLD}{CYAN}╔══════════════════════════════════╗")
    print(f"║        CAESAR CIPHER TOOL        ║")
    print(f"╚══════════════════════════════════╝{RESET}")



def main():
    print_header()

    # keep the menu running until the user chooses to exit
    while True:
        # display the menu options
        print(f"\n{BOLD}  What do you want to do?{RESET}")
        print(f"  {CYAN}1.{RESET} Encrypt a message")
        print(f"  {CYAN}2.{RESET} Decrypt a message")
        print(f"  {CYAN}3.{RESET} Brute force a message")
        print(f"  {CYAN}4.{RESET} Exit")

        choice = input(f"\n  {BOLD}Enter choice (1-4):{RESET} ").strip()  # .strip() removes accidental spaces

        if choice == "1":
            message = input(f"\n  {BOLD}Enter message to encrypt:{RESET} ")
            key_input = input(f"  {BOLD}Enter shift key (1-25):{RESET} ")

            key = validate_key(key_input)  # validate the key before using it
            if key is None:
                print(f"\n  {RED}✗  Invalid key — please enter a number between 1 and 25{RESET}")
                continue  # continue skips back to the top of the while loop

            encrypted = encrypt(message, key)
            print(f"\n  {GREEN}✓  Encrypted:{RESET} {BOLD}{encrypted}{RESET}")
            print(f"  {DIM}Shift key used: {key}{RESET}")

        elif choice == "2":
            message = input(f"\n  {BOLD}Enter message to decrypt:{RESET} ")
            key_input = input(f"  {BOLD}Enter shift key (1-25):{RESET} ")

            key = validate_key(key_input)  # validate the key before using it
            if key is None:
                print(f"\n  {RED}✗  Invalid key — please enter a number between 1 and 25{RESET}")
                continue  # skip back to the menu

            decrypted = decrypt(message, key)
            print(f"\n  {GREEN}✓  Decrypted:{RESET} {BOLD}{decrypted}{RESET}")
            print(f"  {DIM}Shift key used: {key}{RESET}")

        elif choice == "3":
            message = input(f"\n  {BOLD}Enter message to brute force:{RESET} ")
            brute_force(message)
            print(f"\n  {DIM}Scan the list above for the message that makes sense{RESET}")

        elif choice == "4":
            print(f"\n  {CYAN}Goodbye!{RESET}\n")
            break  # break exits the while loop, ending the program

        else:
            print(f"\n  {RED}✗  Invalid choice — please enter 1, 2, 3 or 4{RESET}")  # handles anything unexpected



# Only runs main() if this file is executed directly (not imported as a module)
if __name__ == "__main__":
    main()
            

