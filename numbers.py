from threading import Thread


def get_odd_numbers(a, b):
    for num in range(int(a), int(b) + 1):
        if (num % 2) != 0:
            print(num)


def get_even_numbers(a, b):
    for num in range(int(a), int(b) + 1):
        if (num % 2) == 0:
            print(num)


if __name__ == "__main__":
    t1, t2 = (
        Thread(target=get_odd_numbers, args=[1, 20]),
        Thread(target=get_even_numbers, args=[1, 20]),
    )

    t1.start()
    t2.start()

    t1.join()
    t2.join()
