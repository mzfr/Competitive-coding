def isprime(n):
    prime_list = [2, 3, 5, 7]
    while n > 0:
        if (n % 10) in prime_list:
            n = int(n / 10)
        else:
            return False
    return True

def prime_prime(n):
    count = 0
    k = 0
    while count < n:
        k+=1
        if isprime(k):
            count += 1
    return k

def main():
    n=int(input())
    while n > 0:
        num = int(input())
        print(prime_prime(num))
        n -= 1

if __name__ == "__main__":
    main()
