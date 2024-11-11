import os

class Create:
    def __init__(self):
        self.value = "Create a new text file"

    def run(self):
        if os.path.exists("data.txt"):
            with open("data.txt", 'r') as f:
                f = f.read()
                print(f)
        else:
            with open('data.txt', 'w') as f:
                f.write(self.value)
                
Create().run()