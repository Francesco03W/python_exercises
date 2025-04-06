import psutil
import argparse
import time

def main():
    parser=argparse.ArgumentParser()
    # argomento facoltativo (--)
    parser.add_argument("--interval", help="Interval between cpu usage sampling (s)",
                        type=int, default=1)
    args=parser.parse_args()
    while(True):
        print(f'{time.time()} - {psutil.cpu_percent()}')
        time.sleep(args.interval)

if __name__ == "__main__":
    main()



