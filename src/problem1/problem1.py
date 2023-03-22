from math import floor


def sum_to_n_a(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

def sum_to_n_b(n):
    return int(n/2 * (n + 1))

def sum_to_n_c(n):
    if n%2 == 0:
        # Even
        num_of_pairs = n/2
        sum_of_first_and_last = 1 + n
        return int(num_of_pairs*sum_of_first_and_last)
    else:
        # Odd
        num_of_pairs = floor(n/2)
        mid_point = num_of_pairs + 1
        sum_of_first_and_last = 1 + n
        
        return int(sum_of_first_and_last*num_of_pairs + mid_point)
    
print(sum_to_n_a(150))
print(sum_to_n_b(150))
print(sum_to_n_c(150))