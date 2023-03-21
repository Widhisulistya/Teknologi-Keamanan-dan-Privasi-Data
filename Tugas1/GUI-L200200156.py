from tkinter import *
import numpy as np

# Shift Cipher


def shift_encrypt(message, key):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result += char
    return result


def shift_decrypt(message, key):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char
    return result


# Vigenere Cipher


def vigenere_encrypt(message, key):
    result = ""
    key_index = 0
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) +
                          ord(key[key_index].upper()) - 130) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        elif char.islower():
            result += chr((ord(char) +
                          ord(key[key_index].lower()) - 194) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result


def vigenere_decrypt(message, key):
    result = ""
    key_index = 0
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) -
                          ord(key[key_index].upper()) + 26) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        elif char.islower():
            result += chr((ord(char) -
                          ord(key[key_index].lower()) + 26) % 26 + 97)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

# Substitution Cipher


def substitution_encrypt(message, key):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += key[ord(char)-65].upper()
        elif char.islower():
            result += key[ord(char)-97].lower()
        else:
            result += char
    return result


def substitution_decrypt(message, key):
    result = ""
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr(key.index(char.lower()) + 65).upper()
        elif char.islower():
            result += chr(key.index(char.lower()) + 97).lower()
        else:
            result += char
    return result

# Transposition Cipher


def transposition_encrypt(message, key):
    result = ""
    num_columns = len(key)
    num_rows = int(np.ceil(len(message) / num_columns))
    pad_size = num_rows * num_columns - len(message)
    message += " " * pad_size
    matrix = np.array(list(message)).reshape(num_rows, num_columns)
    sorted_columns = np.argsort(list(key))
    for column in sorted_columns:
        result += "".join(matrix[:, column])
    return result.replace(" ", "")


def transposition_decrypt(message, key):
    result = ""
    num_columns = len(key)
    num_rows = int(np.ceil(len(message) / num_columns))
    matrix = np.zeros((num_rows, num_columns))
    pad_size = num_rows * num_columns - len(message)
    message += " " * pad_size
    sorted_key = sorted(list(key))
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][sorted_key.index(key[j])] = ord(message[i*num_columns+j])
    result = "".join([chr(int(i)) for i in matrix.flatten()])
    return result.replace(" ", "")

# Create GUI


def shift_cipher():
    def shift_encrypt_message():
        result = shift_encrypt(input_text.get("1.0", END), int(key.get()))
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)

    def shift_decrypt_message():
        result = shift_decrypt(input_text.get("1.0", END), int(key.get()))
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)

    top = Toplevel()
    top.title("Shift Cipher")

    input_label = Label(top, text="Input:")
    input_label.grid(row=0, column=0, sticky=W)

    input_text = Text(top, width=50, height=5)
    input_text.grid(row=1, column=0, columnspan=2)

    key_label = Label(top, text="Key:")
    key_label.grid(row=2, column=0, sticky=W)

    key = Entry(top)
    key.grid(row=3, column=0)

    encrypt_button = Button(top, text="Encrypt", command=shift_encrypt_message)
    encrypt_button.grid(row=4, column=0)

    decrypt_button = Button(top, text="Decrypt", command=shift_decrypt_message)
    decrypt_button.grid(row=4, column=1)

    output_label = Label(top, text="Output:")
    output_label.grid(row=5, column=0, sticky=W)

    output_text = Text(top, width=50, height=5)
    output_text.grid(row=6, column=0, columnspan=2)


