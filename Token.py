class Token:
    def __init__(self, type, data=None, line=None, column=None):
        self.type   = type
        self.data   = data
        self.line   = line
        self.column = column
    
    def __str__(self):
        return f"{self.line}.{self.column}: ({self.type}, {self.data})"

    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        if type(other) == str:
            if len(other) == 1:
                return self.type == Token.GetType(other)
            else:
                return self.data == other
    
    def __ne__(self, other):
        return not (self == other)
    
    def __le__(self, other):
        raise RuntimeError("not <= comparable")
        
    def __ge__(self, other):
        raise RuntimeError("not >= comparable")
    
    def __lt__(self, other):
        raise RuntimeError("not < comparable")
    
    def __gt__(self, other):
        raise RuntimeError("not > comparable")
    
    @staticmethod
    def GetType(string):
        if (string == ','):
            return "Comma"
        if (string == ':'):
            return "Colon"
        if (string == ';'):
            return "Semicolon"
        
        if (string == '('):
            return "LParent"
        if (string == ')'):
            return "RParent"
        
        if (string == "{"):
            return "LBrace"
        if (string == "}"):
            return "RBrace"
        
        raise RuntimeError(f"bad string arg = {string} for Token.GetType")