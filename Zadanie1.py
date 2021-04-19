def generate_prime_numbers(limit):
    """Funkcja tworząca listę liczb pierwszych z podanego zakresu."""
    candidate = [1*x for x in range(limit + 1)]
    prime_numbers = []
    for i in range(2, limit + 1):
        if candidate[i] != 0:
            prime_numbers.append(i)
            for j in range(i+i, limit + 1, i):
                candidate[j]=0
    return prime_numbers

def generate_fibonacci_numbers(n):
    """Funkcja generująca podaną ilość liczb ciągu Fibonacciego."""
    fibonacci_numbers = [0]
    if n == 1:
        fibonacci_numbers.append(1)
        return fibonacci_numbers
    previous_number = 0
    next_number = 1
    for i in range(n-1):
        next_number += previous_number
        previous_number = next_number - previous_number
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers