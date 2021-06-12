from Token import Token
from File  import File, FileIterator

class LexerIterator:
    def __init__(self, lexer):
        self.lexer = lexer
        self.value = None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.lexer)
    
    def Current(self):
        if self.value is None:
            return self.Next()
        if isinstance(self.value, StopIteration):
            raise self.value
        return self.value
    
    def Next(self):
        try:
            self.value = next(self)
        except StopIteration as e:
            self.value = e
        return self.value

class Lexer:
    def __init__(self, file):
        self.file   = iter(file)
        self.line   = 1
        self.column = 0
    
    def __iter__(self):
        return LexerIterator(self)
    
    def __next__(self):
        while(True):
            line   = self.file.line
            column = self.file.column
            
            char = self.file.Current()
            if char is None:
                raise StopIteration()

            if char.isalpha() or char == "_":
                string = self.TokenizeID("")
                
                if string == "function":
                    return Token("keyword", "function", line, column)
                if string == "begin":
                    return Token("keyword", "begin", line, column)
                if string == "end":
                    return Token("keyword", "end", line, column)
                return Token("ID", string, line, column)
            
            if char.isdigit():       
                string = self.TokenizeNumber("")
                return Token("Number", string, line, column)
            
            if char == '"':
                string = self.TokenizeString("")
                return Token("String", string, line, column)                
            
            if char == "/":
                char = self.file.Next()
                if char == "/":
                    while char != '\n':
                        char = self.file.Next()
            
            if char == ",":
                self.file.Next()
                type = Token.GetType(',')
                return Token(type, None, line, column)
            if char == ":":
                self.file.Next()
                type = Token.GetType(':')
                return Token(type, None, line, column)
            if char == ";":
                self.file.Next()
                type = Token.GetType(';') 
                return Token("Semicolon", None, line, column)
            if char == "(":
                self.file.Next()
                type = Token.GetType('(')
                return Token("LParent", None, line, column)
            if char == ")":
                self.file.Next()
                type = Token.GetType(')')
                return Token("RParent", None, line, column)
            if char == "{":
                self.file.Next()
                type = Token.GetType('{')
                return Token("LBrace", None, line, column)                
            if char == "}":
                self.file.Next()
                type = Token.GetType('}')
                return Token("RBrace", None, line, column)                
            
            
            if char.isspace():
                self.file.Next()
                continue
            
            raise RuntimeError(f"'{char}'")

    def TokenizeString(self, string):
        self.file.Next() # skip "
        
        while(True):
            char = self.file.Current()
            if (char is None):
                raise RuntimeError("eof reached before \"")
            if (char == '\n'):
                raise RuntimeError("eol reached before \"")
            if (char == '"'):
                self.file.Next()
                return string
            
            string += char
            self.file.Next()
        return string        

    def TokenizeID(self, string):
        while(True):
            char = self.file.Current()
            if (char is None):
                break
            
            if char.isalnum() or char == "_":
                string += char
                self.file.Next()
                continue
            
            break
        return string
    
    def TokenizeNumber(self, string):
        while(True):
            char = self.file.Current()
            if (char is None):
                break
            
            if char.isdigit():
                string += char
                self.file.Next()
                continue
            
            break
        return string        
    

if __name__ == "__main__":
    file  = File ("code.txt")
    lexer = Lexer(file)
    
    while(True):
        token = next(lexer)
        print(token)