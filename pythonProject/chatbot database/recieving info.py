class InputProcessOutput:
    def __init__(self, value: str):
        self.value = value

    def face(self):
        self.value = self.value.lower()
        user_info = self.value.split(' ')
        return user_info


while True:
    poop = input("user: ")
    dial = InputProcessOutput(value=poop)
    print(dial.face())


