import multiprocessing
import os,time,random,threading

# 1.多进程
def run_proc(name):
    print('run child procee %s (%s) ' % (name,os.getpid()))

def long_time_task(name):
    s  = time.time()
    time.sleep(random.random()*3)
    e  = time.time()
    print('task %s(%s) cost %0.2f secs' % (name,os.getpid(),(e-s)))
if __name__=='__main__':
    print('Parent procee %s ' % os.getpid())
    p = multiprocessing.Process(target=run_proc,args=('test',))
    print('start child process')
    p.start()
    p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('child process end')

    pool = multiprocessing.Pool()
    for i in range(5):
        pool.apply_async(long_time_task,args=(i,))
    pool.close()
    pool.join()
    print('all child process end')

# 2.多线程
t = threading.Thread(target=run_proc,args=('mythread',),name='run_proc')
t.start()
t.join()

# 3.thread_local
local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))
def process_thread(name):
    local_school.student = name
    process_student()
t1 = threading.Thread(target=process_thread,args=('bobo',),name='thread1')
t2 = threading.Thread(target=process_thread,args=('coco',),name='thread2')
t1.start()
t2.start()
t1.join()
t2.join()