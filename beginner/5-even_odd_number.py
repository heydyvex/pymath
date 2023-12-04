'''
even-odd vending machine that will type the number followed by the next 9 even or odd numbers
'''

def gen_num(n):
    
    tmp = n
    total = ''
    for i in range(9):
        total += f'{tmp+2}, '
        tmp +=2
    
    return total[:-2]

def even_odd(n):
    
    if (n % 2) == 0:
        print(f'{n}, {gen_num(n)}')
    else:
        print(f'{n}, {gen_num(n)}')

if __name__ == '__main__':
    n = input('Enter a number: ') 
    even_odd(int(n))