def vigenere_cipher():
    def vigenere_encrypt_message():
        result = vigenere_encrypt(input_text.get("1.0", END), key.get())
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)

    def vigenere_decrypt_message():
        result = vigenere_decrypt(input_text.get("1.0", END), key.get())
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)

    top = Toplevel()
    top.title("Vigenere Cipher")

    input_label = Label(top, text="Input:")
    input_label.grid(row=0, column=0, sticky=W)

    input_text = Text(top, width=50, height=5)
    input_text.grid(row=1, column=0, columnspan=2)

    key_label = Label(top, text="Key:")
    key_label.grid(row=2, column=0, sticky=W)

    key = Entry(top)
    key.grid(row=3, column=0)

    encrypt_button = Button(top, text="Encrypt",
                            command=vigenere_encrypt_message)
    encrypt_button.grid(row=4, column=0)

    decrypt_button = Button(top, text="Decrypt",
                            command=vigenere_decrypt_message)
    decrypt_button.grid(row=4, column=1)

    output_label = Label(top, text="Output:")
    output_label.grid(row=5, column=0, sticky=W)

    output_text = Text(top, width=50, height=5)
    output_text.grid(row=6, column=0, columnspan=2)


def substitution_cipher():
    def substitution_encrypt_message():
        result = substitution_encrypt(input_text.get("1.0", END), key.get())
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)

    def substitution_decrypt_message():
        result = substitution_decrypt(input_text.get("1.0", END), key.get())
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)

    top = Toplevel()
    top.title("Substitution Cipher")

    input_label = Label(top, text="Input:")
    input_label.grid(row=0, column=0, sticky=W)

    input_text = Text(top, width=50, height=5)
    input_text.grid(row=1, column=0, columnspan=2)

    key_label = Label(top, text="Key:")
    key_label.grid(row=2, column=0, sticky=W)

    key = Entry(top)
    key.grid(row=3, column=0)

    encrypt_button = Button(top, text="Encrypt",
                            command=substitution_encrypt_message)
    encrypt_button.grid(row=4, column=0)

    decrypt_button = Button(top, text="Decrypt",
                            command=substitution_decrypt_message)
    decrypt_button.grid(row=4, column=1)

    output_label = Label(top, text="Output:")
    output_label.grid(row=5, column=0, sticky=W)

    output_text = Text(top, width=50, height=5)
    output_text.grid(row=6, column=0, columnspan=2)


def transposition_cipher():
    def transposition_encrypt_message():
        result = transposition_encrypt(input_text.get("1.0", END), key.get())
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)

    def transposition_decrypt_message():
        result = transposition_decrypt(input_text.get("1.0", END), key.get())
        output_text.delete("1.0", END)
        output_text.insert("1.0", result)

    top = Toplevel()
    top.title("Transposition Cipher")

    input_label = Label(top, text="Input:")
    input_label.grid(row=0, column=0, sticky=W)

    input_text = Text(top, width=50, height=5)
    input_text.grid(row=1, column=0, columnspan=2)

    key_label = Label(top, text="Key:")
    key_label.grid(row=2, column=0, sticky=W)

    key = Entry(top)
    key.grid(row=3, column=0)

    encrypt_button = Button(top, text="Encrypt",
                            command=transposition_encrypt_message)
    encrypt_button.grid(row=4, column=0)

    decrypt_button = Button(top, text="Decrypt",
                            command=transposition_decrypt_message)
    decrypt_button.grid(row=4, column=1)

    output_label = Label(top, text="Output:")
    output_label.grid(row=5, column=0, sticky=W)

    output_text = Text(top, width=50, height=5)
    output_text.grid(row=6, column=0, columnspan=2)


# Main window
root = Tk()
root.title("Cipher Tool")

# Buttons
shift_button = Button(root, text="Shift Cipher", command=shift_cipher)
shift_button.pack(pady=5)

vigenere_button = Button(root, text="Vigenere Cipher", command=vigenere_cipher)
vigenere_button.pack(pady=5)

substitution_button = Button(
    root, text="Substitution Cipher", command=substitution_cipher)
substitution_button.pack(pady=5)

transposition_button = Button(
    root, text="Transposition Cipher", command=transposition_cipher)
transposition_button.pack(pady=5)

exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=5)

# Run the application
root.mainloop()
