from threading import Thread,current_thread

class MyThread(Thread):
    def __init__(self,n):
        if n != "":
            super(MyThread,self).__init__(name=n)
        else:
            super(MyThread,self).__init__()
    
    def run(self):
        print("Name:%s\n" %self.getName())

if __name__ == "__main__":
    t1 = MyThread("t1")
    t2 = MyThread("t2")

    t1.start()
    t2.start()

    print(current_thread().getName())