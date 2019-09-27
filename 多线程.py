'''
import _thread
import time

#为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime())

_thread.start_new_thread(print_time, ("Thread-1", 1))
_thread.start_new_thread(print_time, ("Thread-2", 2))
print("Main Finished")
'''
'''
import threading
import time

class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting" + self.name)
        print_time(self.name, self.delay)
        print("Exiting" + self.name)


def print_time(threadName, delay):
    counter = 0
    while counter <3:
        time.sleep(delay)
        print(threadName, time.ctime())
        counter += 1

threads = []

#创建新线程
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)

#开启新线程
thread1.start()
thread2.start()

#添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

#等待所有线程完成
for t in threads:
    t.join()

print("Exiting Main Thread")

'''

import threading
import requests
import time

link_list = []
with open('alexa.txt', 'r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n', '')
        link_list.append(link)

start = time.time()
class myThread(threading.Thread):
    def __init__(self, name, link_range):
        threading.Thread.__init__(self)
        self.name = name
        self.link_range = link_range
    def run(self):
        print("Starting" + self.name)
        crawler(self.name, self.link_range)
        print("Exiting" + self.name)


def crawler(threadName, link_range):
    for i in range(link_range[0], link_range[1]+1):
        try:
            r = requests.get(link_list[i], timeout=20)
            print(threadName, r.status_code, link_list[i])
        except Exception as e:
            print(threadName, 'Error:', e)


thread_list = []
link_range_list = [(0, 200), (201, 400), (401, 600), (601, 800), (801, 1000)]

#创建新线程
for i in range(1, 6):
    thread = myThread("Thread-" + str(i), link_range_list[i-1])
    thread.start()
    thread_list.append(thread)

#等待所有线程完成
for thread in thread_list:
    thread.join()

end = time.time()
print('简单多线程爬虫的总时间为:', end-start)
print("Exiting Main Thread")