class PFunction:
    def __init__(self, name, fn):
        if (fn.__name__.lower() != name.lower()):
            raise RuntimeError("bad function name")
        #for prop in dir(fn):
        #    print(prop)
        #    print(getattr(fn, prop))
        self.name = name
        self.code = fn
    
    def __call__(self, state, args):
        return self.code(state, args)
    
    def __repr__(self):
        return ""

class LFunction:
    def __init__(self, context, name):
        self.context   = context
        self.name      = name
        self.code      = []
        self.labels    = dict()
    
    def __getitem__(self, key):
        print(self.labels)
        value = self.labels.get(key, None)
        if (value is not None):
            return value
        
        print(self.context)
        value = self.context.get(key, None)
        if (value is not None):
            return value
        
        raise KeyError(f"can not find {key} inside function {self.name}")
    
    def __setitem__(self, key, value):
        if (isinstance(value, Label)):
            self.labels[key] = value
        
        raise TypeError(f"type of value should be Label inside {self.name}")
    
    def __repr__(self):
        return self.name
        