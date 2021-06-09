from Function import PFunction, LFunction

class Command:
    def __init__(self, fn=None, args=None):
        object.__setattr__(self, "fn",   None)
        object.__setattr__(self, "args", None)
    
    def __getattribute__(self, name):
        if (name == "fn"):
            return object.__getattribute__(self, name)
        
        if (name == "args"):
            return object.__getattribute__(self, name)
        
        raise AttributeError(f"{name} attribute is not supported for Command")
    
    def __setattr__(self, name, value):
        if (name == "fn"):
            if isinstance(value, PFunction):
                object.__setattr__(self, name, value)
                return
            if isinstance(value, LFunction):
                object.__setattr__(self, name, value)
                return
            if value is None:
                object.__setattr__(self, name, value)
                return            
            raise TypeError(f"{value} attribute should be PFunction or LFunction")
        
        if (name == "args"):
            if (type(value) != list):
                raise TypeError(f"{value} attribute should be list")
            object.__setattr__(self, name, value)
            return
        
        raise AttributeError(f"{name} attribute is not supported for Command")
    
    def __str__(self):
        if self.fn is not None:
            return f"{self.fn.name} {self.args}"
        else:
            return f"<fn = None> {self.args}"
            
    def __repr__(self):
        return str(self)
    
    def check(self):
        if (self.fn is None):
            raise RuntimeError("fn is not set")
        if (self.args is None):
            raise RuntimeError("args is not set")