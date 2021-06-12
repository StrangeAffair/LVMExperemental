from File     import File
from Token    import Token
from Lexer    import Lexer
from Command  import Command
from Label    import Label
from Function import PFunction, LFunction
from Argument import Arg

import Builtins



class Parser:
    def __init__(self, lexer):

def ParseFile(lexer):
    context = dict()
    
    while True:
        try:
            token = lexer.Current()
        except StopIteration:
            break
        
        
        if token == "import":
            pass
        
        if token == "function":
            function = ParseFunction(lexer, context)
            name     = function.name
            
            if name not in context:
                context[name] = function
            else:
                context[name].code   = function.code
                context[name].labels = function.labels

def ParseFunction(lexer, context):
    token = lexer.Current()
    if token != "function":
        raise SyntaxError("function must start with 'function' keyword")
    token = lexer.Next()
    
    token = lexer.Current()
    if (token.type != "ID"):
        raise SyntaxError(f"bad name of function {token.data}")
    name     = token.data
    function = LFunction(context, name)
    token    = lexer.Next()
    

    ParseArgs(function)
    
    token = self.lexer.Next()
    while True:
        token = self.lexer.Current()
        if (token.type == "ID") and (token.data == "labels"):
            self.ParseLabels(fn)
            continue
        if (token.type == "ID") and (token.data == "vars"):
            self.ParseVars(fn)
            continue
        if (token.type == "keyword") and (token.data == "begin"):
            self.ParseCode(fn)
            break
        raise RuntimeError("unrecognized section of function")
    
    return fn

def ParseArgs(function):
    token = self.lexer.Current()
    if (token.type != "LParent"):
        raise RuntimeError("bad call of ParseArgs")
    token = self.lexer.Next()
    
    if not hasattr(function, "args"):
        function.args = dict()
    
    count = 0
    while True:
        token = self.lexer.Current()
        if (token.type == "RParent"):
            break
        
        if count > 0:
            if (token.type != "Comma"):
                raise SyntaxError("expected comma")
            self.lexer.Next()
        
        token = self.lexer.Current()
        if (token.type != "ID"):
            raise SyntaxError("expected type name")
        type  = token.data
        
        token = self.lexer.Next()
        if (token.type != "ID"):
            raise SyntaxError("expected arg name")            
        name  = token.data
        
        function.args[count] = Variable(name, type, None, function.name + ".args")
        function.args[name]  = function.args[count]
        count += 1
        
        self.lexer.Next()
    
    token = self.lexer.Current()
    if (token.type != "RParent"):
        raise RuntimeError("bad end of call of ParseArgs")        
    token = self.lexer.Next()
    

