import re

admin_pw = re.compile(r'(password).+')

#Validate encoding if necessary or not. 
with open ('config.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

    passwords = admin_pw.finditer(contents)

    for match in passwords:
        print(match)
