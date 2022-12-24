mystring = "111sss"
check= any(not c.isalnum() for c in mystring)
if check:
    print('có chứa ký tự đb')
