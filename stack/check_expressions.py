# def check_xpressions(exp):
#     stack = []
#     for x in exp:
#         if x in("(" ,"{" , "["):
#             stack.append(x)
#         else:
#             if not stack:
#               return False
#             elif match(stack[-1] , x)==False:
#               return False
#             else:
#              stack.pop()
#     if stack:
#        return False
#     else:
#        return True
# def match(a,b):
#    if(a == "(" and b == ")" )or( a == "{" and b == "}") or( a == "[" and b == "]" ):
#       return True
#    else: return False
def expreesions(exp):
    stack = []
    for i in exp:
        if i in ("(" , "[" , "{"):
              stack.append(i)
        else:
             if not stack: #if stack is empty then return false
                return False
             elif match(stack[-1],i) == False:
                 return False
             else:
                 stack.pop()
    if stack: # match operation and pop if any elemnets present in stack then it return False
        return False
    else:
        return True
def match(a,b):
    if (a == "(" and b ==")") or (a =="{" and b =="}") or (a == "[" and b =="]"):
        return True
    else:
        return False
    
print(expreesions("([[][]]))"))