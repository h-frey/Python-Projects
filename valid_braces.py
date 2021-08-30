def validBraces(string):
    brace_lst=["(",")","{","}","[","]"]
    str_lst=[]
    if (len(string) % 2 != 0):
        return False
    else:
        for i in string:
            str_lst.append(i)
            



validBraces("(){}[]")