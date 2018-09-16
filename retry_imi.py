import threading
import requests
import csv


def apicall(line):
    url = 'http://192.168.1.1:PORT/services/{}'.format(line)
    result = requests.post(url=url, headers={'Content-type': 'application/x-www-form-urlencoded'})
    num = line, result.content
    csvwr(num)


def main():
    pool = []
    with open('PATH/to/read/file', 'r') as f:
        counter = 0
        cn = 0
        pool = []
        for line in f.readlines():
            iline = int(line)
            counter += 1
            cn += 1
            thread = threading.Thread(target=apicall, name='Thread{}'.format(counter), args=(iline,))
            thread.start()
            pool.append(thread)
            print(thread.getName())
            if len(pool) == 10:
                thread.join()
                pool = []
    print(cn)


def csvwr(text):
    writer.writerow(text)


if __name__ == "__main__":
    g = open('/PATH/to/write/file', 'w')
    writer = csv.writer(g)
    main()
