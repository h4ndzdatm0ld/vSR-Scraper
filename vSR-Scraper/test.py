# import re
# admin_pw = re.compile('^.*password.+$', re.MULTILINE)
#
import re
exit_all = re.compile('Finished.*', re.MULTILINE | re.DOTALL)
def main():
 with open ('SPFDILUP91A-P-AL-7750-01.txt', 'r+', encoding='utf-8') as f:
     contents = f.read()
     EOLine = exit_all.finditer(contents)
     for match in EOLine:
        print(match)
     Scrubbed = re.sub(exit_all, '', contents, re.MULTILINE)
     # print(Scrubbed)


if __name__ == "__main__": main()
#
#
#     # contents = f.read()
#     # passwords = admin_pw.finditer(contents)
#     # for match in passwords:
# #     #  print(match)
# import re
#
# regex = r"# Finished.*"
# file="SPFDILUP91A-P-AL-7750-01.txt"
#
#
# with open (file, 'r+', encoding='utf-8') as f:
# 	contents = f.read()
# 	matches = re.finditer(regex, contents, re.MULTILINE | re.DOTALL)
#
# 	#
# 	# for matchNum, match in enumerate(matches, start=1):
# 	#
# 	#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
# 	#
# 	#     for groupNum in range(0, len(match.groups())):
# 	#         groupNum = groupNum + 1
# 	#
# 	#         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
