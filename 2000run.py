import time


def timer(function, *args):
    start = time.time()
    function(*args)
    end = time.time()
    return end - start


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
