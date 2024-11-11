import os

class Create:
    def __init__(self, encoding_method=None, *args, **kwargs):
        self._class = encoding_method
        self.value = None
        
        if self._class != None:
            self.instance = self._class(*args, **kwargs)

    def modify(self):
        if os.path.exists("data.txt"):
            with open("data.txt", 'r+') as f:
                f_content = f.read()
                if f_content != self.value and self.value != None:
                    f.seek(0)
                    f.write(self.value)
                    f.truncate()
                else:
                    print(f_content)
        else:
            with open('data.txt', 'w') as f:
                f.write(self.value)
                
    def run(self):
        if self._class != None:
            self.value = self.instance.run()
        self.modify()
