import math

def run():
    seq = fibonacci(100)
    for i in seq:
        print(i)

def fibonacci(n):
    a = 0
    b = 1
    sequence = [a, b]
    
    if n < 1:
        return [0]   
    if n == 1 :
        return sequence
    
    for i in range(n):
        c = a + b
        sequence.append(c) 
        a = b
        b = c
    
    return sequence


if __name__ == '__main__':
    run()
