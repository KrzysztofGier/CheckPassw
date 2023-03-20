from abc import ABC, abstractmethod
    

class Validator(ABC):
    @abstractmethod
    def __init__(self,text):
        


class HasNumberValidator(Validator):
    def __init__(self,text):
        self.text=text
    def is_valid(self):
        for n in range(0,10):
            if str(n) in self.text:
                return True
        return False
class HasSpecialCharactersValidator(Validator):
    def __init__(self,text):
        self.text=text
    def is_valid(self):
class HasUpperCharacterValidator(Validator):
    def __init__(self,text):
        self.text=text
    def is_valid(self):
class HaveIbeenPwndValidator(Validator):
    def __init__(self,text):
        self.text=text
    def is_valid(self):
        


class LengthValidator(Validator):
    def __init__(self,text):
        self.text=text
    def is_valid(self):


class PasswordValidator(Validator):
    def __init__(self, password):
        self.password= password
        self.validators = [
            LengthValidator,
            HasNumberValidator,
            HasSpecialCharactersValidator,
            HasUpperCharacterValidator,
            HasLowerCharacterValidator,
            HaveIbeenPwndValidator
        ]
    def is_valid(self):
        for class_name in self.validators:
            validator = class_name[self.password]
            validator.is_valid()
    

        
validator= PasswordValidator('querty')
print(validator.is_valid())