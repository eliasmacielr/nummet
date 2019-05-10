import time

from false_position import false_position

def main():
    start = time.time()
    xr, it, er = false_position(0, 1.5, 1e-6, 1000, 0)
    end = time.time()
    print(xr, it, er, end - start)

if __name__ == "__main__":
    main()
