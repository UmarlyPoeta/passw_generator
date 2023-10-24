import random
import string

class Password:
    def __init__(self,characters,numbers,schar):
        self._characters=characters
        self._numbers=numbers
        self._schar=schar
        self.password=""
        
    def __str__(self):
        print("Your password is: {self.password}")
        
    def generate(self):
        for _ in range(self._characters):
            self.password+=random.choice(string.ascii_lowercase.join(string.ascii_uppercase))
        for _ in range(self._numbers):
            self.password+=str(random.choice([i for i in range(10)]))
        for _ in range(self._schar):
            self.password+=random.choice("!@#$%^&*()")
        self.password = ''.join(random.sample(self.password, len(self.password)))
    
    
    @property
    def characters(self):
        return self._characters
    
    @property
    def numbers(self):
        return self._numbers
    
    @property
    def schar(self):
        return self._schar
    
    
    
def main():
    characters=int(input("How many characters:"))
    numbers=int(input("How many characters:"))
    schar=int(input("How many characters:"))
    p=Password(characters,numbers,schar)
    print(p.password)
    p.generate()
    print(p.password)
    

if __name__=="__main__":
    main()