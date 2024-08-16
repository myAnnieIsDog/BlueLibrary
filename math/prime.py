import math

def run():
    while True:
        try: 
            n = int(input("What number would you like to test?\n"))
            if type(n) != int or n < 2:
                raise Exception
            result = (f"{n} is {'prime.' if is_prime(n) else 'not prime'}")
            break
        except:
            print("\nYou must enter a positive integer")
            continue
    print(result)

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number < 4:        # 2 and 3 are primes
        return True
    elif not number % 2:  # All even numbers are not primes
        return False

    odd_numbers = range(3, int(math.sqrt(number) + 1), 2)

    return not any(not number % i for i in odd_numbers)
    # from https://github.com/TheAlgorithms/Python/ (I forgot which file)

def list_primes(n):
    primes = []
    for i in range(n):
        if is_prime(i):
            primes.append(i)
    return primes

if __name__ == '__main__':
    run()
