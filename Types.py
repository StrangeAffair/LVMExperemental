from Function import PFunction

class Type:
    pass

class I64(Type):
    name = "I64"
    size = 8
    
    methods = dict()
    
    methods["lcopy"] = {
        "I64":  PFunction("I64 I64 copy",  CopyI64I64),
        "Size": PFunction("I64 Size copy", CopyI64Size),
    }
    
    methods["ladd"] = {
        "I64":  PFunction("I64 I64 add",  None),
        "Size": PFunction("I64 Size add", None),
    }
    
    @staticmethod
    def CopyI64I64(left, right):
        pass
    
    @staticmethod
    def CopyI64Size(left, right):
        pass

class Size(Type):
    name = "Size"
    size = 8
    
    self.methods = dict()
    
    @staticmethod
    def inc(obj):
        obj.data += 1
    
    @staticmethod
    def dec(obj):
        obj.data -= 1

class Object(Type):
    name = "Object"
    size = 8
    
    self.methods = dict()
    
    self.methods["lcopy"] = {
        "Object": PFunction("Object Object Copy", Object.Copy_Object_Object),
        "I64":  PFunction("I64 I64 copy",  I64.CopyI64I64),
        "Size": PFunction("I64 Size copy", I64.CopyI64Size),
    }
    
    self.methods["ladd"] = {
        "I64":  PFunction("I64 I64 add",  None),
        "Size": PFunction("I64 Size add", None),
    }    
    
    def __init__(self, type, value, static=False):
        self.type   = type
        self.data   = value
        self.static = static
    
    @staticmethod
    def Copy_Object_Object(left, right):
        if (left.type != right.type):
            if (left.static):
                raise RuntimeError("could not assign new type to Object")
            
            # free
            left.type = None
            left.data = None
            
            # alloc
            left.type = right.type
            left.data = None
        
        left.data = right.data
    
class Variable(Type):
    # ("Variable", data)
    # data -> Object(type, data)
    name = "Variable"
    size = Object.size + 8


"""
   no op:
     call("nop")

   unary op:
     call("inc", data)

   binary op:
     arg1.type -> type1 + type2?
     arg2.type -> type1 + type2?
     call("add", data1, data2)
    
   argc >= 3:
     call(method, args)
"""


def I64_LADD(left, right, dest):
    assert(left.type.name == "Int64")
    
    # function add(i64, i64) -> i64 / i32 / ...
    # dest.type = ?
    # add {I64, 15}, {I64, 20}, {I32, ??} 
    # add {I64, 15}, {I64, 20}, {MEM, 0}  type = ??
    # add {C, I64, 15}, {C, I64, 20}, {MEM, I32, 0}
    
    # MEM[0] = fixedType I32, value = 0
    # MEM[0] = fixedType Obj, value = 0xff...{fixedType = I32, value = 0}
    
    # add I64 I64 -> I32
    # add I64 I64 -> Object (type = ???)
    # add {I64, 15} {I64, 20} {MEM, Object(type = I32), 0}
    # add "I64 I64 -> MEM.I32" 15, 20, 0
    
    # add  I64 I64 -> I32
    # move I32 -> Object (with type cast)
    
    # add I64 I64 -> Object(type = I64)  type - default
    
    if (right.type.name == "Int64"):
        result = left.data + right.data
        dest

Int64 = Type()
Int64.name = "Int64"
Int64.ladd = None 
Int64.radd = None

Size  = Type()
Size.name = "Size"
Size.ladd = None 
Size.radd = None