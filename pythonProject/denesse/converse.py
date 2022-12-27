import re

pall = "do you know .*"
lime = input("BOT: ")
loop = re.search(pall, lime)
if loop:
    print("yaay")
