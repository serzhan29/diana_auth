from django.test import TestCase

from django.contrib.auth.hashers import make_password

from django.contrib.auth.hashers import check_password

from django.contrib.auth.hashers import PBKDF2PasswordHasher

hasher = PBKDF2PasswordHasher()
password = 'mypassword'
salt = 'random_salt'
hashed_password = hasher.encode(password, salt)
print(hashed_password)
