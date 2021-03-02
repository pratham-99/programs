import re
str = "Geeks_for geek"
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

if regex.search(str) == None:
    print("accept")
else:
    print("not")