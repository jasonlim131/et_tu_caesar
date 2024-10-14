def encrypt_text(plaintext, n, direction='forward'):
    ans = ""
    # Adjust the shift direction (negative shift for 'backward')
    shift = n if direction == 'forward' else -n

    for i in range(len(plaintext)):
        ch = plaintext[i]

        # Maintain spaces as they are
        if ch == " ":
            ans += " "
        # Encrypt uppercase characters
        elif ch.isupper():
            ans += chr((ord(ch) - 65 + shift) % 26 + 65)
        # Encrypt lowercase characters
        else:
            ans += chr((ord(ch) - 97 + shift) % 26 + 97)

    return ans


def generate_caesar_dataset(plaintext, size=5):
    dataset = []

    shift_range = min(size, 4)  # Limit shift range to max 4
    for shift in range(1, shift_range + 1):
        # Generate forward and backward ciphers
        forward_cipher = encrypt_text(plaintext, shift, 'forward')
        backward_cipher = encrypt_text(plaintext, shift, 'backward')

        # Append the results to the dataset
        dataset.append({
            'shift': shift,
            'direction': 'forward',
            'plaintext': plaintext,
            'ciphertext': forward_cipher
        })
        dataset.append({
            'shift': shift,
            'direction': 'backward',
            'plaintext': plaintext,
            'ciphertext': backward_cipher
        })

    # Truncate the dataset to requested size
    return dataset[:size]


# Example usage: Generate a size 5 dataset
plaintext = "HELLO EVERYONE"
dataset = generate_caesar_dataset(plaintext, size=5)

import pandas as pd
df = pd.DataFrame(dataset)
import ace_tools as tools; tools.display_dataframe_to_user(name="Caesar Cipher Dataset")

df
