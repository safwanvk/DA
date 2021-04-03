import re

fh = open(r"/home/safwan/Documents/projects/python/Data Analysis/regex/mail.txt", "r").read()

# for line in fh.split("n"):
#     if "From:" in line:
#         print(line)


for line in re.findall("From:.*", fh):
    print(line)

for line in re.findall("From:.", fh):
    print(line)


match = re.findall("From:.*", fh)

for line in match:
    print(re.findall('\".*\"', line))

# first occurence
math = re.search("From:.*", fh)

math = re.split("\s", fh)

# replace
math = re.sub("\s", "9", fh)