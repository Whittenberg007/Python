import string
import secrets

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

# Generate a 12-character random password
password = generate_password(12)
print(password)
