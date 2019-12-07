from multiprocessing import Process,Pool
import os, time, random
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def main():
    print(search([-1,0,3,5,9,12],9))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)#可以同时跑4个进程，默认大小是cpu核数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')