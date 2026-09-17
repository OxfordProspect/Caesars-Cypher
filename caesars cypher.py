alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def get_valid_mode():
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ").lower().strip()
        if mode in ["e", "d"]:
            return mode
        print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")


def get_valid_shift():
    while True:
        shift_input = input("Enter the shift number: \n").strip()
        try:
            return int(shift_input) % 26
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def caesar(start_text, shift_amount, mode):
    end_text = ""
    if mode == "d":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            newpos = (position + shift_amount) % 26
            end_text += alphabet[newpos]
        else:
            end_text += char

    action_label = "encrypted" if mode == "e" else "decrypted"
    print(f"Here's the {action_label} result: {end_text}")

    redo = input("Would you like to try again? (y/n) ").lower().strip()
    if redo == "y":
        mode = get_valid_mode()
        text = input("Enter your message: \n").lower()
        shift = get_valid_shift()
        caesar(start_text=text, shift_amount=shift, mode=mode)
    else:
        print("Thanks for playing.")


mode = get_valid_mode()
text = input("Enter your message: \n").lower()
shift = get_valid_shift()

caesar(start_text=text, shift_amount=shift, mode=mode)