def add(a,b):
    c = a+b
    return c

def my_function(a):
    if a<0:
        return "Cannot do this on a negative number!"
    x=a+5
    y=a-5
    return x,y 


first_ans, second_ans  = my_function(1)
print(first_ans)
print(second_ans)
