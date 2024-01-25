#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# test_list = ('8.208.115.225 - [2024-01-25 21:00:03.415614] "GET /projects/260 HTTP/1.1" 404 560',
#              '220.195.202.223 - [2024-01-25 21:00:03.771865] "GET /projects/260 HTTP/1.1" 400 316',
#              '210.100.140.62 - [2024-01-25 21:00:04.436124] "GET /projects/260 HTTP/1.1" 404 629',
#              '58.85.199.61 - [2024-01-25 21:00:05.181605] "GET /projects/260 HTTP/1.1" 301 938'
#              '8.208.115.225 - [2024-01-25 21:00:03.415614] "GET /projects/260 HTTP/1.1" 404 560',
#              '220.195.202.223 - [2024-01-25 21:00:03.771865] "GET /projects/260 HTTP/1.1" 316',
#              '210.100.140.62 - [2024-01-25 21:00:04.436124] "GET /projects/260 HTTP/1.1" 404 629',
#              '58.85.199.61 - [2024-01-25 21:00:05.181605] "GET /projects/260 HTTP/1.1" 301 938'
#              '8.208.115.225 - [2024-01-25 21:00:03.415614] "GET /projects/260 HTTP/1.1" 560',
#              '220.195.202.223 - [2024-01-25 21:00:03.771865] "GET /projects/260 HTTP/1.1" 400 316',
#              '210.100.140.62 - [2024-01-25 21:00:04.436124] "GET /projects/260 HTTP/1.1" 404 629',
#              '58.85.199.61 - [2024-01-25 21:00:05.181605] "GET /projects/260 HTTP/1.1" 938')

# for i in range(10000):
for i in range(50):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()
    # print(i)
    # sys.stdout.write(i + '\n')
    sys.stdout.flush()


