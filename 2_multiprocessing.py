from multiprocessing import Process


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    number = 30
    p1 = Process(target=fibonacci, args=[number])
    p2 = Process(target=fibonacci, args=[number])
    p3 = Process(target=fibonacci, args=[number])

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
