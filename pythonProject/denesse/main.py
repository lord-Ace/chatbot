def repeat(message):
    return "i  can hear you! You said '{}'".format(message)


bot_msg = "BOT: "


def response(message):
    bot = bot_msg + repeat(message)
    return bot


j = input('USER: ')
print(response(j))
