class Arg:
    def __init__(self, region, type, data):
        self.region = region
        self.type   = type
        self.data   = data
    
    def __str__(self):
        return f"(region = {self.region}, type = {self.type}, data = {self.data})"
        
    def __repr__(self):
        return str(self)