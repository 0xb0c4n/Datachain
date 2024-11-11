import os

class Create:
    def __init__(self):
        self.value = None


    def make(self):
        if os.path.exists("data.txt"):
            pass
        else:
            with open('data.txt', 'w') as f:
                f.write(self.value)
                
    def run(self):
        self.make()

class Write:
    def __init__(self, path, value, encoding_method=None, *args, **kwargs):
        self._class = encoding_method
        self.value = value
        self.file = path

        if self._class != None:
            self.instance = self._class(*args, **kwargs)

    def make(self):
        if os.path.exists(self.file):
            with open(self.file, "r+") as f:
                f.seek(0)
                f.write(self.value)
                f.truncate()
        else:
            raise ValueError("Le fichier n'existe pas")
    
    def run(self):
        if self._class != None:
            self.value = self.instance.run()
        self.make()