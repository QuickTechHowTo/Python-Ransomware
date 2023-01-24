from cryptography import fernet

key = fernet.Fernet.generate_key()  # Generates key

with open('Key.key', 'wb') as k:
    k.write(key)                    # Write Key to file
