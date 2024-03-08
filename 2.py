def add(x, y): return x+y
def mult(x, y): return x*y
def div(x,y): return x/y
def sub(x,y): return x-y

x = int(input("chatsere ricxvi:"))
y = int (input("chatsere ricxvi:"))

operations = {'+': add,
             '*': mult, 
             ':' :div,
              '-': sub}

print(operations['*'](x,y))