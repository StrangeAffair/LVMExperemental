class Label:
    def __init__(self, name, data=None):
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "data", data)
    
    def __setattr__(self, name, value):
        if (name == "data"):
            if self.data is not None:
                raise RuntimeError(f"overwriting of data {self}")
    
        object.__setattr__(self, name, value)
    
    def __str__(self):
        return f"(name = {self.name}, data = {self.data})"
        
    def __repr__(self):
        return str(self)