class Parser:
    def __init__(self, lexer):
        self.lexer   = iter(lexer)
        self.context = {
            "move":  PFunction("move",  Builtins.MOVE),
            "const": PFunction("const", Builtins.CONST),
            "store": PFunction("store", Builtins.STORE),
            "load":  PFunction("load",  Builtins.LOAD),
            
            "jump":  PFunction("jump",  Builtins.JUMP),
            "jge":   PFunction("jge",   Builtins.JGE),
            
            "add": PFunction("add", Builtins.ADD),
            "inc": PFunction("inc", Builtins.INC),
            "inc_Int64": PFunction("inc64", Builtins.Inc64),
            "ret": PFunction("ret", Builtins.ret),
        }
    
    def ParseFile(self, context):
        try:
            while True:
                token = self.lexer.Current()
            
                if (token.type == "keyword") and (token.data == "function"):
                    fn = self.ParseFunction(context)
                    if fn.name not in self.context:
                        self.context[fn.name] = fn
                    else:
                        self.context[fn.name].code   = fn.code
                        self.context[fn.name].labels = fn.labels
                
                if (token.type == "keyword") and (token.data == "import"):
                    pass
        except StopIteration as e:
            return self.context
        
    
    def ParseFunction(self, context):
        
    
    def ParseLabels(self, function):
        token = self.lexer.Current()
        if (token.type != "ID") or (token.data != "labels"):
            raise RuntimeError("bad call of ParseLabels")
        
        token = self.lexer.Next()
        if (token.type != "Colon"):
            raise RuntimeError("expected ':' after labels")
        token = self.lexer.Next()
        
        if not hasattr(function, "labels"):
            function.labels = dict()
        
        while True:
            token = self.lexer.Current()  
            if (token.type != "ID"):
                raise SyntaxError("expected label name")
            name  = token.data
            
            function.labels[name] = Label(name, None)
            
            token = self.lexer.Next()
            if (token.type == "Comma"):
                self.lexer.Next()
                continue
            if (token.type == "Semicolon"):
                self.lexer.Next()
                break
        
        return function
    
    
    
    def ParseVars(self, function):
        token = self.lexer.Current()
        if (token.type != "ID") or (token.data != "vars"):
            raise RuntimeError("bad call of ParseVars")
        
        token = self.lexer.Next()
        if (token.type != "Colon"):
            raise RuntimeError("expected ':' after vars")
        token = self.lexer.Next()
        
        if not hasattr(function, "vars"):
            function.vars = dict()
        
        while True:
            token = self.lexer.Current()
            if (token.type == "keyword"):
                break
            if (token.type != "ID"):
                raise SyntaxError("expected type name")
            type  = token.data
            
            while True:
                token = self.lexer.Next()
                if (token.type != "ID"):
                    raise SyntaxError("expected var name")
                name  = token.data
                
                function.vars[name] = Variable(name, type, None, function.name + ".vars")
                
                token = self.lexer.Next()
                if (token.type == "Comma"):
                    token = self.lexer.Next()
                    continue
                if (token.type == "Semicolon"):
                    token = self.lexer.Next()
                    break
        
        return function
    
    def ParseCode(self, function):
        token = self.lexer.Current()
        if (token.type != "keyword") or (token.data != "begin"):
            raise SyntaxError("expected 'begin' keyword")
        token = self.lexer.Next()
        
        while True:
            token = self.lexer.Current()
            if (token.type == "keyword") and (token.data == "end"):
                break
            
            self.ParseCommand(function)
        
        token = self.lexer.Current()
        if (token.type != "keyword") or (token.data != "end"):
            raise SyntaxError("expected 'end' keyword")
        token = self.lexer.Next()
        
    def ParseCommand(self, function):
        token = None
        name  = None
        while(True):
            token = self.lexer.Current()
            if (token.type != "ID"):
                raise RuntimeError(f"expected id {token}")
            name = token.data
            
            token = self.lexer.Next()
            if (token.type == "Colon"):
                if name not in function.labels:
                    raise SyntaxError("label should be defined")
                    #dest = len(function.code)
                    #function.labels[name] = Label(name, dest)
                else:
                    if function.labels[name].data is not None:
                        raise SyntaxError("multiple definition")
                    else:
                        dest = len(function.code)
                        function.labels[name].data = dest 
                self.lexer.Next()
            else:
                break
        
        cmd = Command()
        try:
            cmd.fn   = function.context[name]
        except KeyError:
            function.context[name] = LFunction(function.context, name)
            cmd.fn   = function.context[name]
        cmd.args = self.ParseCommandArgs(function)
        function.code.append(cmd)
        
        token = self.lexer.Current()
        if (token.type != "Semicolon"):
            raise SyntaxError("expected ';' at the end of command " + token)
        self.lexer.Next()
        
    def ParseCommandArgs(self, function):
        retval = []
        while(True):
            token = self.lexer.Current()
            if (token.type == "Semicolon"):
                break
            
            while True:
                if (token.type == "LBrace"):
                    token  = self.lexer.Next()
                    region = None
                    if (token.type == "ID"):
                        region = token.data
                        token = self.lexer.Next()
                        token = self.lexer.Next()
                    
                    token = self.lexer.Current()
                    if (token.type != "String"):
                        raise RuntimeError()
                    type = token.data
                    
                    token = self.lexer.Next()
                    token = self.lexer.Next()
                    data  = None
                    if (token.type == "Number"):
                        data = token.data
                        retval.append(Arg(region, type, int(data)))
                    if (token.type != "Number"):
                        data = token.data
                        retval.append(Arg(region, type, data))
                    
                    token = self.lexer.Next()
                    break
                
                if (token.type == "Number"):
                    retval.append(Arg(None, "Unknown", int(token.data)))
                    break
                
                if (token.type == "ID"):
                    name = token.data
                    if name in function.labels:
                        retval.append(Arg(function.name + ".code", "Label", function.labels[name]))
                    if hasattr(function, "vars") and name in function.vars:
                        retval.append(Arg(function.name + ".vars", "Var", name))
                    if hasattr(function, "args") and name in function.args:
                        retval.append(Arg(function.name + ".args", "Var", name))                    
                    break
            
            token = self.lexer.Next()
            if (token.type == "Comma"):
                token = self.lexer.Next()
        
        return retval