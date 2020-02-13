import re
admin_pw = re.compile('^.*password.+$', re.MULTILINE)

def main():
 with open ('config.txt', 'r+') as f:
    scrubbed = []
    for line in f.readlines():
        if re.match(admin_pw, line):
            continue
        scrubbed.append(line)
    print("".join(scrubbed))
if __name__ == "__main__": main()




    # contents = f.read()
    # passwords = admin_pw.finditer(contents)
    # for match in passwords:
    #  print(match)
