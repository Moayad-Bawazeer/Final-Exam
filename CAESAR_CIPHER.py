def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char.isalpha():
            switch = 65 if char.isupper() else 97
            # Encrypt or decrypt based on the mode ('e' for encrypt, 'd' for decrypt)
            result += chr((ord(char) - switch + key) % 26 + switch) if mode == 'e' else chr(
                (ord(char) - switch - key) % 26 + switch)
        else:
            result += char
    return result


def main():
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    ans = input("> ").lower()

    if ans == 'e' or ans == 'd':
        print("Please enter the key (0 to 25) to use.")
        key = int(input("> "))

        if 0 <= key <= 25:
            print("Enter the message to encrypt." if ans == 'e' else "Enter the message to decrypt.")
            message = input("> ")

            result = caesar_cipher(message, key, ans)
            print(result)

            print(f"Full {'encrypted' if ans == 'e' else 'decrypted'} text copied to clipboard.")
        else:
            print("Invalid key. Key must be between 0 and 25.")
    else:
        print("Invalid ans. Please enter 'e' for encrypt or 'd' for decrypt.")


if __name__ == "__main__":
    main()
