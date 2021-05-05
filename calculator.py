d = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    #...
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    #......
}
def word2num(w):
    # return the int value of w. 
    # hint: split the w if w is composition
    # consider w='two' or 'twenty-two'
    l = w.split('-')
    
    if len(l) == 1:
        return d[w]
    n = 0
    for num in l:
        n += word2num(num)
    # print(l)
    return n

s = input('input an expression: ')
# twenty-two + three
n1, op, n2 = s.split()
n1 = word2num(n1)
n2 = word2num(n2)

if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print("%.10f"%(n1/n2))






