import hashlib
password = "admin123"

new_pass = hashlib.sha1(password.encode()).hexdigest()

print(new_pass)