from threading import Thread
from time import sleep,perf_counter
class Employee(Thread):
    def run(self):
        for i in range(3):
            print("joined")
            sleep(2)

class Salary(Thread):
    def run(self):
        for i in range(3):
            print("salary")
            sleep(1)

t1=Employee()
t2=Salary()

start=perf_counter()
t1.start() # start calls the run function 
t2.start()

t1.join() 
t2.join() # after completion of t1 and t2 thread , main thread would work
end=perf_counter()
print(f"execution time {end-start}")

print("main thread work")


def running(seconds):
    print(f"Sleeping for {seconds}")
    sleep(seconds)

start=perf_counter()
t1=Thread(target=running, args=[2])
t2=Thread(target=running,args=[3])
t3=Thread(target=running,args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
end=perf_counter()
print(f"execution time {end-start}")


# concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from time import sleep,perf_counter

def running(seconds):
    print(f"Sleeping for {seconds}")
    sleep(seconds)
    return seconds


with ThreadPoolExecutor(max_workers=1) as executor:
    thread1 = executor.submit(running, 3)
    print(thread1.result())

with ThreadPoolExecutor(max_workers=1) as executor:
    thread2 = executor.submit(running, 2)
    print(thread2.result())

with ThreadPoolExecutor(max_workers=1) as executor:
    thread3 = executor.submit(running, 1)
    print(thread3.result())


#simple map function
# l=[1,2,3]
# cubes= list(map(lambda x: x**2,l))
# print(cubes)



l=[3,2,1]

with ThreadPoolExecutor() as executor:
    start=perf_counter()
    results = executor.map(running,l) #here function started
    for result in results:
        print(result)                 #here function completed
    end= perf_counter()
    print(f"time for execution{end-start}")




