# mystring = "111sss"
# check= any(not c.isalnum() for c in mystring)
# if check:
#     print('có chứa ký tự đb')


# import bcrypt 
# pwd = '123456'
# bytePwd = pwd.encode('utf-8')
# mySalt = bcrypt.gensalt()
# pwd_hash = bcrypt.hashpw(bytePwd, mySalt)
# pwd_hash1 = bcrypt.hashpw(bytePwd, mySalt)
# print(pwd_hash.decode('utf-8'))
# print(pwd_hash1.decode('utf-8'))

import bcrypt
  
# example password
password = '1234'
  
# converting password to array of bytes
bytes = password.encode('utf-8')
  
# generating the salt
salt = bcrypt.gensalt()
  
# Hashing the password
hash = bcrypt.hashpw(bytes, salt)
  
# Taking user entered password 
userPassword =  '1234'
  
# encoding user password
userBytes = userPassword.encode('utf-8')
  
# checking password
result = bcrypt.checkpw(userBytes, hash)
  
print(result)
print(hash)