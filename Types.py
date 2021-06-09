class Type:
    pass

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


def FindType(name):
    if name == "Int64"