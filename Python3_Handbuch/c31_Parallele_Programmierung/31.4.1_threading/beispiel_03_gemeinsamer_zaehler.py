#!/usr/bin/env python

import threading


class MeinThread(threading.Thread):
    zaehler = 0

    def run(self):
        for i in range(2000000):
            MeinThread.zaehler += 1


if __name__ == "__main__":
    A = MeinThread()
    B = MeinThread()
    A.start(), B.start()
    A.join(), B.join()

    print(MeinThread.zaehler)
