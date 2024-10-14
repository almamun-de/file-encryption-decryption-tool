from cryptography.fernet import Fernet

# Function to generate and save a key
def generate_key():
    """
    Generates a new encryption key and saves it to 'secret.key'.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'secret.key'.")

# Function to load the key from a file
def load_key():
    """
    Loads the encryption key from the 'secret.key' file.
    """
    return open("secret.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_name, key):
    """
    Encrypts a file using the provided key.
    
    :param file_name: The name of the file to encrypt.
    :param key: The encryption key.
    """
    f = Fernet(key)
    
    with open(file_name, "rb") as file:
        file_data = file.read()
    
    encrypted_data = f.encrypt(file_data)
    
    with open(file_name + ".enc", "wb") as file:
        file.write(encrypted_data)
    
    print(f"File '{file_name}' encrypted successfully!")

# Function to decrypt a file
def decrypt_file(file_name, key):
    """
    Decrypts an encrypted file using the provided key.
    
    :param file_name: The name of the encrypted file to decrypt.
    :param key: The encryption key.
    """
    f = Fernet(key)
    
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = f.decrypt(encrypted_data)
    
    with open(file_name.replace(".enc", ""), "wb") as file:
        file.write(decrypted_data)
    
    print(f"File '{file_name}' decrypted successfully!")

if __name__ == "__main__":
    print("1. Generate a new key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    
    choice = input("Choose an option (1/2/3): ")
    
    if choice == "1":
        generate_key()
    
    elif choice == "2":
        key = load_key()
        file_name = input("Enter the name of the file to encrypt: ")
        encrypt_file(file_name, key)
    
    elif choice == "3":
        key = load_key()
        file_name = input("Enter the name of the file to decrypt (must have .enc extension): ")
        decrypt_file(file_name, key)
    
    else:
        print("Invalid choice!")
