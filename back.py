def greedy24(list):
    list.sort(reverse=True)
    a, b, c, d = list[0], list[1], list[2], list[3]
    op = ['+','-','*','/']
    value, margin = 0, 24
    tmp = 0
    for i in range(len(op)):
        tmp = eval(str(a) + op[i] + str(b))
        if abs(tmp-24) < margin:
            value = tmp
            margin = abs(tmp-24)
            op1 = ''
            op1 = op[i]
    e = value
    margin = 24
    for i in range(len(op)):
        tmp = eval(str(e) + op[i] + str(c))
        if abs(tmp-24) < margin:
            value = tmp
            margin = abs(tmp-24)
            op2 = ''
            op2 = op[i]
    e = value
    margin = 24
    for i in range(len(op)):
        tmp = eval(str(e) + op[i] + str(d))
        if abs(tmp-24) < margin:
            value = tmp
            margin = abs(tmp-24)
            op3 = ''
            op3 = op[i]  
    lop = [op1, op2, op3]
    if (op1 == '+' or op1 == '-') and (op2 == '*' or op2 == '/') and c != 1:
        exp = '(' + str(a) + op1 + str(b) + ')' # + op2 + str(c) + op3 + str(d)
    else :
        exp = str(a) + op1 + str(b)
    if (op2 == '+' or op2 == '-') and (op3 == '*' or op3 == '/') and d != 1:
        exp2 = '(' + exp + op2 + str(c) + ')' + op3 + str(d)    
    else :
        exp2 = exp + op2 + str(c) + op3 + str(d)
    return exp2

def score(e):
   s = 0
   s = e.count('+') * 5 + e.count('-') * 4 + e.count('*') * 3 + e.count('/') * 2 - e.count('(') - abs(24 - eval(e))
   return s
