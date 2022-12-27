def mini_chat(question):
    still = question.split(' ')
    replies = {
        "what's your name": [
            "they call me denesse. denesse roboto",
            "hi i'm denesse",
            "you can call me denesse"
        ],
        "how you doing": [
            "doing good",
            "happier than ever",
            "dunno how do you want me to feel"
        ],
        "are you useful": [
            "yeah",
            "of course yes",
            "what would be my use if not usefulness"
        ]
    }
    pro_replies = {
        "what's your name": [
            "how about you. What's your name",
            "now you know my name, may i know yours",
            "and you are?"
        ],
        "how you doing": [
            "how about you, how you doing",
            "How you doing",
            "how about you"
        ],
    }
    bot_basis = 'BOT: {}'
    greeting = ["hello", "hi", "goodday", "sup", "wassup", "yollo"]
    unknown = ["why do you think that", "tell me more", "is that so", "why do you say that"]
    greeting_message = ["how you doing", "how can i be of help to you", "what service can i offer you",
                        "what's popping", "of what do i owe this pleasant visit", "wanna chat",
                        "what do you want to do today", "how's your day going"]
    import random
    import time
    for word in still:
        output = replies.get(word, question)
        if output in replies:
            oppo = random.choice(replies[output])
            time.sleep(0.5)
            return bot_basis.format(oppo)
        elif word in greeting:
            reply = [bot_basis.format(random.choice(greeting)), bot_basis.format(word + " to you too")]
            time.sleep(0.5)
            return random.choice(reply)
    time.sleep(0.5)
    return bot_basis.format(random.choice(unknown))


while True:
    msg = input('USER: ').lower()
    print(mini_chat(msg))
