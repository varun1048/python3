from time import perf_counter ,sleep, thread_time 
import threading 
import concurrent.futures as newThread


def do_something(seconds):
    print(f"slepping {seconds}")
    sleep(seconds)
    return f"done {seconds} slepping "

if  __name__ == '__main__':    
    start = perf_counter()

    # old method{
    # threads = []
    # for _ in range(10):
    #     thread = threading.Thread(target=do_something,args=[1.5])
    #     thread.start()
    #     threads.append(thread)
    
    # for x in threads:
    #     x.join()
    # }    

    with newThread.ThreadPoolExecutor() as executor:
        seconds = [1,2,3,4,5]
        for x in executor.map(do_something,seconds):
            print(x)

        # results = [executor.submit(do_something,sec) for sec in seconds ]
        # for x in newThread.as_completed(results):
        #     print(x.result())
        # 
        # 
        #         
    end = perf_counter()
    print(f"time taken {round(end - start,1)}")

