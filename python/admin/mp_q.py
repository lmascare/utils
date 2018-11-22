#!/usr/local/bin/python3

from multiprocessing import Process, Queue

def f(q):
    q.put(['42', None, 'Hello'])

if __name__ == "__main__":
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()