# the luhn algorithm
def split(n):
    return n//10, n%10
def sum_digits(n):
    if n<10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last)+last

def luhn_double(n):
    if n<10:
        return sum_digits(n*2)
    else:
        all_but_last, last = split(n)
        luhn_digit = sum_digits(2*last)
        return luhn_sum(all_but_last)+luhn_digit

def luhn_sum(n): #start calling this function, adding #odd digits
    if n<10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_double(all_but_last)+last


    
