class Encode:
    def __init__(self, str):
        self.str = str

    def run(self):
        return "".join([ord(letter) for letter in self.str])
    
class Decode:
    def __init__(self, str):
        self.str = str
        self.i = 0
        self.decoded = ""

    def run(self):
        if self.i + 2 < len(self.str) and 32 <= int(self.str[self.i:self.i+3]) <= 126:
            self.decoded += chr(int(self.str[self.i:self.i+3]))
            self.i += 3
        elif self.i + 1 < len(self.str) and 32 <= int(self.str[self.i:self.i+2]) <= 126:
            self.decoded += chr(int(self.str[self.i:self.i+2]))
            self.i += 2
        else:
            raise ValueError("La chaîne de caractères donnée est invalide...")
        
        return self.decoded