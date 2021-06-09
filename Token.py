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