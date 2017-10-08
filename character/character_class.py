class Character:


    def __init__(self):  # class constructur (called at creation time)
        self.name = ""   # the default name is the empty string

    def ask(self):
        while 1: # infinite loop
            name = input("Enter your name Hero: ")
            if name == "":
                print("Ops! Retry")
            else:
                print(f"Hello, {name}")
                break  # this will break the loop

        self.name = name  # assign to self.name the value name
