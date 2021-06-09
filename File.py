class FileIterator:
    def __init__(self, file):
        self.file   = file
        self.value  = None
        self.line   = 1
        self.column = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.value == "\n"):
            self.line   += 1
            self.column =  0
        self.value  =  next(self.file)
        self.column += 1
        return self.value
    
    def Current(self):
        if self.value is None:
            return self.Next()
        else:
            return self.value
        
    def Next(self):
        return next(self)

class File:
    def __init__(self, name):
        with open(name) as file:
            self.content = file.read()
        
        self.iterator = iter(self.content)
    
    def __iter__(self):
        return FileIterator(self)
    
    def __next__(self):
        return next(self.iterator)