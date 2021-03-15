#!/bin/env python3

import time
import sys

if __name__ == '__main__':
    print("hello!")

    for i in range(48):
        sys.stdout.write('#'*i+'\r')
        sys.stdout.flush()
        time.sleep(1)
    print("that's all folks")
    print()
