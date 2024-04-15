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


