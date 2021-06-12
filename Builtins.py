# TO DO: Delete
import Types
from Argument import Arg

def MOVE(state, args):
    assert(len(args) == 2)
    assert(args[0].type == "Var")
    
    function = state.cstack[-1]
    variable = args[0]
    value    = args[1]
    
    name = variable.data
    if name in function.vars:
        variable = function.vars[name]
    if name in function.args:
        variable = function.args[name]
    
    if value.type == "Var":
        name = value.data
        if name in function.vars:
            value = function.vars[name]
        if name in function.args:
            value = function.args[name]
    
    # now "variable" and "value" are objects
    if variable.type != value.typ
    
    if (value.type != "Unknown") and (var.type != value.type):
        raise TypeError("bad value type")
    var.value = value.data

# LOAD:
#   size_t index -> state.dstack = state.memory[index]
def LOAD(state, args):
    if (len(args) != 1):
        raise RuntimeError()
    
    if (args[0].type == "Size"):
        index = args[0].data
        value = state.memory[index]
        state.dstack.append(value)
        return
    
    if (args[0].type == "Var"):
        name = args[0].data
        var  = state.cstack[-1].vars[name]
        
        type  = var.type
        value = var.data
        state.dstack.append((type, value))
        return
    
    raise RuntimeError("bad arg0 type")

# STORE:
#   size_t index -> state.memory[index] = state.dstack.top--
def STORE(state, args):
    if (len(args) != 1):
        raise RuntimeError()
    
    index = args[0].data
    value = state.dstack[-1]
    state.dstack.pop()
    state.memory[index] = value

def CONST(state, args):
    if (len(args) != 1):
        raise RuntimeError()
    
    value = ("Int64", args[0].data)
    state.dstack.append(value)

def JGE(state, args):
    if (len(args) != 1):
        raise RuntimeError()

    if (args[0].type != "Label"):
        raise RuntimeError()
    dest  = (args[0].data).data
    
    left  = state.dstack[-2][1]
    right = state.dstack[-1][1]
    
    state.dstack.pop()
    state.dstack.pop()
    
    if (left >= right):
        state.ip = dest

def JUMP(state, args):
    if (len(args) != 1):
        raise RuntimeError()

    if (args[0].type != "Label"):
        raise RuntimeError()
    
    dest     = (args[0].data).data
    state.ip = dest

# add {float} {float}
# add {float} {int}
# ...
# add {class A} {class B}

# dstack = void* -> stack.top
# stack[-2] = {void*, void*}
# 2 inderect

# 1)void* + offset = data
#   (fastest)
#   (type ???)
# 2)void* + offset = data + type
#   (fast)
#   (dstack[-2] = ?)
# 3)void** = data
#   (static memory layout) (type casts)
#   (slow)
#   mov r1, dstack     (type1)
#   mov r2, dstack + 8 (data1)
#   add.Int64.Int64 dstack[-1], dstack[-2] - fast?

def ADD(state, args):
    if (len(args) == 0):
        left  = Arg("DStack", state.dstack[-2][0], state.dstack[-2][1])
        right = Arg("DStack", state.dstack[-1][0], state.dstack[-1][1])
        
        if left.type == "Int64" and right.type == "Int64":
            state.dstack.pop()
            state.dstack.pop()
            state.dstack.append( ("Int64", left.data + right.data) )
        else:
            raise RuntimeError("bad args type in add (argc == 0)")
        return
    
    if (len(args) == 1):
        left  = Arg("DStack", state.dstack[-1][0], state.dstack[-1][1])
        right = args[0]
        
        if left.type == "Int64" and right.type == "Int64":
            state.dstack.pop()
            state.dstack.append( ("Int64", left.data + right.data) )
        else:
            raise RuntimeError("bad args type in add (argc == 1)")        
        return
    
    if (len(args) == 2):
        left  = args[0]
        right = args[1]
        
        if left.type == "Int64" and right.type == "Int64":
            state.dstack.append( ("Int64", left.data + right.data) )
        else:
            raise RuntimeError("bad args type in add (argc == 2)")        
        return
    
    if (len(args) == 3):
        raise NotImplemented()
    
    raise RuntimeError()

"""
def INC(state, args):
    if (len(args) == 0):
        value = state.dstack[-1][1]
        
        state.dstack.pop()
        state.dstack.append( ("Int64", value + 1) )
        
    raise RuntimeError("bad arg count for inc")
"""

def INC(state, args):
    if (len(args) == 0):
        value = state.dstack[-1][1]
        
        state.dstack.pop()
        state.dstack.append( ("Int64", value + 1) )
        return
    if (len(args) == 1):
        if args[0].type == "Var":
            name = args[0].data
            prev = state.cstack[-1]
            var  = None
            
            if name in prev.vars:
                var = prev.vars[name]
            if name in prev.args:
                var = prev.args[name]
            
            var.data += 1
            return
        raise RuntimeError("bad type of arg0 in inc")

def Inc64(state, args):
    if (len(args) != 0):
        raise RuntimeError()
    
    value = state.dstack[-1][1]
    
    state.dstack.pop()
    state.dstack.append( ("Int64", value + 1) )        

def ret(state, args):
    state.cstack.pop()
    if len(state.cstack) > 0:
        state.function = state.cstack[-1].function
        state.ip       = state.cstack[-1].ip
    else:
        state.function = None
        state.ip       = None        