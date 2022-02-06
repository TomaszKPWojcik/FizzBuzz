#wersja 1 prosta
def FizzBuzz(n, m):
    for n in range(n, m + 1):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

#werscja 2 jedna linia
def FizzBuzz2(n, m):
    print("\n".join("FizzBuzz" if n % 3 == 0 and n % 5 == 0 else ("Fizz" if n % 3 == 0 else ("Buzz" if n % 5 == 0 else str(n))) for n in range(n, m + 1)))


if __name__ == '__main__':
    FizzBuzz2(3,50)