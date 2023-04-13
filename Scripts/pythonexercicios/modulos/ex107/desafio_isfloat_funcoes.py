def isfloat(num):
    n = str(num).strip()
    if n.count('.') == 1:
        num = n.replace('.', '')
        return True if num.isnumeric() else False
    else:
        return False
    
print(isfloat(2345,6))