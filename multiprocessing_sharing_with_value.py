import multiprocessing as mp
import time


def increment():
    counter.value += 1


if __name__ == '__main__':
    # counter = 1
    counter = mp.Value('i', 1)

    for i in range(10):
        process = mp.Process(target=increment, args=())
        process.start()
        process.join()

    print('counter:{counter.value}')
