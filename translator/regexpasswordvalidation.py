# password at least 8 char long
# contain any letters, numbers and special characters
import re

password = input("Enter password: ")
pattern1 = r'[A-Za-z0-9@#$%^&+=]{8,}'
pattern2 = r'[A-Za-z0-9@#$%^&+=]{8,}.*[0-9]$'

if re.fullmatch(pattern2, password):
    print("valid password option")
else:
    print("Enter valid a password containing at least 8 char and any letters, special characters and numbers. It should end with a number")

